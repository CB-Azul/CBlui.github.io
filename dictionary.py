def sum_of_products(items):
    total = 0
    for x in items.values():
        total = total + x
    return total

def most_expensive(items):
    pricey = 0
    for y in items.values():
        if y > pricey:
            pricey = y
    return pricey

def add_item(items):
    key = input("Add item:")
    value = input("What is the price of the item?:")
    items[key] = value



items = {"Bread":40, "Rice":55, "Sugar":35, "Coffee":25}
print(sum_of_products(items))
print(most_expensive(items))

# items["Chesse"] = 33
print(add_item(items))
print(items)
# print(items.keys())
# print(items.values())

halo2 = []
