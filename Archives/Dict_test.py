portfolio = {

    "Equities":60,

    "Bonds":20,

    "Alternatives":15,

    "Cash":5

}

print(portfolio)

print()

print(portfolio["Equities"])

print(portfolio["Cash"])

for asset in portfolio:
    print(asset, portfolio[asset])