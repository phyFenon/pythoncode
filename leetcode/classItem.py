'''
The simple example for class.
'''
class Item:
    pay_rate=0.8 # The pay rate is the gloable attribute.
    all=[] # This is the set for all catorgories
    def __init__(self,name:str,price:float,quantity=0):
        #Run validations to the received arguments
        assert price>=0, f"price {price} is not greater than zero!"
        assert quantity>=0,f"quantity {quantity} is not greater than zero!"
        
        self.name=name
        self.quantity=quantity
        self.price=price
        
        #Actions to execute
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_discount(self):
       return self.price*self.pay_rate
    def __repr__(self):
       return f"Item('{self.name}',{self.quantity},{self.price})"
    
   
        
item1=Item('Phone',100,20)
item2=Item('Laptop',20,10)
item3=Item('Cable',30,10)
item4=Item('Mouse',40,10)
for instance in Item.all:
    print(instance)
# print(item2.calculate_total_price())       
# print(Item.__dict__)
# print(item1.__dict__)
# print(item1.apply_discount())
# item1.pay_rate=0.4
# print(item1.apply_discount())

# read data from a csv file