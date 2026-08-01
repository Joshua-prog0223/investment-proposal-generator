# ===============================================
# Investment Proposal
# Version 1.2
# ===============================================

# ---------- Client Information ----------

name = input("Name : ")
capital = float(input("Capital : "))

# ---------- Strategic Asset Allocation ----------

portfolio = {

    "Equities": int(input("Equities (%) : ")),
    "Bonds": int(input("Bonds (%) : ")),
    "Alternatives": int(input("Alternatives (%) : ")),
    "Cash": int(input("Cash (%) : "))

}

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