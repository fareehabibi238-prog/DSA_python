



# 1 check the string is anagram or not
#s1=input("enter first string:")
#s2=input("enter second string:")
#if sorted(s1) ==sorted (s2):
 #   print("anagram")
#else:
 #   print("not anagram")




# 2 check the palidram in a list
#words={"python","world","learning"}
#for w in words:
 #   if w==w[:: -1]:
  #      print()
#print(w,"is palidrom")



#3 find positive and negative number in list
#list={1,-1,2,-2,3,-3}
#p=0
#n=0
#for i in list:
 #   if i>0:
  #      p+=1
   # else:
    #    n+=1
#print("the total positive number is:",p )
#print("the total negative number is:",n)




#4 take string and cut the vowels
#s=input("enter a string:")
#final=""
#for char in s:
 #   if char.lower() not in "aeiou":
  #      final+=char
#print("the string without vowels",final) 






#5 take input from user and take his choice and perfoam opreation
#a=int(input("Enter the value of a:"))
#b=int(input("Enter the value of b:"))
#print("1:for addition")
#print("2:for substraction")
#print("3:for multiplication")
#print("4:for division")
#choice=int(input("enter your choice: "))
#if choice==1:
 #   print("a+b=",a+b)
#elif choice==2:
 #   print("a-b=",a-b)
#elif choice==3:
 #   print("a*b=",a*b)
#elif choice==4:
 #   print("a/b=",a/b)
#else:
 #   print("you enter a wrong number!")    






# 6 cut the negative numbers in list
L=[1,-1,2,-2,3,-3,4,-4]
result=[]
for n in L:
    if n>=0:
        result.append(n)
print("list without negative numbers:",result)




# 7 remove duplicates in list
#L=[1,2,3,3,4,4,9,6,8,5,7]
#result=[]
#for n in L:
    #if n not in result:
       # result.append(n)
#print("list without duplicates:",result)






# 8 check the number is even or odd
#n=int(input("Enter a number:"))
#if n %2==0:
    #print("you enter a even number")
#else:
   # print('you enter a odd number')




# 9 find the largest of three numbers
#x=5
#y=6
#z=10
#if x>y and x>z:
    #print('x is a largest number')
#elif y>x and y>z:
    #print("y is the largest number")
#elif z>x and z>y:
    #print("z is the largest number")
#else:
    #print("all numbers are equal")




      