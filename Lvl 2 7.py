customer_name = "Darshan"
mobile_number = "9876543210"
purchase_cost = 1200.0

discount_rate = 10
discount_amount = (discount_rate / 100) * purchase_cost
total_amount = purchase_cost - discount_amount
print("Customer Name:", customer_name)
print("Mobile Number:", mobile_number)
print("Cost of Purchase: ₹", purchase_cost)
print("Discount Applied:", discount_rate, "%")
print("Discount Amount: ₹", discount_amount)
print("Total Amount to be Paid: ₹", total_amount)
