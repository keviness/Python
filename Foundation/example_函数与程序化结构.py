# plots the growth of a 10-year investment

print("This program plots the growth of a 10-year investment")
principal = eval(input("Enter the initial principal:"))
apr = eval(input("Enter the annualized interest rate:"))
for year in range(1, 11):
    principal = principal * (1 + apr)
    print("%2d" %year, end = '')
    total = int(principal * 4/1000.0)
    print("*" * total)

print("0.0k  2.5k  5.0k  7.5k  10.0k")
