"""def fun(arr1,arr2):
    time1 = 0
    for i in range(len(arr1)):
        if i % 2 == 0:
            time1 += arr1[i]
        else:
            time1 += arr2[i]
    time2 = 0
    for i in range(len(arr2)):
        if i % 2 == 0:
            time2 += arr2[i]
        else:
            time2 += arr1[i]

    return min(time1, time2)
print(fun([]))"""










"""def fun(arr):
 output=[]
 for i in arr:
    if i==i:
       output.append(i)
    if i==i+1:
       output.append(i) 
 return output
print(fun([1,2,2,3,4,5]))"""




"""def fun(arr):
 output=[]
 freq={}
 for i in arr:
    if i  in freq:
        freq[i]+=1
    else:
        freq[i]=1
 for n in freq:
    if freq[n] %2==0:
        output.append(n)
 if output:
    return output
 else:
   return -1
 
print(fun([26,12,56,34,32]))"""






"""arr=(1,4,9,16,25,36,49,64,81,100,49)
x=49
ind=0
for i in range(len(arr)):
    if arr[i]==x:
        print("number found at index:",ind)
        
        ind+=1"""



"""def fun(arr,k):

   arr.insert(arr[-k],arr[k-1])
   arr.pop(k-1)
   print(arr)
print(fun([1,2,3,4,5,6,7,8,9],3))"""






"""def fun(date,car,fine):
 count=0
 if date%2==0:
    for i in range(len(car)):
        if car[i]%2==1:
            count+=fine[i]
 else:
    for i in range(len(car)):
        if car[i]%2==0:
            count+=fine[i]       
 return count
print(fun(12,[2375, 7682, 2325, 2352],[250, 500, 350, 200]))"""



"""def rearrange(arr):
    output = []
    arr.sort()
    while arr:
        output.append(arr.pop(0))  # smallest element
        if arr:
            output.append(arr.pop())  # largest element
    return output
print(rearrange([4, 5, 1, 2, 3]))"""







"""def Rearrange(self, arr):
        #Code Here
 output=[]
 arr.sort()
 for i in range(len(arr)):
       if i%2==0:
            output.append(arr[0])
            arr.remove(arr[0])
       else:
                output.append(arr[-1])
                arr.remove(arr[-1])
 return output"""
            
    
"""def arrange_min_max(arr):
    arr.sort()  # sort array first
    result = []
    i, j = 0, len(arr) - 1

    while i <= j:
        if i == j:  # when only one element left
            result.append(arr[i])
        else:
            result.append(arr[i])   # smallest
            result.append(arr[j])   # largest
        i += 1
        j -= 1

    return result
print(arrange_min_max([4, 5, 1, 2, 3]))"""






"""def fun(arr):
  count=0
  for i in range(len(arr)):
    for j in range(i+1):
      num=arr[i]-arr[j]
      count+=abs(num)
  print(count)"""


"""def fun(arr):
 count=0
 for i in range(len(arr)-1):
    num=arr[i]-arr[i+1]
    print(num)
    count+=abs(num)
 return count
print(fun([4, 1, 5]))"""





"""def specialIntegers(self, n : int, arr : List[int]) -> int:
        # code here
 count=0
 for i in range(n):
    if arr[i]==arr[i]+1 and arr[i]==arr[i]-1:
        count=i
 return count"""



"""def my_strcpy(src):
    rock = ""
    for ch in src:
        rock += ch
    return rock

s = "HelloWorld"
copy_s = my_strcpy(s)
print("Copied string:", copy_s)"""




# 1 referance pointer
"""x=[1,2,3,4]
y=x
y.append(99)
print(x)
print(y)"""



# 2 deep copy
"""import copy
a=[1,2,3,4],[2,3,4,5]
b=copy.deepcopy(a)
b[0][0]=99
print(a)
print(b)

# 3 shallow copy
import copy
a=[1,2,3,4],[2,3,4,5]
b=copy.copy(a)
b[0][0]=99
print(a)
print(b)"""



# 4 function argument pointer
"""def fun(arr):
  arr.append(100)
num=[1,2,3,4] 
fun(num)

print(num)"""




# 5 weak pointer
"""import weakref

class MyClass:
    pass

obj = MyClass()
weak_obj = weakref.ref(obj)

print(weak_obj())  
del obj
print(weak_obj())"""




# 6 null pointer
"""tr = None
if ptr is None:
    print("Pointer is null")"""


"""def fun(num):
    num1=[]
    num2=[]
    mide=len(num)//2
    for i in range(0,mide):

        num1.append(num[i])
    for n in range(mide,len(num)):
        num2.append(num[n])
    return num1,num2
print(fun([1,1,2,2,3,4]))"""



""" def fun(arr):
# code here.
 freq={}
 for i in arr:
    if i  in freq:
        freq[i]+=1
    else:
        freq[i]=1
 while freq:
    for n in freq:
        if n==2:
            if arr[i]>n:
              x=arr[i]
    return n+x
           
print(fun([1,1,2,2,3,4]))      """




