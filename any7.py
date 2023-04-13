def any7(nums):
    check = False
    for i in nums:
        if i == 7:
            check = True
    
    return check

    # YOUR CODE HERE 

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

