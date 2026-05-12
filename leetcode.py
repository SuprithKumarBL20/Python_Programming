 ##             LEETCODE 33. Search in Rotated Sorted Array
    
# class Solution:
#     def search(self, nums: list[int], target: int) -> int:
#         start,end=0,len(nums)-1
#         while start<=end:
#             mid=(start+end)//2
#             if target==nums[mid]:
#                 return mid
#             #check for sorted
#             if nums[start]<=nums[mid]:
#                 if nums[start]<=target<=nums[mid]:
#                     end=mid-1
#                 else:
#                     start=mid+1
#             else:
#                 if nums[mid]<=target<=nums[end]:
#                     start=mid+1
#                 else:
#                     end=mid-1
#         return -1
    

# ##             LEETCODE 189. Rotate Array
# class Solution:
#         def reverseArr(self,nums,i,j):
#             while i<j:
#                 nums[i],nums[j]=nums[j],nums[i]
#                 i+=1
#                 j-=1
#         def rotate(self, nums: List[int], k: int) -> None:
#             """
#             Do not return anything, modify nums in-place instead.
#             """
#             n=len(nums)
#             if k>=n:
#                 k=k%n
#             self.reverseArr(nums,0,n-1)
#             self.reverseArr(nums,0,(k-1))
#             self.reverseArr(nums,k,n-1)
        
# ##             LEETCODE 283. Move Zeroes
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n=len(nums)
#         count=0
#         for i in range(0,n):
#             if nums[i]!=0:
#                 nums[count]=nums[i]
#                 count+=1
#         for i in range(count,n):
#             nums[i]=0



# ##       LEETCODE 81. Search in Rotated Sorted Array II
# class Solution:
#     def search(self, nums: list[int], target: int) -> bool:
#         start,end=0,len(nums)-1
#         while start<=end:
#             mid=(start+end)//2
#             if target==nums[mid]:
#                 return True
#             #check for sorted
#             if nums[start]<nums[mid]:
#                 if nums[start]<=target<=nums[mid]:
#                     end=mid-1
#                 else:
#                     start=mid+1
#             elif nums[start]>nums[mid]:
#                 if nums[mid]<=target<=nums[end]:
#                     start=mid+1
#                 else:
#                     end=mid-1
#             else:
#                 start+=1
#         return False
#                            # OR 
# class Solution:
#     def search(self, nums: list[int], target: int) -> int:
#         start,end=0,len(nums)-1
#         while start<=end:
#             mid=(start+end)//2
#             if target==nums[mid]:
#                 return True
#             if nums[start]==nums[mid]==nums[end]:
#                 start+=1
#                 end-=1
#                 continue
#             #check for sorted
#             if nums[start]<=nums[mid]:
#                 if nums[start]<=target<=nums[mid]:
#                     end=mid-1
#                 else:
#                     start=mid+1
#             else:
#                 if nums[mid]<=target<=nums[end]:
#                     start=mid+1
#                 else:
#                     end=mid-1
#         return False

# #LEETCODE 12. Integer to Roman
# class Solution:
# def intToRoman(self, num: int) -> str:
#     dict={"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
#     romans=""
#     for key,val in dict.items():
#         while num>=val:
#             romans=romans+key
#             num=num-val
#         if num<=0:
#             break 
#     return romans


def generateOccStr(s):
    ascii=[0]*26
    occ=""
    for i in range(0,len(s)):
        ascii[ord(s[i])-97]=ascii[ord(s[i])-97]+1
    for i in range(0,len(ascii)):
        if ascii[i]!=0:
            occ=occ+chr(i+97)+str(ascii[i])
    return occ
s=input("entr")
p=generateOccStr(s)
print(p)

# i need all occcurance of string generated in same format
# what is the error in the above code is that the variable `occ` is not defined before it is used in the loop to concatenate the characters and their counts. To fix this, you need to initialize `occ` as an empty string before the loop. Here is the corrected code:


leetcode 49. Group Anagrams
