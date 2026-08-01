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

financial_crisis = {

    "Equities": -0.30,
    "Bonds": 0.08,
    "Alternatives": -0.15,
    "Cash": 0.00

}

inflation_shock = {

    "Equities": -0.12,
    "Bonds": -0.18,
    "Alternatives": 0.08,
    "Cash": 0.00

}

interest_rate = {

    "Equities": -0.10,
    "Bonds": -0.22,
    "Alternatives": -0.05,
    "Cash": 0.00

}

test_crash = {

    "Equities": -0.45,
    "Bonds": 0.05,
    "Alternatives": -0.10,
    "Cash": 0.00

}

oil_crisis = {

    "Equities": -0.18,
    "Bonds": 0.03,
    "Alternatives": 0.12,
    "Cash": 0.00

}



# ---------- Scenario Analysis ----------

print("Choose Scenario")

print("1 Financial Crisis")

print("2 Inflation Shock")

print("3 Interest Rate Shock")

print("4 Tech Crash")

print("5 Oil Crisis")

choice = input("Selection : ")

if choice == "1":

    scenario = financial_crisis

elif choice == "2":

    scenario = inflation_shock

elif choice == "3":

    scenario = interest_rate

elif choice == "4":

    scenario = test_crash

elif choice == "5":

    scenario = oil_crisis



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