""" def fun(arr):
    freq={}
    output=[]
    for i in arr:
        if i in freq:
            freq[i]+=1
            output.append(i)
        else:
            freq[i]=1
    repeat=set(arr)
    n=len(repeat)+1
    total=n*(n+1)//2
    l=total-sum(repeat)
    output.append(l)
    return output
print(fun([1,2,3,3,5])) """




""" def fun(arr1, arr2, x):
    output = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            y = arr1[i] + arr2[j]
            if x == y:
                output.append((arr1[i], arr2[j]))  
    return output

print(fun([1,2,3,4,5], [1,2,3,4,5], 9))
 """
 
 
 
 
 
 
""" def getPairs(arr):
# code here
    output=[]
    for i in range(len(arr)):
       for j in range(i+1,len(arr)):
            if arr[i] !=arr[j]:
                if arr[i]+arr[j]==0:
                   output.append([arr[i],arr[j]])
    print(output)
print(getPairs([-1, 0, 1, 2, -1, -4]))
                         """
                         
                         
""" def longest_common_prefix(strs):
    if not strs:
        return ""

    first, last = min(strs), max(strs)
    print(first)
    print(last)
    for i, ch in enumerate(first):
        print(last[i])
        if i >= len(last) or last[i] != ch:
            return first[:i]
    return first
print(longest_common_prefix(["flower", "flow", "flight"])) """






""" def maxValue(arr): 
    # Complete the function
    output=[]
    array=0
    for i in range(len(arr)):
        array=arr[i]*i
        print(array)
        output.append(array)
    return sum(output)
print(maxValue([5, 3, 2, 4, 1])) """



""" def fun(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print(fun(list,idx+1))
fruits=["mango","banana","apple"]
fun(fruits) """





""" def segregateElements(arr):
    # Your code goes here
    array = []
    for i in arr[:]:       
        if i < 0:
            array.append(i)
            arr.remove(i)
            total=arr+array
    return total
print(segregateElements([1, -1, 3, 2, -7, -5, 11, 6])) """



""" def fun(arr):
 result = []
 for i in arr:
    if result and (result[-1] < 0 <= i or result[-1] >= 0 > i):
        result.pop()
    else:
        result.append(i)
 return result
print(fun([4,2,-2,1]))
                
            """
            
            
""" def fun(arr):
    result=[]
    for i in range(len(arr)-2):
        arr[i],arr[i+2]=arr[i+2],arr[i]
        result.append(arr[i])
    return arr
print(fun([1, 2, 3])) """



""" def maxSum(arr):
    # code here
  array=sorted(arr)
  for i in range(len(array)):
      if arr[i]==array[i]:
         arr[i]=i
  return arr
print(maxSum([4, 2, 1, 8])) 

 """



""" def fun(arr):
    evenNum:list[int]=[]
    oddNum:list[int]=[]
    newArray:list[int]=[]
    for i in arr:
        if i%2==0:
            evenNum.append(i)
        else:
            oddNum.append(i)
    even=0
    odd=0
    for i in range(len(arr)):
        if i%2==0:
            if even<len(evenNum):
                newArray.append(evenNum[even])
                even+=1
        else:
            if odd<len(oddNum):
                newArray.append(oddNum[odd])
                odd+=1
    return newArray
print(fun([2,3,5,4,1,6]))
 """
 
 
 
 
""" def fun(seats,n):
    for i in range(len(seats)):
            if seats[i]==0 and (i==0 or seats[i-1]==0) and (i==(len(seats)-1)or seats[i+1]==0):
                seats[i]=1
                n-=1
                if n==0:
                   return "Yes"
    return "No"
print(fun([1,1,1,0,0,0],1)) """







""" def fun(mat):
    sumrow=sum(mat[0])
    print(sumrow)
print(fun([[1,2,3],[4,5,6],[7,8,9]]))
      """
      
      
      
def isFit (arr, brr) : 
        #Complete the function
    ab=sorted(arr)
    bc=sorted(brr)
    newArray=[]
    nnext=[]
    for i in range(len(arr)):
        if ab[i]<=bc[i]:
            newArray.append(bc[i])
    for i in range(len(brr)):
        if ab[i]>=bc[i]:
            nnext.append(ab[i])
        
    if len(ab)==len(newArray):
            return "Yes"
    elif len(bc)==len(nnext):
            return "Yes"
    return "No"
print(isFit( {7, 5, 3, 2}, {5, 4, 8, 7})) 
 

""" def fun(arr):
 max_height = 0
 for i in range(0, len(arr), 2):
        feet = arr[i]
        inches = arr[i + 1]
        total = feet* 12 + inches
        max_height = max(max_height, total)
 return max_height
print(fun( [3, 2, 2, 3, 1, 2]))  """



""" def minMoves(arr):
 n = len(arr)
 pos = {val: i for i, val in enumerate(arr)}
 longest = 1
 current = 1

 for i in range(2, n + 1):
        if pos[i] > pos[i - 1]:
            current += 1
        else:
            current = 1
        longest = max(longest, current)

 return n - longest
print(minMoves([3, 2, 1, 4])) """



def fun(name,value):
   for i in range(len(name)):
        for j in range(len(value)):
           dict={name[i]:value[j]}
   for k ,v in dict.items():
       print(k,":"v)
print(fun(["Aqsa","Fareeha"],[50,100]))
    