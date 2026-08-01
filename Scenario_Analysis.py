# ===============================================
# Investment Proposal Generator
# Version 3.0
# Scenario Analysis
# ===============================================

# ---------- Client Information ----------

capital = float(input("Capital (CHF): "))

# ---------- Strategic Asset Allocation ----------

portfolio = {

    "Equities": 60,
    "Bonds": 25,
    "Alternatives": 10,
    "Cash": 5

}

# ---------- Scenario ----------

scenario = {

    "Equities": -0.30,
    "Bonds": 0.08,
    "Alternatives": -0.15,
    "Cash": 0.00

}

# ---------- Scenario Analysis ----------

portfolio_value = 0

print()
print("=" * 50)
print("           SCENARIO ANALYSIS")
print("=" * 50)

print()
print("Scenario : Financial Crisis")
print()

for asset in portfolio:

    # Initial Value

    initial_value = capital * portfolio[asset] / 100

    # New Value after stress

    stressed_value = initial_value * (1 + scenario[asset])

    # Gain / Loss

    variation = stressed_value - initial_value

    # Portfolio Value

    portfolio_value += stressed_value

    # ---------- Report ----------

    print("-" * 50)

    print(asset)

    print(f"Allocation : {portfolio[asset]} %")

    print(f"Initial Value : {initial_value:,.0f} CHF")

    print(f"Scenario : {scenario[asset] * 100:.0f} %")

    print(f"New Value : {stressed_value:,.0f} CHF")

    print(f"Variation : {variation:,.0f} CHF")

print("-" * 50)

portfolio_return = (
    (portfolio_value - capital)
    / capital
) * 100

print()
print("Portfolio Value")
print(f"{portfolio_value:,.0f} CHF")

print()

print("Portfolio Return")
print(f"{portfolio_return:.2f} %")



