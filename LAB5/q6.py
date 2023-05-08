def is_perfect(number):
    if number <= 0:
        return False
    
    divisors_sum = sum(divisor for divisor in range(1, number) if number % divisor == 0)
    
    return divisors_sum == number


number = int(input())

if is_perfect(number):
    print("Perfect")
else:
    print("Not Perfect")