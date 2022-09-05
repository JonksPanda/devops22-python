#1. Programmet ska vara icke-case-sensitive. Det ska alltså inte spela någon roll
#om användaren använder stora eller små bokstäver. Namn som skrivs ut ska
#dock alltid börja med stor bokstav.

#2. Programmet ska låta användaren mata in tre personers namn, ålder och
#skostorlek. Dessa uppgifter måste sparas under programmets körning.

#3. Programmet ska sedan skriva ut namn och skostorlek på den person som är
#äldst samt namn och ålder på den som har medianskostorlek.

#4. Efter det ska användaren kunna söka efter personer genom att mata in en av
#de tre datatyperna. Om programmet hittar någon som matchar ska dennes
#kompletta uppgifter skrivas ut.

#hämta info om person1
name1 = input("Name of person 1: ").lower()
age1 = int(input("age of person 1: "))
size1 = int(input("Shoe size of person 1: "))

#hämta info om person2
name2 = input("Name of person 2: ").lower()
age2 = int(input("age of person 2: "))
size2 = int(input("Shoe size of person 2: "))

#hämta info om person3
name3 = input("Name of person 3: ").lower()
age3 = int(input("age of person 3: "))
size3 = int(input("Shoe size of person 3: "))

#spara ner info i dictionary??
people = [
    {"name":name1.capitalize(), "age":age1, "shoesize":size1},
    {"name":name2.capitalize(), "age":age2, "shoesize":size2},
    {"name":name3.capitalize(), "age":age3, "shoesize":size3}
]

#Ge info om vem som är äldst, åldern och skostorlek
sorted_people = sorted(people, key=lambda k: k["age"])

print("Oldest person is " + str(sorted_people[-1]["name"]) + ", with a stunning age of " + str(sorted_people[-1]["age"]) + " years! Shoe size is " + str(sorted_people[-1]["shoesize"]))

#Visa namn på vem som har median-skostorlek och printa ut skostorleken och ålder
sorted_people = sorted(people, key=lambda k: k["shoesize"])

print("Person with median Shoe Size is " + str(sorted_people[1]["name"]).capitalize() + ", with a shoe Size of " + str(sorted_people[1]["shoesize"]) + " and an age of " + str(sorted_people[1]["age"]))

#Be användaren söka på person baserat på ålder, namn eller skostorlek
search_dict = {
    "age":{
        str(age1):people[0],
        str(age2):people[1],
        str(age3):people[2] 
    },
    "name":{
        str(name1):people[0],
        str(name2):people[1],
        str(name3):people[2]    
    },
    "shoesize":{
        str(size1):people[0],
        str(size2):people[1],
        str(size3):people[2] 
    }
}

key, value = input("Enter search value, name, age or size followed by value. (Example: age 25): ").split(" ")

key = key.lower()

found_person = search_dict[key.lower()][value.capitalize()]
print("Found person!")
print(f"Name: {found_person['name']}")
print(f"Age: {found_person['age']}")
print(f"Shoe size: {found_person['shoesize']}")