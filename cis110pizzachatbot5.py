userName = input("Enter your name: ").lower()

while len(userName) == 0:
    print("Name cannot be blank! Please enter your name:")
    userName = input("Enter your name: ").lower()

if userName == "tyquan wilson":
    print(f"\nMy creator, {userName}. Pleasure to serve you!")
else:
    print(f"\nHello, {userName}. Nice to meet you!")

# ==== PIZZA INFO VALIDATION ====

# Size
size = input("What size pizza? (small, medium, large): ").lower()
while size not in ["small", "medium", "large"]:
    size = input("Invalid size! Enter small, medium, or large: ").lower()

# Flavor
flavor = input("What flavor? (cheese, pepperoni, veggie, etc.): ").lower()
while len(flavor) == 0:
    flavor = input("Flavor cannot be blank! Enter a flavor: ").lower()

# Crust
crustType = input("What crust type? (thin, regular, stuffed): ").lower()
while crustType not in ["thin", "regular", "stuffed"]:
    crustType = input("Invalid crust! Enter thin, regular, or stuffed: ").lower()

# Quantity (must be a NUMBER)
quantity = input("How many of these do you want to order? Enter a numeric value: ")
while not quantity.isdigit():
    print("Value not recognized. Please enter a numeric value.")
    quantity = input("How many of these do you want to order? ")

quantity = int(quantity)

# ==== DELIVERY VALIDATION ====
orderType = input("Delivery or carryout?: ").lower()
while orderType not in ["delivery", "carryout", "carry-out", "carry out"]:
    orderType = input("Invalid entry! Type 'delivery' or 'carryout': ").lower()

# Delivery Fee
if orderType == "delivery":
    deliveryFee = 5
else:
    deliveryFee = 0

# ==== PRICE LOGIC ====
if size == "small":
    pizzaCost = 8.99
elif size == "medium":
    pizzaCost = 12.99
elif size == "large":
    pizzaCost = 17.99

# Subtotal
totalCost = pizzaCost * quantity + deliveryFee

# Coupon Logic
coupon = 0
if totalCost >= 50:
    coupon = 10

# ==== OUTPUT ====
print("\n--- ORDER SUMMARY ---")
print(f"Customer: {userName}")
print(f"Pizza size: {size}")
print(f"Flavor: {flavor}")
print(f"Crust: {crustType}")
print(f"Quantity: {quantity}")
print(f"Order Type: {orderType}")
print(f"Delivery Fee: ${deliveryFee:.2f}")
print(f"Subtotal: ${totalCost:.2f}")

if coupon > 0:
    print("Congrats! Your order qualifies for a free $10 coupon!")