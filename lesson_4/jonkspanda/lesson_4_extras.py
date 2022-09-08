import random
from itertools import cycle

#1.
name = input("what's your name?").lower()

for x in range(0,10):
    print(f"hello {name.capitalize()}!")

#2.
for x in range(1, 10):
    print(str(x)*x)

#3.
answer = random.randint(0,100)
guess = None

while(guess != answer):
    guess = int(input("Enter an integer "))
    if(guess > answer):
        print("Wrong, it's lower")
    elif(guess < answer):
        print("Wrong, it's higher")
    elif(guess == answer):
        print("Congratulations, you're correct!")
#4.

numbers = [4, 6, 8, 10, 16, 18, 17, 24, 40, 42, 2, 35]
for x in range(0, len(numbers)):
    if((numbers[x] % 2) == 0):
        print(numbers[x])
    else:
        print("Not allowed!")
        break

#5.
first_list = [1, 5, 6, 10, 2]
second_list = [5, 6, 10, 2, 1]
output = []

for x in range(0, len(second_list)):
    output.append((second_list[x], first_list.index(second_list[x])))

print(output)

#7.
fruits = ["apple", "orange", "pear", "banana", "grapes"]
fruit_space = int(input("How much fruit fits in your basket? "))
basket = []

while(fruit_space > 0):
    for x in fruits:
        if(fruit_space > 0):
            basket.append(x)
            fruit_space = fruit_space - 1
        else:
            break

print(basket)

#8.
prime_numbers = []

n=1
while(n <= 100):
    x = 2
    is_prime_number = True
    while(x <= n):
        if((n % x) == 0 and x != n):
            is_prime_number = False
            break
        x += 1
    
    if(is_prime_number == True):
        prime_numbers.append(n)
    n += 1
    


print(prime_numbers)
        