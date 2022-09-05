X = 1
Y = 4
addresses = {"Adam": "Ormvägen 5",
"Bella": "Klockgatan 1",
"Cornelia": "Vikingagatan 3"}
cars = ["Volvo", "Opel", "BMW"]
numbers1 = {1, 2, 3, X, 6}
numbers2 = {Y, 2, 3, 4, 7}

#1. Vilken datatyp har variablerna X och Y?
#integer

#2. Vilken datatyp har variabeln addresses?
#dictionary

#3. Hur kan man få ut bellas adress ur variabeln addresses?
print(addresses["Bella"])

#4. Vad händer om man skriver addresses[“Daniel”] = “Prinsgränd 2”?
addresses["Daniel"] = "Prinsgränd 2"
print(addresses["Daniel"])

addresses["Åke"] = "Prinsgränd 3"
addresses["Jonathan"] = "Arinsgränd 4"

#5. Få ditt program att skriva ut hur många keys addresses har.
print(f"Number of keys in addresses: {len(addresses)}")

#   5.1. Utöka programmet så att adressen skrivs ut till den personen som kommer sist i bokstavsordning
print(f"{sorted(list(addresses))[-1]}s address är {addresses[sorted(list(addresses))[-1]]}")

#   5.2. Utöka programmet så att namnet skrivs ut på den personen som bor
#   på adressen som kommer först i bokstavsordning. Tips: följande rad
#   byter plats på keys och values i my_dict:
#   my_dict = {v: k for k, v in my_dict.items()}
#   Förklaring kommer nästa lektion!
print(f"Första addressen i listan är {sorted(list({v: k for k, v in addresses.items()}))[0]}")

#6. Vilken datatyp har variabeln cars?
#Lista

#7. Vad returneras om man skriver cars[X]?
#Opel
print(cars[X])

#8. Vad returneras om man skriver cars[Y], varför?
#får error då det inte finns något på plats 4
#print(cars[Y])

#9. Vad returneras om man först skriver cars.sort() och på nästa rad skriver cars[0]?
#Då får man första bilen i bokstavsordning
cars.sort()
print(cars[0])

#10. Skapa en ny variabel genom att skriva cars_2 = cars, och på följande rad ska
#strängen “Saab” läggas till cars med hjälp av append(). Notera att det alltså
#bara är ena variabeln som ska utökas. Vad innehåller variablerna cars_2 och
#cars nu? Förklara!
cars_2 = cars
cars.append("Saab")

#cars_2 innehåller allt som cars innehåller och "Saab"
#cars innehåller "Volvo", "Opel", "BMW". Alltså allt som har tilldelats till cars, förutom det som tilldelats till cars_2. cars_2 är en ny lista
print(cars)
print(cars_2)

#Hade fel.. cars får visst värden som appendas till cars_2. De kommer bara referera till varandra. Måste skriva cars_2 = cars.copy()

#10.1. Skapa ytterligare en variabel cars_3 som får sina element av cars
#men som inte påverkas av vad som läggs till i cars.
cars_3 = cars.copy()
cars_3.append("Skoda")

print(cars)
print(cars_3)

#10.2. Utöka variabeln cars så att den innehåller dubbletter av varje bilmärke
#sorterat i omvänd bokstavsordning.
cars.extend(cars)
cars.sort()
cars.reverse()

print(cars)

#10.3 Från den utökade versionen av cars ifrån förra uppgiften, skapa
#variabeln unique_cars som ska vara en lista där varje bilmärke finns
#med exakt en gång.
unique_cars = list(set(cars))
print(unique_cars)

#11. Vilken datatyp har variablerna numbers1 och numbers2?
#Är sets

#12. Vilka värden finns lagrade i variablerna numbers1 och numbers2?
#numbers1 = 1, 2, 3, 6
#numbers2 = 4, 2, 3, 7

print(numbers1)
print(numbers2)

#13. Vad är snittet (intersection) mellan variablerna numbers1 och numbers2?
print(numbers1.intersection(numbers2))
#{2, 3}

#14. Vad är unionen mellan variablerna numbers1 och numbers2?
print(numbers1.union(numbers2))
#{1, 2, 3, 4, 6, 7}

#15. Vilken är den symmetriska differensen mellan numbers1 och numbers2?
print(numbers1.symmetric_difference(numbers2))
#{1, 4, 6, 7}