principal = float(input("Principal: "))
rate = int(input("Rate: "))
term = int(input("Term: "))

if principal >= 0 and rate >= 0 and rate <= 100 and term >= 0:
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
else:
    print("ERROR: Invalid inputs.")
