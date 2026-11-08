# Energy disaggregation (NILM): split one meter reading by appliance

**NILM** = Non-Intrusive Load Monitoring: software splits the whole-house meter signal into per-appliance use, with no sensor on each appliance.

## Sources (verified 2026-11-08)
1. G. W. Hart, "Nonintrusive appliance load monitoring," *Proceedings of the IEEE*, 80(12):1870–1891, 1992. https://doi.org/10.1109/5.192069
   - The founding paper: appliances show up as step jumps (on/off "fingerprints") in total power.
2. J. Z. Kolter and M. J. Johnson, "REDD: A Public Data Set for Energy Disaggregation Research," SustKDD workshop, 2011. https://www.zicokolter.com/publications/kolter2011redd.pdf
   - US homes; whole-house + per-circuit ground truth.
3. J. Kelly and W. Knottenbelt, "The UK-DALE dataset, domestic appliance-level electricity demand and whole-house demand from five UK homes," *Scientific Data*, 2:150007, 2015. https://doi.org/10.1038/sdata.2015.7
4. N. Batra, M. Gulati, A. Singh, M. B. Srivastava, "It's Different: Insights into home energy consumption in India," ACM BuildSys 2013. https://nipunbatra.github.io/papers/2013/buildsys13_iawe.pdf
   - iAWE: one Delhi home, 73 days. Shows Indian homes differ (voltage swings, many fans, geysers, inverters).

## How it works (plain)
1. Spot the jumps in total power.
2. Match each jump to an appliance fingerprint (size + timing + pattern).
3. Train a model on data where each appliance was also measured (REDD, UK-DALE).

## What this means for a project
- Indian data is very scarce (iAWE is one house) → possible gap: collect/label Indian-home data, or test how well US/UK-trained models transfer to Indian homes.
- Explainer: `explainers/electricity-breakdown.html`
