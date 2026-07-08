import { useState } from "react";

import { formatAmount } from "./format";

const CURRENCIES = ["EUR", "USD", "GBP", "JPY"];

export default function App() {
  const [amount, setAmount] = useState(1);
  const [source, setSource] = useState("EUR");
  const [target, setTarget] = useState("USD");
  const [result, setResult] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function handleConvert() {
    setError(null);
    setResult(null);
    try {
      const params = new URLSearchParams({
        amount: String(amount),
        source,
        target,
      });
      const response = await fetch(`/api/convert?${params}`);
      if (!response.ok) {
        throw new Error(`Erreur ${response.status}`);
      }
      const data = await response.json();
      setResult(formatAmount(data.result, data.target));
    } catch (e) {
      setError(e instanceof Error ? e.message : "Erreur inconnue");
    }
  }

  return (
    <main
      style={{
        fontFamily: "system-ui, sans-serif",
        maxWidth: 480,
        margin: "4rem auto",
        padding: "0 1rem",
      }}
    >
      <h1>💱 Convertisseur de devises</h1>
      <div
        style={{
          display: "flex",
          gap: "0.5rem",
          alignItems: "center",
          flexWrap: "wrap",
        }}
      >
        <input
          aria-label="montant"
          type="number"
          value={amount}
          min={0}
          onChange={(e) => setAmount(Number(e.target.value))}
          style={{ width: 100, padding: "0.4rem" }}
        />
        <select aria-label="source" value={source} onChange={(e) => setSource(e.target.value)}>
          {CURRENCIES.map((c) => (
            <option key={c}>{c}</option>
          ))}
        </select>
        <span aria-hidden>→</span>
        <select aria-label="cible" value={target} onChange={(e) => setTarget(e.target.value)}>
          {CURRENCIES.map((c) => (
            <option key={c}>{c}</option>
          ))}
        </select>
        <button onClick={handleConvert}>Convertir</button>
      </div>

      {result && (
        <p role="status" style={{ fontSize: "1.5rem", fontWeight: 600 }}>
          Résultat : {result}
        </p>
      )}
      {error && (
        <p role="alert" style={{ color: "crimson" }}>
          {error}
        </p>
      )}
    </main>
  );
}
