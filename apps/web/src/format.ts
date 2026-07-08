/** Fonction PURE de formatage d'un montant + devise.
 *  Isolée pour être testable en unitaire (Vitest) sans rendu React. */
export function formatAmount(amount: number, currency: string): string {
  return `${amount.toFixed(2)} ${currency}`;
}
