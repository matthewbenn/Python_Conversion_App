import convert

def menu(name):
    DISTANCE_CHOICE = 1
    VOLUME_CHOICE = 2
    WEIGHT_CHOICE = 3
    LENGTH_CHOICE = 4
    TEMP_CHOICE = 5
    QUIT_CHOICE = 6
    
    error_count = 0
    i = 0
    try:
        display_menu()
        menu_choice = int(input('Enter your selection: '))
        print()
    except:
        print('You must enter a valid menu number')
        display_menu()
        menu_choice = int(input('Enter your selection: '))
    
    while menu_choice != QUIT_CHOICE and error_count < 4 and i < 10:
        if menu_choice == DISTANCE_CHOICE:
            # ---Question 1---
            try:
                # Requesting miles to convert
                miles = input(f"Good Sir {name}, how many miles would you like to convert to kilometers? ")
                if int(miles) > 0:
                    # Call conversion function
                    convert.milesToKm(name,miles)
                    # increment iteration counter
                    i += 1
                else:
                    print(f"The number of miles must be a number greater than 0")
                    # increment error counter
                    error_count += 1

            # if invalid entry is entered   
            except:
                print(f"The number of miles must be a number greater than 0")
                # increment error counter
                error_count += 1
          
            # If too many errors, exit the program and notify the user
            if error_count == 4:
                print('Too many errors!')
                error_count = 5
                convert.exit()

            # After 10x, return to the menu
            if i == 10:
                error_count = 0
                i = 0
                try:
                    display_menu()
                    menu_choice = int(input('Enter your selection: '))
                    print()
                except:
                    print('You must enter a valid menu number')
                    display_menu()
                    menu_choice = int(input('Enter your selection: '))

        elif menu_choice == VOLUME_CHOICE:
            # ---Question 2---
            try:
                # Requesting gallons to convert
                gallons = input(f"How many gallons, good Sir {name}, do you require converting to litres? ")
                if int(gallons) > 0:
                    # Call conversion function
                    convert.GalToLit(name,gallons)
                    # increment iteration counter
                    i += 1
                else:
                    print(f"The number of gallons must be a number greater than 0")
                    # increment error counter
                    error_count += 1

            # if invalid entry is entered   
            except:
                print(f"The number of gallons must be a number greater than 0")
                # increment error counter
                error_count += 1
          
            # If too many errors, exit the program and notify the user
            if error_count == 4:
                print('Too many errors!')
                error_count = 5
                convert.exit()

            # After 10x, return to the menu
            if i == 10:
                error_count = 0
                i = 0
                try:
                    display_menu()
                    menu_choice = int(input('Enter your selection: '))
                    print()
                except:
                    print('You must enter a valid menu number')
                    display_menu()
                    menu_choice = int(input('Enter your selection: '))
                
        elif menu_choice == WEIGHT_CHOICE:
            # ---Question 3---
            try:
                # Requesting pounds to convert
                pounds = input(f"Now, Sir {name}, how many pounds shall we convert into kilograms? ")
                if int(pounds) > 0:
                    # Call conversion function
                    convert.PoundsToKg(name,pounds)
                    # reset error count
                    error_count = 0
                    # increment iteration counter
                    i += 1
                else:
                    print(f"The number of pounds must be a number greater than 0")
                    # increment error counter
                    error_count += 1

            # if invalid entry is entered   
            except:
                print(f"The number of pounds must be a number greater than 0")
                # increment error counter
                error_count += 1
              
            # If too many errors, exit the program and notify the user
            if error_count == 4:
                print('Too many errors!')
                error_count = 5
                convert.exit()

            # After 10x, return to the menu
            if i == 10:
                error_count = 0
                i = 0
                try:
                    display_menu()
                    menu_choice = int(input('Enter your selection: '))
                    print()
                except:
                    print('You must enter a valid menu number')
                    display_menu()
                    menu_choice = int(input('Enter your selection: '))
                
        elif menu_choice == LENGTH_CHOICE:
            # ---Question 4---
            try:
                # Requesting inches to convert
                inches = input(f"Good Sir {name}, how many inches would you like to convert? ")
                if int(inches) > 0:
                    # Call conversion function
                    convert.InchesToCm(name,inches)
                    # reset error count
                    error_count = 0
                    # increment iteration counter
                    i += 1
                else:
                    print(f"The number of inches must be a number greater than 0")
                    # increment error counter
                    error_count += 1

            # if invalid entry is entered   
            except:
                print(f"The number of inches must be a number greater than 0")
                # increment error counter
                error_count += 1
              
            # If too many errors, exit the program and notify the user
            if error_count == 4:
                print('Too many errors!')
                error_count = 5
                convert.exit()
                
            # After 10x, return to the menu
            if i == 10:
                error_count = 0
                i = 0
                try:
                    display_menu()
                    menu_choice = int(input('Enter your selection: '))
                    print()
                except:
                    print('You must enter a valid menu number')
                    display_menu()
                    menu_choice = int(input('Enter your selection: '))

        elif menu_choice == TEMP_CHOICE:
            # ---Question 5---
            try:
                # Requesting temperature to convert
                Fh = input(f"What temperature does {name} want converted to Centigrade? ")
                if int(Fh) < 1000:
                    # Call conversion function
                    convert.FahToCel(name,Fh)
                    # reset error count
                    error_count = 0
                    # increment iteration counter
                    i += 1
                else:
                    print("The temperature must be less than 1000")
                    # increment error counter
                    error_count += 1

            # if invalid entry is entered   
            except:
                print("The temperature must be less than 1000")
                # increment error counter
                error_count += 1
              
            # If too many errors, exit the program and notify the user
            if error_count == 4:
                print('Too many errors!')
                error_count = 5
                convert.exit()
                    
            # After 10x, return to the menu
            if i == 10:
                error_count = 0
                i = 0
                try:
                    display_menu()
                    menu_choice = int(input('Enter your selection: '))
                    print()
                except:
                    print('You must enter a valid menu number')
                    display_menu()
                    menu_choice = int(input('Enter your selection: '))
    else:
        print()
        if menu_choice == QUIT_CHOICE:
            print()
            print(f"Have a brilliant holiday good Sir {name}, we hope you\'ll enjoy \n the United Kingdom so much, you\'ll never want to leave! \n Do not hestate to ask us for additional conversions.")
            error_count = 5
            i = 11

            

def display_menu():
    print()
    print('1) Convert some distance')
    print('2) Convert some volume')
    print('3) Convert some weight')
    print('4) Convert some length')
    print('5) Convert some temperature')
    print('6) Quit this immediately')
    print()
