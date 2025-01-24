#Mark Hanherly Abig CyberSec yr1
#e3{}[]
#Vending Machine time babyyyyy

Drinks = {
'A1':{'name':'Cok', 'price': 5.20, 'stock':99},
'A2':{'name':'Sprint', 'price': 3, 'stock':4},
'A3':{'name':'Hill Dew', 'price': 4, 'stock':10},
'A4':{'name':'Fantastic', 'price': 2.50, 'stock':6},
'A5':{'name':'Pepi', 'price': 3.50, 'stock':5},
}
Snacks = {
'B1':{'name':'Lays', 'price': 2.50, 'stock':4},
'B2':{'name':'Piatoos', 'price': 3.50, 'stock':1},
'B3':{'name':'Hadoogs', 'price': 3.50, 'stock':3},            #Vending machine menu
'B4':{'name':'Dotoes', 'price': 4.10, 'stock':2},
'B5':{'name':'Pingles', 'price': 5, 'stock':2},
}
Miscellaneous = {
'C1':{'name':'Grow Shroom', 'price': 8, 'stock':8},
'C2':{'name':'C4', 'price': 6, 'stock':9},
'C3':{'name':'Speed Up Pill', 'price': 2, 'stock':2},
'C4':{'name':'Fire Flower', 'price': 10, 'stock':1},
'C5':{'name':'Doom Shroom', 'price': 12, 'stock':5},
}

cart = []               #Cart for the items to go in

def Vend():
    print('This vending machine offers these Choose one :\n1. Snacks\n2. Drinks\n3. Miscellaneous')      #Tells the user the possible choices

def cart2():
    return sum(item['price'] for item in cart)              #this function is used to calc the items in cart

def purchases():
    for item in cart:
        print(f"Please be patient while we dispense your item")                     #shows the user what items are dispensed from the vending machine
        print(f"Thank you for buying!! Your {item['name']} has now been dispensed.")

def user_receipt():
    price_total = cart2()               
    print('Your Receipt is printing... Please wait.')
    for item in cart:                                                         #Give the user a receipt of what they bought including the total
        print(f"{item['name']}: {item['price']} AED")
    print(f'Total Price: {price_total} AED')
    print('Thank you for choosing our vending machine. Come again!')

def checkout():
    final_amount = cart2()
    while True:
        try:
            cash_money = float(input(f"Please enter {final_amount} AED to dispense your product: "))
            if cash_money == final_amount:
                purchases()     #if you have equal to the total it moves on
                break
            elif cash_money < final_amount:                                          #this is responsible for the payment and makes sure that the user pays the right amount
                print('The money entered is not enough brokie. Please try again.')        #if you have less it prints out this msg
            elif cash_money > final_amount:               
                change = cash_money - final_amount      #if you put more than required then it calculates for your change and moves on
                purchases()
                print(f"Your change is {change:.2f} AED. Thanks for buying!")
                break
        except ValueError:
            print('Invalid input. Please enter a valid number.')        #if you put anything other than numbers it gives a valueerror and prints out this msg

def display_menu(menu):
        for code, item in menu.items():
            stock = f"(In stock: {item['stock']})" if item['stock'] > 0 else "(Out of stock)"         #Shows the menu as well as its code, price and name
            print(f"{code}: {item['name']} - {item['price']} AED {stock}")

def run_all():

    while True:                 #This while loop keeps running till the user chooses to stop (by typing N if asked when they want more shi)
        Vend()
        category = input('What category do you wanna look at (Snacks, Drinks, Miscellaneous)?: ').capitalize()
        if category in ['Snacks', 'Drinks', 'Miscellaneous']:
            selected_category = {'Snacks': Snacks, 'Drinks': Drinks, 'Miscellaneous': Miscellaneous}[category]
            display_menu(selected_category)
        else:
            print("Category doesnt exist. Please try again.")
            continue

        item_code = input("Enter the code of the item you want: ").upper()
        if item_code in selected_category:
            item = selected_category[item_code]
            if item['stock'] > 0:            #this checks if item is in stock
                cart.append(item)   
                item['stock'] -= 1              #decreases stock by 1 everytime the user selects it
                print(f"{item['name']} has been added to your cart.")
            else:
                print(f"Sorry, {item['name']} is out of stock.")

        more_items = input('Wanna add more items? (Y/N): ').capitalize()       #asks the user if they want to add more or not
        if more_items == 'N':
            break

    if cart:
        print('\nYour cart items:')
        for item in cart:
            print(f"{item['name']} - {item['price']} AED")
        checkout()
        receipt_choice = input('you want a receipt? (Y/N): ').capitalize()
        if receipt_choice == 'Y':                                                 #asks the user if they want a receipt which prints out all the items chosen and total price
            user_receipt()

print('Welcome to my Vending Machine Cuh!')
run_all()                                       #Runs the whole Program
