def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива равен 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние
def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы
    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
def binary_search(data_list, input_element, index_left, index_right):
    # Бинарный поиск
    if index_left > index_right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (index_right + index_left) // 2  # находим середину
    if data_list[middle] == input_element:  # если элемент в середине,
        x = data_list[: middle]  # ищем индекс последнего элемента в левой половине, он и есть ближайшее меньшее число
        for i in x:
            if i == input_element:
                x.remove(input_element)
        index_1 = (len(x) - 1)
        y = data_list[middle:]  # # ищем индекс первого элемента в правой половине, он и есть ближайшее большее число
        for n in y:
            if n <= input_element and len(y) > 1:
                y.remove(n)
        f = y[0]
        index_2 = data_list.index(f)
        if index_1 < 0:
            print(
                f'Это первый элемент списка. Индекс слева Отсутствует. Индекс большего числа справа = {index_2}')
        elif index_2 == len(data_list) :
            print(f'Индекс меньшего числа слева = {index_1}. Это последний элемент списка. Индекс справа отсутствует')
        else:
            print(f'Индекс меньшего числа слева = {index_1}. Индекс большего числа справа = {index_2}')
        return index_1, index_2  # возвращаем эти индексы
    elif input_element < data_list[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(data_list, input_element, index_left, middle - 1)
    else:  # иначе в правой
        return binary_search(data_list, input_element, middle + 1, index_right)
s = []
inp = input().split(' ')
for i in inp:
    if i.isdigit():
        s.append(int(i))
    else:
        print ('Ошибка ввода:', i)
cur = int(input())
if cur in s:
    pass
else: s.append(cur)
x = merge_sort(s)
print(binary_search(x, cur, 0, len(x)))
