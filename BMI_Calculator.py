name = input ("Please enter your name: ")
print ("Nice to meet you, " + name + " :)")

height_cm = float ( input ("Please type in your height in cm: ") )
weight_kg = float ( input ("Thank you, " + name + ". Now please enter your weight in kg: ") )

bmi = weight_kg / ((height_cm / 100) ** 2)

print (" ")
if bmi >= 18.5 and bmi <= 25.00 :
    print ("Congratz! You're in the healthy range.")

elif bmi < 18.5 :
    print ("You are underweight.")

else :
    print ("You are overweight!")

print()
print ("----------------------------------------------- ")
print ("Thanks for using my program.")
