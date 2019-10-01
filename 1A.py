a=int(input('Enter the number of rows to be printed'))
for i in range(0,a):
    for j in range(0,i+1):
        print(i+1,end=" ")
        j+=1
    print('\n')
    i+=1