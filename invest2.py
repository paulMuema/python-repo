principal = 10000
rate = 0.06
term = 5
totalinterest = 0
for year in range(1, term + 1):
    interest = principal * rate
    print(year, round(principal, 2), round(interest, 2))
    principal = principal + interest
    totalinterest = totalinterest + interest
print('Total Interest:', round(totalinterest, 2))
print('Final Principal:', round(principal, 2))
