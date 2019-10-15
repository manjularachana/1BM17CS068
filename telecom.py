class CallDetail:
    callednum=0
    receivednum=0
    timeduration=0
    typeofcall=' '

    def  detailsofobject(self,list1):
         self.callednum=int(list1[0])
         self.receivednum=int(list1[1])
         self.timeduration=int(list1[2])
         self.typeofcall=str(list1[3])
         return self
    def  printdetails(self):
        print("the details are :")
        print(self.callednum,end=" ")
        print(self.receivednum,end=" ")
        print(self.timeduration,end=" ")
        print(self.typeofcall,end=" ")

class Util:
    list_of_call_objects=[]
    def __init__(self):
        self.list_of_call_objects=None
    def parse_customer(self,list_of_call_string):
        list1=[]
        for item in list_of_call_string:
          a=item.split(",")
          object1=CallDetail().detailsofobject(a)
          list1.append(object1)
        self.list_of_all_objects=list1
        for i in self.list_of_all_objects:
            print(CallDetail.printdetails(i))
call='9963343894,8897211417,23,std'
call2='9963343895,8897211411,24,std'
call3='9963343893,8897211412,20,LOCAL'
list_of_call_string=[call,call2,call3]
Util().parse_customer(list_of_call_string)
