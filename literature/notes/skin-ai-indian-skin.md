# Skin-disease AI on Indian (darker) skin — prior work (searched 2026-11-12)

- DermaCon-IN: 5,450 clinical images from Indian outpatient clinics, Fitzpatrick IV–VI; NeurIPS 2025 Datasets & Benchmarks. https://arxiv.org/abs/2506.06099 (also https://openreview.net/pdf/7d53d989204cfbb8445f4fcf8c1d3060e5954643.pdf)
- DermaCon-IN cites a ~30–40% accuracy drop on darker skin (DDI) for models trained on Fitzpatrick17k — secondary citation, verify original.
- Dataset skew: >60% light-skin images in a major dataset (ICCS 2025). https://www.iccs-meeting.org/archive/iccs2025/papers/159070432.pdf
- CycleGAN synthetic dark-skin augmentation, small study (71.95% acc). https://emerginginvestigators.org/articles/25-159
- Related (checked, already well studied in India — NOT recommended): oral cancer from smartphone photos, e.g. Cancers 2023 IIIT-H https://mdpi.com/2072-6694/15/16/4120 ; arXiv 2608.21583.

Gap idea: train on Western data → test on DermaCon-IN → show drop → new method to close it (domain adaptation / fairness). Verify with full papers.
