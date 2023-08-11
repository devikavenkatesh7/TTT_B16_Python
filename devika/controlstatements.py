salary = float(input("Enter salary"))
year = int(input("Enter year"))
if year > 5:
    bonus = 5
    bonus_amount = (salary * bonus) / 100
    print("5% bonous", bonus_amount)
else:
    print("not eligible")
length = (input("Enter length"))
breadth = input("Enter breadth")
if length == breadth:
    print("it is a square")
else:
    print("not a square")
