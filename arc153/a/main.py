N = int(input())

coef = [1,0,0,0,0,0]

num=0
for i in range(6):
    num += coef[i]*10**(5-i)
num += N-1

s_num= str(num)
for s in range(6):
    coef[s]=int(s_num[s])

result = coef[0]*10**8 + coef[0]*10**7+ coef[1]*10**6 + coef[2]*10**5 + coef[3]*10**4 + coef[3]*10**3 + coef[4]*10**2 + coef[5]*10 + coef[4]

print(result)
