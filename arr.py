# arr=[1,2,3,4,]
# print("type of arr is",type(arr))
# print("elements of arr are:",arr)
# print("length of arr is:",len(arr))

# s="abejdw"
# print("type of s is",type(s))
# print("elements of s are:",s)
# print("length of s is:",len(s))

# dict={"name":"abc","age":22}
# print("type of dict is",type(dict))
# print("elements of dict are:",dict)
# print("length of dict is:",len(dict))

# s1={1,2,3,4,5,5,4}
# print("type of s1 is",type(s1))
# print("elements of s1 are:",s1)
# print("length of s1 is:",len(s1))

# arr=[]
# print(len(arr))
# arr.append(10)
# arr.append("abs")

#to create an array
# import array as arr
# a=arr.array('i',[1,2,3,4,5])
# print("array a is:",a)
#to create an array input given by user

# to print min of array input given by user
# def createintarray(arr):
#     n=int(input("enter the number of elements you want in array:"))
#     for i in range(n):
#         x=int(input("enter the element:"))
#         arr.append(x)
#     return arr
# arr=[]
# arr=createintarray(arr)
# print("array a is:",arr)
# min1=arr[0] 
# for i in range(1,len(arr)):
#     if arr[i]<min1:
#         min1=arr[i]
# print("minimum element in array is:",min1)
#               ----------------- or
# for i in arr:
#     if i<min1:
#         min1=i
# print("minimum element in array is:",min1)

# # to print min of array input given by user using -2**31
# def createintarray(arr):
#     n=int(input("enter the number of elements you want in array:"))
#     for i in range(n):
#         x=int(input("enter the element:"))
#         arr.append(x)
#     return arr
# arr=[]
# arr=createintarray(arr)
# print("array a is:",arr)
# min1=2**31-1  
# for i in range(0,len(arr)):
#     if arr[i]<min1:
#         min1=arr[i]
# print("minimum element in array is:",min1)

#to print second max of array input given by user using -2**31

# def createarr():
#     arr = []
#     while True:
#         try:
#             n = int(input("Enter num: "))
#             arr.append(n)
#         except Exception as e:
#             return arr
# def secondmax(arr):
#     max=-2**31
#     secondmax=-2**31
#     maxindex=-1
#     secondmaxindex=-1   
#     for i in range(0,len(arr)):
#         if arr[i]>max:
#             secondmax=max
#             max=arr[i]
#             secondmaxindex=maxindex
#             maxindex=i

#         elif arr[i]>secondmax and arr[i]!=max:
#             secondmax=arr[i]
#             secondmaxindex=i
#     return [max,maxindex,secondmax,secondmaxindex]
# l=createarr()
# print("original array: ",l)
# res=secondmax(l)
# print(f"max{res[0]},maxindex{res[1]}")
# print(f"secondmax{res[2]},secondmaxindex{res[3]}")


# import array as arr
# n=int(input("enter the number of elements you want in array:"))
# arr=arr.array('i',[])






#                            Linear Search
# def createarr():
#     arr = []
#     while True:
#         try:
#             n = int(input("Enter num: "))
#             arr.append(n)
#         except Exception as e:
#             return arr
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return True, i  
#     return False, -1     
# arr = createarr()
# target =int(input("Enter target: "))
# found, index = linear_search(arr, target)
# print("Element Found:", found)
# print("Index:", index)



# def selectionsort(arr):
# n=len(arr)
# for i in range(0,(n-1)):
#         actualind=n-1-i
#         cmax=-2**31
#         cmaxind=-1
#         for j in range(0,(n-i)):
#           if cmax<a[j]:
#               cmax=a[j]
#               cmaxind=j
#         arr[actualind],arr[cmaxind]=(arr[cmaxind],arr[actualind])
# return arr
# print("array a is:",arr)
# arr=createintarray(arr)
# print("before, sorting array is:",arr)
# selectionsort(arr)
# print("sorted array is:",arr)


##                   SELECTION SORT
# def createarr():
#     arr = []
#     while True:
#         try:
#             n = int(input("Enter num: "))
#             arr.append(n)
#         except Exception as e:
#             return arr
# def selectionsort(arr):
#     n=len(arr)
#     for i in range(0,n-1):
#         actindex=n-1-i
#         max=-2**31
#         maxindex=-1
#         for j in range(0,n-i):
#             if max<arr[j]:
#                 max=arr[j]
#                 maxindex=j
#         arr[actindex],arr[maxindex]=arr[maxindex],arr[actindex]
# l1=createarr()
# print("original array: ",l1)
# selectionsort(l1)
# print("sorted array: ",l1)

