---
layout: default
title: iCal zu HTML
nav_exclude: true
search_exclude: true
---

# iCal zu HTML

<div class="ical-tool">
  <div class="ical-field">
    <label for="ical-url">iCal-URL</label>
    <input id="ical-url" type="url" value="https://intranet.tam.ch/klw/rest/ics/type/calendar/date/1783439452/auth/gr001@Y3lyaWwuYmx1bQ==:Y2JhMDMyNTkyNmI1NmFiNjAxZTBhN2JmNzA4N2M1ZDNmOWQyMTUwMw==/calendar.ics">
  </div>

  <p class="ical-hint">
    Die URL wird direkt an Python weitergegeben.
  </p>

  <fieldset>
    <legend>Ausgabe</legend>
    <label>
      <input type="radio" name="event-mode" value="next" checked>
      Nächste Termine
    </label>
    <label>
      <input type="radio" name="event-mode" value="all">
      Alle Termine
    </label>
    <label class="inline-number">
      Anzahl
      <input id="event-limit" type="number" min="1" step="1" value="3">
    </label>
  </fieldset>

  <div class="ical-actions">
    <button id="generate-html" type="button">HTML generieren</button>
    <button id="copy-html" type="button" disabled>HTML kopieren</button>
  </div>

  <p id="ical-status" role="status">Bereit.</p>
  <textarea id="html-output" rows="18" spellcheck="false" readonly></textarea>
</div>

<style>
  .ical-tool {
    display: grid;
    gap: 1rem;
    max-width: 58rem;
  }

  .ical-field,
  .ical-actions,
  .inline-number {
    display: flex;
    gap: .6rem;
    align-items: center;
  }

  .ical-field {
    flex-wrap: wrap;
  }

  .ical-field label,
  .inline-number {
    font-weight: 600;
  }

  .ical-field input[type="url"] {
    flex: 1 1 24rem;
    min-width: 16rem;
  }

  .ical-tool input[type="url"],
  .ical-tool input[type="number"],
  .ical-tool textarea {
    border: 1px solid #bbb;
    border-radius: 4px;
    padding: .45rem .55rem;
    font: inherit;
  }

  .ical-tool input[type="number"] {
    width: 5rem;
  }

  .ical-tool fieldset {
    border: 1px solid #ddd;
    border-radius: 6px;
    padding: .8rem 1rem;
  }

  .ical-tool fieldset label {
    margin-right: 1rem;
  }

  .ical-actions {
    flex-wrap: wrap;
  }

  .ical-actions button {
    border: 1px solid #555;
    border-radius: 4px;
    padding: .45rem .8rem;
    background: #fff;
    color: #222;
    cursor: pointer;
  }

  .ical-actions button:disabled {
    border-color: #bbb;
    color: #777;
    cursor: not-allowed;
  }

  #ical-status {
    margin: 0;
  }

  .ical-hint {
    margin: 0;
    color: #555;
  }

  #html-output {
    width: 100%;
    min-height: 24rem;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: .85rem;
  }
</style>

