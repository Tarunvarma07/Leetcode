class Solution(object):
    def minElement(self, nums):
        arr1=[]
        for num in nums:
            digit=0
            while num>0:
                digit+=num%10
                num//=10
            arr1.append(digit)
        smallest=arr1[0]
        for i in range(1,len(arr1)):
            if smallest>arr1[i]:
                smallest=arr1[i]
        return smallest
        