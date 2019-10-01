e=0
while True:
         a=input('Enteer the string')
         if len(a)>=3 and a[0]==a[len(a)-1]:
             e+=1
         b=input('Press N to terminate the program')
         if b=='n' or b=='N':
             break

print('The Number of string with the given condition is',e)