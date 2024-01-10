import random


def guess_number():
    target = random.randint(1, 100)
    guesses = 0

    print("猜數字遊戲開始！猜一個1到100的數字。")

    while True:
        guess = int(input("猜數字："))
        guesses += 1
        if guess < target:
            print("Your answer is lower than final answer")
        elif guess > target:
            print("Your answer is higher than final answer")
        else:
            print(
                f"Congratulation! The answer is {target}. you take {guesses} rounds to get the answer!")
            break


guess_number()
