# Time Converter

Seconds = int(input("Enter the number of seconds: "))

Hours = Seconds // 3600
Minutes = (Seconds % 3600) // 60
Seconds = Seconds % 60

print(f"{Hours} hours, {Minutes} minutes, {Seconds} seconds")

# Electricity

Units=int(input("Enter the number of units consumed: "))
Cost=Units*100
print("Total cost of electricity bill is:",Cost)

# Restraunant Bill Splitter

bill=int(input('Total Food Bill:'))
people=int(input('Number of People:'))
gst=int(input("GST:"))
tip=int(input("TIP:"))

total_bill=bill+gst+tip
bill_per_person=total_bill/people
gst_amount=(gst/100)*bill
tip_amount=(tip/100)*bill
print("bill_per_person",bill_per_person)
print("gst:",gst_amount)
print("tip:",tip_amount)
print("Each person has to pay:",bill_per_person)

# Profit and Loss Calculator

cost_price=int(input("Enter the cost price:"))
selling_price=int(input("Enter the selling price:"))

if selling_price>cost_price:
    profit=selling_price-cost_price
    print("Profit:",profit)
else:
    loss=cost_price-selling_price
    print("Loss:",loss)
