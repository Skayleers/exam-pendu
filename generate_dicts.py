"""
Depuis le fichier liste_mots.txt, on récupère tous les mots de 6,7,8,9,10 lettres.
et on génère 5 fichiers textes contenant les mots en fonction de leur taille (un mot par ligne, séparé par un \n):
dico_6_lettres.txt
dico_7_lettres.txt
dico_8_lettres.txt
dico_9_lettres.txt
dico_10_lettres.txt
On enlève les accents, les espaces, les tirets et les mots en double.
"""
import unidecode

def lire_filtrer_mots(chemin_lexique, longueur):
    """
    Lit tous les mots d'un fichier texte et les filtre pour ne conserver que ceux ayant la longueur
    demandée. La fonction retourne ces mots en majuscules et nettoyés (accents, espaces, tirets) sous forme de liste.

    Args:
        chemin_lexique (str): Chemin vers le fichier contenant la liste des mots.
        longueur (int): Longueur des mots à filtrer.

    Returns:
        List[str]: Liste des mots filtrés ayant la longueur spécifiée, en majuscules et nettoyés.
    """
    mots_filtre = set()
    with open(chemin_lexique, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        if not lines:
            raise ValueError("Le fichier est vide.")

        for line in lines:
            line_clean = line.strip()
            if line_clean:
                word = line_clean.split()[0]
                word = unidecode.unidecode(word)
                word = word.upper()
                word = word.replace('-', '')
                if len(word) == longueur:
                    mots_filtre.add(word)
    return list(mots_filtre)


def ecrire_liste_mots(liste_mots:list, longueur:int) -> None:
    """Génère un fichier texte contenant tous les mots pour une longueur donné"""

    chemin_dico_ecriture:str = f"data/dico_{longueur}_lettres.txt"

    with open(chemin_dico_ecriture, 'w', encoding='utf-8') as file:
        file.writelines(f"{mot}\n" for mot in liste_mots)




def main(chemin:str) -> None:
    for long in range(6,11):
        # génère la liste de mot pour la longueur donné
        lst_mots = lire_filtrer_mots(chemin_lexique=chemin, longueur=long)

        # Génère un fichier texte correspondant
        ecrire_liste_mots(lst_mots, longueur=long)

if __name__ == '__main__':
    chemin = "data/liste_mots.txt"
    main(chemin= chemin)