from abc import ABC, abstractmethod
from datetime import date

class Product(ABC):
    def __init__(self, pro_id, name, price):
        self.pro_id = pro_id
        self.name = name
        self.price = price

    @abstractmethod
    def final_price(self):
        pass

class Electronics(Product):
    def __init__(self, pro_id, name, price, warranty):
        super().__init__(pro_id, name, price)
        self.warranty = warranty

    def final_price(self):
        gst_per = 18
        total_price = (gst_per * self.price) / 100
        return total_price + self.price

class Clothing(Product):
    def __init__(self, pro_id, name, price, size, fabric_type):
        super().__init__(pro_id, name, price)
        self.size = size
        self.fabric_type = fabric_type

    def final_price(self):
        gst_per = 5
        total_price = (gst_per * self.price) / 100
        return total_price + self.price

class Grocery(Product):
    def __init__(self, pro_id, name, price, expiry_date):
        super().__init__(pro_id, name, price)
        self.expiry_date = expiry_date

    def final_price(self):
        dis_percentage = 30

        days_left =  (self.expiry_date - date.today()).days
        if days_left <= 7:
            dis_per = dis_percentage * self.price / 100
            final_price = self.price - dis_per
            return final_price

        else:
            return self.price

class Cart:
    pass



elec = Electronics("E1", "Mobile", 10000, 30)
g = Grocery("G1", "Oil", 1000, date(2026, 5, 6))
print(elec.pro_id, elec.name, elec.price)
print(elec.final_price())
print(g.final_price())

# date(2026, 1, 30) to pass


