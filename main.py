# import required files
import menu_system
import convert

# erase contents of existing data from previous runs
erase_file = open('conversions.txt','w')
erase_file.close()

def main():
    # Initialize error counter
    error_count = 0
    # loop for getting valid name
    while error_count < 4:
        name = input("By what name shall ye be called? ")

        # Validate input
        if len(name) <= 0:
            print(f"We can\'t continue sir, unless we know what to call you.")
            error_count += 1
            input("Press Enter to continue.")

            # Set message for error count hit
            if error_count == 4:
                print('Too many errors!')
                convert.exit()

        else:
            error_count = 5
            menu_system.menu(name)

                
# call the main function
main()
    
