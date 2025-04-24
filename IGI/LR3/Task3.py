# main for task3
# Task3 24
# Stetsurin Elisey 353504
# 23.03.2025

from text_processing import is_binary_value
    
def run_task3():
    """
    Executes Task 3: Analyzes user-input text for binary value.

    This function repeatedly:
    - Prompts the user to input text.
    - Asks if the user wants to analyze another text, exiting to the menu if not.

    Returns:
        None
    
    Notes:
        - Handles exceptions for empty input and unexpected errors.
        - Continues looping until the user chooses to stop (input other than 'да').
    """
    print("Добро пожаловать в программу анализа текста!")
    print("Эта программа определяет является ли строка двоичным числом.")
    while True:
        try:
            text = input("\nВведите текст для анализа: ")
            if not text:
                raise ValueError("Текст не может быть пустым")
            is_binary = is_binary_value(text)
            if(is_binary):
                print("Это двоичное число")
            else:
                print("Это не двоичное число")
        except ValueError as ve:
            print(f"Ошибка ввода: {ve}")
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")
        again = input("\nАнализировать еще раз? (да/нет): ").strip().lower()
        if again != 'да':
            print("До свидания!")
            return