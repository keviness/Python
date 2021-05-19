# BMI 2018.11.4

height = eval(input("enter your height:"))
weight = eval(input("enter your weight:"))
BMI = weight / height**2
if BMI < 18.5:
    print("so slim ")

elif BMI <25 :
    print("healthy")

elif BMI < 28 :
    print("litter fat")

elif BMI < 32:
    print("fat")

else:
    print("so fat")
