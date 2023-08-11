# title method()

# str1="hell0-good afternoon"
# str2=str1.title()
# print(str2)
# ---------------------------------------------------------------------------------------
# Slicing:

# str1="I am phani kiran"
# str2=str1[2:11:2]+str1[11:]
# print(str2)
# ---------------------------------------------------------------------------------------
# isdigit()

# n="123456"
# stat=n.isdigit()
# print(stat)

# problem
# Using ASCII values of characters, count and print all the digits using isdigit() function.
#
# Algorithm:
#
# Initialize a new string and a variable count=0.
# Traverse every character using ASCII value, check if the character is a digit.
# If it is a digit, increment the count by 1 and add it to the new string, else traverse to the next character.
# Print the value of the counter and the new string.

# newStr=""
# c=0
# for x in range(int(input("Enter the limit: "))):
#     j=chr(x)
#     if(j.isdigit()==True) :
#         newStr=newStr+j
#         c=c+1
# print(newStr)
# print(c)

# subscripts comes under digits only
# n="3"
# m="4"
# num='3\u00B2'
# stat=num.isdigit()
#
# print(num)
# if(num.isdigit()==True):
#      stat="Num comes under digit"
# else:
#    stat="Num is not digit"
# print(stat)

# decimalPoints
# n="3.125"
# stat=n.isdigit()
# print(stat)
# res="num is digit" if (n.isdigit()==True) else "Num is not digit"
# print(res)

# ---------------------------------------------------------------------------------------
# String find method
# str1="Geeks for Geeks"
# str2=str1.find("Geeks ",2)
# print(str2)

# program to find no.of occurences
# str1="hello I am Phani and hello are you practicing well hello thank you"
# str2="hello"
# starting_index=0
# c=0
#
# for i in range(len(str1)):
#     j=str1.find(str2,starting_index)
#     if j != -1:
#         starting_index=j+1
#         c=c+1
# print("no.of occurences of value",c)

# ---------------------------------------------------------------------------------------


# number="12345"
# number=number.lower()
# print(number)

# msg=input()
# c=0
# for i in msg:
#     if(i.isdigit()):
#         msg=msg.strip(i)
#
# print(msg)

# dt="180722"
# dt1="18/07/2022"
# print(dt==dt.lower())
# print(dt1==dt1.lower())


# sen=" banana"
# sen=sen.strip("a")
# print(len(sen))

# stri=input()
# for x in stri:
#     if(x.isdigit()):
#         stri=stri.strip(x)
#
# str=stri.upper()
# stat=str.startswith("HI5")
# print(stat)

# palindrome="Racecar"
# palindrome=palindrome.strip("r a ")
# print(palindrome)

# sen=".H.e.l.l.o. .w.o.r.l.d. "
# sen=sen.strip(".")
# print(sen)

# word="Hi5"
# for i in word:
#     print(id(i))
# print(id(word),"word")


# Given a string, write a program to modify the string as given below
# Add a space before each uppercase character excluding the first uppercase character
# txt = "TheLionKing"
# txt2 = txt[0]
# for i in range(1, len(txt)):
#     if (txt[i].isupper()):
#         txt2 = txt2 + " " + txt[i]
#     else:
#         txt2 = txt2 + txt[i]
#
# print(txt2)

# Check if given string is palindrome
# a=input()
# a=a.lower()
# if (a==a[::-1]):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# Given a Sentence write a program to remove all vowels in the given sentence.

# original_txt = input()
# txt2 = ""
#
# for i in original_txt:
#     j = i
#     i = i.lower()
#     if (i != "a") and (i != "e") and (i != "i") and (i != "o") and (i != "u"):
#
#         if (j.isupper()):
#             txt2 = txt2 + i.upper()
#         else:
#             txt2 = txt2 + i
#
# print(txt2)

# -------------------------------------------------
# write a program to shuffle the given string

# txt=input()
# shuffled_txt=""
# for x in range(len(txt)):
#     index=int(input("Enter index values: "))
#     shuffled_txt= shuffled_txt + txt[index]
#
# print(shuffled_txt
#

# season=input()
# shuffle=""
# for i in range(len(season)):
#     index=int(input())
#     shuffle=shuffle+season[index]
#     print(shuffle)

