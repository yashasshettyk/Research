# Can Wi-Fi see shape, height or width? (searched 2026-11-07)

**Short answer:**
- **Cheap ESP32 boards** can sense movement, a rough body size (person vs pet) and the room. They can't capture exact shape, height or width.
- **Better hardware plus AI** can draw a rough body outline or pose.
- **Why there's a limit:** a 2.4 GHz Wi-Fi wave is about 12.5 cm long, so smaller details blur. ESP32 also has only 1 antenna and a narrow channel (20–40 MHz).

## Papers
1. **J. Geng, D. Huang, F. De la Torre.** "DensePose From WiFi." arXiv:2301.00250, Dec 2022 (preprint).
   - Uses Wi-Fi phase and amplitude to estimate the body surface (24 body regions) of several people. Reported to be close to camera-based methods.
   - The hardware was cheap routers (about US $30, per TechXplore).
   - https://arxiv.org/abs/2301.00250
2. **F. Adib, C.-Y. Hsu, H. Mao, D. Katabi, F. Durand.** "Capturing the Human Figure Through a Wall" (RF-Capture). *ACM Trans. Graphics* 34(6), 2015. DOI 10.1145/2816795.2818072.
   - Builds a rough figure of a person behind a wall and tells 15 users apart.
   - Uses a special custom radio with an antenna array, not normal Wi-Fi.
   - https://people.csail.mit.edu/hongzi/content/publications/RFcapture-TOG.pdf

## Use in Home Guardian
Rough body size (pet vs adult vs child) could help Theft mode ignore pets. The design keeps it as an optional extra.
