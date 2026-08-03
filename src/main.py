from client import get_client_information
from portfolio import build_portfolio
from stress_testing import run_stress_test
from visualization import create_allocation_chart
from reporting import generate_pdf


def main():

    # Client
    client = get_client_information()

    # Portfolio Construction
    portfolio = build_portfolio(client)

    # Stress Testing
    stress_results = run_stress_test(client, portfolio)

    # Chart
    create_allocation_chart(portfolio)

    # PDF
    generate_pdf(client, portfolio, stress_results)

    print()
    print("=" * 50)
    print("Investment Proposal Generated Successfully")
    print("=" * 50)


if __name__ == "__main__":
    main()