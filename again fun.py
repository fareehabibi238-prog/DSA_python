# 1 print inverted triangle of star
#def row(n):
 #for i in range(n,0,-1):
  #return "*" *i
#print(row(6))





# 2 convert the string into uppercase
#def to_upper(s):
   
 #  return s.upper()
#print (to_upper("hello"))






# 3 length of string
#def length(s):
   
 #  return len(s)
#print(length("python "))




#4 Smallest in list
#def smallest(lst):
 #   return min(lst)
#print(smallest([2, 8, 1, 10, 5]))  




# 5 Average of list
#def average(lst):
   # return sum(lst) / len(lst)
#print(average([2, 4, 6, 8]))  





# 6 Remove duplicates
#def dup(lst):
 #   return list(set(lst))
#print(dup([1,2,2,3,4,4,5])) 




# 7 Sort ascending
def sorting(lst):
    return sorted(lst)

print(sorting([5,2,8,1]))  



# 8 Celsius to Fahrenheit
#def f(c):
 #   return (c * 9/5) + 32
#print(f(0))  



# 9 find the minimum number

#def find(arr):
 #   minimum = arr[0]
  #  for num in arr:
   #     if num < minimum:
    #        minimum = num
    #return minimum

#print(find([10, 4, 7, 1, 9])) 




# 10 find factorial recursive
#def fac(n):
    #if n == 0 or n == 1:
       # return 1
   # return n * fac(n-1)

#print(fac(9))   