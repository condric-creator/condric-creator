from datetime import datetime

class Sale:
    def __init__(self, amount_liters, price_per_liter):
        self.amount_liters = amount_liters
        self.price_per_liter = price_per_liter
        # This records the exact time the sale object is created
        self.time_of_sale = datetime.now()

    def calculate_total(self):
        return self.amount_liters * self.price_per_liter

# List to store our sale objects
sales_list = []

while True:
    user_input = input("Enter liters sold (or 'w' to quit): ").lower()
    
    if user_input == 'w':
        break
    
    try:
        liters = float(user_input)
        price = float(input("Enter price per liter: "))
        
        # Create a NEW object instance and add it to our list
        new_sale = Sale(liters, price)
        sales_list.append(new_sale)
        print("Sale recorded!")
        
    except ValueError:
        print("Please enter a valid number.")

# Final Report
print("\n--- DAILY MILK LEDGER ---")
total_revenue = 0

for sale in sales_list:
    # We check if the hour of the sale is before 10 AM
    if sale.time_of_sale.hour < 10:
        revenue = sale.calculate_total()
        total_revenue += revenue
        print(f"Time: {sale.time_of_sale.strftime('%H:%M')} | Revenue: {revenue} KSH")
    else:
        print(f"Time: {sale.time_of_sale.strftime('%H:%M')} | Sale skipped (After 10:00 AM)")

print(f"Total Revenue before 10 AM: {total_revenue} KSH")