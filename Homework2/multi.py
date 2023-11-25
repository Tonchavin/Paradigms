# В императивном стиле будет более понятна реализация
def multi():
    print("Таблица умножения")
    n = int(input("Введите число: "))
    for i in range(1, n + 1):
        for k in range(1, n + 1):
            print(f"{i} * {k} = {i * k}\t", end="")
        print('')


if __name__ == '__main__':
    multi()
