menu={
    "burger":5.99,
    "fries":2.99,
    "soda":1.49,
    "salad":4.49,
    "pizza":8.99,
    "ice cream":3.49,
    "brownie":2.99
}
cart=[]
total=0
print("Welcome to the restaurant!")
for key,value in menu.items():
    print(f"{key}:${value:.2f}")
print("----------")   
while True:
    item=input("Enter the food item you want to order (press q to quit): ").strip().lower() 
    if item=='q':
        break
    elif item in menu:
        cart.append(item)
        total+=menu[item]
        print(f"{item} added to cart.")
    else:
        print(f"Sorry, we don't have {item} on the menu.")
print("----------RECEIPT---------")    
for item in cart:
    print(f"{item}: ${menu[item]:.2f}")
print(f"\nTotal amount to be paid is: ${total:.2f}")
print("Thank you for dining with us!")    