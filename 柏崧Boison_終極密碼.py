import random


def guess_number_game():
    # 生成一個1到100之間的隨機數字
    number_to_guess = random.randint(1, 100)
    number_of_guesses = 0  # 用來記錄猜測的次數
    guess = 0  # 初始化猜測的數字

    print("歡迎來到猜數字遊戲！請猜一個1到100之間的數字。")

    # 當猜測的數字不等於要猜的數字時，持續遊戲
    while guess != number_to_guess:
        # 獲取玩家的猜測
        guess = int(input("請猜一個數字："))
        number_of_guesses += 1  # 每猜一次，次數加1

        # 提供猜測的提示
        if guess < number_to_guess:
            print("你的猜測低於正確答案。")
        elif guess > number_to_guess:
            print("你的猜測高於正確答案。")

    # 猜中數字，遊戲結束
    print(f"恭喜你！正確答案是 {number_to_guess}。你共猜了 {number_of_guesses} 次。")


# 呼叫函數開始遊戲
guess_number_game()
