import math
from copy import copy


def generate_valid_words(possible_words, letters_in_secret, letters_not_in_secret):
    """
    Prend en compte les lettres déjà jouées pour générer la liste des mots encore valides.

    Args:
        possible_words (List[str]): Liste des mots possibles.
        letters_in_secret (List[Tuple[str, int]]): Liste de tuples (lettre, position dans le mot) des lettres
        déjà trouvées présentes dans le mot.
       letters_not_in_secret (List[str]): Liste des lettres qui ne sont pas dans le mot.

    Returns:
        List[str]: Liste des mots encore valides.
    """
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
    """
    Suggère la meilleure lettre à jouer en fonction des mots encore valides et des lettres n'ayant pas encore été jouées.

    Cette fonction calcule la fréquence moyenne de chaque lettre n'ayant pas encore été jouée dans les mots
    encore valides.
    Elle retourne la lettre avec la fréquence moyenne la plus élevée, soit la plus susceptible d'être dans le
    mot à trouver.

    Args:
        possible_words (List[str]): Liste des mots encore valides.
        letters_not_played (List[str]): Liste des lettres qui n'ont pas encore été jouées.
        letters_in_secret (List[Tuple[str, int]]): Liste de tuples (lettre, position dans le mot) des lettres trouvées
        présentes dans le mot.
        letters_not_in_secret (List[str]): Liste des lettres qui ne sont pas dans le mot.

    Returns:
        str: Message suggérant la meilleure lettre possible.
    """
    freq_letter = {}

    total_words = len(possible_words)

    for letter in letters_not_played:
        total_occurrences = sum(word.count(letter) for word in possible_words)
        freq_letter[letter] = total_occurrences / total_words

    best_letter = max(freq_letter, key=freq_letter.get)

    return f"Essayez la lettre {best_letter}"









