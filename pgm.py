# #                                             for loop with range fn
# l=[1,2,3,]
# for i in range(0,3):
#     print('index',i,"element",l[i])

# #                                             for loop without range
# l=[1,2,3]
# for i in l:
#     print("ele:",i,"index:",l.index(i))

#                                                #WHILE LOOP
# example 1
#  n=int(input("enter n value:"))
# i=3
# while i<=n:
#     print(i,end=" ")
#     i=i+1
# print("\n prog exec")
# print("last i:",i)

# # example 2
# n=int(input("enter n value:"))
# i=0
# while n>0:
#     print(n,end=" ")
#     n=n-1-i
#     i=i+1

# #=================WAP to check whether a given number is even or odd using customized function
# def check_even_odd(num):
#     return num%2==0
      
# num=int(input("enter n value:"))
# flag=check_even_odd(num)
# if flag==True:
#     print(f"{num}is even")    
# else:
#     print(num,"is odd")

# #•	WAP to print all even num present in a user defined range
# def checkevenodd(num):
#     return num%2==0
# n=int(input("enter start value:"))
# e=int(input("enter end value:"))
# if n>e:
#     print("invalid range")  
# else:
#     print("even numbers are:")
#     for i in range (n,(e+1)):
#             flag=checkevenodd(i)
#             if flag:
#                 print(i,end=" ")
#     print("\n odd numbers are:")
#     for i in range (n,(e+1)):
#             flag=checkevenodd(i)
#             if flag==False:
#                 print(i ,end=" ")
       
# #================================================LEAP YEAR=====================
# def isleapyear(year):
#      return ((year%4==0) and (year%100!=0) or (year%400==0))
# str=int(input("enter start year:"))
# end=int(input("enter end year:"))
# if str>end:
#     print("invalid range")
# else:
#     print("leap years are:")
#     for i in range(str,(end+1)):
#         flag=isleapyear(i)
#         if flag:
#             print(i,end=" ")
#     print("\nNon leap years")
#     for i in range(str,(end+1)):
#         flag=isleapyear(i)
#         if not flag:
#             print(i,end=" ")


# #========================count of digits in a number========================
# n=int(input("enter n value:"))
# count=0
# while n>0:
#     n=n//10
#     count=count+1
# print("count of digits:",count)


# # def countdigits(n):
# #     count=0
# #     while n>0:
# #         n=n//10
# #         count=count+1
# #     return count
# # n=int(input("enter n value:"))
# # res=countdigits(n)
# # print(f"count of digits in {n} is {res}")


# def count_digits(n):
#     count = 0
#     while n > 0:
#         count += 1
#         n = n // 10
#     return count
# start=int(input("Enter start number: "))
# end=int(input("Enter end number: "))
# for i in range(start, end+1):
#     res=count_digits(i)
#     print(f"{i} has {res} digits")


# # =========================================ARM STRONG NUMBER
# def countdigits(n):
#     count=0
#     while n>0:
#         n=n//10
#         count=count+1
#     return count
# n=int(input("enter n value:"))
# temp=n
# pow=countdigits(n)
# asn=0
# while n>0:
#     base=n%10
#     asn=asn+(base**pow)
#     n=n//10
# if asn==temp:
#     print(f"{temp} is armstrong number")
# else:
#     print(f"{temp} is not armstrong number")

# #==================================FACTORIAL OF A NUMBER

# num = int(input("Enter a number: "))
# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i

# print("The factorial of", num, "is", fact)


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# num = int(input("Enter a number: "))
# print("The factorial of", num, "is", factorial(num))


#                                                                       factors of a number
# n=int(input("enter n value:"))
# print(f"the factors of {n} are:")
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=" ")



# def displayfactors(n):
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i,end=" ")
# n=int(input("enter n value:"))
# print(f"the factors of {n} are:")
# displayfactors(n)


# #=============================COUNT OF FACTORS OF A NUMBER"
# def displayfactors(n):
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i,end=" ")
# def countfactors(n):
#     count=0
#     countcycle=0
#     for i in range(1,n+1):
#         countcycle+=1
#         if n%i==0:
#             count=count+1
#     return count,countcycle
# n=int(input("enter n value:"))
# print(f"the factors of {n} are:")
# displayfactors(n)
# rescount,rescountcycle=countfactors(n)
# print(f"\nthe count of factors of {n} is {rescount}")
# print(f"the count cycle executed is {rescountcycle}")

# def displayfactors(n):
#     i=1
#     countcycle=0
#     while i*i<=n:
#         countcycle+=1
#         if n%i==0:
#             print(i,end=" ")
#             if i!=n//i:
#                 print(n//i,end=" ")
#         i+=1
#     return countcycle    




