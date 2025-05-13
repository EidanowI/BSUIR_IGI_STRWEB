"""
Lab №4
Completed by Fyodor Kovalchuck, group 353504.
variant 12
The program presents work with classes, serializers, regular expressions, standard libraries.
v1.0
Development date:
10.05.2025
"""

from .ITask import ITask

import re, zipfile
from collections import Counter

class Task2(ITask):
    """
    A class that processes text from a specified file and performs various analyses.

    Attributes:
    - _filepath (str): The path to the directory containing the text file.

    Methods:
    - __init__(filepath: str): Initializes the Task2 instance with the file path.
    - run(): Reads the text from 'text.txt', performs analyses, and writes results to 'result.txt' and 'result.zip'.
    """
    def __init__(self, filepath: str):
        self._filepath = filepath
        """
        Initializes the Task2 instance.

        Parameters:
        - filepath (str): The path to the directory containing the text file.
        """

    def run(self):
        """
        Reads the text from 'text.txt', performs various text analyses, 
        and saves the results to 'result.txt' and 'result.zip'.

        The analyses include:
        - Counting sentences
        - Counting question sentences
        - Counting exclamatory sentences
        - Counting declarative sentences
        - Calculating average word length
        - Calculating average sentence length
        - Counting smileys
        - Finding binary numbers
        - Finding words with specific letter conditions
        - Counting words that start or end with a vowel
        - Counting occurrences of all characters
        - Sorting words that follow a comma alphabetically

        Results are printed to the console and saved to the specified result files.
        """

        with open(self._filepath + '/text.txt', 'r', encoding="utf-8") as file:
            text = file.read()
            print(text)
        
            print(f"\n Количество предложений в тексте: {count_sentences(text)}")
            print(f"Количество вопросительных предложений в тексте: {count_vopr_sent(text)}")
            print(f"Количество восклицательных предложений в тексте: {count_voskl_sent(text)}")
            print(f"Количество повествовательных предложений в тексте: {count_povest_sent(text)}\n")
            print(f"\nСреднее значение длины слова: {count_sr_word_length(text)}")
            print(f"Среднее значение длины предложения: {count_sr_sent_length(text)}")
            print(f"Количество смайликов: {count_smileys(text)}")
            print(f"Найти бинарные числа: {get_binary_nums(text)}")
            print(f"\nНайти числа, где 1-я буква гласная, 2-я согласная:\n{get_words_ab(text)}")
            print(f"\nКоличество слов нач. или заканч. на гласную: {count_words_aa(text)}")
            print(f"\nПосчитать количество вхождений всех символов:\n{count_all_symbols(text)}")
            print(f"\nНайти слова после \",\" по алфавиту:\n{sort_words(text)}")

            with open(self._filepath + '/result.txt', 'w', encoding="utf-8") as file:
                file.write(f"Количество предложений в тексте: {count_sentences(text)}\n" 
                        + f"Количество вопросительных предложений в тексте: {count_vopr_sent(text)}\n"
                        + f"Количество восклицательных предложений в тексте: {count_voskl_sent(text)}\n"
                        + f"Количество повествовательных предложений в тексте: {count_povest_sent(text)}\n"
                        + f"Среднее значение длины слова: {count_sr_word_length(text)}\n"
                        + f"Среднее значение длины предложения: {count_sr_sent_length(text)}\n"
                        + f"Количество смайликов: {count_smileys(text)}\n"
                        + f"Найти бинарные числа: {get_binary_nums(text)}\n"
                        + f"Найти числа, где 1-я буква гласная, 2-я согласная:\n{get_words_ab(text)}\n"
                        + f"Количество слов нач. или заканч. на гласную: {count_words_aa(text)}\n"
                        + f"Посчитать количество вхождений всех символов:\n{count_all_symbols(text)}\n"
                        + f"Найти слова после \",\" по алфавиту:\n{sort_words(text)}\n")
            
            with zipfile.ZipFile(self._filepath + '/result.zip', 'w') as archive:
                archive.write(self._filepath + '/result.txt')
                info = zipfile.ZipInfo(self._filepath + '/result.txt')
                print(f"Информация о файле: {info}")

