import { expect, test } from "@playwright/test";

// Test E2E : navigateur réel qui charge le front servi par nginx,
// lequel appelle le vrai back via /api. C'est la chaîne complète.
test("convertit EUR vers USD de bout en bout", async ({ page }) => {
  await page.goto("/");
  await expect(page.getByRole("heading")).toContainText("Convertisseur");

  await page.getByLabel("montant").fill("10");
  await page.getByLabel("source").selectOption("EUR");
  await page.getByLabel("cible").selectOption("USD");
  await page.getByRole("button", { name: "Convertir" }).click();

  await expect(page.getByRole("status")).toContainText("USD");
});
