##              to convert all uppercase to lowercase without inbuilt function
# def to_lowercase(s): 
#     nstr=""
#     for i in range(0,len(s)):
#         if "A"<= s[i]<="Z":
#             nstr=nstr+chr(ord(s[i])+32)
#         else:
#             nstr=nstr+s[i]
#     return nstr
# string=input("Enter a string: ")
# result=to_lowercase(string)
# print("Lowercase string:", result)

##               lower to upper case without 
# def to_uppercase(s): 
#     nstr=""
#     for i in range(0,len(s)):
#         if "a"<= s[i]<="z":
#             nstr=nstr+chr(ord(s[i])-32)
#         else:
#             nstr=nstr+s[i]
#     return nstr

# string=input("Enter a string: ")
# result=to_uppercase(string)
# print("Uppercase string:", result)

##                          to switch cases

# def switch_case(s): 
#     nstr=""
    # for i in range(0,len(s)):
    #     if "a"<= s[i]<="z":
    #         nstr=nstr+chr(ord(s[i])-32)
    #     elif "A"<= s[i]<="Z":
    #         nstr=nstr+chr(ord(s[i])+32)
    #     else:
    #         nstr=nstr+s[i]
    # return nstr
# sring=input("Enter a string: ")
# result=switch_case(sring)
# print("Switched case string:", result)

##                         to add numbers in a string

# def addnumbers(s):
#     total=0
#     nstr=""
#     for i in range(0,len(s)):
#         if "0"<= s[i]<="9":
#             total=total+(ord(s[i])-48)
#         else:
#             nstr=nstr+s[i]
#     return nstr+str(total)
# string=input("Enter a string: ")
# total=addnumbers(string)
# print(total)

#                               to add digits in a string 
# def addnumbers(s):
#     total=0
#     nsum=0
#     nstr=""
#     for i in range(0,len(s)):
#         if "0"<= s[i]<="9":
#             total=(total*10)+(ord(s[i])-48)
#         else:
#             if total>0:
#                 nsum=nsum+total
#                 total=0
#             nstr=nstr+s[i]
#     if total>0:
#         nsum=nsum+total
#     return nstr+str(nsum)
# string=input("Enter a string: ")
# total=addnumbers(string)
# print(total)

#=============================================REVERSE STRING ============================================================
##              Reverse the given string incrementing loop
# def reverse_string(s):
#     nstr=""
#     for i in range(len(s)):
#         nstr=s[i]+nstr
#     return nstr
# string=input("Enter a string: ")
# result=reverse_string(string)
# print("Reversed string:", result)


##              Reverse the given string  in incrementing using recursion
# def reverseRecursive(s,i,nstr):
#     if i>=len(s):
#         return nstr
#     nstr=s[i]+nstr
#     return reverseRecursive(s,i+1,nstr)
# string=input("Enter a string: ")
# result=reverseRecursive(string,0,"")
# print("Reversed string:", result)

##              Reverse the given string decrementing loop
# def reverse_string(s):    
#     nstr=""
#     for i in range(len(s)-1,-1,-1):
#         nstr=nstr+s[i]
#     return nstr
# string=input("Enter a string: ")
# result=reverse_string(string)
# print("Reversed string:", result)

##              Reverse the given string  in decrementing using recursion
# def reverseRecursive(s,i,nstr):
#     if i<0:
#         return nstr
#     nstr=nstr+s[i]
#     return reverseRecursive(s,i-1,nstr)
# string=input("Enter a string: ")  
# result=reverseRecursive(string,len(string)-1,"")
# print("Reversed string:", result)


# to reverse each individual word in a string without reversing the position of the words ignoring unwanted spaces

# def reverse_words(s):
#     word=""
#     nsentence=""
#     for i in range(0,(len(s)+1)):
#         s=s+" "
#         if s[i]!=" ":
#             word=s[i]+word
#         elif word!="":
#             if nsentence==" ":
#                 nsentence=nsentence+word
#             else:
#                 nsentence=nsentence+" "+word
#             word=""
#     return nsentence
# string=input("Enter a string: ")
# result=reverse_words(string)
# print("Reversed words in the string:", result)


#======================================STRING PALINDROME==========================================================

# def is_palinfilter(s):
#     nstr=""
#     for i in range(0,len(s)):
#         if "A" <=s[i]<="Z":
#             nstr=nstr+chr(ord(s[i])+32)
#         elif "a" <=s[i]<="z" or "0" <=s[i]<="9":
#             nstr=nstr+s[i]
#     return nstr
# def is_palindrome(s):
#     s=is_palinfilter(s)
#     left,right=0,len(s)-1
#     while left<right:
#         if s[left]!=s[right]:
#             return False
#         left+=1
#         right-=1
#     return True
# s=input("Enter a string: ")
# print("Original string:", s)
# flag=is_palindrome(s)
# if flag:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")