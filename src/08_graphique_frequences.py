"""Histogramme de la fréquence des lettres (A-Z) sur le dictionnaire (image : docs/frequences_lettres.png)."""
from collections import Counter
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from wordle_core import charger_mots

mots = charger_mots()
c = Counter("".join(mots))
total = sum(c.values())
lettres = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
freqs = [100 * c[l] / total for l in lettres]

plt.figure(figsize=(9, 4.5))
plt.bar(lettres, freqs, color="skyblue")
plt.title("Fréquence des lettres de A à Z")
plt.xlabel("Lettres")
plt.ylabel("Fréquence (%)")
plt.tight_layout()
sortie = Path(__file__).resolve().parent.parent / "docs" / "frequences_lettres.png"
plt.savefig(sortie, dpi=150)
print(f"Graphique enregistré : {sortie}")
