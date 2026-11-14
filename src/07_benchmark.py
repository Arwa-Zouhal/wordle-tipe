"""
Évalue le solveur sur TOUS les mots du dictionnaire (chaque mot est la cible
une fois) et affiche le nombre moyen d'essais et la répartition.

Usage :
    python src/07_benchmark.py            # premier mot calculé par l'algorithme
    python src/07_benchmark.py AEREE      # imposer le premier mot
"""
import sys
from collections import Counter
from wordle_core import charger_mots, retour, filtrer_mots, choisir_pivot


def simuler(mots, premier):
    """Joue toutes les parties. Mémoïsation : deux parties qui ont eu les mêmes
    retours partagent les mêmes états, donc on ne recalcule pas."""
    cache = {}  # (historique) -> (liste de candidats, prochain mot)
    resultats = {}
    for cible in mots:
        hist, cands, mot, essais = (), mots, premier, 1
        while mot != cible and essais < 50:
            motif = retour(mot, cible)
            hist = hist + ((mot, motif),)
            if hist not in cache:
                nouveaux = filtrer_mots(cands, mot, motif)
                cache[hist] = (nouveaux, choisir_pivot(nouveaux))
            cands, mot = cache[hist]
            essais += 1
        resultats[cible] = essais
    return resultats


def main():
    mots = charger_mots()
    premier = sys.argv[1].upper() if len(sys.argv) > 1 else choisir_pivot(mots)
    res = simuler(mots, premier)
    n = len(res)
    moyenne = sum(res.values()) / n
    rep = Counter(res.values())
    print(f"Premier mot : {premier}  |  {n} parties simulées")
    print(f"Nombre moyen d'essais : {moyenne:.3f}")
    print(f"Maximum : {max(res.values())} essais")
    for k in sorted(rep):
        print(f"  {k} essai(s) : {rep[k]:5d}  ({100*rep[k]/n:5.2f} %)")
    print(f"Réussite en 6 essais ou moins : {100*sum(v for k,v in rep.items() if k<=6)/n:.2f} %")


if __name__ == "__main__":
    main()
