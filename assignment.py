print(" !!! welcome in kon banega corerpati show !!! ")

amount_won = 0

print("the first question is for $2000 \n")

str(input("type READY! to start the game : "))

print("Which planet is the largest in the solar system...\n")

print("option (a) earth")
print("option (b) mars")
print("option (c) saturn")
print("option (d) jupiter")

answer = str(input("enter your answer here:"))

if answer.lower() == "d" or answer.lower() == "jupiter":
    amount_won = 2000
    print("you won 2000$")
else:
    print("you loose the game")
    print(f"Total amount you won is ${2000}")
    exit()

print("the second question is for $5000 \n")

print("Which is largest continent in the world...\n")

print("option (a) africa")
print("option (b) asia")
print("option (c) europe")
print("option (d) austrialia")

answer = str(input("enter your answer here:"))

if answer.lower() == "b" or answer.lower() == "asia":
    amount_won = 5000
    print("you won 5000$")
else:
    print("you loose the game")
    print(f"Total amount you won is ${5000}")
    exit()

print("the third question is for $7000 \n")

print("what is the currency of japan...\n")

print("option (a) dollar")
print("option (b) won")
print("option (c) yen")
print("option (d) peso")

answer = str(input("enter your answer here:"))

if answer.lower() == "c" or answer.lower() == "yen":
    amount_won = 7000
    print("you won 7000$")
else:
    print("you loose the game")
    print(f"Total amount you won is ${7000}")
    exit()

print("the forth question is for $10000 \n")

print("Which is the largest ocean in the world?...\n")

print("option (a) Indian Ocean")
print("option (b) Atlantic Ocean")
print("option (c) Arctic Ocean")
print("option (d) Pacific Ocean")

answer = str(input("enter your answer here:"))

if answer.lower() == "d" or answer.lower() == "pacific ocean":
    amount_won = 10000
    print("you won 10000$")
else:
    print("you loose the game")
    print(f"Total amount you won is ${10000}")
    exit()

print("!!congratulations!! you won the game. Total amount you won is $", amount_won)