
sum = 0
sum1 =0
while True:

    b = int(input('Enter the number'))
    if b % 2 == 0:
        sum += b
    else:
        sum1 = sum1 * b
    a = input('Enter a character press q to terminate')
    if a=='q' or a=='Q':
        break
    else:
        continue

print('Sum of even Number', sum)
print('Product Of odd number', sum1)
