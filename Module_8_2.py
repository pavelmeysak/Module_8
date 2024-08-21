def personal_sum(numbers):
    sum_result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            sum_result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    total_result = (sum_result, incorrect_data)
    return total_result


def calculate_average(numbers):
    try:
        result = personal_sum(numbers)
        total_result = result[0]/(len(numbers) - result[1])

    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        return None
    except ZeroDivisionError:
        return 0
    return total_result


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

