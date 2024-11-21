def reverse_int(number):
    reverse_number = 0
    while number > 0:    
        last_digit = number % 10
        reverse_number = reverse_number * 10 + last_digit
        number //= 10
    return reverse_number

print(reverse_int(12))