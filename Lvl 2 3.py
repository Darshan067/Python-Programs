def is_perfect(n):
    if n < 2:
        return False
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n

num = 6
if is_perfect(num):
    print("It is a perfect number")
else:
    print("It is not a perfect number")
