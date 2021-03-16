#exercise3_t11_20190429
'''input:a:12, b:13, ...
   output:输入成功！'''
def add_data(data):
    name = input("Enter your name(a string):")
    age = eval(input("Enter your age(a number):"))
    data[name] = age
    print("project added successfully!")
    return data
def change_data(data):
    old_name = input("Enter the old name:")
    old_age = data.get( old_name, data[old_name])
    new_name = input("Enter your new name:")
    data[new_name] = old_age
    del data[old_name]
    print("project changed successfully!")
    return data
def visit_data(data):
    for k in data:
        s = "{}:{}".format(k, data[k])
        return s
def main():
    data = {}
    while True:
        Quest = input("Do you want to add or change data you input?(a or c)")
        if Quest == "a":
            add_data(data)
            print("Now, your new project is : ",visit_data(data))
        elif Quest == "c":
            change_data(data)
            print("Now, your new project is : ",visit_data(data))
        else:
            print("The end, Goodbye!~")
            break
if __name__ == "__main__":
    main()
        
    
        
    
    
        
        