# i=0
# s=0
# while(i<3):
#     j=0
#     while(j<3):
#         if((i**j)):
#             s=s+1
#         j=j+1
#     i=i+1
# print(s)

# for i in range(0,1):
#     for j in range(1,3):
#         print(i)
# k=0
# while(k<3):
#     l=3
#     while(l<3):
#         print(k)
#         l=l+1
#     k=k+1

# c1=0
# c2=0
# for i in range(3,5):
#     j=4
#     while(j<6):
#         if(i<j):
#             c2=c2+1
#         else:
#             c1=c1+1
#         j=j+1
# print(c2)
# print(c1)

# country=input()
# total=0
# for i in range(0,len(country)):
#     for j in range(0,len(country)):
#         if(i==j):
#             total=total+1
#             print(total)
# print(total)

# cond=True and False
# if cond:
#     for i in range(1,5):
#         for j in range(0,1):
#             print(i)
# else:
#     for i in range(1,4):
#         for j in range(0,1):
#             print(i)


# num=int(input())
# for i in range(1,3):
#     k=num-1
#     while(k>=0):
#         s=" "*k
#         st="* "*(i-1) +"*"
#         k=k-1
#     print(s+st)

# txt1="Program"
# txt2="Code"
# s=0
# for a in txt1:
#     for b in txt2:
#         if(a==b):
#             s=s+1
# print(s)

# t1=1
# t2=0
# for i in range(4,6):
#     j=6
#     while(j<8):
#         if(i<j):
#             t2=t2+1
#         else:
#             t1=t1+1
#         j=j+1
# print(t2)
# print(t1)

# decorators
# def sample_divide(func):
#     def inner(a,b):
#         print("Ia m goint to divide a and b")
#         if(b==0):
#             print("cant divide")
#         return func(a,b)
#     return inner
#
# @smart_divide
# def divide(a,b):
#     print(a/b)
#     divide(20,10)


# txt="Word"
# print(ord(txt))
# print(ord("t"))
# print(ord("c"))
# print(ord("a"))

# message=input()
# c1=0
# c2=0
# c3=0
# for i in range(len(message)):
#     if(message[i].isdigit()):
#         continue
#     elif(ord(message[i])>=65 and ord(message[i])<=90):
#         c2=c2+1
#     elif(ord(message[i])>=97 and ord(message[i])<=122):
#         c1=c1+1
#     else:
#         c3=c3+1
# print(c1)

# Given a sentence S contains space-separated words, write a proram
# to print the word that comes first when the words are in dictionary order

# s=input()
# first_wrd=s
# wrd=""
# for i in range(len(s)):
#     char=s[i]
#     wrd=wrd+char
#     if(char==" " or i==len(s)-1):
#         if( wrd.lower() < first_wrd.lower()):
#             first_wrd=wrd
#         wrd=""
#
# print(first_wrd)

# def distinct_chars(word):
#     count = 0
#     l = list(word)
#     for i in range(len(l) - 1):
#         if l[i] == l[i + 1]:
#             l.insert(i - 1, l.pop(i))
#             count += 1
#     res = ''.join(l)
#     if count == 0:
#         return res
#     else:
#         return distinct_chars(res)
#
#
# print(distinct_chars('asseccessories'))
# print(distinct_chars('tresspassing'))
# print(distinct_chars('quee'))
# print(distinct_chars('eeabc'))
# print(distinct_chars('eeaabc'))

#Finding the min value word in a string
# s = input()
# first_wrd = s
# last_wrd = ""
# wrd = ""
#
#
# for i in range(len(s)):
#
#     char = s[i]
#     wrd = wrd + char
#
#     if (char == " " or i == len(s) - 1):
#         if (first_wrd.lower() > wrd):
#             first_wrd=wrd
#
#
#
#         wrd = ""
# print(first_wrd)

