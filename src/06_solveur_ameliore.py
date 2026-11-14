"""
Solveur Wordle (version améliorée) en ligne de commande.

Usage :
    python src/06_solveur_ameliore.py

À chaque tour le programme propose un mot ; tu joues ce mot sur Wordle puis tu
saisis le retour : 5 chiffres, 0 = gris, 1 = jaune, 2 = vert (ex. 02010).
"""
from wordle_core import charger_mots, filtrer_mots, choisir_pivot


def main():
    mots = charger_mots()
    candidats = mots
    pivot = choisir_pivot(candidats)
    for tour in range(1, 7):
        print(f"\nEssai {tour} -> joue : {pivot}   ({len(candidats)} mots possibles)")
        saisie = input("Retour (ex. 02010, ou 22222 si trouvé) : ").strip()
        if len(saisie) != 5 or any(c not in "012" for c in saisie):
            print("Format invalide : 5 chiffres parmi 0, 1, 2.")
            continue
        motif = tuple(int(c) for c in saisie)
        if motif == (2, 2, 2, 2, 2):
            print(f"Trouvé en {tour} essai(s) !")
            return
        candidats = filtrer_mots(candidats, pivot, motif)
        if not candidats:
            print("Aucun mot compatible : vérifie les retours saisis.")
            return
        pivot = choisir_pivot(candidats)
    print("Perdu : 6 essais utilisés.")


if __name__ == "__main__":
    main()
