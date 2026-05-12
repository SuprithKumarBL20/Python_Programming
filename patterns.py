# #                                             print()
# print("hello world ",end="")
# print()
# print("world")
# print("hello world ")
# print()
# print("world")

# print("*")
# -----------------------------------
# n=int(input("Enter number of rows: "))
# for i in range(1,n+1):
#     print("*")

# n=int(input("Enter number of clo: "))
# for j in range(1,n+1):
#     print("*",end="")

# n=int(input("Enter number of rows: "))
# print("*"*n,end="")

# n=int(input("Enter number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()



# n=int(input("Enter number of rows: "))
# noc=1
# for i in range(1,(n*2)):
    
#     for j in range(1,(noc+1)):                          
#             print("*",end="")
#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1 
# *
# **
# ***
# ****
# ***
# **
# *

# n=int(input("Enter number of rows: "))
# noc=1
# for i in range(1,(n*2)):
#     for k in range(n,noc,-1):
#         print(" ",end="")
#     for j in range(1,(noc+1)):                          
#             print("*",end="")
#     print()
#     if i<n:
#         noc+=1
#     else:
#         noc-=1

#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *


# n=int(input("Enter number of rows: "))
# noc=1
# for i in range(1,(n*2)):
#     for k in range((n*2)-1,noc,-2):
#         print(" ",end="")
#     for j in range(1,(noc+1)):                          
#             print("*",end="")
#     print()
#     if i<n:
#         noc+=2
#     else:
#         noc-=2
#       * 
#     * * *
#   * * * * *
# * * * * * * *
#   * * * * *
#     * * *
#       *


# n=int(input("Enter number of rows: "))
# noc=n
# for i in range(1,(n*2)):
#     for j in range(1,noc+1):                          
#             print("*",end="")
#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1
# ****
# ***
# **
# *
# **
# ***
# ****

# n=int(input("Enter number of rows: "))
# noc=n
# for i in range(1,(n*2)):
#     for k in range(n,noc,-1):
#         print(" ",end="")                
#     for j in range(1,noc+1):                          
#             print("*",end="")
#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1
#    ****
#     ***
#      **
#       *
#      **
#     ***
#    ****


# n=int(input("Enter number of rows: "))
# noc=n
# for i in range(1,(n*2)):
#     for k in range(n,noc,-1):
#         print(" ",end="")                
#     for j in range(1,noc+1):                          
#             print("* ",end="")
#     print()
#     if i<n:
#         noc-=1
#     else:
#         noc+=1
# * * * * 
#  * * *
#   * *
#    *
#   * *
#  * * *
# * * * *


# n=int(input("Enter number of rows: "))
# noc=(n*2)-1
# for i in range(1,(n*2)):
#     for k in range((n*2)-1,noc,-2):
#         print(" ",end="")                
#     for j in range(1,noc+1):                          
#             print("*",end="")
#     print()
#     if i<n:
#         noc-=2
#     else:
#         noc+=2
# *******
#  *****
#   ***
#    *
#   ***
#  *****
# *******





# * * * * * 
# * *   * *
# *   *   *
# * *   * *
# * * * * *
# n=int(input("ENter "))
# for i in range (1,n+1):
#     for j in range (1,n+1):
#         if i==j or j==1 or i==1 or i==n or j==n or i+j==n+1:

#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# * * * * * 
#   * * * * *
#     * * * * *
#       * * * * *
#         * * * * *
# n=int(input("ENter "))
# for i in range (1,n+1):
#     for k in range (1,i):
#         print(" ",end=" ")
#     for j in range (1,n+1):
#         print("*",end=" ")
#     print()





# n=int(input("ENter "))
# for i in range (1,n+1):
#     for k in range (n,i,-1):
#         print(" ",end=" ")
#     for j in range (1,n+1):
#         print("*",end=" ")
#     print()
#         * * * * * 
#       * * * * *
#     * * * * *
#   * * * * *
# * * * * *


# n=int(input("ENter "))
# for i in range (1,n+1):
#     for k in range (1,i):
#         print(" ",end=" ")
#     for j in range (1,n+1):
    #     if i==n or j==n or i==1 or j==1:
    #         print("*",end=" ")
    #     else:
    #         print(" ",end=" ")
    # print()
#
# * * * * * 
#   *       *
#     *       *
#       *       *
#         * * * * *


# n=int(input("ENter "))
# for i in range (1,n+1):
#     for k in range (n,i,-1):
#         print(" ",end=" ")
#     for j in range (1,n+1):
#         if i==n or j==n or i==1 or j==1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#         * * * * * 
#       *       *
#     *       *
#   *       *
# * * * * *





