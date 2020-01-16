nums = [1,2,3,4,1]


# for i in range(len(nums)):
#     if nums[i] in nums[i+1:len(nums)]:
#         print("True")
#         break
# else:
#     print("False")
print(len(set(nums))!=len(nums))
