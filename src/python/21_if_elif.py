# SHOW TICKET PRICING
# 1 TO 3 (FREE)
# 4 TO 10 (150)
# 11 TO 60 (250)
# ABOVE 60 (200) 

age = int(input("Enter your age :-  ").strip())
if age>=1 and age<=3:
    print("FREE TICKET")
elif age>3 and age<=10:
    print("TICKET PRICE = 150 ")
elif age>10 and age<=60:
    print("TICKET PRICE = 250 ")
elif  age>60:
    print("TICKET PRICE = 200 ")