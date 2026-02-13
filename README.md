
# OpenSpace Seat Organizer

![OpenSpace Seat Organizer](/assets/ChatGPT Image 13 Şub 2026 15_50_31.png)

## 🚀 Challenge Overview
**Type:** Consolidation  
**Repository:** [openspace-organizer](https://github.com/Ardatekk/openspace-organizer)  
**Duration:** 2 days  
**Team:** Solo or Team  
**Deadline:** dd/mm/yy H:i AM/PM  

**Mission:** Create a Python program that randomly assigns colleagues to seats in an open space to encourage collaboration and team interaction.

---

## 🎯 Mission Objectives
- Randomly assign people to spots in the open space.
- Use Object-Oriented Programming (OOP) principles effectively.
- Apply clean architecture and project structuring.
- Handle data import/export with Excel files.

**Optional (Team Challenge):**
- Collaborate using Git & Trello.
- Split functionalities into tasks, assign, and use PRs for merging.

---

## 🧩 Learning Objectives
- Implement classes and objects with proper encapsulation.
- Use imports correctly and maintain a clean code structure.
- Read data from an Excel file.
- Organize a Python project for real-world scenarios.
- Apply code style with `black` and include clear docstrings.

---

## 🏢 The Scenario
Your company moved to a new office with **6 tables of 4 seats each**. To help new colleagues get to know each other, the seating changes **daily**.  
Your program should:

- Load a list of colleagues from an Excel file.
- Randomly distribute colleagues across the 24 seats.
- Indicate free seats.
- Handle more colleagues than available seats gracefully.

**Nice-to-have Features:**

- Dynamic room configuration via `config.json`.
- Add colleagues or tables on the fly.
- Avoid leaving someone alone at a table.
- Respect seating preferences (blacklist/whitelist) from Excel.
- Provide an interactive HTML page for execution and configuration.

---

## ⚙️ Project Structure

openspace-organizer/
│
├─ README.md
├─ main.py
├─ assets/
│ └─ OpenSpaceBanner.png
└─ utils/
├─ file_utils.py
├─ table.py
└─ openspace.py