prices={"coffee" : 1.50, "water" : 1.00, "coke" : 1.40, "snacks" : 2.00}
calc=lambda product, quantity:prices[product]*int(quantity)
print(f"{calc(input(),input()):.2f}")