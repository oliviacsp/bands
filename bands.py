#BRUCES AND SHEILAS
#Jalaya King and Olivia Luchetti
#NEED A LIST








import random

#^^^^ PROCEDURES (need 2)


#MAIN PROGRAM

print("Welcome to Bruces and Sheilas")
print("")
print("")

    
#RANDINT OF 4 DIG START NUM
for n in range(0,12):
    dig1=str(random.randint(1,9))
    dig2=str(random.randint(0,9))
    dig3=str(random.randint(0,9))
    dig4=str(random.randint(0,9))
    
    #if dig1==dig2 or dig1==dig3 or dig1==dig4 or dig2==dig1 or dig2==dig3 or dig2==dig4 or dig3==dig1 or dig3==dig2 or dig3==dig4 or dig4==dig1 or dig4==dig2 or dig4==dig3:
    if dig1!=dig2 or dig1!=dig3 or dig1!=dig4 or dig2!=dig1 or dig2!=dig3 or dig2!=dig4 or dig3!=dig1 or dig3!=dig2 or dig3!=dig4 or dig4!=dig1 or dig4!=dig2 or dig4!=dig3:
         print(dig1+dig2+dig3+dig4)

        #print("Please choose a 4 digit integer: ")
        #else:
            
            
