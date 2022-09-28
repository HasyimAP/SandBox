#=========================================================#
# Goal Description
# A number is considered 'pretty' if all its digits are the same number and not 0 (eg 333, 5, 44). Given a number X which is not divisible by 2 and 5 (relatively prime by 10 in short). Write a program that accepts input X and returns the smallest 'pretty' number that is divisible by X.
#=========================================================#

def check_same_digits(N: int) -> bool:
    # find the last digit
    digit = N % 10

    while (N != 0):
        # current last digit
        current_digit = N % 10;

        # update the value of N
        N = N // 10

        # if there are any different digit return False
        if (current_digit != digit):
            return False
    
    # otherwise return True
    return True

def pretty_number(X: int):
    N = X

    if (X % 2 == 0):
        return f'{X} is multiple of 2. Try other number'
    elif (X % 5 == 0):
        return f'{X} is multiple of 5. Try other number'


    while True:
        if check_same_digits(N) and (N % 2 != 0) and (N % 5 != 0):
            break
        else:
            N += X
    
    return f'The smallest pretty number that is divisible by {X} is {N}'

#=========================================================#
# Testing
#=========================================================#
print(pretty_number(7))
print(pretty_number(13))
print(pretty_number(259))
print(pretty_number(222))
print(pretty_number(15))
print(pretty_number(123))