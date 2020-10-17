# Follow the assignment instructions to code an app that
# will tell a user their birthstone.
month = input("Enter the number of the month you were born (1-12): ")
month = int(month)
if month == 1:
    birthstone = "Garnet"
elif month == 2:
    birthstone = "amethyst"
elif month == 3:
    birthstone = "aquamarine"
elif month == 4:
    birthstone = "Diamond"
elif month == 5:
    birthstone = "Emerald"
elif month == 6:
    birthstone = "Pearl"
elif month == 7:
    birthstone = "Ruby"
elif month == 8:
    birthstone = "Peridot"
elif month == 9:
    birthstone = "Sapphire"
elif month == 10:
    birthstone = "Opal"
elif month == 11:
    birthstone = "Topaz"
elif month == 12:
    birthstone = "Tanzanite"
print(f"Your birthstone is {birthstone}")
