def save_transaction(price, credit_card, description) :
    file = open ("C:\\Users\HP\Desktop\\transactions.txt", "a")
    file.write("%07d%16s%16s\n" % (price * 100, credit_card , description))
    file.close()


items   = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
prices  = [1.50, 2.20, 1.80, 1.20]
running = True

while running :
    option = 1
    for choice in items :
        print(str(option) + ". " + choice)
        option = option + 1
    print(str(option) + ". Quit")
    choice = int(input("choose an option: "))
    if choice == option:
        running = False
    else:
        credit_card = input ("Credit card number: ")   
        save_transaction(prices[choice -1], credit_card, items[choice -1])
