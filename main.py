def calculate_balance(return_amount):
    # initialise a list of cash notes and cents
    notes = [100, 50, 20, 10, 5, 1, 0.5, 0.2, 0.1, 0.05, 0.01]
    i = 0
    print("\nAmount to returned: RM%.2f" % return_amount)
    while return_amount > 0:
        i = i + 1
        if return_amount < notes[i - 1]:    # search for the largest cash notes or cents to pay back
            continue
        num = return_amount // notes[i - 1]     # get number of cash note or cents return
        return_amount = round(return_amount % notes[i - 1], 2)      # get remaining amount
        print("RM %.2f: %dpcs" % (notes[i - 1], num))


def validation(num, total):
    return (len(num.rsplit('.')[-1]) <= 2 or num.rfind('.') == -1) and float(num) >= total


if __name__ == "__main__":
    print("Vending Machines")
    print("No.  Drink            RM ")
    print("1    Coca Cola        1.50")
    print("2    Pepsi            1.80")
    print("3    Orange           3.00")
    print("4    Coffee           4.50")
    print("5    Boba Milk Tea    7.80")

    try:
        price = [1.5, 1.8, 3.0, 4.5, 7.8]
        total_cost = 0
        flag = True
        while flag:
            no = int(input("\nWhich drink you want to buy: "))
            quan = int(input("How many you want: "))
            total_cost = total_cost + (price[no - 1] * quan)
            print("Press 'y' to add more order, any key to proceed to payment")
            flag = True if str(input("Choice: ")) == "y" else False

        print("\nTotal: RM%.2f" % total_cost)
        while True:
            cash = str(input("How much you pay: RM "))
            if not validation(cash, total_cost):  # input validation for 2 decimal places
                print("Invalid amount paid")
                continue
            break

        cash_received = float(cash)
        calculate_balance(cash_received - total_cost)

    except:
        print("Invalid input value")
