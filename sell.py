import main
import datetime
def sell_laptop():
    laptops = main.store_details()
    Customer_Name = str(input("Write your Name:"))
    print("                                     Drakenight Store                                          ")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
    print('S.N''\t''Name of laptops''\t\t\t''Brand''\t\t\t''Price' '\t\t\t ''Quantity' '\t\t\t''Processor''\t\t''Graphics')
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
    SN = 1
    for name, specs in laptops.items():
        print(f"{SN}\t{name:<30}\t{specs['brand']:<20}${specs['price']:<20}\t{specs['quantity']:<20}\t{specs['processor']:<20}\t{specs['graphics']:<20}")
        SN +=1

    Success = False
    while Success == False:                                                                                                                       
        try:
            laptop_name = input("Enter name of the laptop: ")
            if laptop_name.upper() not in laptops:
                raise KeyError
            Success = True
        except KeyError:
            print(f"Error: {laptop_name} not found in stock.")

    laptop = laptops[laptop_name.upper()]
    Success = False
    while not Success:
        try:
            quantity = int(input("Enter the number of laptop that you want to buy: "))
            if quantity <= 0:
                print("Wrong Input! Please enter a number greater than 0.")
                continue
            
            if laptop['quantity'] < quantity:
                print(f"Sorry! We do not have enough {laptop_name} in stock to sell {quantity} units.")
                continue
            Success = True
        except ValueError:
            print("Wrong input! Input must be in a integer.")
    
    total_price_without_ship_cost= laptop['price'] * quantity
    ship = str(input("Do you need to get your laptop shipped?"))
    if(ship.upper() == "YES"):
        ship_cost = 50  
    else:
        ship_cost = 0 
    total_cost_with_ship_cost = total_price_without_ship_cost + ship_cost

    laptop['quantity'] -= quantity

    invoice =f"""----------------------------------------------
         "            Drakenight Store
         "                      Laliptur
         "----------------------------------------------
         "                SALE INVOICE
         "----------------------------------------------
         DATE: {datetime.datetime.now():%Y-%m-%d %H:%M:%S}
         CUSTOMER NAME: {Customer_Name.upper()}
         f"----------------------------------------------
         PRODUCT: {laptop_name.upper()}
         QUANTITY: {quantity}
         UNIT PRICE: ${laptop['price']:.2f}
        ----------------------------------------------
         SUBTOTAL: ${total_price_without_ship_cost:.2f}
         SHIPPING COST: ${ship_cost:.2f}
         TOTAL: ${total_cost_with_ship_cost:.2f}
        Thank you for your purchase!\n" \
         "We hope to see you again soon"""

    print(invoice)
    print("Check txt file for invoice")


    with open(f"{Customer_Name}_sale_invoice.txt", "w") as file:
        file.write(invoice)    

    #function that updates stock in txt file if laptop is sold
    with open('lap.txt', 'w') as file:
        for laptop_name, laptop_details in laptops.items():
            name = laptop_name
            brand = laptop_details['brand']
            price = laptop_details['price']
            quantity = laptop_details['quantity']
            processor = laptop_details['processor']
            graphics = laptop_details['graphics']
            file.write(f"{name}, {brand}, ${price}, {quantity}, {processor}, {graphics}\n")
