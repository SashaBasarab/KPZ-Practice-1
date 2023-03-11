def prime_num_generator():

    # Початкове просте число
    prime = 2

    # Безкінечний цикл для генерації простих чисел
    while True:
        # Перевірка, чи є поточне число простим
        is_prime = True
        for num in range(2, int(prime ** 0.5) + 1):
            if prime % num == 0:
                is_prime = False
                break

        # Якщо число є простим, повернути його і перейти до наступного простого числа
        if is_prime:
            yield prime
        prime += 1

# Створюємо генератор простих чисел
gen = prime_num_generator()

# Виводимо перші 10 простих чисел
for i in range(5):
    print(next(gen))