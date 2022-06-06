b=int(input("Enter card number:"))
s=str(b)
p=len(s)-4
s1=s[p:]
a=""
for i in range(p):
    a=a+"*"
print(a+s1)