# def countfactors(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count=count+1
#     return count
# n=int(input("enter n value:"))
# print(f"the factors of {n} are:")
# countcycle=displayfactors(n)
# rescount=countfactors(n)
# print(f"\nthe count of factors of {n} is {rescount}")
# print(f"the count cycle executed is {countcycle}")


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
# n=int(input("enter n value:"))
# flag=isprime(n)
# if flag:
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is not prime number")


# #============================         HCF of a given two numbers
# n1=int(input("enter n1 value:"))
# n2=int(input("enter  n2 value:"))
# lower=n1 if n1<n2 else n2
# hcf=1
# for i in range(2,lower+1):
#     if n1%i==0 and n2%i==0:
#         hcf=i
# print(f"hcf of {n1}and {n2} is {hcf}")

# n1,n2=map(int,input().split())
# lower=n1 if n1<n2 else n2
# hcf=1
# for i in range(2,lower+1):
#     if n1%i==0 and n2%i==0:
#         hcf=i
# print(hcf)

# def hcf(n1,n2):
#     lower=n1 if n1<n2 else n2
#     hcf=1
#     for i in range(2,lower+1):
#         if n1%i==0 and n2%i==0:
#             hcf=i
#     return hcf
# n1,n2=map(int,input().split())
# res=hcf(n1,n2)
# print(res)

# #                     ===========================FIBONACCI SERIES
# #                                  incrementing while loop version

# def fibonacci(pos):
#     n1,n2=0,1
#     i=1
#     while i<=pos:
#         print(n1,end=" ")
#         temp=n1+n2
#         n1=n2
#         n2=temp
#         i+=1
# pos=int(input("enter no of positions:"))
# print(f"fibonacci series upto {pos} positions is:")
# fibonacci(pos)
# #                                 decrementing while loop version
# print("decrementing while loop version")
# def fibonacci(pos):
#     n1,n2=0,1
#     while pos>0:
#         print(n1,end=" ")
#         temp=n1+n2
#         n1=n2
#         n2=temp
#         pos-=1
# pos=int(input("enter no of positions:"))
# print(f"fibonacci series upto {pos} positions is:")
# fibonacci(pos)


# #                                      incrementing For loop version
# print("incrementing for loop version")
# def fibonacci_list(pos):
#     n1,n2=0,1
#     for pos in range(1,pos+1):
#         print(n1,end=" ")
#         temp=n1+n2      
#         n1=n2
#         n2=temp
# pos=int(input("enter no of positions:"))
# print(f"fibonacci series upto {pos} positions is:")
# fibonacci_list(pos)


# #                                       decrementing for loop version
# print("decrementing for loop version") 
# def fibonacci_list(pos):
#     n1,n2=0,1
#     for pos in range(1,pos+1):
#         print(n1,end=" ")
#         temp=n1+n2      
#         n1=n2
#         n2=temp
# pos=int(input("enter no of positions:"))
# print(f"fibonacci series upto {pos} positions is:")
# fibonacci_list(pos)

# print("decrementing for loop version by giving our inputs") 
# def fibonacci_list(pos):
#     n1=int(input("enter first number:"))
#     n2=int(input("enter second number:"))
#     print(f"fibonacci series upto {pos} positions is:")
#     for pos in range(1,pos+1):
#         print(n1,end=" ")
#         temp=n1+n2      
#         n1=n2
#         n2=temp
# pos=int(input("enter no of positions:"))
# fibonacci_list(pos)




# #                                  LCM of two given numbers
# print("LCM of two given numbers using for loop")
# def lcm(n1,n2):
#     lcm=n1 
#     if n1>n2:
#         lcm=n2
#     for i in range (lcm, n1*n2+1):
#         if i%n1==0 and i%n2==0:
#              return i
#         i+=1
# n1,n2=map(int,input("enter two numbers:").split())
# res=lcm(n1,n2)
# print(f"lcm of {n1} and {n2} is {res}")

# print("LCM of two given numbers using while loop")
# def lcm(n1,n2):
#     lcm=n1 
#     if n1>n2:
#         lcm=n2
#     while n1*n2:
#         if lcm%n1==0 and lcm%n2==0:
#             return lcm
#         lcm+=1
# n1,n2=map(int,input("enter two numbers:").split())
# res=lcm(n1,n2)
# print(f"lcm of {n1} and {n2} is {res}")

# #                                      to print 1 2 3 4 
# def printnum(n):
#     if n<=0:
#         return
#     printnum(n-1)
#     print(n)
# n=int(input("enter n value:"))
# printnum(n)

# #                                     to print 4 3 2 1
# def printnum(n):
#     if n<=0:
#         return
#     print(n)
#     printnum(n-1)

# n=int(input("enter n value:"))
# printnum(n)

# #                                 to print 4 3 2 1 1 2 3 4 
# def printnum(n):
#     if n<=0:
#         return
#     print(n)
#     printnum(n-1)
#     print(n)
# n=int(input("enter n value:"))
# printnum(n)

