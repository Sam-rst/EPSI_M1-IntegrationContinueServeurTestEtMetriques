import { defineConfig } from "@playwright/test";

export default defineConfig({
  testDir: "./e2e",
  reporter: "list",
  use: {
    // En CD, on pointe vers la stack Docker déployée (variable d'env BASE_URL).
    baseURL: process.env.BASE_URL || "http://localhost:8080",
  },
});
