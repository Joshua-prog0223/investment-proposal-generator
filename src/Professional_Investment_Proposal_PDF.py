from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ------------------------------------------------
# Client Information
# ------------------------------------------------

name = input("Client name : ")

capital = float(input("Capital (CHF): "))

# ------------------------------------------------
# Portfolio
# ------------------------------------------------

portfolio = {

    "Equities": 60,
    "Bonds": 25,
    "Alternatives": 10,
    "Cash": 5

}

# ------------------------------------------------
# Scenario
# ------------------------------------------------

scenario = {

    "Equities": float(input("Equities (%) : ")) / 100,

    "Bonds": float(input("Bonds (%) : ")) / 100,

    "Alternatives": float(input("Alternatives (%) : ")) / 100,

    "Cash": float(input("Cash (%) : ")) / 100

}

# ------------------------------------------------
# Calculations
# ------------------------------------------------

portfolio_value = 0

worst_asset = ""
worst_variation = 0

best_asset = ""
best_variation = 0

for asset in portfolio:

    initial_value = capital * portfolio[asset] / 100

    stressed_value = initial_value * (1 + scenario[asset])

    variation = stressed_value - initial_value

    portfolio_value += stressed_value

    if variation < worst_variation:

        worst_variation = variation
        worst_asset = asset

    if variation > best_variation:

        best_variation = variation
        best_asset = asset

portfolio_return = ((portfolio_value - capital) / capital) * 100

# ------------------------------------------------
# Risk
# ------------------------------------------------

if portfolio_return <= -15:

    risk = "HIGH"

    recommendation = (
        "Reduce equity exposure.<br/>"
        "Increase bond allocation.<br/>"
        "Increase cash allocation.<br/>"
        "Review diversification."
    )

elif portfolio_return <= -5:

    risk = "MEDIUM"

    recommendation = (
        "Portfolio remains acceptable.<br/>"
        "Consider increasing fixed income.<br/>"
        "Review equity allocation."
    )

else:

    risk = "LOW"

    recommendation = (
        "Portfolio remains resilient.<br/>"
        "Maintain current allocation."
    )

# ------------------------------------------------
# PDF
# ------------------------------------------------

styles = getSampleStyleSheet()

document = SimpleDocTemplate("Investment_Proposal.pdf")

story = []

# Title

story.append(
    Paragraph("<b>INVESTMENT PROPOSAL</b>", styles["Title"])
)

story.append(Spacer(1,20))

# Client

story.append(Paragraph("<b>Client</b>", styles["Heading2"]))
story.append(Paragraph(name, styles["Normal"]))

story.append(Spacer(1,12))

story.append(Paragraph("<b>Capital</b>", styles["Heading2"]))
story.append(
    Paragraph(f"{capital:,.0f} CHF", styles["Normal"])
)

story.append(Spacer(1,20))

# Allocation

story.append(
    Paragraph("<b>Strategic Asset Allocation</b>", styles["Heading1"])
)

story.append(Spacer(1,12))

for asset in portfolio:

    amount = capital * portfolio[asset] / 100

    story.append(
        Paragraph(
            f"<b>{asset}</b> — {portfolio[asset]}% — {amount:,.0f} CHF",
            styles["Normal"]
        )
    )

story.append(Spacer(1,20))

# Stress Test

story.append(
    Paragraph("<b>Stress Test Results</b>", styles["Heading1"])
)

story.append(
    Paragraph(f"Portfolio Value : {portfolio_value:,.0f} CHF",
              styles["Normal"])
)

story.append(
    Paragraph(f"Portfolio Return : {portfolio_return:.2f} %",
              styles["Normal"])
)

story.append(
    Paragraph(f"Risk Level : {risk}",
              styles["Normal"])
)

story.append(Spacer(1,20))

# Executive Summary

story.append(
    Paragraph("<b>Executive Summary</b>", styles["Heading1"])
)

story.append(
    Paragraph(
        f"Worst Contributor : {worst_asset} ({worst_variation:,.0f} CHF)",
        styles["Normal"]
    )
)

story.append(
    Paragraph(
        f"Best Contributor : {best_asset} (+{best_variation:,.0f} CHF)",
        styles["Normal"]
    )
)

story.append(Spacer(1,20))

story.append(
    Paragraph("<b>Recommendation</b>", styles["Heading1"])
)

story.append(
    Paragraph(recommendation, styles["Normal"])
)

story.append(Spacer(1,30))

story.append(
    Paragraph(
        "Prepared by Investment Proposal Generator",
        styles["Italic"]
    )
)

document.build(story)

print()
print("Investment_Proposal.pdf generated successfully.")