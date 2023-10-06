class product:
    def __init__(self,name,mrp,mgdate):
        self.name = name
        self.mrp = mrp
        self.mgdate = mgdate
    def get_product_details(self):
        print(self.name,self.mrp,self.mgdate)

obj_1 = product("Car",80,"1208")
obj_1.get_product_details()