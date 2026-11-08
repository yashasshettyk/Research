# Better idea: Wi-Fi stampede early warning (2026-11-08)

Shravya asked for "some other better idea" after set 7. One strong pick instead of another list.

**Idea:** Cheap ESP32 Wi-Fi boards at crowded choke points (stadium gates, temple queues, railway foot-bridges) sense how packed the crowd is and whether it is surging, then alert guards before a crush. No cameras are needed.

**Why it's better**
- Real, recent need: Bengaluru Chinnaswamy stadium stampede, 4 Jun 2025, 11 dead (see lit note).
- Reuses her Home Guardian skills and hardware (ESP32 CSI), so one skill set serves two projects.
- Works in the dark, in rain and in smoke, and needs no faces (privacy-safe), where cameras struggle.

**Gap (initial check)**
- Camera-based stampede detection is already crowded with papers.
- Wi-Fi crowd counting exists, but mostly indoors with small groups (~6–10 people).
- Dense crowds at gates and detecting pushing/surges (not just counting) look open. Needs a deeper search.

**Catch:** testing real dense crowds is hard. Plan: a class of 30–50 students walking through a corridor or gate, plus a simulation.

Sources: `literature/notes/crowd-safety.md`
