# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:11:46 2020

@author: Nick
"""

nums = []

def get_data():
    data = input()
    global nums
    nums = data.split(",")
    nums = list(map(float, nums))
    
    #print("LIST BEFORE: ", nums)
    
def my_max():
    global nums
    max = nums[0]
    
    for x in range(len(nums)):
        if max < nums[x]:
            max = nums[x]
            
    return max
        

def my_min():
    global nums
    min = nums[0]
    
    for x in range(len(nums)):
        if min > nums[x]:
            min = nums[x]
    
    return min


def my_range():
    max = my_max()
    min = my_min()
    
    return max - min


def my_sum():
    global nums
    total = 0
    
    for x in range(len(nums)):
        total += nums[x]
    
    return total


def mean():
    global nums
    total = 0
    count = 0
    
    for x in range(len(nums)):
        total += nums[x]
        count += 1
    
    return total / count


def median():
    global nums
    sortedNums = sorted(nums)
    length = len(nums)
    index = (length - 1) // 2
    
    if len(nums) % 2:
        return sortedNums[index]
    else:
        return (sortedNums[index] + sortedNums[index + 1]) / 2


def mode():
    global nums
    maxCount = (0, 0)
    
    for num in nums:
        freq = nums.count(num)
        if freq > maxCount[0]:
            maxCount = (freq, num)
    
    modes = [maxCount[1]]
    return modes
    
    
def prime():
    global nums
    num = int(nums[0])
    #print(num)
    
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return "not prime"
                break
        else:
            return "prime"
    else:
        return "not prime"
    

def factorize():
    global nums
    num = int(nums[0])
    i = 2
    factors = []
    
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    
    return factors


def fib(num):
    
    if num == 0: 
        return 0
    elif num == 1: 
        return 1
    else: 
        return fib(num - 1) + fib(num - 2) 


def main():
    
    while (1):
        cmd = input()
        cmd = cmd.lower()
        global nums
        #nums = [1,2,3,3,4,4]
    
        if cmd == "get_data":
            get_data()
            print(">", nums)
            
        elif cmd == "my_max":
            print(">", my_max())
            
        elif cmd == "my_min":
            print(">", my_min())
            
        elif cmd == "my_range":
            print(">", my_range())
            
        elif cmd == "my_sum":
            print(">", my_sum())
            
        elif cmd == "mean":
            print(">", mean())
            
        elif cmd == "median":
            print(">", median())
        
        elif cmd == "mode":
            print(">", mode())
            
        elif cmd == "prime":
            print(">", prime())
            
        elif cmd == "factorize":
            print(">", factorize())
            
        elif cmd == "fib":
            print(">", fib(nums[0]))
        
        elif cmd == "exit":
            print(">", "goodbye")
            break
        else:
            print("invalid command")
        


main()