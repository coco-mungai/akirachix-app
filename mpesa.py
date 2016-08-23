from datetime import datetime
class MPESA:
	def __init__(self):
		self.name=input("Please enter the account name:\n ")
		self.number=input("Please the enter the phone number:\n ")
		self.balance=0.0
		self.deposits=[]
		self.withdrawals=[]		
		print("Welcome",self.name)

	def deposit(self, amount):
		if amount<50:
			print("Please enter more than 50")			
		else:
			self.balance +=amount
			now=datetime.now()
			time=now.strftime("%c")
			details={"time":time, "amount":amount}
			self.deposits.append(details)
			#self.deposits.append(amount)
			print("Dear", self.name, "you have deposited", amount, "new balance is", self.balance)
		return

	def withdraw(self, amount):
		if amount<0:
			print("Enter a valid amount")			
		elif amount>self.balance:
			print("You have insufficient balance")			
		else:
			self.balance-=amount
			now=datetime.now()
			time=now.strftime("%c")
			details={"time":time, "amount":amount}
			self.withdrawals.append(details)
			#self.withdrawals.append(amount)
			print("Dear", self.name, "you have withdrawn", amount, "new balance is", self.balance)
		return
	def showDeposits(self):
		if len(self.deposits)<1:
			print("You have not made any deposits")
		else:
			for deposit in self.deposits:
				print("On", deposit['time'], "you deposited", deposit["amount"])

	def showWithdrawals(self):
		if len(self.withdrawals)<1:
			print("You haven't made any withdrawals")
		else:
			for withdraw in self.withdrawals:
				print("On", withdraw['time'], "you withdrew", withdraw["amount"])
	def giveLoan(self):
		"""
		Condition for getting a loan:
			-User has made at least 10 deposits.
			-Loan requested is less than 1/3 of total sum of deposit history.
			-User has non deposit blance.
			-User has no outstanding loans.
			-Loan has an interest of 10%.
		The loan given is amount of outstanding loan
		"""

		amount=int(input("Please enter the amount:\n"))

		if len(self.deposits)<10:
			print("You must have made 10 deposits.")
		elif amount < 50:
			print("Dear",self,",you can't withdraw less than 50 Ksh.")
		elif amount * 3 > sum([deposit["amount"] for deposit in self.deposit]):
			print("You don't have enough credit score")
		elif self.balance != 0:
			print("You can't have a balance before taking a loan")
		elif self.loan != 0:
			print("You have an outstanding loan of: ",self.loan)
		else:
			loan_interest = 0.1*amount
			loan_amount = amount + loan_interest
			self.loan += loan_amount
			print("Success: You have received a loan of ",amount,"your outstanding loan balance is ",self.loan)
		return		

	def payLoan(self, amount):
		"""
		Accept loan payment if:
			-amount is larger than 50.
			-user has a loan or else save as deposit.
		Amount contributes to loan repayment 
		If amount is larger than remaining loan, the remainder is kept as deposit 
		"""
		now = datetime.now()
		time = now.strftime("%c")

		if amount < 50:
			print("You must enter an amount more than", amount, "to repay the loan.")

		elif self.loan == 0:
			self.balance += amount
			details = {
				"date": time,
				"amount": amount
			}
			self.deposits.append(details)
			print("Dear,", self.name, "You have no loan balance so", amount, "has been deposited to your account on", time,"Your new balance is", self.balance)

		elif amount > self.loan:
			diff = amount - self.loan
			old_loan = self.loan
			self.loan = 0
			self.balance += diff
			details = {
				"date": time,
				"amount": diff
			}
			self.deposits.append(details)
			print("Dear,", self.name, "you have fully settled your loan of", old_loan, "and the balance of", diff, "has been deposited to your account on", time, "new account balance is", self.balance)
			
		else:
			self.loan -= amount
			if not self.loan:
				print("Dear,", self.name, "you have fully settled your loan.")
			else:
				print("Dear,", self.name, "you have paid", amount, "towards your loan. New loan balance is", self.loan)
		return





