import pytest

from solver import generate_valid_words




def test_generate_valid_words_start_d():
    """On sait que la première lettre du mot est un D"""
    assert generate_valid_words(
        possible_words=["DEVANT", "ENTREE", "PORTER", "GAUCHE"],
        letters_in_secret=[('D', 0)],
        letters_not_in_secret=[]
    ) == ["DEVANT"]

def test_generate_valid_words_vide():
    """Vérifie que renvoie une liste vide si possible_words est vide"""
    assert generate_valid_words(
        possible_words=[],
        letters_in_secret = [('D',0)],
        letters_not_in_secret= []
    ) == []

def test_generate_valid_words_0_letter():
    """Vérifie que, lorsque l'utilisateur n'a joué aucune lettre, la liste des mots possibles reste inchangée."""
    possible_words = ["ECOUTE", "CAMION", "DECIDE", "ARRETE"]
    letters_in_secret = []
    letters_not_in_secret = []
    assert generate_valid_words(possible_words, letters_in_secret, letters_not_in_secret) == possible_words

def test_generate_valid_words_in_out_letters():
    """Test en fonction de lettres déjà utilisées et présentes ou non dans le mot"""
    assert generate_valid_words(
        possible_words=["AVION", "DEMON", "ROUTE", "BATON"],
        letters_in_secret=[('N', 4), ('O', 3)],
        letters_not_in_secret=["B", "T"]
    ) == ["AVION", "DEMON"]