#IT DOES NOT CREATE NEW ARRAY IT CHANGES THE VALUE IN ORIGINAL ARRAY
#BECAUSE WE HAVE GIVEN THE ADDRESS OF ORIGINAL ARRAY TO FUNCTION AND IT CHANGED THE VALUE IN THAT ADDRESS
#WE HAVE GIVEN A ADDRESS AND IT HAD SEEN THE VALUE AND IT CHANGED THE VALUE IN THAT ADDRESS
#BUT THE ADDRESS IS SAME SO IT CHANGED THE VALUE IN ORIGINAL ARRAY



##                       BUBBLE SORT        

# def createintarray(arr):
#     n=int(input("enter the number of elements you want in array:"))
#     for i in range(n):
#         x=int(input("enter the element:"))
#         arr.append(x)
#     return arr

# def bubblesort(arr):
#     n=len(arr)
#     for i in range(0,n-1):
#         for j in range(0,n-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=(arr[j+1],arr[j])
# ar=[]
# arr=createintarray(ar)
# print("before, sorting array is:",arr)
# bubblesort(arr)
# print("sorted array is:",arr)


##                               INSERTION SORT 

# def createintarray():
#     l=[]
#     while True:
#         try:
#             x=int(input("enter the element:"))
#             l.append(x)
#         except Exception as e:
#             return l
# def insertionsort(arr):
#     n=len(arr)
#     for i in range(0,n-1):
#         for j in range(i+1,0,-1):
#             if arr[j-1]<arr[j]:
#                 arr[j],arr[j-1]=arr[j-1],arr[j]
# arr=createintarray()
# print("before, sorting array is:",arr)
# insertionsort(arr)
# print("sorted array is:",arr)



##                        BINARY SEARCH(time COMPLEXITY =====O(log n))

# def createarr():
#     l1 = []
#     while True:
#         try:
#             n = int(input("Enter num: "))
#             l1.append(n)
#         except Exception as e:
#             return l1
# def orderagnosticbinarysearch(arr, target):
#     start, end = 0, len(arr)-1

#     arr = "asc"
#     if arr[start] > arr[end]:
#         arr = "desc"

#     while start <= end:
#         mid = (start + end) // 2
#         if target == arr[mid]:
#             return mid

#         if arr == "asc":
#             if target < arr[mid]:
#                 end = mid - 1
#             else:
#                 start = mid + 1
#         else:
#             if target < arr[mid]:
#                 start = mid + 1
#             else:
#                 end = mid - 1
#     return -1

# arr = createarr()
# target = int(input("Enter the ele to be searched: "))
# print("Array: ", arr)
# resindex = orderagnosticbinarysearch(arr, target)
# if resindex != -1:
#     print(f"{target} is found at index: {resindex}")
# else:
#     print(f"{target} is not found")



#                  REVERSE ARRAY

# def createarray():
#     l1=[]
#     while True:
#         try:
#             n=int(input("enteer the number"))
#             l1.append(n)
#         except Exception as e:
#             return l1
# def reversearray(arr):
#     i,j=0,len(arr)-1
#     while i<j:
        # arr[i],arr[j]=arr[j],arr[i]
#         i+=1
#         j-=1
# arr=createarray()
# print("initial array",arr)
# reversearray(arr)
# print("reversed array",arr)



##                       ROTATION OF ARRAY

###                         LEFT ROTATION
# def createarray():
#     l1=[]
#     while True:
#         try:
#             n=int(input("enteer the number"))
#             l1.append(n)
#         except Exception as e:
#             return l1
# def reversearray(arr,i,j):
#     while i<j:
#         arr[i],arr[j]=arr[j],arr[i]
#         i+=1
#         j-=1
# def leftrotation(arr,k):
#     n=len(arr)
#     if k>=n:
#        k=k%n
# #     step1
#     reversearray(arr,0,(k-1))
# #     step2    
#     reversearray(arr,k,n-1)
# #     step3
#     reversearray(arr,0,(n-1))     

# arr=createarray()
# k=int(input("enter number of rotation"))
# print("initial array",arr)
# leftrotation(arr,k)
# print("roataed arry",arr)




# #                                          RIGHT ROTATION 
# def createarray():
#     l1=[]
#     while True:
#         try:
#             n=int(input("enteer the number"))
#             l1.append(n)
#         except Exception as e:
#             return l1
# def reversearray(arr,i,j):
#     while i<j:
#         arr[i],arr[j]=arr[j],arr[i]
#         i+=1
#         j-=1
# def rightrotation(arr,k):
#     n=len(arr)
#     if k>=n:
#        k=k%n

