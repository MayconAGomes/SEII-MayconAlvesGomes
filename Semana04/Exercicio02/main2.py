from item2 import Item
from phone2 import Phone

item1 = Item("MyItem", 750)

item1.apply_icrement(0.2)
item1.apply_discount()

print(item1.price)