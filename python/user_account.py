class account:
    #object initilization
    #member variables serverId,name,ip,status,memory_usage
    def __init__(self,Holdename, Accountno, Balance=0):
        self.Holdename=Holdename
        self.Accountno=Accountno
        self.Balance= float(Balance)

    #methods
    def getBalance(self):
             return f"The current balance is {self.Balance}"

    def deposit(self, amt):
        if amt > 0:
            self.Balance += amt
            return f"{amt} deposited successfully. {self.getBalance()}"
        else:
            return "Deposited amount must be greater than zero"

    def withdraw(self, amt):
        if  amt <= 0:
           return "withdrawl amount must be greater than zero"

        elif  amt > self.Balance :
           return "Insufficinet fund"
        
        else:
            self.Balance -= amt
            return f"{amt} withdrawl Successfully!!.{self.getBalance()}"


acc1 = account("Sam Gourav Nag", "SBIN001818", "1000")

print(acc1.getBalance())
print(acc1.deposit(500))
print(acc1.withdraw(200))
print(acc1.withdraw(2000))
print(acc1.deposit(-100))


#server is a class
#create 4 object web1,web2,web3,web4 .They have there own memory
#ip,name,memory,status
#self means object itself
#