<script>
  const pyodideBaseUrl = "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/";
  const scriptUrl = "{{ site.baseurl }}/ical-to-html/ical-to-html.py?v=20260708-encoded-ical-url";
  const statusEl = document.querySelector("#ical-status");
  const outputEl = document.querySelector("#html-output");
  const urlInput = document.querySelector("#ical-url");
  const copyButton = document.querySelector("#copy-html");
  const generateButton = document.querySelector("#generate-html");
  const limitInput = document.querySelector("#event-limit");
  const modeInputs = document.querySelectorAll("input[name='event-mode']");

  function setStatus(message) {
    statusEl.textContent = message;
  }

  function selectedLimit() {
    const mode = document.querySelector("input[name='event-mode']:checked").value;
    if (mode === "all") {
      return null;
    }
    return Math.max(1, Number.parseInt(limitInput.value || "3", 10));
  }

  function getIcalUrl() {
    const url = urlInput.value.trim();
    if (!url) {
      throw new Error("Bitte eine iCal-URL eingeben.");
    }
    if (!/^https?:\/\//i.test(url)) {
      throw new Error("Bitte eine gültige iCal-URL mit http:// oder https:// eingeben.");
    }

    const parsedUrl = new URL(url);
    if (parsedUrl.username || parsedUrl.password) {
      throw new Error("Bitte eine iCal-URL ohne Zugangsdaten vor dem Host eingeben.");
    }

    parsedUrl.pathname = parsedUrl.pathname
      .split("/")
      .map((segment) => encodeURIComponent(decodeURIComponent(segment)))
      .join("/");
    return parsedUrl.toString();
  }

  function createPythonWorker() {
    const workerSource = `
      let pyodideReady = null;

      async function loadConverter(pyodideBaseUrl, scriptUrl) {
        if (!pyodideReady) {
          self.postMessage({ type: "status", message: "Python wird geladen..." });
          importScripts(pyodideBaseUrl + "pyodide.js");
          const pyodide = await loadPyodide({ indexURL: pyodideBaseUrl });
          self.postMessage({ type: "status", message: "Python-Skript wird geladen..." });
          const sourceResponse = await fetch(scriptUrl, { cache: "no-store" });
          if (!sourceResponse.ok) {
            throw new Error("Python-Skript konnte nicht geladen werden.");
          }
          pyodide.globals.set("__name__", "ical_to_html_browser");
          pyodide.runPython(await sourceResponse.text());
          pyodideReady = pyodide;
        }
        return pyodideReady;
      }

      self.onmessage = async (event) => {
        const { pyodideBaseUrl, scriptUrl, url, limit } = event.data;
        try {
          const pyodide = await loadConverter(pyodideBaseUrl, scriptUrl);
          self.postMessage({ type: "status", message: "Python lädt die iCal-URL..." });
          pyodide.globals.set("browser_ical_url", url);
          pyodide.globals.set("browser_limit", limit);
          const html = await pyodide.runPythonAsync(
            "await generate_calendar_html_from_source(browser_ical_url, source_kind='url', limit=browser_limit, subscribe_url=browser_ical_url)"
          );
          self.postMessage({ type: "result", html });
        } catch (error) {
          self.postMessage({ type: "error", message: error.message || "Python ist fehlgeschlagen." });
        }
      };
    `;
    const workerUrl = URL.createObjectURL(new Blob([workerSource], { type: "application/javascript" }));
    return {
      worker: new Worker(workerUrl),
      workerUrl,
    };
  }

  async function generateHtml() {
    let worker = null;
    let workerUrl = null;
    let fetchTimeoutId = null;
    let overallTimeoutId = null;

    function cleanup() {
      window.clearTimeout(fetchTimeoutId);
      window.clearTimeout(overallTimeoutId);
      if (worker) {
        worker.terminate();
      }
      if (workerUrl) {
        URL.revokeObjectURL(workerUrl);
      }
    }

    try {
      generateButton.disabled = true;
      copyButton.disabled = true;
      outputEl.value = "";
      setStatus("URL wird an Python übergeben...");

      const url = getIcalUrl();
      const limit = selectedLimit();
      const workerHandle = createPythonWorker();
      worker = workerHandle.worker;
      workerUrl = workerHandle.workerUrl;

      await new Promise((resolve, reject) => {
        overallTimeoutId = window.setTimeout(() => {
          cleanup();
          reject(new Error("Python braucht zu lange zum Starten. Bitte die Seite neu laden und nochmals versuchen."));
        }, 60000);

        worker.onmessage = (event) => {
          const data = event.data;

          if (data.type === "status") {
            setStatus(data.message);
            if (data.message === "Python lädt die iCal-URL...") {
              fetchTimeoutId = window.setTimeout(() => {
                cleanup();
                reject(new Error("Python wartet zu lange auf die iCal-URL. Die Intranet-Seite blockiert den Zugriff wahrscheinlich oder antwortet nicht rechtzeitig."));
              }, 15000);
            }
            return;
          }

          if (data.type === "result") {
            outputEl.value = data.html;
            copyButton.disabled = false;
            setStatus("HTML generiert.");
            cleanup();
            resolve();
            return;
          }

          if (data.type === "error") {
            cleanup();
            reject(new Error(data.message));
          }
        };

        worker.onerror = (event) => {
          cleanup();
          reject(new Error(event.message || "Python-Worker ist fehlgeschlagen."));
        };

        worker.postMessage({ pyodideBaseUrl, scriptUrl, url, limit });
      });
    } catch (error) {
      setStatus(error.message);
    } finally {
      generateButton.disabled = false;
    }
  }

  async function copyHtml() {
    await navigator.clipboard.writeText(outputEl.value);
    setStatus("HTML in die Zwischenablage kopiert.");
  }

  modeInputs.forEach((input) => {
    input.addEventListener("change", () => {
      limitInput.disabled = document.querySelector("input[name='event-mode']:checked").value === "all";
    });
  });

  generateButton.addEventListener("click", generateHtml);
  copyButton.addEventListener("click", copyHtml);
</script>
