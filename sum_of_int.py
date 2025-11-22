def sum_of_int(x):
    sum = 0
    for i in range(x+1):
        sum = i + sum
    return sum

print(sum_of_int(4))