# #                                    to print 1 2 3 4 4 3 2 1
# def printnum(n, i):
#     if i > n:
#         return
#     print(i)
#     printnum(n, i+1)
#     print(i)
# n =int (input("enter n value:"))
# printnum(n, 1)

# #                                          factors
# def fact(n,i):
#     if i*i>n:
#         return 
#     if n%i==0:
#         print(i)
#         if i!=(n//i):
#             print((n//i))
#     fact(n,(i+1))
# n=int(input("enter the number"))
# fact(n,1)      

# #                                  CountFactors
# def countfact(n,i,count):
#     if i*i>n:
#         return count
    
#     if n%i==0:
#         count=count+1
#         print(i)
#         if i!=(n//i):
#             count=count+1
#             print(n//i)
#     return countfact(n,(i+1),count)
# n=int(input("enter the number"))
# count=countfact(n,1,0)
# res=countfact(n,1,0)
# print(res)
# print("count is",count)



# #                                      prime
# def is_prime(n,i):
#     if i*i>n:
#         return True
#     if n%i==0:
#         return False
#     return is_prime(n,i+1)
# n=int(input("enter number"))
# res=is_prime(n,2)
# if res:
#     print("prime ")
# else:
#     print("not prime")




# def hcf(n1,n2,i,hcf,lower):
#     if i>lower:
#         return hcf
#     if (n1%i==0) and(n2%i==0):
#         hcf=i
#     return hcf(n1,n2,i,hcf,lower)
# n1=int(input("enter the first number"))
# n2=int(input("enter the second number"))
# lower=n1
# if n2<n1:
#     lower=n2
# res=hcf(n1,n2,1,1,lower)
# print(res)




# #                                     Fibonacci   
# def fibo(pos,n1,n2):
#     if pos<=0:
#         return
#     print(n1,end=" ")
#     fibo(pos-1,n2,n1+n2)
# pos=int(input("enter no of positions:"))
# fibo(pos,0,1)





# def fibo(pos,n1,n2):
#     if pos<=1:
#         return print(n1)
#     fibo(pos-1,n2,n1+n2)
# pos=int(input("enter no of positions:"))
# fibo(pos,0,1)
# #                       n thFibonacci returning value  
# def fibo(pos):
#     if pos==1 or pos==0:
#         return pos
#     return fibo(pos-1)+fibo(pos-2)
# pos=int(input("enter no of positions:"))
# res=fibo(pos)
# print(res)




# #                                          Happy Number
# def happy(n):
#     if n==1:
#         print("happy number")
#         return
#     elif n==4:
#         print("not a happy number")
#         return
#     sum=0
#     while n>0:
#         rem=n%10
#         sum=sum+(rem**2)
#         n=n//10
#     happy(sum)
# n=int(input("enter n value:"))
# happy(n)
# what ishappy number?
# # A happy number is a number which eventually reaches 1 when replaced repeatedly by the sum of the
# # square of its digits. If it loops endlessly in a cycle that does not include 1, then it is not a happy number. For example, 
# # 19 is a happy number because 1^2 + 9^2 = 82
# # 8^2 + 2^2 = 68
# # 6^2 + 8^2 = 100
# # 1^2 + 0^2 + 0^2 = 1




# def findDigits(n):
#     count=0
#     while n>0:
#         n=n//10
#         count+=1
#     return count
# n=int(input())
# res=findDigits(n)  
# print(res)    

# def countDigits(n,count):
#     if n==0:
#         return count
#     while n>0:
#         n=n//10
#         count+=1
#     return countDigits(n,count)
# n=int(input())
# res=countDigits(n,0)  
# print(res)









# def palindrome(n):
#     rev=0
#     while n>0:
#         base=n%10
#         rev=(rev*10)+base
#         n=n//10
#     return rev
# n1=int(input("enter n value:"))  
# temp=n
# fal=palindrome(n)
# if fal==temp:
#     print("palindrome")     
# else:
#     print("not palindrome")






# start=int(input("enter start value:"))
# end=int(input("enter end value:"))
# for i in range(start,end+1):
#     temp=i
#     rev=0
#     while i>0:
#         base=i%10
#         rev=(rev*10)+base
#         i=i//10
#     if rev==temp:
#         print(temp,end=" ")         


# def palindrome(n):
#     rev=0
#     while n>0:
#         base=n%10
#         rev=(rev*10)+base
#         n=n//10
#     return rev
# start=int(input("enter start value:"))
# end=int(input("enter end value:"))
# for i in range(start,end+1):
#     temp=i
#     fal=palindrome(i)
#     if fal==temp:
#         print(temp,end=" ")


# n=int(input("enter n value:"))
# count=n
# s=1
# rev=0
# while count>n:
#     temp=s
#     while s>0:
#         base=s%10
#         rev=(rev*10)+base
#         s=s//10
#     if rev==temp:
#         print(temp,end=" ")
#         count-=1
#     s+=1







