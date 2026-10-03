# Loi du khi-deux (χ²) : applications réelles et implémentation en Python et R

Projet académique (Master Mathématiques et Ingénierie Numérique, option Intelligence Artificielle, Université Mohammed V de Rabat, mai 2026).

L'objectif est d'étudier la loi du khi-deux, ses applications en statistique et l'implémentation des tests associés en **Python** et en **R**.

## Contenu du dépôt

| Fichier | Description |
|---|---|
| `presentation_khi2.pptx` | Présentation : définition et propriétés, applications, implémentations, comparaison Python vs R, limites et bonnes pratiques |
| `chi2_independence.py` | Tests d'indépendance et d'ajustement en Python (`numpy`, `scipy`) |
| `chi2_independence.R` | Mêmes tests en R (base R, sans package externe) |

## Notions abordées

- **Définition :** la loi χ²(k) est la loi de la somme des carrés de k variables normales centrées réduites indépendantes. Espérance k, variance 2k.
- **Statistique du test :** χ² = Σ (O − E)² / E
- **Trois tests :** indépendance (ddl = (r−1)(c−1)), ajustement (ddl = k−1) et homogénéité.
- **Taille d'effet :** V de Cramér, pour mesurer la force de l'association et pas seulement sa significativité.

## Utilisation

**Python**
```bash
pip install numpy scipy
python chi2_independence.py
```

**R**
```bash
Rscript chi2_independence.R
```

## Exemple : genre × préférence de boisson

| | Café | Thé | Jus |
|---|---|---|---|
| Homme | 45 | 20 | 35 |
| Femme | 30 | 40 | 30 |

- H0 : le genre et la préférence de boisson sont indépendants
- Résultat : **χ² = 10,05, ddl = 2, p = 0,0066** : on rejette H0 au seuil de 5 %
- V de Cramér = 0,22 : association faible à modérée

## Limites et bonnes pratiques

- Vérifier que tous les effectifs attendus sont ≥ 5. Sinon, utiliser le test exact de Fisher.
- Pour les tables 2×2, appliquer la correction de Yates.
- Le test ne s'applique qu'à des variables qualitatives. Il indique s'il y a association, pas sa direction ni son intensité (d'où le V de Cramér).

## Auteure

Khadija Baazioui, [LinkedIn](https://www.linkedin.com/in/khadija-baazioui-89106928b)
