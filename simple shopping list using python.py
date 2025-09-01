import math

foods=[]
prices=[]
 
while True:
    food=input("Enter the food you want to buy:")
    if food=="y":
        break
    else:
        while True:
            price=float(input("Enter the price:"))
   
            if price<=0:
                print("price can not be less or equal to zero")
            else:
                break

    foods.append(food)
    prices.append(price)

for food in foods:
    print("---------------")
    print(food)

Amount=sum(prices)

print(f"Amount:{round(Amount,2)}")
