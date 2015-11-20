#inheritance example
class A():      
    def __init__(self, id, field1):
        self.id = id
        self.field1 = field1

class B(A):
    def __init__(self, id, field2):
        super().__init__(id, 12)
        self.field2 = field2
        self.id = id
                
obj = B(5,10)
print(obj.id,obj.field1,obj.field2)



