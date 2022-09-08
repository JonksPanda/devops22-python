members = ("Kalle", "Pelle", "Lisa", "Anna", "Lars")

name = input("Who are you? ").lower()
name = name.capitalize()

if(name in members):
    print(f"Welcome {name}, you're on the list")
else:
    print("Sorry, you're not on the list..")