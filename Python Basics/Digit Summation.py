inp = input()
numbers = inp.split()

N = int(numbers[0])
M = int(numbers[1])

last_digit_of_N = N % 10
last_digit_of_M = M % 10

sum = last_digit_of_N + last_digit_of_M

print(sum)