#     reversearray(arr,0,n-1)
#     reversearray(arr,k,(n-1))   
#     reversearray(arr,0,(k-1))  

# arr=createarray()
# k=int(input("enter number of rotation"))
# print("initial array",arr)
# rightrotation(arr,k)
# print("roataed arry",arr)



##      MERGE ARRAY

#concatination of array
# arr1=[1,2,3,4,]
# arr2=[5,6,7,8,9]
# print(a+b)


# arr1.extend(arr2)
# print("after")
# print(arr1)
# # print(a)
# # print(b)
# # a.append(b)
# for i in range (0,len(arr2)):
#     arr1.insert(len(arr1),arr2[i])
# print("after")
# print(arr1)
# print(arr2)


##              MERGE ARRAY

# def createarray():
#     l1=[]
#     while True:
#         try:
#             n=int(input("enteer the number"))
#             l1.append(n)
#         except Exception as e:
#             return l1
# def mergearray(arr1,arr2):
#     res=[]
#     i,j=0,0
#     n1,n2=len(arr1),len(arr2)
#     for k in range (0,(n1+n2)):
#         #to print od numbers in odd place and even in even place
#         if i<n1 and k%2==0:
#             res.append(arr1[i])
#             i+=1
#         elif j<n2 and k%2!=0:
#             res.append(arr2[j])
#             j+=1
#         else:
#                           # to print normally
#             if i<n1 :
#                 res.append(arr1[i])
#                 i+=1
#             elif j<n2:
#                 res.append(arr2[j])
#                 j+=1
#     return res
# print("arr1 1 elemnts")
# arr1=createarray()
# print("arr2 elements")
# arr2=createarray()
# res=mergearray(arr1,arr2)
# print("arrr1",arr1)
# print("arr2",arr2)
# print("res",res)

# #                       MERGE SORT
# def createarray():
#     l1=[]
#     while True:
#         try:
#             l1.append(int(input("NEter num")))
#         except Exception as e:
#             return l1
# def mergesortmerge(arr,start,mid,end):
#     res=[]
#     i=start
#     j=mid+1
#     for k in range(0,(mid+end)+1):
#         if i<=mid and j<=end:
#             if arr[i]<arr[j]:
#                 res.append(arr[i])
#                 i+=1
#             else:
#                 res.append(arr[j])
#                 j+=1
#         else:
#             if i<=mid:
#                 res.append(arr[i])
#                 i+=1
#             elif j<=end:
#                 res.append(arr[j])
#                 j+=1
# #for UPDATING I/P array
#     for k in range(0,len(res)):
#         arr[start]=res[k]
#         start+=1
# def mergesortdivide(arr,start,end):
#     if start==end:
#         return
#     mid=(start+end)//2
#     #LHS
#     mergesortdivide(arr,start,(mid))
#     #RIGHT
#     mergesortdivide(arr,(mid+1),end)
#     #MERGING
#     mergesortmerge(arr,start,mid,end)
# print("enter the eel in array")
# arr=createarray()
# print("array before sorting",arr)
# mergesortdivide(arr,0,len(arr)-1)
# print("array after sorting",arr)






#                                           STRINGS
# def sumdigits(s):
#     sum=0
#     nstr="" 
#     for i in range (0,len(s)):
#         if "0"<=s[i]<="9":
#             sum=sum+(ord(s[i])-48)
#         else:
#             nstr=nstr+s[i]
#     nsum=""
#     while sum>0:
#         rem=sum%10
#         nsum=chr(rem+48)+nsum
#         sum=sum//10
#     return nstr+nsum
# s=input("enter the string")
# res=sumdigits(s)
# print("resultant string is:",res)





# def sumdigits(s):
#     s+=" "
#     sum=0
#     num=0
#     nstr="" 
#     for i in range (0,len(s)):
#         if "0"<=s[i]<="9":
#             num=(num*10)+(ord(s[i])-48)
#         else :
#             if num!=0 :
#                 sum=sum+num
#                 num=0
# # #TO NOT INCLUDE SPACE
#             if (i+1)!=len(s):
#                 nstr=nstr+s[i]

# # #              TO CONVERT SUM INTO STRING      
#     nsum=""
#     while sum>0:
#         rem=sum%10
#         nsum=chr(rem+48)+nsum
#         sum=sum//10
#     return nstr+nsum
# s=input("enter the string")
# res=sumdigits(s)
# print("resultant string is:",res)

#to reverse a string using negative indexing using inbluit
# s=input("enter the string")
# res=s[::-1]
# print("reversed string is:", res)

