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



# def createarr():
#     arr = []
#     while True:
#         try:
#             n = int(input("Enter num: "))
#             arr.append(n)
#         except Exception as e:
#             return arr
# def selectionsort(arr):
#         n=len(arr)
#         for j in range(0,n-1):
#                 if arr[j]>arr[j+1]:
#                     arr[j],arr[j+1]=arr[j+1],arr[j]
# l1=createarr()
# selectionsort(l1)
# print("sorted array: ",l1)


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




# def createarray():
#     l1=[]
#     while True:
#         try:
#             n=int(input("enteer the number"))
#             l1.append(n)
#         except Exception as e:
#             return l1
# def sum(arr):
#     n=len(arr)
#     sum=0
#     pd=1
#     for i in range (0,n):
#         sum=sum+arr[i]
#         pd=pd*arr[i]
#     return pd-sum
# arr=createarray()
# res=sum(arr)
# print(res)




## GEEK FOR GEEKS
# class Solution:
#     def selectionSort(self, arr):
#         n = len(arr)
#         for j in range(0, n-1):
#             if arr[j] >= arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#         return arr


## Hackerrank Find the Runner-Up Score
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     max=-2**31
#     secondmax=-2**31 
#     for i in range(0,len(arr)):
#         if arr[i]>max:
#             secondmax=max
#             max=arr[i]
#         elif arr[i]>secondmax and arr[i]!=max:
#             secondmax=arr[i]
#             secondmaxindex=i
#     print(secondmax)


# def isprime(n):
#     countfact=0
#     i=1
#     while i*i<=n:
#         if n%i==0:
#             countfact+=1
#             if i!=n//i:
#                 countfact+=1
#         i+=1
#     return countfact==2
# arr=[]
# start=int(input("Enter start: "))
# end=int(input("Enter end: "))
# for i in range(start, end):
#     if isprime(i):
#         arr.append(i)
# print(arr)
