def table(n,i):

    if(i>10):
        return
    print(n , " *" , i, " = " , n*i)
    return table(n,i+1)

N=12
table(N,1)