def count_sentences(text):
    """
    Counts the number of sentences in the given text.

    Parameters:
    - text (str): The text to analyze.

    Returns:
    int: The number of sentences found in the text.
    """
    pattern = r'[.!?]\s+'
    sentences = re.findall(pattern, text)
    return len(sentences)

def count_vopr_sent(text):
    """
    Counts the number of question sentences in the given text.

    Parameters:
    - text (str): The text to analyze.

    Returns:
    int: The number of question sentences found in the text.
    """
    pattern = r'\?\s+'
    sentences = re.findall(pattern, text)
    return len(sentences)

def count_voskl_sent(text):
    """
    Counts the number of exclamatory sentences in the given text.

    Parameters:
    - text (str): The text to analyze.

    Returns:
    int: The number of exclamatory sentences found in the text.
    """
    pattern = r'!\s+'
    sentences = re.findall(pattern, text)
    return len(sentences)

def count_povest_sent(text):
    """
    Counts the number of declarative sentences in the given text.

    Parameters:
    - text (str): The text to analyze.

    Returns:
    int: The number of declarative sentences found in the text.
    """
    pattern = r'\.\s+'
    sentences = re.findall(pattern, text)
    return len(sentences)

def count_sr_sent_length(text):
    """
    Calculates the average sentence length in the given text.

    Parameters:
    - text (str): The text to analyze.

    Returns:
    int: The average length of sentences in the text.
    """
    sentences = re.split(r'[.!?]\s+', text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    lengths = 0
    count = 0
    for sent in sentences:
        words = re.findall(r'\b\w+\b', sent)
        length = 0
        for word in words:
            length += len(word)
        lengths += length
        count += 1
    
    return int(lengths / count)

def count_sr_word_length(text):
    """
    Calculates the average word length in the given text.

    Parameters:
    - text (str): The text to analyze.

    Returns:
    int: The average length of words in the text.
    """
    sentences = re.split(r'[.!?]\s+', text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    length = 0
    count = 0
    for sent in sentences:
        words = re.findall(r'\b\w+\b', sent)
        for word in words:
            length += len(word)
            count += 1
    
    return int(length / count)

def count_smileys(text):
    """
    Counts the number of smileys in the given text.

    Parameters:
    - text (str): The text to analyze.

    Returns:
    int: The number of smileys found in the text.
    """
    pattern = r'[;:]-*[\(\[\]\)]+'
    smileys = re.findall(pattern, text)
    
    return len(smileys)

def get_binary_nums(text):
    """
    Extracts binary numbers from the given text.

    Parameters:
    - text (str): The text to analyze.

    Returns:
    list: A list of binary numbers found in the text.
    """
    pattern = r'\b(?:[01]+(?:[.,][01]+)?)\b'
    nums = re.findall(pattern, text)
    return nums

def get_words_ab(text):
    """
    Finds words where the first letter is a vowel and the second is a consonant.

    Parameters:
    - text (str): The text to analyze.

    Returns:
    list: A list of matching words found in the text.
    """
    pattern = r'\b[ёуеыаоэяию][^ёуеыаоэяию_\W\s]\w*\b'
    words = re.findall(pattern, text, re.IGNORECASE) 
    return words

def count_words_aa(text):
    """
    Counts the number of words that start or end with a vowel.

    Parameters:
    - text (str): The text to analyze.

    Returns:
    int: The number of words found that start or end with a vowel.
    """
    pattern = r'\b[ёуеыаоэяию]\w*\b|\b\w+[ёуеыаоэяию]\b'
    words = re.findall(pattern, text, re.IGNORECASE)
    return len(words)

def count_all_symbols(text):
    """
    Counts occurrences of all symbols in the given text.

    Parameters:
    - text (str): The text to analyze.

    Returns:
    dict: A dictionary with symbols as keys and their counts as values.
    """
    pattern = r'.'
    symbols = re.findall(pattern, text)
    symb_counts = dict(Counter(symbols))

    return symb_counts

def sort_words(text):
    """
    Sorts words that follow a comma alphabetically.

    Parameters:
    - text (str): The text to analyze.

    Returns:
    list: A sorted list of words that follow a comma.
    """
    pattern = r'(?<=,\s)\w+'
    words = re.findall(pattern, text)
    return sorted(words)