#Finding the max val word in string
# s=input()
# maxValue=""
# new_sen=""
# minVal=""
# for i in range(len(s)):
#     if s[i]==" ":
#         maxValue=s[:i]
#         new_sen=s[i+1:]
#         minVal=maxValue
#         break
# # print(maxValue)
# # print(new_sen)
# wrd=""
# for j in range(len(new_sen)):
#     char=new_sen[j]
#     wrd=wrd+char
#     if(char==" " or j==len(new_sen)-1):
#         if(maxValue.lower()<wrd.lower()):
#
#
#         wrd=""
# print(maxValue)
# print(minVal)

#Finding the min val and max val of a string
# s=input()
# minVal=""
# wrd=""
# res=""
# for i in range(len(s)):
#     if(s[i]==" "):
#         minVal=s[:i]
#         newSen=s[i+1:]
#
#         break
# for j in range(len(newSen)):
#     char=newSen[i]
#     wrd=wrd+char
#     if(char==" " or j==len(newSen)-1):
#         if(minVal.lower()<wrd.lower()):
#             res=wrd+res
#             minVal=wrd
#         wrd=""
# print(minVal)




# s= "tosdfsdfsdfsdfsdfsdfsdfsdf get the ball rolling ldsjflsjdljfsld"
#
# lists = s.split(" ")
#
# max = 0
# min = 0
# print(lists)
# for item in lists:
#
#     if min == 0:
#         min = ord(item[0])
#
#     if ord(item[0]) < min:
#         min = ord(item[0])
#     elif ord(item[0]) >= max:
#         max = ord(item[0])
#
# print( chr(max)+" "+chr(min))



# def fun(a,b):
#     s=a+b
#     continue
#     print(s)
# call=fun(9,3)

# def fun(l):
#     l=l*5
#     print(l)
# l=[1,2,3,4]
# print(l*5)
#the above  code prints[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4]

# def fun(l):
#     for i in range(len(l)):
#         l[i]=l[i]*5
#     print(l)
# l=[1,2,3,4]
# ans=fun(l)
# print(l)


# def fun (l):
#     l=l*5
#     print(l)
# l=6
# ans=fun(l)
# print(l)


# s=input()
# minVal="z"
# maxVal="a"
#In this pgm we took z as min value and a as max Value
#because z is the maximum char in letters so that any char other than z
#is  less than z.
#Same In case of a any char other than a is greater than a.
# wrd=""
# for i in range(len(s)):
#     char=s[i]
#     if(char !=" "):
#         wrd=wrd+char
#     if(char==" " or i==len(s)-1):
#         if(wrd.lower() < minVal.lower()):
#             minVal=wrd
#         if(wrd.lower() > maxVal.lower()):
#             maxVal=wrd
#         wrd=""
# print(minVal)
# print(maxVal)

#Given a variable name S, check if S is a valid variable name. The
#variable name is valid if it contains only upper case letters, lowercase
# and digits

#print True if string contains lowercase and  uppercase or lowercase and numbers.
#print False if string contains other than above cases except " ".

# s=input()
# is_valid=True
# for i in range(len(s)):
#     unicode=ord(s[i])
#     valid_char=(65<=unicode and unicode<=90) or (97<=unicode and unicode<=122) or(48<=unicode and unicode<=57)
#
#     if not valid_char:
#         is_valid=False
# print(is_valid)

#Given a Sentence S, write a program to print the sentence by replacing
#the first letter of every word with its next letter based on its unicode value

#Ex:East and West
#Fast Bnd Xest
#
# s=input()
# res=""
# index=100
# for i in range(len(s)):
#     if(i==index):
#         continue
#     char=s[i]

#     if(i==0):
#         unico=chr(ord(char)+1)
#     elif(i!=0 or char!=" "):
#         unico=chr(ord(char))
#     res=res+unico
#     if(char==" "):
#        index=i+1
#        unico=chr(ord(s[i+1])+1)
#        res=res+unico
# print(res)

#Given a string S, write a program that prints the character with
#the Least Unicod Value and the Character with the Highest Unicode Value separated by a space



#round
# a="phani"
# a=round("k")
# print(a)
#throws error that type str doesn't define __round__ method

# a=3.1456
# a=round(a,4)
# print(a)


# l=[1,2,3,4,5]
# l1=[7,8]
# l2=[8,9]
# l.extend(l1,l2)
# #extend takes only one argument that too iterable object
# print(l)

