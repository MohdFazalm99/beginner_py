# Simple method for raising any number with the power of any number, python has a simple method where we use two * sign

print(2 ** 3)


# Example for the exponent function

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(2, 3))
