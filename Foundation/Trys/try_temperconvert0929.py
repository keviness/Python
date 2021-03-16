# tempconvert.py

tempstr = input("Enter a temperature please:")

if tempstr[-1] in ['F','f'] :
    C = (eval(tempstr[0:-1]) - 32) / 1.8
    print("\n The converted temperature is:{:.2f}C".format(C))

elif tempstr[-1] in ['C','c']:
    F = 1.8 * eval(tempstr[0:-1]) + 32
    print("\n The converted temperature is: {:.2f}F".format(F))
