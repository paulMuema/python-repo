principal = float(input("Principal: "))
rate = int(input("Rate: "))
term = int(input("Term: "))

if principal <= 0:
    print("ERROR: Principal must be greater that zero.")
elif rate <= 0:
    print("ERROR: Rate must be greater than zero.")
elif rate > 100:
    print("ERROR: Rate must not exceed 100.")
elif term <= 0:
    print("ERROR: Term must be greater than zero.")
else:
    rate = rate / 100
    totalinterest = 0
    heading_years = "YEARS"
    heading_pri = "PRINCIPAL"
    heading_int = "INTEREST"
    print(f"{heading_years} {heading_pri:>17} {heading_int:>20}")
    for year in range(1, term + 1):
        interest = principal * rate
        print(f"{year} {principal:20.2f} {interest:20.2f}")
        principal = principal + interest
        totalinterest = totalinterest + interest
    print('Total Interest:', round(totalinterest, 2))
    print('Final Principal:', round(principal, 2))
