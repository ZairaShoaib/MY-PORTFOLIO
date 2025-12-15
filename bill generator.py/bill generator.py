# -----------------------------------------------MINI PROJECT-------------------------------------------------------------

# -----------------------------------------ELECTRICITY BILL GENERATOR-----------------------------------------------------

# PROBLEM STATEMENT :

# Calculate electricity bill based on the following:
# First 100 units → Free
# Next 100 units (101–200) → 5 per unit
# Above 200 units → 10 per unit

# CODE :

units = int(input("Enter electricity units :"))

if units <= 100:
    bill = 0

elif units <= 200:
    bill = (units - 100) * 5

else:
    bill = (100 * 5) + (units - 200) * 10


print("Your electricity bill is:", bill)


# SAMPLE OUTPUT:

# Enter electricity units: 250
# Your electricity bill is: 1000