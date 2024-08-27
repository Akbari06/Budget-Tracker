import re

                                                        # Classes below
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def ReturnItem(self):
        return f"Item('{self.name}', '{self.quantity}', '{self.price}')"

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
    
class Tracker:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        item = Item(name, quantity, price)
        self.items.append(item)

    def remove_item(self, name, quantity, price):
        items_to_remove = []
        remaining_items = []
        item_found = False

        for item in self.items:
            if item.name == name and item.quantity == quantity and item.price == price:
                items_to_remove.append(item)
                item_found = True
            else:
                remaining_items.append(item)

        self.items = remaining_items

        if not item_found:
            print("Item not found")
            
    def update_quantity(self, name, quantity, price, new_name, new_quantity, new_price):
        for item in self.items:
            if (item.name == name and item.quantity == quantity and item.price == price):
                item.name = new_name
                item.quantity = new_quantity
                item.price = new_price
                
    def display_items(self):
        for item in self.items:
            print(item.ReturnItem())
   
    def get_number_of_purchases(self):
        return len(self.items)

    def get_items(self):
        return self.items
    
##############################################################################################################################################################
##############################################################################################################################################################
##############################################################################################################################################################
                                                           # Main Program all below
                 
tracker = Tracker()

##############################################################################################################################################################
##############################################################################################################################################################

def RemovePurchases():
    actualPrice = 0.00
    actualQuantity = 0
    BoolPrice = False
    BoolQuantity = False
    pattern = r"^\d+\.\d{2}$"
    
    name = input("Enter name to remove: ")

    while (BoolPrice == False):
        price = input("Enter price of each product: ")

        if re.match(pattern, price):
            actualPrice = float(price)
            BoolPrice = True
        else:
            print("Not a valid price")

    while (BoolQuantity == False):
        quantity = input("Enter the quantity of that purchase:")

        if (quantity.isdigit()):
            actualQuantity = int(quantity)
            BoolQuantity = True
        else:
            print("Not a valid quantity")

    tracker.remove_item(name, actualQuantity, actualPrice)
    print("Successfully removed")
    Purchases()

######################################################################################################################################################################
######################################################################################################################################################################

def MergeSortItemsList(arr):

    if (len(arr) <= 1):
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = MergeSortItemsList(left_half)
    right_half = MergeSortItemsList(right_half)

    return MergeItemsList(left_half, right_half)

def MergeItemsList(left,right):
    
    merged = []
    left_index, right_index = 0, 0

    while ((left_index < len(left)) and (right_index < right)):
        if (left[left_index][2] < right[right_index][2]):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(left[left_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extent(right[right_index:])

    return merged

def BubbleSortItems(arr):

    n = len(arr)
    if (n <= 1):
        return arr

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            if arr[j][2] > arr[j + 1][2]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            
            break

    return arr




def ViewPurchases(): # You need to also filter purchases by bubble for lists under 100 and merge for 100 or more

    items_list = tracker.get_items()

    items_2d_list = []

    for item in items_list:
        items_2d_list.append([item.name, item.quantity, item.price])


    if (tracker.get_number_of_purchases() >= 20):

        print("Purchases from cheapest to most expensive:")

        items_2d_list = MergeSortItemsList(items_2d_list)
        
        for index in items_2d_list:
            print("-" *50)

            print(index[0])
            print(index[1])
            print(index[2])

            print("-" *50)

    else:

        items_2d_list = BubbleSortItems(items_2d_list)

        for index in items_2d_list:
            print("-" *50)

            print(index[0])
            print(index[1])
            print(index[2])

            print("-" *50)
        
    
    Purchases()
    
######################################################################################################################################################################
######################################################################################################################################################################

def AddPurchases():

    
    pattern = r"^\d+\.\d{2}$"
    validName = False
    validPrice = False
    validAmount = False
    nameOfPurchase = ""
    priceOfPurchase = ""
    actualPriceOfPurchase = 0.00
    amountOfPurchaseBought = ""
    actualAmountOfPurchaseBought = 0


    while (validAmount == False):
        amountOfPurchaseBought = input("Please enter the amount of the same item you bought: ")

        if (amountOfPurchaseBought.isdigit()):
            actualAmountOfPurchaseBought =  int(amountOfPurchaseBought)
            validAmount = True
        else:
            validAmount = False
        
    
    while (validName == False):
        nameOfPurchase = input("Please enter the name of the item purchased: ")
       
        if (len(nameOfPurchase) == 0):
            print("Please enter name of item correctly")
        else:
            validName = True
            
    while (validPrice == False):
        priceOfPurchase = input("Please enter the price of the item purchased: £")

        if re.match(pattern, priceOfPurchase):
            actualPriceOfPurchase = float(priceOfPurchase)
            validPrice = True
        else:
            print("Try again")

        
    tracker.add_item(nameOfPurchase, actualAmountOfPurchaseBought, actualPriceOfPurchase)
    print("Successfully added")
    Purchases()
     
#############################################################################################################################################################
#############################################################################################################################################################

def Purchases():
    selection = False


    while (selection == False):
        choice = input("1 - Add purchases\n2 - Remove purchases\n3 - View purchases\n4 - Menu\n5 - Exit\n")
        
        if (choice == "1"):
            selection = True
            AddPurchases()

        elif (choice == "2"):
            selection = True
            RemovePurchases()

        elif (choice == "3"):
            selection = True
            ViewPurchases()
    
        elif (choice == "4"):
            selection = True
            Menu()
            
        elif (choice == "5"):
            selection = True
            print("Have a good day")
            break

        else:
            print("Please enter a valid option")

#############################################################################################################################################################
#############################################################################################################################################################

def Menu():
    selection = False

    while (selection == False):
        choice = input("1 - Purchases\n2 - Exit\n")

        if (choice == "1"):
            selection = True
            Purchases()

        elif (choice == "2"):
            selection = True
            print("Have a good day!")
            break
    
        else:
            print("Please enter a valid option")    

Menu()

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
