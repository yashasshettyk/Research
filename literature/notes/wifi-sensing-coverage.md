# Wi-Fi sensing coverage: where in a room can a fall be sensed?

Question (2026-11-07): can a fall in a room corner be detected if the router is outside the room?

## Key idea: the Fresnel zone
- Between a sender and a receiver there are egg-shaped (elliptical) zones called Fresnel zones. Movement inside or near them changes the signal most. Movement far from them changes it less.
- Wi-Fi also bounces off walls, floor and ceiling (multipath), so a person anywhere in the room changes some paths. The change is weaker far from the boards.
- Sensing has a boundary: past it, the signal change is too small compared to noise. This is measured by SSNR (sensing signal-to-noise ratio).

## Sources (verified)
1. D. Zhang, H. Wang, D. Wu, "Toward Centimeter-Scale Human Activity Sensing with Wi-Fi Signals," *IEEE Computer*, 50(1):48–57, 2017. DOI: 10.1109/MC.2017.7. https://researchportal.ip-paris.fr/en/publications/toward-centimeter-scale-human-activity-sensing-with-wi-fi-signals/
   - Presents the Fresnel zone model for Wi-Fi sensing.
2. D. Wu, D. Zhang, C. Xu, H. Wang, X. Li, "Device-Free WiFi Human Sensing: From Pattern-Based to Model-Based Approaches," *IEEE Communications Magazine*, 55(10):91–97, 2017. DOI: 10.1109/MCOM.2017.1700143. https://researchportal.ip-paris.fr/en/publications/device-free-wifi-human-sensing-from-pattern-based-to-model-based-/
   - Moves from pattern-based to model-based (Fresnel zone) Wi-Fi sensing.
3. SMU research seminar, Zhang Daqing, "Towards Millimeter-Scale Contactless Sensing with Wi-Fi/4G/5G" (seminar page). https://computing.smu.edu.sg/newsletter/research-seminar-zhang-daqing-towards-millimeter-scale-contactless-sensing-wi-fi/4g/5g
   - Describes SSNR as a measure of the sensing boundary.
4. "Fresnel zone based theories for contactless sensing" (book chapter, BUAA research portal). https://research.buaa.edu.cn/en/publications/fresnel-zone-based-theories-for-contactless-sensing/
   - Reflection model near the line between the boards; diffraction model far from it.

## What this means for Home Guardian
- Router outside the room: the wall weakens the signal, and corners far from the line between boards are weakest. A fall there may be missed.
- Fix: (1) put our own sender board inside the room; (2) use 2 receivers on different walls (already in the design); (3) run a "corner test" at setup (lie down in each corner and check the dashboard); (4) add a 3rd board in a big room.
- Explainer: `explainers/wifi-corner-coverage.html` (simple model, not exact physics).
- Paper idea: report detection rate per room zone (centre vs edges vs corners). Most papers report one overall number.
