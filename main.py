print("Welcome to Gross Margin Evaluation program")
revenue = float(input("Revenue generated:\n"))
cogs = float(input("Cost Of Goods Sold(COGS):\n"))
Gross_Margin = ((revenue-cogs)/revenue)*100
print("Your Gross Margin is " + str(Gross_Margin))