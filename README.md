# pem-fuel-cell-model
A physics-based PEM fuel cell simulator modeling Nernst voltage, electrochemical losses, polarization behavior, and power output.

**What Is a Polarization Curve?**

A polarization curve describes how a fuel cell’s output voltage decreases as current density increases, revealing how real-world inefficiencies reduce the ideal thermodynamic voltage. The curve begins near the reversible standard potential, which represents the maximum possible voltage predicted by thermodynamics. As current increases, voltage drops due to irreversible losses that arise from reaction kinetics, electrical resistance, and gas transport limitations. This creates a characteristic downward-sloping curve that reflects the fuel cell’s true electrochemical behavior under load.

The polarization curve is commonly divided into three distinct regions, as illustrated in the figure. At low current densities, activation polarization dominates due to slow electrochemical reaction rates at the electrodes. At intermediate currents, the voltage drop becomes nearly linear due to ohmic polarization, caused by electrical resistance in the membrane and conductive materials. At high current densities, concentration polarization appears when reactant gases cannot be delivered fast enough, leading to a sharp voltage decline near the limiting current. Together, these regions explain the fundamental physical processes governing fuel cell performance.

<img width="850" height="558" alt="image" src="https://github.com/user-attachments/assets/cbf95a7c-a7d0-4782-b785-339e39e67d4f" />

Source: DOI:10.1126/sciadv.1500564

**Why Polarization Curves Matter in Fuel Cell Study**

Polarization curves are one of the most important tools for analyzing, diagnosing, and optimizing fuel cell performance. By examining the shape and slope of the curve, researchers can determine which physical losses dominate at different operating conditions, helping to evaluate catalyst activity, membrane resistance, electrode design, and gas diffusion efficiency. The curve also identifies the optimal operating range where voltage remains high while power output is maximized, making it essential for system control and stack design.

Beyond performance measurement, polarization curves provide insight into durability, degradation, and real-world operating limits. Changes in curve shape over time can indicate membrane aging, catalyst degradation, flooding, or fuel starvation. Engineers use this information to improve materials, enhance efficiency, scale fuel cell stacks, and predict lifetime behavior. For these reasons, polarization curves serve as a foundational diagnostic and design tool in both fuel cell research and industrial development.
