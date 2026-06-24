import random

'''
1 = Snake
-1 = Water
0 = Gun
'''

computer = random.choice([-1, 0, 1])

your = input("Enter your choice (S/W/G): ").upper()

youDict = {
    "S": 1,
    "W": -1,
    "G": 0
}

reverseDict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

if your not in youDict:
    print("Invalid choice! Please enter S, W, or G.")
    exit()

you = youDict[your]

print(f"You chose: {reverseDict[you]}")
print(f"Computer chose: {reverseDict[computer]}")

if computer == you:
    print("🤝 It's a draw!")

elif computer == -1 and you == 1:
    print("🎉 You Win!")

elif computer == -1 and you == 0:
    print("💻 You Lose!")

elif computer == 1 and you == -1:
    print("💻 You Lose!")

elif computer == 1 and you == 0:
    print("🎉 You Win!")

elif computer == 0 and you == -1:
    print("🎉 You Win!")

elif computer == 0 and you == 1:
    print("💻 You Lose!")
