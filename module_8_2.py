def personal_sum(*numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        for j in i:
            try:
                result += j
            except TypeError:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {j}')
    return result, incorrect_data


def calculate_average(*numbers: list | tuple):
    len_elem_num = 0
    try:
        s = personal_sum(*numbers)
        for i in numbers:
            for j in i:
                if isinstance(j, int | tuple):
                    len_elem_num += 1
        return s[0]/len_elem_num
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')