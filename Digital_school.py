class School():
    school_name = "M.D.S School"

    def schoolName():
        print(School.school_name)

class Class(School):
    students = 0
    def __init__(self,name,ph,addrass,father,mother,standerd):
        self.name = name
        self.ph_no= ph
        self.father_name = father
        self.mother_name = mother
        self.addrass = addrass
        self.standerd= standerd
        Class.students += 1
        self.roll_no = Class.students
    
    def __call__(self):
        detail = {"Name" : self.name,"Address" : self.address,
        "Phone no" : self.phone,"Roll no" : self.roll_no}
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

class Boy(Class):
    Gender = "Boy"

class Girl(Class):
    Gender = "Girl"