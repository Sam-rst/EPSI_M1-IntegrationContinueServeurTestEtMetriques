import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

import App from "./App";

// Test d'INTÉGRATION front : on rend le composant <App/> et on simule
// l'API back (fetch mocké). On vérifie la chaîne saisie -> appel -> affichage.
describe("App (intégration)", () => {
  beforeEach(() => {
    globalThis.fetch = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({ result: 10.8, target: "USD" }),
    }) as unknown as typeof fetch;
  });

  it("affiche le résultat renvoyé par l'API", async () => {
    render(<App />);
    fireEvent.click(screen.getByRole("button", { name: "Convertir" }));

    await waitFor(() => {
      expect(screen.getByRole("status")).toHaveTextContent("10.80 USD");
    });
  });
});
