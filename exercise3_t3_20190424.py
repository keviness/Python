#exercise3_T3_20190324
name = "keviness"
password = "123434"
while True:
    meg_name = input("Enter your name:")
    meg_password = input("Enter your password:")
    if meg_name == name and meg_password == password:
        print("Welcome!")
        break
    else:
        print("The enter is wrong!")
