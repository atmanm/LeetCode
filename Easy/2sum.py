#Given an array of integers, return indices of the two numbers such that they
#add up to a specific target.

def twoSum(nums, target):
    numDict = {}
    for index in range(len(nums)):
        diff = target - nums[index]
        try:
            #If difference of target and current number in array
            #is in the dict, we're done
            otherIndex = numDict[diff]
            break
        except:
            #This means difference is not in dict. Add the number
            #to the dict so if we get (target-number) in future, we
            #will be able to get 2 sum
            numDict[nums[index]] = index

    #Testcases want the smaller index to be returned first
    if index < otherIndex:
        return [index, otherIndex]
    else:
        return [otherIndex, index]


if __name__ == "__main__":
    nums = [int(x) for x in input().strip().split(' ')]
    target = int(input())
    print (twoSum(nums, target))
