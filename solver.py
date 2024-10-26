import math
from copy import copy


def generate_valid_words(possible_words, letters_in_secret, letters_not_in_secret):
    valid_words = []
    for word in possible_words:
        valid = True
        for letter in letters_not_in_secret:
            if letter in word:
                valid = False

        if valid:
            for letter, index in letters_in_secret:
                if word[index] != letter:
                    valid = False

        if valid:
            valid_words.append(word)
    return valid_words


def generate_best_letters(possible_words:list, letters_not_played:list[str], letters_in_secret, letters_not_in_secret):
    # Dictionnaire pour stocker la fréquence moyenne de chaque lettre jouable
    freq_letter = {}

    # Nombre total de mots restants
    total_words = len(possible_words)

    # Calculer la fréquence moyenne de chaque lettre non jouée dans les mots restants
    for letter in letters_not_played:
        total_occurrences = sum(word.count(letter) for word in possible_words)
        freq_letter[letter] = total_occurrences / total_words

    # Sélectionner la lettre avec la fréquence moyenne la plus élevée
    best_letter = max(freq_letter, key=freq_letter.get)

    return f"Essayer la lettre {best_letter}"









