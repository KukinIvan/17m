sequence_of_numbers = list(map(int, input('Введите числа через пробел : \n').split()))
print('Последовательность чисел', sequence_of_numbers)

while True:
   try:
      number = int(input('Введите любое целое произвольное число: \n'))
      print('Число', number)
      break
   except:
       print("Это не целое число!")
array = sequence_of_numbers + [number]
print('Последовательность чисел', array)

for i in range(len(array)): 
    idx_min = i
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:
        array[i], array[idx_min] = array[idx_min], array[i]

print(array)

def binary_search(array, number, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == number:
        return middle
    elif number < array[middle]:
        return binary_search(array, number, left, middle - 1)
    else:
        return binary_search(array, number, middle + 1, right)

print(binary_search(array, number, 0, len(array)-1))