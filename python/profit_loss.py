purschase_price = float(input("Enter the purchase price: "))
selling_price = float(input("Enter the selling price :"))

if selling_price > purschase_price:
    profit = selling_price - purschase_price
    print(f"profit of {profit:.2f}")
elif selling_price < purschase_price:
    loss = purschase_price - selling_price
    print(f"Loss of {loss:.2f}")
else: 
    print("No profit , no Loss")


