colors = []
color = "red"

colors.append(color)

print(colors[0])

colors.extend(["pink", "blue"])

pick = input("Pick a color: ").lower()

res = pick in colors
print(f"Color {pick} is in list == {res}")

pick = input("Pick a new color: ").lower()

res = pick not in colors
print(f"Color {pick} is not in list == {res}")

more_colors = ["yellow", "purple", "green"]

colors + more_colors

multiple_colors = []

multiple_colors.extend(["red"] * 2)
multiple_colors.extend(["yellow"] * 3)

print(multiple_colors[0:4])
print(multiple_colors.count("red"))
print(multiple_colors.index("yellow"))

print(f"length of list colors = {len(colors)}")
print(f"length of list more_colors = {len(more_colors)}")
print(f"length of list multiple_colors = {len(multiple_colors)}")

numbers = [5, 2, 3, 9, 8, 14, 17]

print(f"Lowest number in list is {min(numbers)}")
print(f"Total value of list is {sum(numbers)}")