class user:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.special = "special only"
    def fDisplay_1(self):
        print("name = " + self.name + " password = " + self.password)
class admin(user): #gamit ang () para ma access ang user class
    def  __init__(self, name, password, code):       
        self.code = code
        #super ginagamit lang ito pag naghakawig sila ng name ng instance var at methods
        #both admin at user class
        super().__init__(name, password) 
    def fDisplay_2(self):
        print("name = " + self.name + " password = " + self.password + " code = " + self.code)
        
admin_1 = admin("abc", "123", "ab12") #priority ng admin ang sariling ka-name na function
admin_1.fDisplay_1()
admin_1.fDisplay_2()
print(admin_1.special) #may acess ang admin sa special variable ng user

