attentionMSG = "ATTENTION: If you suspect your pup has ingested something potentially harmful, immediately call your veterinarian or the ASPCA Animal Poison Control Center (APCC) at (888) 426-4435. There is a moderate fee for the call, but they are your best resource for any animal poison-related emergency, 24 hours a day, 365 days a year. This program is not meant to replace proper research and may not recognize all dangerous foods. Please do research and ask your vet before feeding your pet anything that is not specifically made for them."
print(attentionMSG)
dogDangers = {"chocolate", "xylitol", "grapes", "raisins", "currants", "avocado", "grape", "raisin", "currant", "avocados", "cinnamon", "raw potato", "onions", "raw potatos", "onion", "garlic", "chives", "macadamia", "pecans", "walnuts", "nutmeg", "sugar", "mushrooms", "chive", "macadamia nut", "macadamia nuts", "pecan", "walnut", "mushroom", "alcohol", "bones", "bone", "bread dough"}

again = "y"

while again.lower() == "y":
    food = input("What food are you thinking about feeding your dog?\n")
    if food.lower() in dogDangers:
        print("That food is dangerous for your dog! Please do not feed it to your dog. You can do more research on the internet if you would like to know why.")
    else:
        print("That food isn't on our list of dangerous foods, but that might not mean it is safe! Please ask your vet and do thorough research before feeding anything to your pet.")
    again = input("Would you like to input another food? (y or n)\n")