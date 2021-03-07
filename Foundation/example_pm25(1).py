# new2.5(1).py

def main():
    PM = eval(input("The PM2.5 of today:"))

    if PM < 35:
        print("Good ,Go running!")
    elif PM < 75:
        print("Moderate, Go walking!")

    elif PM < 115:
        print("Unhealthy for sensitive group!")

    elif PM < 150:

        print("Unhealthy. limit prolonged exertion!")
    elif Pm < 250:

        print("Very unhealthy. Avoid prolonged exertion!")
    else:
        print("Hazardous. REMAIN INDOORS!")


main()
