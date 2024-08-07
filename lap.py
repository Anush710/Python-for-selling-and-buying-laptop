file = open("lap.txt", "r")
lap_dictionary = {}
lap_id = 1
for line in file:
    line = line.replace("\n", "")
    lap_dictionary.update({lap_id: line.split(",")})
    lap_id = lap_id+1
file.close()

loop = True
while loop == True:
    print("Press 1 to sell the laptop to customer.")
    print("Press 2 to purchase from Manufacture.")
    print("Press 3 to Exit from the system.")
    print("/n")

    op=int(input("Enter any of the option to continue: "))

    print("\n")

    if op == 1:
        print("We are here.")
        print("\n")
    elif op == 2:
        print("We are here 1.")
        print("\n")
    elif op == 3:
        loop = False
        print("Thank you")
        print("\n")
    else:
        print("The option you have clicked is invalid")
        print("\n")
    

    
    