# Extend:extend will take only one  iterable object and it expands elem in it and add it to existing list
#append: append will take only one object but doesn't matter whether it is iterable or not

#String is an immutable object that is the reason if we add any new char to the existing obj , it creates
#another obj will be created with modified obj.

#Ex:
# a=10
# b=10
# print(id(a))
# print(id(b))
# c="gopi"
# d="gopi"
# print(id(c))
# print(id(d))
# c="gopi"+"e"
# print(id(c))
# print(id(d))


# l=[1,2,3,4,5]
# l=l[2:4
#     :-1]
# print(l)
# t=(1,2)
# l=[1,2,3,4]
# d={"k1":"value1","t1":"valu2"}
# c=d
# print(c)
# print(id(c))
# print(id(d))
# c=0
# while(c<5):
#     print("Hi")
#     c+=1

# def fun(a=10,b):
#     return a+b
# x=fun(2)
# print(x)
#The default parameter should come at end

# def fun(a,b=10):
#     return a+b
# x=fun(2,5)
# print(x)
#when we pass arg the default param will get override by passed arg

# def fun(*par):
#     return 5,1,15,25
# x=fun()
# print(x)

# tax=round((42.562+2.531),1)
# print(tax)
# cond=(tax==45.1)
# print(cond)
# print(cond=="True")

# num="5.57865"
# print(round(float(num)))
# print(float(num))

# num=5.54
# print(round(num),"k")

# wrd="4.562"
# new_str=wrd*2
# print(len(new_str))
# new_str=new_str[4:]
# print(new_str)
# new_str=float(new_str.strip("."))
#strip method is used to remove head and trail part of str
#Here "." is in middle of string so it won't work
# print(new_str)
# print(round(new_str))

# res1="49.99"
# res2="49.531"
# val1=round(float(res1))
# val2=round(float(res2))
# #The digit after decimal point should be above 5 to get next number or else the number will not increase
# print(val1,val2)
# val=(round(float(res1)))>=round((float(res2)))
# print(len(res1))
# print(val)

# print((round(99.99,1)) < round(99.999,2))
# input1="5.46"
# res=input1*2
# res=res[7:]
# print(res)
# res=float(res.strip("."))
# print(res)
# res=round(res)
# print(res)

# nm="5.541"
# res=int(nm)
# print(res)
#Throws Value error

# print((round(24.567,0)))

# val=4.246
# print(int(val))
# print(round(val))

# val=3.45
# print(round(val))
#
# num=((0.5*0.2))
#
# print(num)

# num=99.999
# print((round(float(num),1)) < round(float(num),3))


# num=24.567
# num1=round(num,0)
# print(num1)
# print(type(round(24.567,0)))

# num=99.999
# # print(round(num,l))
# print(round(num))
#throws name error

# num="2.456"
# num2="3.456"
# num=round(float(num))
# print(num)

# val=5.462
# print(int(val) != round(val))
import requests
# import requests
#
# url = "https://p7evogw7di.execute-api.us-east-1.amazonaws.com/test/movies"  # Replace with the URL that returns JSON data
#
# response = requests.get(url)
#
# if response.status_code == 200:
#     data = response.json()  # This parses the JSON response into a Python dictionary
#     print("Fetched JSON data:", data)
# else:
#     print("Failed to fetch data. Status code:", response.status_code)

# import requests
# import json
# url = "https://p7evogw7di.execute-api.us-east-1.amazonaws.com/test/movies"
#
# response = requests.get(url)
# response = response.content.decode()
# jsonData = json.loads(response)
#
# print("Below are avaialble movies for booking")
#
# for dict in jsonData:
#     print(dict["MovieName"])

# if response.status_code == 200:
#     data_list = response.json()  # Parse JSON array response into a Python list of dictionaries
#     print("Fetched JSON data:", data_list)
# else:
#     print("Failed to fetch data. Status code:", response.status_code)


# import sys
# def fun():
#     l=[]
#     for i in range(5):
#         l.append(i)
#     return l
# ans1=fun()
# print(ans1)
# print(type(ans1))
# print(sys.getsizeof(ans1))
# print(ans1.__sizeof__)

