#Online Shopping Cart


class ShoppingList:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
    
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")


print("Item 1")
item1_name = input("What is the item name: ")
item1_price = float(input("What is the item price: "))
item1_quantity = int(input("What is the item quantity: "))

item1 = ShoppingList(item1_name, item1_price, item1_quantity)

print("\nItem 2")
item2_name = input("What is the item name: ")
item2_price = float(input("What is the item price: "))
item2_quantity = int(input("What is the item quantity: "))

item2 = ShoppingList(item2_name, item2_price, item2_quantity)


print("\nTotal Cost")
item1.print_item_cost()
item2.print_item_cost()

total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print(f"\nTotal: ${total_cost}")
