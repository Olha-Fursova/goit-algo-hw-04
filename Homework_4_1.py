import random
import timeit
from heapq import heappush, heappop

# Алгоритми сортування відтворила, як і у конспекті

# Сортування вставками

def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key
  return arr



# Сортування злиттям

def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr) // 2
  left_half = arr[:mid]
  right_half = arr[mid:]

  return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
  merged = []
  left_index = 0
  right_index = 0

  while left_index < len(left) and right_index < len(right):
    if left[left_index] <= right[right_index]:
      merged.append(left[left_index])
      left_index += 1
    else:
      merged.append(right[right_index])
      right_index += 1
    
  while left_index < len(left):
    merged.append(left[left_index])
    left_index += 1
  while right_index < len(right):
    merged.append(right[right_index])
    right_index += 1
  
  return merged


# Здійснюю генерацію тестових даних

def generate_random_list(size):
  return [random.randint(0, 100000) for _ in range(size)]

# Функція, що вимірюватиме час виконання
def time_test(sort_func, data):
  return timeit.timeit(lambda: sort_func(data.copy()), number=1)



# головна функція скрипту
if __name__ == "__main__":
  sizes = [1000, 2000, 5000]
  for size in sizes:
    data = generate_random_list(size)

    time_ins = time_test(insertion_sort, data)
    time_merge = time_test(merge_sort, data)
    time_timsort = time_test(sorted, data)

    print(f"The size of the array: {size}")
    print("Insertion Sort:", time_test(insertion_sort, data.copy()))
    print("Merge Sort:", time_test(merge_sort, data.copy()))
    print("Timsort:", time_test(sorted, data.copy()))
    print()


# Виконання додаткових умов із сортування списків цілих чисел
# Спробувала відтворити сортування за допомогою пакету heapq, де n - це загальна кількість елементів
# а k - кількість списків. l - це один список у наборі списків, який ми перебиратимемо
 
# def merge_k_lists(lists):
#   heap = []
#   for l in lists:
#     for item in l:
#       heappush(heap, item)
#   return [heappop(heap) for _ in range(len(heap))]

# # Тест
# if __name__ == "__main__":
#   lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
#   merged = merge_k_lists(lists)
#   print("Відсортований список:", merged)