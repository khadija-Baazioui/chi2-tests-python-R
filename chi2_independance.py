"""Test du khi-deux (χ²) en Python : indépendance et ajustement.

Dépendances : numpy, scipy  (pip install numpy scipy)
Usage       : python chi2_independance.py
"""
import numpy as np
from scipy.stats import chi2_contingency, chisquare


def cramers_v(table):
    """V de Cramér : mesure la force de l'association (0 = aucune, 1 = totale)."""
    table = np.asarray(table)
    chi2 = chi2_contingency(table, correction=False)[0]
    n = table.sum()
    return np.sqrt(chi2 / (n * (min(table.shape) - 1)))


def test_independance(table, noms=("Lignes", "Colonnes"), alpha=0.05):
    """Test d'indépendance sur une table de contingence."""
    table = np.asarray(table)
    chi2, p, ddl, attendu = chi2_contingency(table)

    print(f"\n=== Test d'indépendance : {noms[0]} x {noms[1]} ===")
    print("Effectifs observés :\n", table)
    print("Effectifs attendus :\n", np.round(attendu, 2))
    if (attendu < 5).any():
        print("Attention : au moins un effectif attendu < 5, "
              "envisager le test exact de Fisher.")
    print(f"χ² = {chi2:.3f} | ddl = {ddl} | p-value = {p:.4f}")
    print(f"V de Cramér = {cramers_v(table):.3f}")
    if p < alpha:
        print(f"p < {alpha} : on rejette H0 (association significative).")
    else:
        print(f"p >= {alpha} : on ne rejette pas H0.")


def test_ajustement(observes, probas, alpha=0.05):
    """Test d'ajustement à une distribution théorique."""
    observes = np.asarray(observes)
    attendus = np.asarray(probas) * observes.sum()
    chi2, p = chisquare(observes, f_exp=attendus)
    print("\n=== Test d'ajustement ===")
    print(f"Observés = {observes.tolist()} | attendus = {np.round(attendus, 2).tolist()}")
    print(f"χ² = {chi2:.3f} | ddl = {len(observes) - 1} | p-value = {p:.4f}")
    print("Rejet de H0." if p < alpha else "On ne rejette pas H0.")


if __name__ == "__main__":
    # Exemple 1 : table 2x2
    test_independance([[30, 10], [5, 55]], ("Groupe", "Résultat"))

    # Exemple 2 : genre x préférence de boisson (Café, Thé, Jus)
    test_independance([[45, 20, 35], [30, 40, 30]], ("Genre", "Boisson"))

    # Exemple 3 : ajustement, ici un dé supposé équilibré
    test_ajustement([16, 18, 16, 14, 19, 17], [1 / 6] * 6)
