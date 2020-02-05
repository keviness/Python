#exercise3_t7_20190426
'''input:year/month/day
   output:alldays'''

while True:
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    yea_mon_day = input("Enter(year/month/day):")
    if yea_mon_day !="":   
        yea , mon, day = yea_mon_day.split("/")
        yea = int(yea)
        mon = int(mon)
        day = int(day)
        if yea%4 == 0 or yea%400 == 0:
            if 0<mon<13 and 0<day<32:
                mon[1] = 28
                for i in month[0:mon-1] :
                    day += i
                print("the day is the\'s:",day)
            else:
                print("The range is wrong!")
        else:
            if 0<mon<13 and 0<day<32:
                for j in month[0:mon-1]:
                    day += j
                print("the day is the\'s:",day)
            else:
                print("The range is wrong!")
        
    else:
        print("The end!")
        break
        
    
