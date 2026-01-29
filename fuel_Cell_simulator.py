import numpy as np
import matplotlib.pyplot as plt

# --- 1. Physical Constants & Parameters ---
class FuelCellParameters: #contain all relevant constants and tunable parameters
    def __init__(self, T_kelvin=353, P_H2_atm=1.0, P_O2_atm=1.0):   # 353K = 80°C
        # Universal Constants
        self.R = 8.314        # Ideal Gas Constant (J/mol*K)
        self.F = 96485        # Faraday's Constant (C/mol)
        
        # Operating Conditions
        self.T = T_kelvin     # Temperature in Kelvin, higher T -> faster reactions -> better performance
        self.P_H2 = P_H2_atm  # Partial Pressure Hydrogen (atm), more hydrogen -> potentially higher voltage -> better performance
        self.P_O2 = P_O2_atm  # Partial Pressure Oxygen (atm), more oxygen -> potentially higher voltage -> better performance
        
        # Cell Specifics (Tunable parameters for study)
        self.alpha = 0.5      # Charge transfer coefficient, how easy electron transfer (0 = reaction harder to 1 = reaction easier)
        self.area_resistance = 0.2  # Membrane Resistance (Ohm*cm^2)
        self.i_limit = 1.8    # Limiting current density (A/cm^2) - point where fuel runs out

# --- 2. Physics Equations ---

def calc_nernst_voltage(params):
    """
    Calculates the Theoretical Open Circuit Voltage (E_thermo).
    Equation: E = E0 - (RT/2F) * ln(1 / (P_H2 * P_O2^0.5))
    """
    E0 = 1.229 # Standard voltage at 25°C
    
    # Temperature correction for standard potential (simplified linear approx). If temp increases, voltage decreases slightly
    E_standard_T = E0 - 0.85e-3 * (params.T - 298.15)
    
    # Pressure correction (Nernst term), if partial pressures increase when more H2 and O2, voltage increases
    term_pressure = (params.R * params.T / (2 * params.F)) * np.log(params.P_H2 * (params.P_O2**0.5))
    return E_standard_T + term_pressure

def calc_activation_loss(i, params):
    """
    This calculates voltage lost because chemical reactions are slow (Tafel Equation).
    V_act = (RT / 2*alpha*F) * ln(i / i0)
    """
    i0 = 1e-3  # Exchange current density (reaction speed at equilibrium)
    
    term_tafel = (params.R * params.T) / (2 * params.alpha * params.F)  #This calculates how sensitive voltage loss is to reaction speed.
    v_act = term_tafel * np.log((i + 1e-6) / i0) #Reaction becomes harder -> voltage loss increases.
    
    return np.maximum(0, v_act) # Loss cannot be negative

def calc_ohmic_loss(i, params):
    """
    Loss due to resistance of the membrane (V = IR).
    """
    return i * params.area_resistance

def calc_concentration_loss(i, params):
    """
    Loss due to running out of gas at high speed, voltage loss when gas supply cannot keep up (Mass Transport).
    V_conc = -(RT/nF) * ln(1 - i/i_limit)
    """
    # Prevent math error if i > i_limit
    i_safe = np.minimum(i, params.i_limit - 1e-4) # Prevents current from exceeding the maximum fuel supply limit.
    
    term_conc = (params.R * params.T) / (2 * params.F) # physics scaling factor
    v_conc = -term_conc * np.log(1 - (i_safe / params.i_limit)) #sharp drop at the end of the curve, Fuel runs out -> voltage collapses quickly
    
    return v_conc # Voltage loss due to mass transport limitations

# --- 3. Main Simulation Loop ---

def simulate_fuel_cell(params):
    # Create an array of current densities (0 to 1.8 A/cm^2)
    current_density = np.linspace(0.001, params.i_limit - 0.05, 100) # This creates 100 current values starting from almost zero up to near the maximum fuel cell limit
    
    # 1. Theoretical Max Voltage
    E_nernst = calc_nernst_voltage(params)
    
    # 2. Calculate Losses
        
    v_act = calc_activation_loss(current_density, params) # voltage lost because chemical reactions are slow
    v_ohmic = calc_ohmic_loss(current_density, params) # voltage lost due to electrical resistance
    v_conc = calc_concentration_loss(current_density, params) # voltage lost because gas cannot reach the reaction fast enough
    
    # 3. Final Cell Voltage
    v_cell = E_nernst - v_act - v_ohmic - v_conc # Real Voltage = Ideal Voltage − All Losses
    
    # 4. Power Density (P = V * I) [Watts / cm^2]
    p_cell = v_cell * current_density # usable energy the fuel cell produces.
    
    return current_density, v_cell, p_cell, [v_act, v_ohmic, v_conc]

# --- 4. Visualization ---

# Initialize parameters (Try changing Temperature to 300 or 360!)
my_fc = FuelCellParameters(T_kelvin=353, P_H2_atm=3.0, P_O2_atm=3.0)

i, v, p, losses = simulate_fuel_cell(my_fc)

fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Voltage (Left Axis)
color = 'tab:blue'
ax1.set_xlabel('Current Density ($A/cm^2$)', fontsize=12)
ax1.set_ylabel('Cell Voltage (V)', color=color, fontsize=12)
ax1.plot(i, v, color=color, linewidth=3, label='Polarization Curve')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(0, 1.2)
ax1.grid(True, alpha=0.3)

# Plot Power Density (Right Axis)
ax2 = ax1.twinx()  
color = 'tab:orange'
ax2.set_ylabel('Power Density ($W/cm^2$)', color=color, fontsize=12)
ax2.plot(i, p, color=color, linestyle='--', linewidth=2, label='Power Density')
ax2.tick_params(axis='y', labelcolor=color)

plt.title(f'Fuel Cell Performance\n(T={my_fc.T}K, P={my_fc.P_H2}atm)', fontsize=14)

# --- 5. Breakdown Analysis ---
print(f"--- Simulation Results at 1.0 A/cm^2 ---")
idx = np.abs(i - 1.0).argmin() # Find index closest to 1.0 A
print(f"Total Voltage:      {v[idx]:.4f} V")
print(f"Max Power Peak:     {np.max(p):.4f} W/cm^2")
print(f"Loss Breakdown:")
print(f"  - Activation Loss: {losses[0][idx]:.4f} V (Starting the reaction)")
print(f"  - Ohmic Loss:      {losses[1][idx]:.4f} V (Resistance)")
print(f"  - Mass Transport:  {losses[2][idx]:.4f} V (Gas starvation)")

plt.show()