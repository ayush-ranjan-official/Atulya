a = int(input('Enter lower limit:'))
b = int(input('Enter upper limit:'))
c=[]
for i in range(a,b+1):
    if i>1:
        for j in range(2, int(i / 2) + 1):
            if (i % j) == 0:

                break
        else:
            c.append(i)


    else:
        continue
print('List of prime numbers in given range :',c)