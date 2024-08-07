import sell
import purchase
import sys

def choose_category():
    print("\t\t\t\t-----Welcome to Drakenight Store-----")
    print("""
        Enter the desired number to view the detail
        1 : Sell
        2 : purchase
        3 : Exit Store
        """)
    option = input("Enter which option you want to choose ")
    if option.upper() == "1":
        sell.sell_laptop()
    elif option.upper() == "2":
        purchase.purchase_laptop()
    elif option.upper() == "3":
        print("Thank you for your visit!")
        sys.exit()
    else:
        print("Incorrect input")

while True:
    try:
        choose_category()
    except Exception as e:
        print(f"An error occurred: {e}")
        continue
    
    
          
