import { describe, expect, it } from "vitest";

import { formatAmount } from "./format";

describe("formatAmount", () => {
  it("formate avec deux décimales et la devise", () => {
    expect(formatAmount(10.8, "USD")).toBe("10.80 USD");
  });

  it("complète les décimales manquantes", () => {
    expect(formatAmount(10.1, "EUR")).toBe("10.10 EUR");
  });

  it("gère les entiers", () => {
    expect(formatAmount(5, "GBP")).toBe("5.00 GBP");
  });
});
