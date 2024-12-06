principal = 10000
rate = 0.06
term = 5
totalinterest = 0
for year in range(term):
    print(principal)
    interest = principal * rate
    print(interest)
    principal = principal + interest
    totalinterest = totalinterest + interest
print(totalinterest)
print(principal)
