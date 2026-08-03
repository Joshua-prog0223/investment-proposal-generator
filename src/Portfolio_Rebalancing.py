# ---------- Client Information ----------

capital = float(input("Capital : "))

# ---------- Strategic Asset Allocation ----------

current_portfolio = {

    "Equities": 72,
    "Bonds": 18,
    "Alternatives": 5,
    "Cash": 5

}

target_portfolio = {

    "Equities": 60,
    "Bonds": 25,
    "Alternatives": 10,
    "Cash": 5

}

# ---------- Portfolio Rebalancing ----------

print()
print("-" * 45)
print("PORTFOLIO REBALANCING")
print("-" * 45)

for asset in current_portfolio:

    difference = target_portfolio[asset] - current_portfolio[asset]
    amount = capital * abs(difference) / 100

    print()
    print(asset)

    if difference > 0:
        print("BUY")

    elif difference < 0:
        print("SELL")

    else:
        print("UNCHANGED")

    print(f"{amount:,.0f} CHF")
