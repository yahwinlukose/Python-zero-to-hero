food=[]
prices=[]
total=0
while True:
    food_item = input("enter a food to buy (press q to quit): ").strip().lower()
    if food_item == 'q':
        break
    else:
        
        price=input(f"enter the price of {food_item}: ")
        food.append(food_item)
        prices.append(float(price))
# ...existing code...
print("----------RECEIPT---------")
for food_item in food:
    print(food,end=" ")
for price in prices:
    print(price,end=" ")
    total+=price    
print(f"\nTotal amount to be paid is: {total}")    