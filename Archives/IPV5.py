# ===============================================
# Investment Proposal
# Version 1.2
# ===============================================

# ---------- Client Information ----------

name = input("Name : ")
capital = float(input("Capital : "))

# ---------- Strategic Asset Allocation ----------

Conservative = {

    "Equities": 40,
    "Bonds": 45,
    "Alternatives": 10,
    "Cash": 5

}

Balanced = {

    "Equities": 60,
    "Bonds": 30,
    "Alternatives": 5,
    "Cash": 5

}

Growth = {

    "Equities": 80,
    "Bonds": 10,
    "Alternatives": 5,
    "Cash": 5

}

print()
print("Choose Risk Profile")
print("1 - Conservative")
print("2 - Balanced")
print("3 - Growth")

profile = int(input("Your choice : "))

if profile == 1:

    portfolio = Conservative

elif profile == 2:

    portfolio = Balanced

elif profile == 3:

    portfolio = Growth

else:

    print("Invalid choice.")
    exit()

# ---------- Allocation Validation ----------

total_weight = sum(portfolio.values())

if total_weight != 100:

    print()
    print("=" * 45)
    print("ERROR")
    print("=" * 45)
    print()
    print("Portfolio Allocation Invalid")
    print(f"Current Allocation : {total_weight}%")
    print("Allocation must equal 100%")

else:

    # ---------- Report ----------

    print()
    print("=" * 45)
    print("      INVESTMENT PROPOSAL")
    print("=" * 45)

    print()
    print("Client")
    print(name)

    print()
    print("Capital")
    print(f"{capital:,.0f} CHF")

    print()
    print("-" * 45)
    print("Strategic Asset Allocation")
    print("-" * 45)

    for asset in portfolio:

        amount = capital * portfolio[asset] / 100

        print()
        print(asset)
        print(f"{portfolio[asset]} %")
        print(f"{amount:,.0f} CHF")

    print()
    print("-" * 45)

    print()
    print("Total Allocation")
    print(f"{total_weight} %")
    print(f"{capital:,.0f} CHF")

    print()

    print("Portfolio Validation")
    print("PASSED")

    print()

    print("Status")
    print("READY FOR REVIEW")