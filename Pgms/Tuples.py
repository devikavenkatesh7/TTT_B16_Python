#creatioin of tuple
# Tuple=("phani","Kiran","kondaveeti",None)
# sortedTuple=sorted(Tuple)
# print(Tuple)
# print(sortedTuple)

# Tuple=tuple("phani",)
# print(Tuple)

# Tuple1=(1,2,"phani",["kiran","hello"])
# for x in range(len(Tuple1)):
#
#     if(isinstance(Tuple1[x],list)):
#         for y in range(len(Tuple1[x])):
#             if(Tuple1[x][y]=="hello"):
#                 Tuple1[x][y]="Kondaveeti"
#                 Tuple1[x].append(32)
#
#         # Tuple1[x] = tuple(Tuple1[x]) -will not work bcoz we are trying to modify data which is not possible
# print(Tuple1)


# Tuple1=(1,2,3)
# Tuple2=(1,5,6)
# print(id(Tuple1[0]))
# print(id(Tuple2[0]))

#if condition
# a=int(input("Enter the number 1: "))
# b=int(input("Enter the number 2: "))
# if(a>b):
#     if(a%b==0):
#         res="a is divisible by b"
#     else:
#         res="a is not divisble by b"
# elif(b>a):
#     if(b%a==0):
#         res="b is divisible by a"
#     else:
#         res="b is not divisible by a"
# print(res)

# print prime numbers in given range
# num=int(input())
# for x in range(2,num):
#     # print(x,"x")
#     c=0
#     for y in range(1, x//2+1):
#         # print(y,"y")
#         if(x%y==0):
#             # print("true")
#             c=c+1
#     if (c<=1):
#         print(x,"prime")



