numbers = [1, 99, 456, 54, 78]
# numbers.sort()
# print(numbers[-1])

maxNum = numbers[0]
for num in numbers:
    if num > maxNum:
        maxNum = num
print(maxNum)