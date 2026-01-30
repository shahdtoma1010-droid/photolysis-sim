# Toluene Photolysis Simulator

**Advanced Spatio-Temporal Simulation of UV254-Irradiated Toluene Degradation**

A professional-grade web application for simulating and analyzing the photochemical degradation of toluene using UV254 radiation, based on Michelson interferometry principles.

## 📋 Project Overview

This simulator models the UV-induced photodegradation of toluene (C₆H₅CH₃), a volatile organic compound (VOC) commonly found in industrial processes. The application implements the scientific principles from the research paper **"Spatio-temporal photolysis rate profiles of UV254 irradiated toluene"** by Ahmed S. El-Tawargy (Scientific Reports, 2022).

### Key Features

**Interactive Simulation Lab**
- Real-time control of UV intensity (0-100%)
- Temperature adjustment (20-50°C)
- Two experimental conditions: with oxygen exposure and without oxygen
- Live calculation of refractive index changes and photolysis rates
- Particle animation showing UV photon interactions and radical formation

**Scientific Theory Section**
- Detailed explanation of photolysis mechanisms
- Michelson interferometry principles
- Governing equations with full mathematical derivations
- Experimental methodology and setup

**Comparative Analysis**
- Side-by-side comparison of degradation kinetics with and without oxygen
- Statistical analysis of reaction rates
- Visualization of the speedup factor due to oxygen-assisted oxidation

## 🔬 Scientific Foundation

### Photolysis Mechanism

When toluene molecules absorb UV254 photons (4.9 eV), C-C and C-H bonds dissociate:

```
C₆H₅-CH₃ + hν(254nm) → C₆H₅-CH₂• + H•
```

The primary photoproduct is the **benzyl radical** (C₆H₅-CH₂•), which undergoes rapid oxidation in the presence of oxygen.

### Governing Equation

The refractive index profile is modeled as:

```
n(t, y) = n₀ - Δn_max · (1 - e^(-t/τ)) · e^(-αy)
```

Where:
- **n₀** = Initial refractive index (1.48785 at 632.8 nm)
- **Δn_max** = Maximum refractive index change (UV intensity dependent)
- **τ** = Time constant (300s with air, 600s without air)
- **α** = Absorption coefficient (0.5 mm⁻¹)
- **y** = Depth from surface (mm)

### Experimental Setup

- **UV Source**: 4W lamp at 254 nm (UV-C)
- **Probe System**: 10 mW He-Ne laser at 632.8 nm
- **Sample**: 1 mL pure toluene in sealed quartz cuvette
- **Conditions**: 27 ± 1°C, 50 ± 2% relative humidity
- **Duration**: 60 minutes irradiation

## 🎨 Design Philosophy

The application follows a **Dark Glassmorphism Lab** aesthetic:

- **Color Palette**: Deep slate background (#0f172a) with cyan (#06b6d4) and purple (#a855f7) accents
- **Visual Effects**: Frosted glass panels with backdrop blur, subtle glows, and gradient accents
- **Typography**: Inter (sans-serif) for general text, JetBrains Mono (monospace) for technical values
- **Interactions**: Smooth transitions, hover effects, and real-time data updates

## 🚀 Getting Started

### Installation

```bash
# Install dependencies
pnpm install

# Start development server
pnpm dev

# Build for production
pnpm build
```

### Usage

1. **Simulation Lab**: Adjust UV intensity and temperature, select experimental conditions, and click "Start" to begin the simulation
2. **Theory**: Explore detailed scientific explanations and mathematical equations
3. **Comparison**: Analyze the differences between oxygen-exposed and oxygen-free conditions

## 📊 Key Findings

- Photolysis is **significantly faster** at the air/toluene interface due to oxygen-assisted oxidation
- Refractive index changes correlate directly with molecular degradation
- The exponential decay model accurately describes temporal photolysis behavior
- Spatial profiles reveal maximum photolysis intensity near the surface, decreasing with depth

## 🛠️ Technology Stack

- **Frontend**: React 19 + TypeScript
- **Styling**: Tailwind CSS 4 + shadcn/ui
- **Visualization**: Recharts for data plotting, Canvas API for particle animations
- **Build Tool**: Vite
- **Deployment**: Manus platform

## 📚 References

El-Tawargy, A. S. (2022). Spatio-temporal photolysis rate profiles of UV254 irradiated toluene. *Scientific Reports*, 12, 12744. https://doi.org/10.1038/s41598-022-16941-6

## 📝 License

This project is part of a Physics graduation project (2026).

## 👨‍🎓 Author

Developed as an advanced computational modeling project for Physics education.

---

**Note**: This simulator provides educational insights into photochemical degradation processes. For industrial applications, consult with environmental engineering professionals.
