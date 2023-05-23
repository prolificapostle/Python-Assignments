def discount_rate():
    price = float(input("Enter the price of the item you want to buy: "))
    discount = price * 0.1
    discounted_price = price - discount
    print("Your Discounted price:", discounted_price)


discount_rate()
