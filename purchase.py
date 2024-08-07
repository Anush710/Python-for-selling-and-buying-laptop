
import main
import datetime
def purchase_laptop():
    laptops = main.store_details()
    name_of_distributor = str(input("Enter name of distributor: "))
    success = False
    while success == False:
        try:
            laptop_name = input("Enter name of laptop you want to buy: ")
            if laptop_name.upper() not in laptops:
                raise KeyError
            success = True
        except KeyError:
            print(f"Error: {laptop_name} not found in stock.")
            
    laptop = laptops[laptop_name.upper()]
    success = False
    while not success:
        try:
            quantity = int(input("Enter the number of laptops you want to buy: "))
            if quantity <= 0:
                print("Invalid input! Please enter a number greater than 0.")
                continue
            success = True
        except ValueError:
            print("Error: Input must be a number.")
           
    total_prize_without_VAT = laptop['price'] * quantity
    VAT_amount = (0.13 * total_prize_without_VAT)
    total_prize_with_VAT = VAT_amount + total_prize_without_VAT

    laptop['quantity'] += quantity

    invoice =f"""----------------------------------------------
         "            Drakenight Store
         "                      Laliptur
         "----------------------------------------------
         "                SALE INVOICE
         "----------------------------------------------
    DATE: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    DISTRIBUTOR NAME: {name_of_distributor.upper()}  
    --------------------------------------------------
     f"PRODUCT: {laptop_name.upper()}\n" \
         f"QUANTITY: {quantity}\n" \
         f"UNIT PRICE: ${laptop['price']:.2f}
         f"--------------------------------------------------\n" \
         f"SUBTOTAL (WITHOUT VAT):  ${total_prize_without_VAT:.2f}
         f"VAT AMOUNT: ${VAT_amount:.2f}\n" \
         f"TOTAL AMOUNT (WITH VAT): ${total_prize_with_VAT:.2f}\n" \
    --------------------------------------------------
    THANK YOU FOR YOUR BUSINESS!
    We hope to see you again soon. 
    """
    print("Purchase Successful!")
    print(invoice)

    with open(f"{name_of_distributor}_purchase_invoice.txt", "w") as file:
        file.write(invoice)

    #function which updates stock of laptop in txt file if laptop is purchased
    with open('lap.txt', 'w') as file:
        for laptop_name, laptop_details in laptops.items():
            name = laptop_name
            brand = laptop_details['brand']
            price = laptop_details['price']
            quantity = laptop_details['quantity']
            processor = laptop_details['processor']
            graphics = laptop_details['graphics']
            file.write(f"{name}, {brand}, ${price}, {quantity}, {processor}, {graphics}\n")
    
    
