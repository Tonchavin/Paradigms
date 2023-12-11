from random import randint

if __name__ == '__main__':
    # Искомое число
    value = 6

    # Создание списка
    a = []
    for i in range(10):
        a.append(randint(1, 50))
        # Сортировка по возрастанию
        a.sort()
    print(a)

    # Создание переменных для середины списка, начала и конца
    mid = len(a) // 2
    low = 0
    high = len(a) - 1

    # Цикл поиска значения
    while a[mid] != value and low <= high:
        if value > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        print("No value - 1")
    else:
        print("ID =", mid)
