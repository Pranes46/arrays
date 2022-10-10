class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1]  #creating a list with value 1
        
        for i in range(1,len(nums)):
            result.append(nums[i-1]*result[-1]) # we are appending the prefix value multiplied with result
            
        suffixrunningproduct = 1  #to calculate the suffix we are creating a variable
        for i in range(len(result)-2,-1,-1):  #to access the list from backwards
            result[i]= result[i]* nums[i+1] *suffixrunningproduct  #we are multiplying the result, num and suffix and storing it in the same place of result
            suffixrunningproduct = suffixrunningproduct* nums[i+1] #updating the suffix value by multiplying with nums
            
        return result  
        