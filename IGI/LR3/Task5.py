# TASK5
# 12
# kOVALCHUK FEODOR 353504

from list_processing import input_list, generate_random_list, find_product_of_positive, find_sum_before_min_abs, print_list

def run_task5():
    """
    Executes Task 5: Processes a list of numbers for specific calculations.

    Returns:
        None
    
    Notes:
        - Handles invalid input with error messages.
        - Depends on external functions: input_list, generate_random_list, find_product_of_negatives, 
          find_sum_before_max_abs, print_list.
    """
    print("Добро пожаловать в программу обработки списка!")
    print("Вы можете ввести список вручную или сгенерировать его случайным образом.")
    while True:
        try:
            choice = input("\nВыберите способ заполнения (1 - вручную, 2 - случайно): ").strip()
            if choice == '1':
                numbers = input_list()
            elif choice == '2':
                size = int(input("Введите количество элементов в списке: "))
                numbers = generate_random_list(size)
            else:
                print("Неверный выбор. Выберите 1 или 2.")
                continue
            print_list(numbers)
            product_pos = find_product_of_positive(numbers)
            sum_pos = find_sum_before_min_abs(numbers)
            print(f"Произведение положительных элементов: {product_pos}")
            print(f"Сумма до минимального по модулю: {sum_pos}")
        except ValueError as ve:
            print(f"Ошибка ввода: {ve}")
        except Exception as e:
            print(f"Ошибка: {e}")
        again = input("\nХотите обработать ещё один список? (да/нет): ").strip().lower()
        if again != 'да':
            print("До свидания!")
            return