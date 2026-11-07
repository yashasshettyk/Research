# Home Guardian: design v1 (2026-11-07)

**Working paper title:** "Home Guardian: A Self-Learning, Dual-Mode (Fall + Intruder) Wi-Fi Sensing System on Low-Cost ESP32 Boards"

**One line:** Cheap ESP32 boards sense movement through Wi-Fi. One AI model learns each home's own movement pattern and works in two modes: **Guardian** (protect elders) and **Theft** (protect the empty house).

## 1. What makes it stand out
Checked against the 11 papers in `literature/notes/wifi-fall-detection.md`. No single paper does all of these together. A deeper search is still needed before the final claim.

| # | Unique feature | Closest paper and what it lacks |
|---|---|---|
| 1 | **Two modes, one system.** The same boards and the same model work in both modes. They switch automatically when everyone's phone leaves the home Wi-Fi, or by a tap. | SiFall detects falls only. AR-Alarm detects intruders only. |
| 2 | **Learns the home's routine.** It keeps learning every night with no labels. It flags a fall, a very long stay in the bathroom, no movement by 9 am, or movement in an empty house. | SiFall self-learns for falls only. Routine-anomaly work uses other sensors, not Wi-Fi. |
| 3 | **Family vs stranger.** It combines the family's phones being home with learned walking style, so a family member coming home early is not an "intruder". | AR-Alarm can't tell a resident from an intruder. |
| 4 | **"Are you OK?" voice check plus feedback taps.** Every reply ("I'm OK", "only the cat") becomes a label that teaches the model. | No fall paper we found uses this loop. |
| 5 | **Cheap multi-floor setup.** ESP32 boards on each floor report which floor and room. | The UIT-ESP32 paper uses one area; DeFall and XFall use costlier Wi-Fi cards. |
| 6 | **Live dashboard.** A phone or web page shows a live house map with moving dots, the mode, a confidence meter and alerts. It runs at home with no camera and no cloud. | Papers show offline results only. |

## 2. The two modes
- **Guardian mode (family at home):** falls, long stillness in risky rooms, unusual routine. Alert = voice check → call/SMS family.
- **Theft mode (house empty or night):** any human movement → check phones + walking style → if unknown: siren/alert + which room. Pets, fans and curtains are ignored using a learned "pet/object" class, as AR-Alarm does.
- **Auto switch:** all family phones off home Wi-Fi → Theft. A known phone returns → Guardian. Night schedule: Guardian for bedrooms + Theft for doors/windows.

## 3. The ML model (plain words)
1. **Collect:** each receiver records CSI (fine signal details) about 100 times per second, cut into 2-second windows.
2. **Clean:** remove spikes and noise (Hampel + low-pass filter); use amplitude and phase difference.
3. **Encoder ("brain"):** a small CNN + transformer turns each window into a short "movement fingerprint". It is pre-trained **self-supervised** (learns from unlabeled data, like AutoFi) and small enough for a Raspberry Pi.
4. **Three heads (small output parts):**
   - Activity: empty / still / walk / sit / lie / fall / pet-or-object.
   - "Normal or strange" score compared with this home's learned routine (time + room).
   - Where + who: floor/room and family vs unknown.
5. **Night learning (continual learning):** retrain on today's data + feedback labels, and replay old examples so it doesn't forget.
6. **Precision trick:** 2 receivers per floor must agree, then the voice check confirms. If it is unsure, it asks; it never stays silent.

**Start:** train on the public UIT-ESP32 dataset + our own acted data, then let it learn in the home.

## 4. Hardware and cost (approx., India)
| Item | Qty (2-floor home) | Approx. cost |
|---|---|---|
| ESP32 boards (1 sender + 2 receivers per floor) | 6 | ₹400–800 each |
| USB chargers / cables | 6 | reuse or ₹100–300 each |
| Hub: laptop (prototype) → Raspberry Pi (later) | 1 | ₹0 now / ≈₹5,000–7,000 later |
| Small speaker + mic (voice check), or an old phone | 1 | ₹0–700 |
| **Prototype total** | | **≈ ₹3,000–6,000** |

## 5. How we prove it (for the paper)
- **Tests:** acted falls on a mattress (young volunteers, with consent), 1–3 people, 2 floors, a pet if possible, and 2–4 weeks of live running.
- **Measures:** % of falls caught, false alarms per day, % of intruders caught, time to alert, cost.
- **Compare with:** a classic method (WiFall-style) and a self-learning method (SiFall-style), on Day 1 vs after learning.
- **Honest target:** catch ≥95% of falls and intruders with <1 false alarm per week after learning. The voice check covers the rest. 100% is not claimable.

## 6. Build order
1. Live dashboard on simulated data (upgrade `explainers/wifi-house-simulation.html`).
2. Buy 3 ESP32s; record CSI in one room.
3. Train a first model (falls + empty/motion).
4. Add Theft mode + auto switch → 2 floors → self-learning → full tests.
