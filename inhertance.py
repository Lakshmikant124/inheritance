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
        #updated has been made
        

obj_1 = product("Car",80,"1208")
obj_1.get_product_details()