# n=int(input("ENter "))
# noc=1
# for i in range (1,n*2):
#     for k in range (n,noc,-1):
#         print(" ",end="")
#     for j in range (1,noc):
#         print("* ",end="")
#     if i<n:
#         noc+=1
#     else:
#         noc-=1
#     print()

#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *




# n=int(input("ENter "))
# noc=1
# for i in range (1,n*2):
#     for k in range (n,noc,-1):
#         print(" ",end="")
#     for j in range (1,noc+1):
#         if  j==noc or j==1 :
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     if i<n:
#         noc+=1
#     else:
#         noc-=1
#     print()

#     * 
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *


# n=int(input("ENter "))
# noc=1
# for i in range (1,n*2):
#     for j in range(1,noc+1):
#         if j==1 or j==noc:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     for k in range(1, (n - noc) * 2 + 1):
#         print(" ", end="")
#     for j in range(1,noc+1):
#         if j==1 or j==noc:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     if i<n:
#         noc+=1
#     else:
#         noc-=1
#     print()

# *      *
# **    **
# * *  * *
# *  **  *
# * *  * *
# **    **
# *      *



# n=int(input("ENter "))
# noc=1
# for i in range (1,n*2):
#     for j in range(1,noc+1):
#         print("*",end="")
#     for k in range(1, (n - noc) * 2 + 1):
#         print(" ", end="")
#     for j in range(1,noc+1):
#             print("*",end="")
#     if i<n:
#         noc+=1
#     else:
#         noc-=1
#     print()

# *      *
# **    **
# ***  ***
# ********
# ***  ***
# **    **
# *      *


# n=int(input("ENter "))
# for i in range(n,1-1,-1):
#     for j in range(i,1-1,-1):
#         print(j,end="")
#     print()

# 4321
# 321
# 21
# 1



# n=int(input("ENter "))
# noc=1
# for i in range (1,n*2):
#     for j in range(noc,1-1,-1):
#         print(j,end="")
#     if i<n:
#         noc+=1
#     else:
#         noc-=1
#     print()
# 1
# 21
# 321
# 4321
# 321
# 21
# 1




# n=int(input("enyet"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if (i+j)%2==0:
#             print('1',end="")
#         else :
#             print('0',end="")

#     print()
# 1
# 01
# 101
# 0101



# n=int(input("enyet"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i<j:
#             print(i,end="")
#         else:
#             print(j,end="")
#     print()
# 1111
# 1222
# 1233
# 1234



# n=int(input("enyet"))
# for i in range(n,1-1,-1):
#     for j in range(n,0,-1):
#         if i<j:
#             print(i,end="")
#         else:
#             print(j,end="")
#     print()
# 4321
# 3321
# 2221
# 1111


# n=int(input("enyet"))
# for i in range(n,0,-1):
#     for j in range(n,1-1,-1):
#         if i<j:
#             print(j,end="")
#         else:
#             print(i,end="")
#     print()
# 4444
# 4333
# 4322
# 4321



# n=int(input("enyet"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i<j:
#             print(j,end="")
#         else:
#             print(i,end="")
#     print()
# 1234
# 2234
# 3334
# 4444


# n=int(input("enyet"))
# ncn=n*n
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(ncn,end=" ")
#         ncn-=1
#     print()
# 16 15 14 13 
# 12 11 10 9
# 8 7 6 5
# 4 3 2 1

# n=int(input("enyet"))
# ncn=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(ncn,end=" ")
#         ncn+=1
#     print()
# 1 2 3 4 
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

# n=int(input("enyet"))
# count=1
# for i in range(1,n+1):
#     for j in range (1,n+1):
#         if i%2!=0:
#             print(count,end=" ")
#             #collecting the printed value of odd row
#             count2=count
#         else:
#             print(count2,end=" ")
#             count2-=1
#         count+=1
#     print()
#     count2=count2+n#before going to even row sum 
# #         #collected val =n
# 1 2 3 4 
# 8 7 6 5
# 9 10 11 12
# 16 15 14 13



# n=int(input("enyet"))
# noc=n
# for i in range(1,(n*2)):
#     for j in range(1,noc+1):
#         if i<j:
#             print(j,end=" ")
#         else:
#             print(j,end=" ")
#     if i<n:
#         noc-=1
#     else:
#         noc+=1
#     print()

# 1 2 3 4 
# 1 2 3
# 1 2
# 1
# 1 2
# 1 2 3
# 1 2 3 4





    