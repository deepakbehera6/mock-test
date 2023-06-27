nums = [0,1,0,3,12]
count = 0
for i in nums:
   if(i==0):
      nums.remove(i)
      count = count+1
for i in range(count):
   nums.append(0)
print(nums)