numbers_list = [3.4, 5.1, 2.2, 4.1, 1.0, 3.8]


# Императивный стиль
def sort_list_imperative(numbers_lis):
    for i in range(len(numbers_lis) - 1):
        for j in range(len(numbers_lis) - i - 1):
            if numbers_list[j] < numbers_list[j + 1]:
                numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
    print(f'After sorting imperative: {numbers_list}')
    return numbers_list


# Декларативный стиль
def sort_list_declarative():
    numbers_list.sort(reverse=True)
    print(f'After sorting declarative: {numbers_list}')


if __name__ == '__main__':
    sort_list_imperative(numbers_list)
    sort_list_declarative()
