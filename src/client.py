def get_client_information():

    name = input("Client name : ")

    capital = float(input("Capital (CHF): "))

    return {

        "name": name,

        "capital": capital

    }