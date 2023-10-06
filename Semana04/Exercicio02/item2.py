import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, __price: float, quantity=0):

        # Run validations to the received arguments

        assert __price >= 0, f"__price {__price} is not grater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not grater than or equal to zero!"

        # Assign to self objects
        self.__name = name
        self.__price = __price
        self.quantity = quantity

        # Actions to execute

        Item.all.append(self)

    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_icrement(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    # Property Decorator =  Read-Only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total___price(self):
        return self.__price * self.quantity


    def apply_discount2(self):
        self.__price = self.__price * Item.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__}'{self.name}', {self.__price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open('C:/Users/Windows 10/Desktop/Programação/Semana04/items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    @property
    def read_only_name(self):
        return "AAA"
    
    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone.
        We have {self.name} {self.quantity} times.
        Regards, JimShapedCoding     
        """
    
    def __send(self):
        pass

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()