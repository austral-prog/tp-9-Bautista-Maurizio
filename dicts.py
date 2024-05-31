
def create_inventory(items):
    inventory = dict()
    for item in items:
        if item not in inventory:
            inventory[item] = 1
        else:
            inventory[item] += 1
    return inventory




def add_items(inventory, items):
    for item in items:
        if item not in inventory:
            inventory[item] = 1
        else:
            inventory[item] += 1
    return inventory


   


def decrement_items(inventory, items):
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory



def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    if item not in inventory:
        return inventory


def list_inventory(inventory):
    Tupla = [(item, cantidad) for item, cantidad in inventory.items() if cantidad>0]
    return Tupla

