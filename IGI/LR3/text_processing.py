# 12
# kOVALCHUK FEODOR 353504


from decorator import log_decorator

@log_decorator
def is_binary_value(text):
    """
    Defs if text is binary value.

    Args:
        text (str): The input text to analyze.

    Returns:
        bool: if text is binary
    """
    
    for char in text:
        if char != '0' and char != '1': 
            return False
    return True

@log_decorator
def split_text(text):
    """
    Splits the text into words based on spaces and commas.

    This function replaces all commas in the text with spaces and then splits the resulting string
    into a list of words using spaces as delimiters.

    Args:
        text (str): The input text to be split.

    Returns:
        list: A list of words extracted from the text.
    """
    return text.replace(',', ' ').split()

@log_decorator
def count_words(words):
    """
    Counts words count.

    Args:
        words (list): A list of words to analyze.
        max_length (int, optional): The maximum length of words to count. Defaults to 5.

    Returns:
        int: The number of words in the list with length less than or equal to max_length.
    """

    return len(words)

@log_decorator
def find_first_z_contein_word(words):
    """
    Finds the shortest word that ends with 'w' (case insensitive).

    This function filters the list for words ending with 'w' (ignoring case) and returns the shortest one.
    If no such word exists, it returns None.

    Args:
        words (list): A list of words to search through.

    Returns:
        str or None: The shortest word ending with 'w', or None if no such word is found.
    """

    first_z_word = None
    first_z_index = -1
    for index, word in enumerate(words):
        if 'z' in word:
            first_z_word = word
            first_z_index = index + 1
            break

    return first_z_word, first_z_index

@log_decorator
def without_a_start_words(words):
    """
    Sorts the words by their length in ascending order.

    Args:
        words (list): A list of words to sort.

    Returns:
        list: A new list containing the words sorted by their length.
    """
    filtered_words = [word for word in words if not word.startswith('a')]
    filtered_string = ' '.join(filtered_words)

    return filtered_string