# Алгоритми сортування: емпіричне порівняння

 ## Опис проєкту:

 Цей проєкт реалізує та порівнює три алгоритми сортування:
 - Сортування вставками (Insertion Sort)
 
 - Сортування злиттям (Merge Sort)
 
 - Timsort (вбудований алгоритм Python)
 
Мета — емпірично підтвердити теоретичні оцінки складності та показати ефективність Timsort як гібридного методу.
  
# Методика дослідження
 ## Генерація даних:
  
 Для тестування використовуються списки випадкових цілих чисел різного розміру: 1000, 2000, 5000 елементів. Генерація здійснюється за допомогою random.randint.
  
 ## Вимір часу
  
 Час виконання кожного алгоритму вимірюється за допомогою модуля timeit.
  
 ## Підхід
  
 Один і той самий список копіюється перед кожним запуском алгоритму, щоб забезпечити чесне порівняння.
  
## Часова складність
Insertion Sort	     -          O(n²)  
Merge Sort          -        	O(n log n)  
Timsort	           -          O(n log n)  
  
# Результати обчислень:
 Розмір масиву: 1000  
 Insertion Sort: 0.012983800028450787  
 Merge Sort: 0.001196000026538968  
 Timsort: 0.00012969993986189365  
  
 Розмір масиву: 2000  
 Insertion Sort: 0.046921500004827976  
 Merge Sort: 0.0019890000112354755  
 Timsort: 0.00017069990281015635  
  
 Розмір масиву: 5000  
 Insertion Sort: 0.27998839993961155  
 Merge Sort: 0.005425299983471632  
 Timsort: 0.0005629999795928597  
  
 З чого можемо зробити висновок, що Timsort значно ефективніший та швидший за інші залучені до обчисленнь алгоритми, особливо за участі великих об'ємів даних. Це і пояснює, чому розробники полюбляють використовувати вже вбудовані методи сортування у Python, оскільки вони заощаджують використання пам'яті та часу написання скрипту, ніж здійснення того вручну. "Не потрібно винаходити велосипед", якщо він уже існує та повноцінно функціонує.

# Додаткове завдання
 ## Функція merge_k_lists()
 Реалізовано функцію merge_k_lists(), що об'єднує відсортовану кількість k списків у один:
  
 lists = [[1, 4, 5], [1, 3, 4], [2, 6]]  
 merged_list = merge_k_lists(lists)  
  
 ## Результат:
 [1, 1, 2, 3, 4, 4, 5, 6]  

 # Висновки
 Теоретичні та практичні характеристики алгоритмів збігаються у результатах, відрізняється час обробки масиву та виконання повного обчислення. В даному випадку, написання власного алгоритму є зайвим, як показують результати і найкраще робити подібне, лише якщо це необхідно у конкретній ситуації задіяти відповідний алгоритм або для практики реалізації алгоритмів та розуміння їх функціонування. 
