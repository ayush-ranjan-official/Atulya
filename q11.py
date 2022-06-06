s=input('Enter the string:')
a=0
for i in range(int(len(s)/2)+1):
    if s[i]==s[len(s)-1-i]:
        a+=1

if a == int(len(s)/2)+1:
    print('Palindrome')
else:
    print('Not a palindrome')