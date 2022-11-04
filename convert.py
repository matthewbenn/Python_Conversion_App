def milesToKm(name,miles):
    # Convert the miles
    m_to_km = (float(miles) * 1.6)
    miles_display = float(miles)
    
    # Providing converted distance to the user
    dist_msg = print(f"Sir {name}, That converts to {m_to_km:,.2f}. There are {m_to_km:,.2f} many kilometers in {miles_display:,.2f} miles.")

    # open file for writing
    file = open('conversions.txt','a')
    
    # Write conversion info to file
    file.write('miles, ' + str(f"{miles_display:,.2f}") + ', kilometers, ' + str(f"{m_to_km:,.2f}\n"))

    # Close the file
    file.close()
    
    return dist_msg


    
def FahToCel(name,Fh):
    # Convert the temp
    Fh_to_C = (float(Fh) - 32) * (5/9)
    Fh_display = float(Fh)
    
    # Providing converted temperature to the user
    temp_msg = print(f"\"What temperature is {Fh_display:,.2f} degrees in Centigrade?\", you wondered aloud. The answer is {Fh_to_C:,.2f} degrees, Sir {name}. {Fh_display:,.2f} degrees Fahrenheit is {Fh_to_C:,.2f} degrees Centigrade.")

    # open file for writing
    file = open('conversions.txt','a')
    
    # Write conversion info to file
    file.write('fahrenheit, ' + str(f"{Fh_display:,.2f}") + ', celsius, ' + str(f"{Fh_to_C:,.2f}\n"))


    # Close the file
    file.close()

    return temp_msg 



def GalToLit(name,gallons):
    # Convert the volume
    gal_to_L = (float(gallons) * 3.9)
    gal_display = float(gallons)

    # Providing converted volume to the user
    vol_msg = print(f"Good Sir {name}, when you asked how many litres were in {gal_display:,.2f} gallons, we knew you\'d be thrilled to discover the answer is {gal_to_L:,.2f} litres!")

    # open file for writing
    file = open('conversions.txt','a')

    # Write conversion info to file
    file.write('gallons, ' + str(f"{gal_display:,.2f}") + ', liters, ' + str(f"{gal_to_L:,.2f}\n"))


    # Close the file
    file.close()

    return vol_msg



def PoundsToKg(name,pounds):
    # Convert the the weight
    lb_to_kg = (float(pounds) * 0.45)
    pounds_display = float(pounds)
    
    # Providing converted weight to the user
    weight_msg = print(f"Hey Sir {name}! Do you think its possible for there to be {lb_to_kg:,.2f} kilograms in {pounds_display:,.2f} pounds? Well, it\'s true!")

    # open file for writing
    file = open('conversions.txt','a')

    # Write conversion info to file
    file.write('pounds, ' + str(f"{pounds_display:,.2f}") + ', kilograms, ' + str(f"{lb_to_kg:,.2f}\n"))


    # Close the file
    file.close()

    return weight_msg
    
def InchesToCm(name,inches):
    # Convert the length
    in_to_cm = (float(inches) * 2.54)
    inches_display = float(inches)
    
    # Providing converted length to the user
    len_msg = print(f"I know you won\'t believe me, good Sir {name}, but it\'s true. There are {in_to_cm:,.2f} centimeters in {inches_display:,.2f} inches. Who could have guessed?")

    # open file for writing
    file = open('conversions.txt','a')

    # Write conversion info to file
    file.write('inches, ' + str(f"{inches_display:,.2f}") + ', centimeters, ' + str(f"{in_to_cm:,.2f}\n"))

    # Close the file
    file.close()

    return len_msg

def exit():
    print('The program has ended due to excessive errors.')
