# Wi-Fi fall detection — the receiver & components (2026-11-07)

**Receiver = ESP32 development board.** It's a ready-made, small (thumb-sized) board with a chip that has Wi-Fi built in.
- Buy it ready-made (Robu.in, Amazon, local electronics shops). No circuit building or soldering.
- What we "implement" is the **software**: flash free firmware that records CSI (Channel State Information, a detailed record of how the Wi-Fi signal changed),
  then write Python code + an AI model on the laptop.
- Firmware options: Espressif esp-csi (https://github.com/espressif/esp-csi), ESP32-CSI-Tool (https://github.com/StevenMHernandez/ESP32-CSI-Tool).
- Normal Wi-Fi routers/phones don't share this signal detail, so we can't use them as receivers. A few commercial Wi-Fi motion products exist, but they're closed systems that don't share their raw data.

## Components (approx. prices, India)
| Item | Qty | Approx. cost |
|---|---|---|
| ESP32 dev board (e.g. ESP32-DevKitC / ESP32-S3) — 1 sender, 1 receiver | 2 (+1 spare) | ₹400–800 each |
| USB data cables | 2 | ₹100 each |
| USB charger / power bank (powers the sender) | 1 | ₹300–500 (or reuse phone charger) |
| Laptop with Python (free software) | 1 | already have |
| Thick mattress / gym mat (safe acted falls) | 1 | borrow |
| **Total** | | **≈ ₹1,500–2,500** |

Optional later: ESP32 board with external antenna (e.g. ESP32-WROOM-32U) for a stronger signal.

## Setup
Sender ESP32 sends ~100 small Wi-Fi messages per second → receiver ESP32 records the signal details → sends them to the laptop over USB → Python saves the data and the AI model detects falls.
