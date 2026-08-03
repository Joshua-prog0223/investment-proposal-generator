# ===============================================
# Investment Proposal
# Version 1.0
# ===============================================

# --------- Client Information -----------

client_name = "John Smith"

capital = 23500000

# ------ Strategic Asset Allocation ------

equity_weight = 62
bond_weight = 23
alternative_weight = 10
cash_weight = 5

# ------ Allocation Validation ------------

total_weight = (
    equity_weight
    + bond_weight
    + alternative_weight
    + cash_weight
)

if total_weight != 100:
    print("Error : Allocation must total 100%")
else:
    # -------- Portfolio allocation -----------

    equity_amount = capital * equity_weight / 100
    bond_amount = capital * bond_weight / 100
    alternative_amount = capital * alternative_weight / 100
    cash_amount = capital * cash_weight / 100

    # --------- Report --------------

    print("=" * 45)
    print(" INVESTMENT PROPOSAL")
    print("=" * 45)

    print(f"client : {client_name}")
    print(f"capital : {capital:,.0f} CHF")

    print()

    print("sugessted allocation")
    print("=" * 45)

    print(f"Equities       : {equity_weight}%   | {equity_amount:,.0f} CHF")
    print(f"Bonds          : {bond_weight}%   | {bond_amount:,.0f} CHF")
    print(f"Alternatives   : {alternative_weight}%   | {alternative_amount:,.0f} CHF")
    print(f"Cash           : {cash_weight}%   | {cash_amount:,.0f} CHF")

    print("-" * 45)

    print("Portfolio Allocation Completed.")