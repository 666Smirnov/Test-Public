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


def binary_search(list, item):
  # в low и high хранятся границы части списка, где выполняется поиск
  low = 0
  high = len(list) - 1
  i = 0
  # Пока не останется один элемент
  while low <= high:
    # Проверяем средний элемент
    mid = (low + high) // 2
    guess = list[mid]
    # Значение найдено
    if guess == item:
      return mid
    # Значение велико
    if guess > item:
      high = mid - 1
    # Значение мало
    else:
      low = mid + 1
    i=i+1
    #print(i)

  # Значение не найдено
  return None
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
#print(s)
x = merge_sort(s)
print(x)
print(binary_search(s, cur))
#2 3 17 12 32 50 47