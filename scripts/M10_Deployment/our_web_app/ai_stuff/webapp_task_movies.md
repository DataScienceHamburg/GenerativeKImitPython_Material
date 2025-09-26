## 1. Task Title
Streamlit Web App: Filme aus Handlungsbeschreibung finden

## 2. Task Overview
Erstelle eine kleine Streamlit‑Webapp in `our_scripts/our_web_app/app.py`, die wie das Wireframe `our_scripts/our_web_app/ai_stuff/wireframe_of_app_layout.png` aussieht. Nutzer geben eine Handlungsbeschreibung ein; die App ruft mit `get_movies_from_plot` aus `our_scripts/our_web_app/helper_funs.py` passende Filme ab und zeigt Titel, Darsteller, Regisseur und Veröffentlichungsjahr an.

## 3. Project Analysis

### Project Context
- **Current State:** Es existieren `app.py` (mit Platzhalter) und `helper_funs.py` (liefert strukturierte Filmdaten). Es gibt ein Wireframe zur Zieloberfläche.
- **Relevant Codebase:** Streamlit Frontend in `app.py`; Model‑/Chain‑Logik und Outputschema in `helper_funs.py`.

### Dependencies & Constraints
- **Required Libraries/APIs:** Streamlit, `langchain_groq`, `pydantic`, `python-dotenv` (bereits im Projekt). Externer LLM via Groq.
- **Constraints:**
  - Einfache Lösung, keine neuen Patterns/Frameworks.
  - Keine Änderungen an `.env` erzwingen.
  - UI soll dem Wireframe sehr nahekommen: Überschrift, Eingabefeld mit Platzhalter „eingabefeld“, Senden‑Button rechts, Ergebnisliste mit Trennlinie.

## 4. Context & Problem Definition
- **Background:** Nutzer möchten aus einer vagen Plotbeschreibung schnell passende Filme finden.
- **The Problem:** Aktuell gibt es keine UI. Es wird eine minimale, klare Oberfläche benötigt, die die vorhandene Funktion nutzt und Ergebnisse strukturiert darstellt.

## 5. Technical Requirements
- **Platform/Environment:** Python, Streamlit App (`streamlit run our_scripts/our_web_app/app.py`).
- **Key Functionality:**
  - Eingabe eines Textes (Plotbeschreibung).
  - Triggern der Abfrage via Button.
  - Aufruf `get_movies_from_plot(plot: str) -> dict` und Auslesen von `movies`.
  - Darstellung pro Film: Titel, Darsteller, Regisseur, Veröffentlichungsjahr.
  - Fehlerfälle anzeigen, falls `error` im Rückgabewert vorhanden ist.
- **Performance:** Single‑request UI; direkte Antwortanzeige reicht.
- **Security:** Keine Persistenz; keine sensiblen Daten loggen.

## 6. API & Backend Changes
### New Endpoints
Keine. Es wird ausschließlich `get_movies_from_plot` genutzt.

### Database Schema Changes
Keine.

### Logic/Business Rules
- Leer‑/Kurztexteingaben (< 3 Zeichen) nicht anfragen, stattdessen Hinweis anzeigen.
- Ergebnisse in der Reihenfolge der Rückgabe zeigen.

## 7. Frontend Changes
- **UI Components:**
  - Überschrift: „Beschreibe die Handlung“.
  - Eingabefeld mit Platzhalter „eingabefeld“.
  - Absenden‑Button rechts neben dem Eingabefeld (so nah wie möglich am Wireframe; in Streamlit mit Spalten lösen).
  - Ergebnisliste: Für jeden Film ein Block mit:
    - „Filmtitel“ (fett)
    - „Darsteller: …“
    - „Regisseur: …“
    - „Veröffentlichungsjahr: …“
    - Dünne Trennlinie zwischen Einträgen.
- **User Flow:** Nutzer tippt Plot -> klickt Button -> lädt/zeigt Resultate -> weitere Anpassungen möglich, ohne Seite zu reloaden.
- **State Management:** Lokaler State via Streamlit Widgets; keine zusätzliche State‑Lib.

## 8. Implementation Plan
### Step 1: Planning & Design
1. Layout an Wireframe `ai_stuff/wireframe_of_app_layout.png` ausrichten (Spalten für Input + Button; Ergebnisliste darunter).

### Step 2: Backend Implementation
1. Keine – Backend ist vorhanden (`helper_funs.get_movies_from_plot`).

### Step 3: Frontend Implementation
1. In `app.py`: Titel/Anleitung rendern.
2. Zwei‑Spalten‑Layout: links `st.text_input(placeholder="eingabefeld")`, rechts `st.button("▶")`.
3. Bei Klick und gültigem Text: `get_movies_from_plot(text)` aufrufen.
4. Fehlerbehandlung: Falls `error` vorhanden, `st.error` mit Meldung anzeigen.
5. Ergebnisse rendern: Für jeden Eintrag Überschrift + 3 Metazeilen; `st.divider()` zwischen den Filmen.
6. Optional: `st.spinner` während des Aufrufs.

### Step 4: Integration & Testing
1. Lokal starten: `streamlit run our_scripts/our_web_app/app.py`.
2. Positivtest mit typischen Plots (z. B. „Detektivgeschichte“).
3. Negativtest mit leerem Input und sehr kurzem Input.

## 9. File Structure & Organization
### New/Modified Files
- Modifizieren: `our_scripts/our_web_app/app.py` (nur UI‑Code, keine neue Technologie).

## 10. Acceptance Criteria
- Überschrift und Eingabebereich entsprechen dem Wireframe.
- Button rechts vom Eingabefeld; Klick startet Suche.
- Ergebnisse zeigen Titel, Darsteller, Regisseur, Veröffentlichungsjahr, getrennt durch Linien.
- Fehler werden sichtbar angezeigt, ohne Absturz.
- Es wird ausschließlich `helper_funs.get_movies_from_plot` zur Datenbeschaffung verwendet.


