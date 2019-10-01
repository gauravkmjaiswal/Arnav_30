a=int(input('Enter the number of rows here '))
c=a+3
for i in range(0,a):
    if((i%2)==0):
        for j in range(0,17):
            print('0',end="")
            j+=1
    else:
        for k in range(0,c-1):
            print('0', end="")
            k += 1
    print('\n')
    i+=1
