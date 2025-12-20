class Bank():
    bank_name = "ISC BANK"
    @staticmethod
    def bank_name():
        print(Bank.bank_name)

class Account(Bank):
    balance = 0
    account = 0
    def __init__(self,name,add,pan,adhar,ph):
        self.name = name
        self.address = add
        self.pan_no = pan
        self.adhar = adhar
        self.phone = ph
        Account.account += 1
        self.account_No = str(Account.account).zfill(12)

    def deposit(self,add):
        if add > 0 :
         self.balance += add
         print(f"amount {add} depsited.")
        else:
            print("Give valid amount.Deposit failed.")

    def credit(self,sub):
        if 0 < sub <= self.balance:
         self.balance -= sub
         print(f"amount {sub} credited.")
        else:
            print("Enter valid amount.credit faild.")

    def __str__(self):
        return f"Dear coustamer your name is {self.name} and your balance in account no [{self.account_No}] is {self.balance}.0 Rs"
    
    def __call__(self):
        detail = {"Name" : self.name,"Address" : self.address,"PAN no" : self.pan_no,
        "Addhar no" : self.adhar,"Phone no" : self.phone,"Account No" : self.account_No}
        for val , pair in detail.items():
            print(val,"=",pair)

    @property
    def givename(self):
        return self.name
    
    @givename.setter
    def name_update(self,new_name):
        self.name = new_name
        print(f"Name change to {self.name} sucessfully.")
    
    @property
    def givephone(self):
        return self.phone
    
    @givephone.setter
    def phone_update(self,new_no):
        self.phone = new_no
        print(f"Phone no change to {self.phone} sucessfully.")

    @property
    def giveaddress(self):
        return self.address
    
    @giveaddress.setter
    def address_update(self,new_add):
        self.address = new_add
        print(f"Name change to {self.address} sucessfully.")

c1 = Account("Om Shri","Amarpur","QUIO0023","0233 0989 7594","2346780984")
print(c1)
c1()

c2 = Account("Sanjana","Kumarkhal","PNIO0025","0256 0909 7544","2456780984")
print(c2)
c2()