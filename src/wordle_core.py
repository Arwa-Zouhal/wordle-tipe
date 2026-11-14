"""
Noyau commun du projet : chargement du dictionnaire, calcul du retour
(0 = gris, 1 = jaune, 2 = vert), filtrage et choix du mot pivot.

Contrairement aux scripts d'origine, le dictionnaire est lu une seule fois
depuis data/mots.txt (au lieu d'être recopié dans chaque fichier) et le calcul
des couleurs gère correctement les lettres répétées, comme le vrai Wordle.
"""
from collections import Counter
from pathlib import Path

DICO = Path(__file__).resolve().parent.parent / "data" / "mots.txt"


def charger_mots(chemin=DICO):
    with open(chemin, encoding="utf-8") as f:
        return [ligne.strip().upper() for ligne in f if len(ligne.strip()) == 5]


def retour(devinette, cible):
    """Retourne le motif de 5 chiffres (0 gris, 1 jaune, 2 vert) du vrai Wordle."""
    motif = [0] * 5
    restantes = Counter()
    for i in range(5):
        if devinette[i] == cible[i]:
            motif[i] = 2
        else:
            restantes[cible[i]] += 1
    for i in range(5):
        if motif[i] == 0 and restantes[devinette[i]] > 0:
            motif[i] = 1
            restantes[devinette[i]] -= 1
    return tuple(motif)


def filtrer_mots(mots, devinette, motif):
    """Garde uniquement les mots qui auraient donné exactement ce motif."""
    motif = tuple(motif)
    return [m for m in mots if retour(devinette, m) == motif]


def choisir_pivot(mots):
    """Même idée que le TIPE : score = somme des fréquences des lettres
    DISTINCTES du mot, calculées sur la liste de mots restants."""
    if not mots:
        return None
    freq = Counter()
    for m in mots:
        freq.update(m)
    return max(mots, key=lambda m: sum(freq[l] for l in set(m)))