# import sys
# def gen():
#     for i in range(5):
#         yield  i
# ans2=gen()
# print(ans2)
# print(ans2.__next__())
# print("Hi")
# print(ans2.__next__())
# print(ans2.__next__())
# print(type(ans2))
# print(sys.getsizeof(ans2))
# print(ans2.__sizeof__())

# l=[12,3,4,5]
# l=l.sort()
# l=l.count(5)
# a=print("5")
# print(a)
# print(l)
#
# name="phani2000@"
# name=sorted(name)
# print(name)

#decorator:a function that takes another function as an argument

# minage=18
# def voteeligibility(fun):
#
#     def check(num):
#
#         if(num>minage):
#             num=num+10
#         else:
#             print("Not Eligible")
#         return fun(num)
#     return check
#
# @voteeligibility
# def vote(age):
#     print("hello",age)
#
# (vote(25))

# n=5
# end=n*5
# end_limit=end-1
# start=65
# spaces=0
# for i in range(0,end_limit):
#     if(i==0 or i== end_limit):
#         res = (" ") * (n - i) + (chr(start) + " ")
#     elif(i<=4):
#         start=start+1
#         res=(" ") *(n-i)+(chr(start)+" ")+("  ") * spaces +(chr(start)+" ")
#         spaces=spaces+1
#     elif(i>4):
#         start=start-1
#         res=(" ")*(n-i)+(chr(start)+" ")+("  ")* spaces + (chr(start)+" ")
#         spaces=spaces-1
#     print(res)


    # elif(i>1):
    #
    #     res=("  ")*(n-i)+(chr(start)+"  ")+(" ")*(spaces)+(" "+chr(start))
    #     spaces = spaces + 1
    # print(res)
    # start=start+1

# n=int(input())
# hollowSpace=0
# end=n*2
# end_limit=end-1
# star=65
# spaces=0
# res=""
# for i in range(end_limit):
#     if(i==0 or i==end_limit-1):
#         star=65
#         res=(" ")*(n)+(chr(star)+" ")
#     elif(i<=n-1):
#         spaces=i-1
#         star = star + 1
#         res=(" ")*(n-i)+(chr(star)+" ")+("  ")*(i-1)+(chr(star)+" ")
#
#     elif (i > n-1 and i <= end_limit - 2):
#             spaces=spaces-1
#             star=star-1
#             res=(" ")*((i+2)-n)+(chr(star)+" ")+("  ")*(spaces)+(chr(star)+" ")
#     print(res)







#-----------------------------------------------
# n = int(input())
# alpha = 65
# for row in range(n):
#     left_spaces = " " * (n - row - 1)
#     hollow_spaces = " " * (2 * row - 1)
#     if row == 0:
#         each_row = left_spaces + chr(alpha)
#         alpha += 1
#     else:
#         each_row = left_spaces + chr(alpha) + hollow_spaces + chr(alpha)
#         alpha += 1
#     print(each_row)

# alpha -= 2
#
# for row in range(1, n):
#     left_spaces = " " * row
#     hollow_spaces = " " * (2 * (n - row - 1) - 1)
#     if row == n - 1:
#         each_row = left_spaces + chr(alpha)
#     else:
#         each_row = left_spaces + chr(alpha) + hollow_spaces + chr(alpha)
#         alpha -= 1
#     print(each_row)

#
# n = int(input())
# end = n * 2
# digits = 1
# p = 1
# end_limit = end - 1
# hollowSpace = 0
# for i in range(end_limit):
#     if (i == 0 or i == end_limit - 1):
#         digits = 1
#         res = (". ") * (n - 1) + ("0 ") * (digits) + (". ") * (n - 1)
#     elif (i > 0 and i <= n - 1):
#         digits = digits + 2
#         res = (". ") * (n - i - 1) + ("0 ") * (digits) + (". ") * (n - i - 1)
#
#     elif (i > n - 1 and i <= end_limit - 2):
#         digits = digits - 2
#         res = (". ") * (p) + ("0 ") * (digits) + (". ") * p
#
#         # res=(". ")*(p)+("0 ")*(digits)+(". ")*p
#         p = p + 1
#     print(res)