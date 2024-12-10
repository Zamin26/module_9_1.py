def apply_all_func(int_list, *functions):
    results = {}            # создание пустого словаря
    for x in functions:
        results[x.__name__] = x(int_list)  # присвоение ключу функции искомое значение
    return results  # итоговый словарь





print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))