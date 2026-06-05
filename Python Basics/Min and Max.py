inp = input()
numbers = inp.split()

A = int(numbers[0])
B = int(numbers[1])
C = int(numbers[2])

min = A
max = A

if B < min:
    min = B

if C < min:
    min = C


if B > max:
    max = B

if C > max:
    max = C

print(min, max)