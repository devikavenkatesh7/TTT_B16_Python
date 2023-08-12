def NumberCheckin(num):
    if(num%2==0):
        number='Even'
    else:
        number="Odd"
    return number
n=10
res=NumberCheckin(n)
print("Given ","number ", n, " is ",res," Number")

