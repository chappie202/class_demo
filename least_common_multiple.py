def lcm(int1,int2):
    """
    int1: number
    int2: number
    returns the least common multiple
    """
    sum = 0
    while True:
        sum += max(int1,int2)
        if sum % int1 == 0 and sum % int2 == 0:
            return sum

print("The least common multiple is:", lcm(4,6))
print("The least common multiple is:", lcm(10,30))
print("The least common multiple is:", lcm(5,9))