class University:
    def __init__(self,Id,Age,Marks):
        self.Id=Id
        self.Age=Age
        self.Marks=Marks
    def validate_age(self):
        if(self.Age>20):
          return True
        else:
          return False
    def validate_marks(self):
        if self.Marks>=0 and self.Marks<=100 :
         return True
        else:
          return False
    def check_qualification(self):
        if self.validate_age() and self.validate_marks() and self.Marks>65:
          return True
        else:
           return False
    def set(self):
        self.Id=int(input("enter ID"))
        self.Age=int(input("enter Age"))
        self.Marks=int(input("enter Marks"))
    def getter(self):
        print("the details of student are : Id , Age ,Marks in order -")
        print(self.Id,end=" ")
        print(self.Age,end=" ")
        print(self.Marks,end=" ")

ob1=University(1,28,70)
ob1.set()
x=ob1.check_qualification()                       
if x:
 ob1.getter()
else:
  print("Requirements Not Satisfied")                     
    
