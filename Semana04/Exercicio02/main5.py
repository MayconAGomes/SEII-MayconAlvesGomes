from phone2 import Phone
from keyboard import Keyboard

item1 = Phone("jscPhone", 1000, 3)
item2 = Keyboard("jscPhone", 1000, 3)

item1.send_email()

item1.apply_discount()
item2.apply_discount()

print(item1.price)
print(item2.price)