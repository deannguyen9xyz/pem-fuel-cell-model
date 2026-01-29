# pem-fuel-cell-model
A physics-based PEM fuel cell simulator modeling Nernst voltage, electrochemical losses, polarization behavior, and power output.

---

## 🎯 Purpose of This Project

The purpose of this project is to develop a physics-based Python simulator for modeling the performance of a PEM (Proton Exchange Membrane) fuel cell. The model applies thermodynamic principles and semi-empirical electrochemical equations to predict cell voltage, polarization behavior, and power density under varying operating conditions. By incorporating the Nernst equation, activation losses, ohmic losses, and concentration losses, the simulator provides a realistic representation of real-world fuel cell behavior.

--- 

## ▶️ How to Run

1. Install dependencies:

       pip install numpy matplotlib

3. Run the script: **fuel_cell_simulatorn.py**

---

## 👉 Theory

### **What Is a Polarization Curve?**

A polarization curve describes how a fuel cell’s output voltage decreases as current density increases, revealing how real-world inefficiencies reduce the ideal thermodynamic voltage. The curve begins near the reversible standard potential, which represents the maximum possible voltage predicted by thermodynamics. As current increases, voltage drops due to irreversible losses that arise from reaction kinetics, electrical resistance, and gas transport limitations. This creates a characteristic downward-sloping curve that reflects the fuel cell’s true electrochemical behavior under load.

The polarization curve is commonly divided into three distinct regions, as illustrated in the figure. At low current densities, activation polarization dominates due to slow electrochemical reaction rates at the electrodes. At intermediate currents, the voltage drop becomes nearly linear due to ohmic polarization, caused by electrical resistance in the membrane and conductive materials. At high current densities, concentration polarization appears when reactant gases cannot be delivered fast enough, leading to a sharp voltage decline near the limiting current. Together, these regions explain the fundamental physical processes governing fuel cell performance.

<img width="850" height="558" alt="image" src="https://github.com/user-attachments/assets/cbf95a7c-a7d0-4782-b785-339e39e67d4f" />

Source: DOI:10.1126/sciadv.1500564

### **Why Polarization Curves Matter in Fuel Cell Study**

Polarization curves are one of the most important tools for analyzing, diagnosing, and optimizing fuel cell performance. By examining the shape and slope of the curve, researchers can determine which physical losses dominate at different operating conditions, helping to evaluate catalyst activity, membrane resistance, electrode design, and gas diffusion efficiency. The curve also identifies the optimal operating range where voltage remains high while power output is maximized, making it essential for system control and stack design.

Beyond performance measurement, polarization curves provide insight into durability, degradation, and real-world operating limits. Changes in curve shape over time can indicate membrane aging, catalyst degradation, flooding, or fuel starvation. Engineers use this information to improve materials, enhance efficiency, scale fuel cell stacks, and predict lifetime behavior. For these reasons, polarization curves serve as a foundational diagnostic and design tool in both fuel cell research and industrial development.

---

## 📊 Result and Discussion

<img width="905" height="573" alt="image" src="https://github.com/user-attachments/assets/ae518beb-f3ab-4164-8d12-11a1074c0994" />

The simulation produces a realistic polarization curve, showing the expected voltage decrease as current density increases due to activation, ohmic, and concentration losses. The model successfully reproduces the three characteristic fuel cell operating regions, indicating that the implemented physics captures real PEM fuel cell behavior.

The corresponding power density curve identifies an optimal operating point where power output is maximized. At 1.0 A/cm², the predicted cell voltage is approximately 0.78 V, which is consistent with typical experimental PEM fuel cell data. Loss analysis indicates that activation and ohmic losses dominate at moderate current levels, while mass transport losses become more significant at high current, demonstrating the model’s usefulness for performance evaluation and design insight.

--- 

## 🧑‍💻 Author

Developed by: Vu Bao Chau Nguyen, Ph.D.

Keywords: Fuel Cell, PEM Fuel Cell, Polarization Curve.

---
