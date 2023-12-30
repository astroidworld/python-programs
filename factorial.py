# program for factorial

def facto(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial*i
        
    return factorial    



# driver program
number = 4
print(f"The factorial of {number} is : ", facto(number))