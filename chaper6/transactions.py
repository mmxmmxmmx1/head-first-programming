def save_transaction(price, credit_card, description) :
    file = open ("C:\\Users\HP\Desktop\\transactions.txt", "a")
    file.write("%07d%16s%16s\n" % (price * 100, credit_card , description))
    file.close()
