import pytest
from generate_dicts import lire_filtrer_mots

def test_lire_filtrer_mots_vide():
    # Fichier vide ==> retourne une erreur
    with pytest.raises(ValueError):
        lire_filtrer_mots("data_test/filetest_empty.txt", 8)

def test_lire_filtrer_mots_long():
    liste_mots = lire_filtrer_mots("data_test/filetest3.txt", 6)
    liste_mots_2 = lire_filtrer_mots("data_test/filetest1.txt", 6)
    for mot in liste_mots:
        assert len(mot) == 6
    for mot in liste_mots_2:
        assert len(mot) == 6

def test_lire_filtrer_mots_nettoyage():
    liste_mots = lire_filtrer_mots("data_test/filetest1.txt", 6)
    mots_valides = ["ECOUTE", "ARRETE", "CAMION"]
    assert sorted(mots_valides) == sorted(liste_mots)
    liste_mots_2 = lire_filtrer_mots("data_test/filetest1.txt", 7)
    mots_valides_2 = ["CHATEAU", "DECIDER"]
    assert sorted(mots_valides_2) == sorted(liste_mots_2)
    liste_mots_3 = lire_filtrer_mots("data_test/filetest1.txt", 11)
    mots_valides_3 = ["CHASSENEIGE"]
    assert sorted(mots_valides_3) == sorted(liste_mots_3)