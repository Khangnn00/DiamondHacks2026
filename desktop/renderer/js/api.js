/**
 * Renderer API helper — scaffold only.
 */
const base = window.jobAgent?.apiBaseUrl || "http://127.0.0.1:8000";
document.getElementById("base").textContent = base;

const btn = document.getElementById("ping");
const out = document.getElementById("out");
btn.disabled = false;

btn.addEventListener("click", async () => {
  out.textContent = "Loading…";
  try {
    const res = await fetch(`${base}/health`);
    const body = await res.json();
    out.textContent = JSON.stringify(body, null, 2);
  } catch (e) {
    out.textContent = String(e);
  }
});
