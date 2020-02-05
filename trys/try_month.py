# month.py


months = "JanFebMayAprMayJunJulAugSepOctNovDec"
n = input("输入一个月份数字（1-12）：")
pos = (int(n)-1) * 3
monthAbbrev = months[pos : pos + 3]

print("月份简历是：" + monthAbbrev + ".")
