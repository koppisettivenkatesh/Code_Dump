x =121
if x < 0 :
    return False
temp =  x
rev = 0
while  x > 0 :
    mod = x % 10
    rev = rev *10 + mod
    x = x//10
return temp == rev
