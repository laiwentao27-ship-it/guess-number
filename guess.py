import random


def main():
    answer = random.randint(1, 100)
    chances = 7

    print("我已经想好了一个 1 到 100 之间的整数，你有 7 次机会猜中它。")
    for attempt in range(1, chances + 1):
        guess = int(input(f"第 {attempt} 次猜测："))

        if guess == answer:
            print(f"恭喜你，猜中了！你用了 {attempt} 次机会。")
            return
        if guess > answer:
            print("猜大了。")
        else:
            print("猜小了。")

    print(f"7 次机会用完了，答案是 {answer}。")


if __name__ == "__main__":
    main()
