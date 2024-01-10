import random


def guess_number():
    target = random.randint(1, 100)
    guesses = 0

    print("猜數字遊戲開始！猜一個1到100的數字。")

    while True:
        guess = int(input("猜數字："))
        guesses += 1
        if guess < target:
            print("太低了。")
        elif guess > target:
            print("太高了。")
        else:
            print(f"猜對了！數字是{target}，你猜了{guesses}次。")
            break


guess_number()