#to reverse a string without inbuilt
# def reversestring(s):
#     res=""
#     for i in range (len(s)-1,-1,-1):
#         res=res+s[i]
#     return res
# s=input("enter the string")
# res=reversestring(s)
# print("reversed string is:", res)

# #to reverse a string without inbuilt using increasing order
# def reversestring(s):
#     res=""
#     for i in range (0,len(s)):
#         res=s[i]+res
#     return res
# s=input("enter the string")
# res=reversestring(s)
# print("reversed string is:", res)

# to reverser string using recursion without inbuilt


# def revstring(s, i,nstr):
#     if i==len(s):
#         return nstr
#     else:
#         nstr=s[i]+nstr
#         return revstring(s, i+1,nstr)
# s = input("enter the string: ")
# res= revstring(s, 0,"")
# print("reversed string is:", res)

# def revstring(s,i,nstr):
#     if i==0:
#         return nstr
#     else:
#         nstr=nstr+s[i-1]
#         return revstring(s, i-1,nstr)


# s=input("enter the string: ")
# res= revstring(s,len(s),"")
# print("reversed string is:", res)

# ##                  STACK USING ARRAY

# size = int(input("Enter size of stack: "))
# stack = [0] * size
# top = -1

# def push_multiple():
#     global top
#     n = int(input("How many elements to push: "))
    
#     for i in range(n):
#         if top == size - 1:
#             print("Stack Overflow")
#             break
#         else:
#             element = int(input("Enter element: "))
#             top = top + 1
#             stack[top] = element

# def pop_multiple():
#     global top
#     n = int(input("How many elements to pop: "))
    
#     for i in range(n):
#         if top == -1:
#             print("Stack Underflow")
#             break
#         else:
#             print("Deleted element:", stack[top])
#             top = top - 1

# def display():
#     if top == -1:
#         print("Stack is empty")
#     else:
#         print("Stack elements:")
#         for i in range(top, -1, -1):
#             print(stack[i])

# while True:
#     print("\n1. Push Multiple")
#     print("2. Pop Multiple")
#     print("3. Display")
#     print("4. Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         push_multiple()
#     elif choice == 2:
#         pop_multiple()
#     elif choice == 3:
#         display()
#     elif choice == 4:
#         break
#     else:
#         print("Invalid choice")



# size = int(input("Enter number of elements: "))
# stack = [0] * size
# top = -1

# # Push elements
# for i in range(size):
#     element = int(input("Enter element: "))
#     top = top + 1
#     stack[top] = element

# print("\nOriginal elements:")
# for i in range(0, size):
#     print(stack[i], end=" ")

# # Reverse using stack (pop logic)
# print("\nReversed elements:")
# while top != -1:
#     print(stack[top], end=" ")
#     top = top - 1


##                     BFS USING ARRAY

# # Function to create graph
# def create_graph():
#     graph = {}
#     n = int(input("Enter number of vertices: "))

#     for i in range(n):
#         node = input("Enter vertex: ")
#         neighbours = input("Enter neighbours separated by space: ").split()
#         graph[node] = neighbours

#     return graph


# # BFS function
# def bfs(graph, start):

#     visited = []
#     queue = [None]*100

#     front = 0
#     rear = 0

#     queue[rear] = start
#     rear = rear + 1

#     print("BFS Traversal:")

#     while front < rear:

#         node = queue[front]
#         front = front + 1

#         if node not in visited:

#             print(node, end=" ")
#             visited.append(node)

#             for neighbour in graph[node]:
#                 queue[rear] = neighbour
#                 rear = rear + 1


# # Main Program
# graph = create_graph()
# start = input("Enter starting node: ")
# bfs(graph, start)



#                     DFS USING ARRAY

# Function to create graph
# def create_graph():
#     graph = {}
#     n = int(input("Enter number of vertices: "))

#     for i in range(n):
#         node = input("Enter vertex: ")
#         neighbours = input("Enter neighbours separated by space: ").split()
#         graph[node] = neighbours

#     return graph


# # DFS function
# def dfs(graph, start):

#     visited = []
#     stack = [None]*100

#     top = -1

#     top = top + 1
#     stack[top] = start

#     print("DFS Traversal:")

#     while top >= 0:

#         node = stack[top]
#         top = top - 1

#         if node not in visited:

#             print(node, end=" ")
#             visited.append(node)

#             for neighbour in graph[node]:
#                 top = top + 1
#                 stack[top] = neighbour

# # Main Program
# graph = create_graph()
# start = input("Enter starting node: ")
# dfs(graph, start)