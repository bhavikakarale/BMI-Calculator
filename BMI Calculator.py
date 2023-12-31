name = input("Please enter your name: ")
weight = float(input("Please enter your weight in pounds: "))
height = float(input("Please enter your height in inches: "))
BMI = (weight*703) / (height*height)
print("Your BMI is: ", BMI)

if BMI>0:
    if (BMI<18.5):
        print("You are underweight")
    elif(BMI>=18.5 and BMI<24.9):
        print("You have normal weight")
    elif(BMI>=25 and BMI<29.9):
        print("You are over weight")
    elif(BMI>=30 and BMI<34.9):
        print("You are obese")
    elif(BMI>=35 and BMI<39.9):
        print("You are severely obese")
    elif(BMI<=40):
        print("You are morbidly obese")
    else:
        print(name, ",enter valid values")
