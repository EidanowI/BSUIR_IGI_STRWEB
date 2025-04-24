# TASK4
# 12
# kOVALCHUK FEODOR 353504


from text_processing import split_text, count_words, find_first_z_contein_word, without_a_start_words

def run_task4():
    """
    Executes Task 4: Analyzes a predefined text for word statistics.

    This function processes a fixed text to:
    a) Count apper and lower case words
    b) First z contein word
    c) Print string without started a words

    Returns:
        None
    
    Notes:
        - The text analyzed is hardcoded within the function.
        - Output is formatted with separators and descriptive messages.
    """
    text = "So shez was considering in her own mind, asw well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
    print("Анализ текста:")
    print("-" * 50)
    words = split_text(text)

    words_count = count_words(words)
    print(f"а) Количество слов: {words_count}")

    first_z_word, z_word_number = find_first_z_contein_word(words)
    if first_z_word:
        print(f"б) Самое первое слово с 'z': {first_z_word} и его номер {z_word_number}")
    else:
        print("б) Нет слов, содержащих 'z'")

    without_astart_words = without_a_start_words(words)
    print("в) Строка без слов начинающихся на 'a':")
    print(without_astart_words)

    print("-" * 50)
    input("Нажмите Enter, чтобы вернуться в меню.")