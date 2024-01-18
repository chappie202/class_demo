def is_perfect(input_int):
    """
    input_int: number
    return: True if sum is equal to input_int, False if antying else
    """
    sum = 0
    for i in range(1,input_int):
        if input_int % i == 0:
            sum = sum+i
            if sum == input_int:
                return True
    return False

print("This is a perfect number:", is_perfect(496))