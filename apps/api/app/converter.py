"""Logique métier PURE de conversion de devises.

Aucune dépendance à FastAPI ici : c'est ce qui rend ce module
trivialement testable en unitaire.
"""

# Taux de change fictifs, exprimés en base EUR (1 EUR = X devise).
RATES: dict[str, float] = {
    "EUR": 1.0,
    "USD": 1.08,
    "GBP": 0.85,
    "JPY": 170.0,
}


class UnknownCurrencyError(ValueError):
    """Levée quand une devise n'est pas supportée."""


def convert(amount: float, source: str, target: str) -> float:
    """Convertit `amount` de la devise `source` vers `target`.

    Passe par l'EUR comme pivot. Arrondi à 2 décimales.
    """
    if amount < 0:
        raise ValueError("Le montant doit être positif.")

    source, target = source.upper(), target.upper()
    for currency in (source, target):
        if currency not in RATES:
            raise UnknownCurrencyError(f"Devise inconnue : {currency}")

    amount_in_eur = amount / RATES[source]
    return round(amount_in_eur * RATES[target], 2)
