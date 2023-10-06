class product:
    def __init__(self,name,mrp,mgdate):
        self.name = name
        self.mrp = mrp
        self.mgdate = mgdate
    def get_product_details(self):
        print(self.name,self.mrp,self.mgdate)

class object(product):
    def __init__(self,name,mrp,mgdate,expdate,is_sold):
        super().__init__(name,mrp,mgdate)
        self.expdate = expdate
        self.is_sold = is_sold
    def get_product_details(self):
         super().get_product_details()
         print(self.expdate,self.is_sold)
        

obj_1 = object("Car",80,"1208","983",True)
obj_1.get_product_details()
