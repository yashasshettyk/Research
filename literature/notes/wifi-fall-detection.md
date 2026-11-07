# Wi-Fi fall detection: key papers (searched 2026-11-07)

All papers below were checked via web search or the paper's own page. Results are as the authors reported them; we haven't verified them ourselves.

## Why it matters
- **WHO, "Falls" fact sheet:** about 684,000 fall deaths worldwide each year. Adults over 60 have the most fatal falls, and over 80% of deaths happen in low- and middle-income countries. https://www.who.int/news-room/fact-sheets/detail/falls

## A. Classic Wi-Fi (CSI) fall detection
1. **Y. Wang, K. Wu, L. M. Ni.** "WiFall: Device-Free Fall Detection by Wireless Networks." *IEEE Trans. Mobile Computing*, 16(2):581–594, 2017. DOI 10.1109/TMC.2016.2557792.
   - The first well-known CSI fall detector. It reported about 94% precision with a 13% false alarm rate (Random Forest), for one person only.
   - Conference version: Han, Wu, Wang, Ni, INFOCOM 2014.
   - https://www.scilit.net/publications/c8829155edd304f3d09f06ffaac95391
2. **H. Wang, D. Zhang, et al.** "RT-Fall: A Real-Time and Contactless Fall Detection System with Commodity WiFi Devices." *IEEE Trans. Mobile Computing*, 2017.
   - Uses phase difference between two antennas, and a sharp power drop at the end of a fall.
   - Beat WiFall by 14% sensitivity and 10% specificity, on average across 4 rooms.
   - https://researchportal.ip-paris.fr/en/publications/rt-fall-a-real-time-and-contactless-fall-detection-system-with-co/
3. **S. Palipana, D. Rojas, P. Agrawal, D. Pesch.** "FallDeFi: Ubiquitous Fall Detection using Commodity Wi-Fi Devices." *Proc. ACM IMWUT*, 1(4), 2018.
   - Uses time-frequency (STFT) features. Accuracy drops to about 80% when the room changes, which shows the "new home" problem.
   - https://bibbase.org/network/publication/palipana-rojas-agrawal-pesch-falldefiubiquitousfalldetectionusingcommoditywifidevices-2018

## B. Working in new homes without retraining
4. **Y. Hu, F. Zhang, C. Wu, B. Wang, K. J. R. Liu.** "DeFall: Environment-Independent Passive Fall Detection using WiFi." *IEEE Internet of Things Journal*, 9:8515–8530, 2022. DOI 10.1109/JIOT.2021.3116136.
   - Matches the speed and acceleration pattern of a fall against a template.
   - Reported over 95% detection with under 1.5% false alarms, using one transmitter–receiver pair, and no retraining in new rooms.
   - https://originwirelessai.com/wp-content/uploads/2024/04/DeFall.pdf
5. **G. Chi, et al.** "XFall: Domain Adaptive Wi-Fi-Based Fall Detection With Cross-Modal Supervision." *IEEE JSAC*, 42(9):2457–2471, 2024.
   - A camera model teaches the Wi-Fi model during training.
   - Reported 96.8% accuracy, 3.1% misses and 3.3% false alarms, and about 1 year of real deployment.
   - https://dblp.dagstuhl.de/rec/journals/jsac/ChiZDMYDXL24.html
6. **Y. Wang, C. Pan, R. Liu, S. Li, H. Ren, K. Wang, J. Wang.** "Robust Cross-Domain WiFi Fall Detection via Physics-Driven Attention-Enhanced Transformers." arXiv:2605.00869, Apr 2026 (preprint, not yet peer-reviewed).
   - Reported about 98.8% in unseen rooms with no fine-tuning.
   - https://arxiv.org/abs/2605.00869

## C. Self-learning (no labels / keeps learning)
7. **J. Yang, X. Chen, H. Zou, D. Wang, L. Xie.** "AutoFi: Toward Automatic Wi-Fi Human Sensing via Geometric Self-Supervised Learning." *IEEE Internet of Things Journal*, 10(8):7416–7425, 2023.
   - Learns from random unlabeled Wi-Fi data, then reuses that knowledge for new tasks. This is close to our "learns at night by itself" idea.
   - https://arxiv.org/abs/2205.01629
8. **F. Wang, T. Zhang, W. Xi, et al.** "A Survey on Wi-Fi Sensing Generalizability: Taxonomy, Techniques, Datasets, and Future Research Prospects." *IEEE Communications Surveys & Tutorials*, 2026 (accepted). arXiv:2503.08008.
   - Covers continual learning (CCS, CAREC, CSI-ARIL) and few-shot adaptation (FewCS). Read this one first for background.
   - https://arxiv.org/abs/2503.08008

## D. Cheap ESP32 hardware
9. **T. Do, X. Le, H. N. Tran, T. H. P. Nguyen.** "Human Fall Detection and Indoor Localization Using WiFi Sensing Approach." CITA 2025, *LNNS* vol. 1581, Springer, 2026, pp. 123–134. DOI 10.1007/978-3-032-00972-2_10.
   - ESP32 boards, with a public **UIT-ESP32** dataset. Reported over 99% precision for both the fall and where it happened.
   - https://elib.vku.udn.vn/handle/123456789/6225

## Background survey
- **Y. Ma, G. Zhou, S. Wang.** "WiFi Sensing with Channel State Information: A Survey." *ACM Computing Surveys*, 52(3), 2019/2020. DOI 10.1145/3310194. https://gzhou.pages.wm.edu/wp-content/blogs.dir/5736/files/sites/13/2017/12/WiFiSenseSurvey_CSUR19.pdf

## Research gap (first look)
- Many papers make one fixed model work in new rooms (DeFall, XFall, the 2026 preprint).
- Self-learning exists for general Wi-Fi sensing (AutoFi, continual-learning methods).
- In this quick search we found **no paper that combines continual self-learning + fall detection + cheap ESP32 + multi-person, multi-floor Indian homes + an "Are you OK?" voice-check safety loop.** That combination is her possible gap. A deeper search is still needed before claiming it.
