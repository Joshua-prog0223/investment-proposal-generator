# ===============================================
# Investment Proposal Generator
# Version 5.0
# Custom Stress Testing Engine
# ===============================================

# ---------- Client Information ----------

capital = float(input("Capital (CHF): "))

# ---------- Portfolio Allocation ----------

portfolio = {

    "Equities": 60,
    "Bonds": 25,
    "Alternatives": 10,
    "Cash": 5

}

# ---------- Custom Scenario ----------

print()
print("=" * 50)
print("CUSTOM STRESS TEST")
print("=" * 50)

scenario = {

    "Equities": float(input("Equities (%) : ")) / 100,
    "Bonds": float(input("Bonds (%) : ")) / 100,
    "Alternatives": float(input("Alternatives (%) : ")) / 100,
    "Cash": float(input("Cash (%) : ")) / 100

}

# ---------- Initialisation ----------

portfolio_value = 0

worst_asset = ""
worst_variation = 0

best_asset = ""
best_variation = 0

print()
print("=" * 50)
print("SCENARIO ANALYSIS")
print("=" * 50)

# ---------- Analysis ----------

for asset in portfolio:

    initial_value = capital * portfolio[asset] / 100

    stressed_value = initial_value * (1 + scenario[asset])

    variation = stressed_value - initial_value

    portfolio_value += stressed_value

    # Best / Worst contributor

    if variation < worst_variation:

        worst_variation = variation
        worst_asset = asset

    if variation > best_variation:

        best_variation = variation
        best_asset = asset

    # Report

    print("-" * 50)

    print(asset)

    print(f"Allocation : {portfolio[asset]} %")

    print(f"Initial Value : {initial_value:,.0f} CHF")

    print(f"Scenario : {scenario[asset] * 100:.0f} %")

    print(f"New Value : {stressed_value:,.0f} CHF")

    print(f"Variation : {variation:,.0f} CHF")

# ---------- Portfolio Statistics ----------

portfolio_return = (
    (portfolio_value - capital)
    / capital
) * 100

print("-" * 50)

print()
print("Portfolio Value")
print(f"{portfolio_value:,.0f} CHF")

print()

print("Portfolio Return")
print(f"{portfolio_return:.2f} %")

# ---------- Risk Assessment ----------

if portfolio_return <= -15:

    risk = "HIGH"

elif portfolio_return <= -5:

    risk = "MEDIUM"

else:

    risk = "LOW"

print()
print("Risk Level")
print(risk)

# ---------- Executive Summary ----------

print()
print("=" * 50)
print("EXECUTIVE SUMMARY")
print("=" * 50)

print()

print("Worst Contributor")
print(worst_asset)
print(f"{worst_variation:,.0f} CHF")

print()

print("Best Contributor")
print(best_asset)
print(f"+{best_variation:,.0f} CHF")

print()

print("Recommendation")

if risk == "HIGH":

    print("- Reduce equity exposure")
    print("- Increase bond allocation")
    print("- Increase cash buffer")
    print("- Review portfolio diversification")

elif risk == "MEDIUM":

    print("- Portfolio remains acceptable")
    print("- Consider increasing fixed income")
    print("- Review equity allocation")

else:

    print("- Portfolio remains resilient")
    print("- Maintain current strategic allocation")
    print("- No immediate action required")

