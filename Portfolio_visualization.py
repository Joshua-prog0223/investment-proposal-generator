import matplotlib.pyplot as plt
portfolio = {

    "Equities":60,

    "Bonds":25,

    "Alternatives":10,

    "Cash":5

}

labels = portfolio.keys()

sizes = portfolio.values()

plt.figure(figsize=(6,6))

plt.pie(

    sizes,

    labels=labels,

    autopct="%1.0f%%",

    startangle=90

)

plt.title("Strategic Asset Allocation")

plt.savefig("allocation_chart.png")

plt.close()
