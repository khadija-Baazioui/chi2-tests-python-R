# Test du khi-deux (χ²) en R : indépendance et ajustement
# Usage : Rscript chi2_independance.R   (aucun package externe requis)

cramer_v <- function(table) {
  chi2 <- suppressWarnings(chisq.test(table, correct = FALSE)$statistic)
  sqrt(as.numeric(chi2) / (sum(table) * (min(dim(table)) - 1)))
}

test_independance <- function(table, titre) {
  cat("\n===", titre, "===\n")
  res <- chisq.test(table)
  print(res)
  cat("Effectifs attendus :\n"); print(round(res$expected, 2))
  cat("Résidus standardisés :\n"); print(round(res$stdres, 2))
  if (any(res$expected < 5)) cat("Attention : effectif attendu < 5, envisager Fisher.\n")
  cat("V de Cramér =", round(cramer_v(table), 3), "\n")
}

# Exemple 1 : table 2x2
t1 <- matrix(c(30, 10, 5, 55), nrow = 2, byrow = TRUE)
test_independance(t1, "Indépendance : table 2x2")

# Exemple 2 : genre x préférence de boisson
t2 <- matrix(c(45, 20, 35, 30, 40, 30), nrow = 2, byrow = TRUE,
             dimnames = list(Genre = c("Homme", "Femme"),
                             Boisson = c("Café", "Thé", "Jus")))
test_independance(t2, "Indépendance : genre x boisson")

# Exemple 3 : test d'ajustement
cat("\n=== Ajustement ===\n")
print(chisq.test(x = c(20, 30, 50), p = c(0.25, 0.25, 0.50), rescale.p = TRUE))
