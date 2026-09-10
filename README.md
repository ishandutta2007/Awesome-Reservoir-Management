# Awesome-Reservoir-Management

## Top Reservoir Management Ecosystem



**Curated List of Commercial Platforms & Open-Source GitHub Projects**  

*Focused on Reservoir Modeling, Simulation, Characterization, Geoscience Interpretation & Subsurface Workflows*  

**Last updated: September 2026**



This repository tracks notable **commercial platforms** and **open-source projects** for **Reservoir Management**. These systems support geological modeling, reservoir simulation, well performance analysis, uncertainty quantification, and integrated subsurface decision-making in oil & gas, geothermal, and CO₂ storage contexts.



**Examples** include SLB Petrel, Halliburton DecisionSpace, Emerson Roxar RMS, KAPPA Workstation, Rock Flow Dynamics tNavigator, Baker Hughes JewelSuite, S&P Global Kingdom, Paradigm SKUA-GOCAD, CMG, Geolog, Petrosys, Ikon Science, and related geoscience suites (the category leaders).



**Open-source emphasis**: Full integrated commercial geoscience and reservoir suites remain dominant for production assets. However, there is a mature and actively developed open-source ecosystem led by **OPM Flow**, **MRST**, **ResInsight**, **OpendTect**, and related tools that support industrial-strength simulation, modeling, and visualization. This section is heavily expanded with every major active project.



Contributions welcome! Open a PR to add/update entries. Keep descriptions factual and link to official sites.



## Table of Contents

- [SaaS/Hosted / Commercial Platforms](#saas-hosted--commercial-platforms)

- [Open-Source GitHub Projects](#open-source-github-projects)

- [How to Contribute](#how-to-contribute)

- [Disclaimer](#disclaimer)



## SaaS/Hosted / Commercial Platforms



- **[SLB Petrel](https://www.software.slb.com/products/petrel)**  

  Industry-leading integrated subsurface platform for seismic interpretation, geological modeling, reservoir engineering, and field development planning.



- **[Halliburton Landmark DecisionSpace](https://www.halliburton.com/)**  

  Comprehensive E&P software environment covering interpretation, earth modeling, reservoir management, and collaborative decision support.



- **[Emerson Roxar RMS](https://www.emerson.com/)**  

  Reservoir modeling and management system widely used for geological modeling, uncertainty handling, and simulation preparation.



- **[Rock Flow Dynamics tNavigator](https://rfdyn.com/)**  

  High-performance reservoir simulation and modeling platform with integrated static and dynamic workflows and growing AI/automation features.



- **[CMG (Computer Modelling Group)](https://www.cmgl.ca/)**  

  Specialized reservoir simulation suite (IMEX, GEM, STARS, etc.) for black-oil, compositional, thermal, and advanced recovery processes.



- **[KAPPA Workstation, Baker Hughes JewelSuite, S&P Global Kingdom](https://www.kappaeng.com/)**  

  Tools focused on well-test analysis, subsurface modeling, geological/geophysical interpretation, and mapping.



- **[Paradigm SKUA-GOCAD, Geolog, Petrosys, Ikon Science](https://www.aspentech.com/)**  

  Additional commercial solutions for 3D geological modeling, petrophysics, mapping, and quantitative interpretation.



- **[Other reservoir & geoscience platforms](https://www.software.slb.com/products/petrel)**  

  Enterprise and specialist tools covering geomechanics, production forecasting, and integrated asset modeling.



## Open-Source GitHub Projects



- **[OPM Flow (Open Porous Media)](https://github.com/OPM/opm-simulators)**  

  Fully implicit black-oil (and extended) reservoir simulator capable of industrial-complexity models. Supports Eclipse-format input, CO₂/H₂ storage, thermal options, and is used operationally on real assets. Core of the OPM initiative.



- **[MRST – MATLAB Reservoir Simulation Toolbox](https://github.com/SINTEF-AppliedCompSci/MRST)**  

  Free open-source toolbox for rapid prototyping and research in porous-media flow and reservoir simulation. Extensive modules for grids, discretizations, black-oil, compositional, EOR, CO₂, geomechanics, and adjoint-based optimization.



- **[ResInsight](https://github.com/OPM/ResInsight)**  

  Open-source 3D visualization and post-processing tool for reservoir models, tightly integrated with OPM and Eclipse-style simulation results.



- **[OpendTect](https://www.opendtect.org/)**  

  Open-source seismic interpretation platform with a rich plugin ecosystem for petroleum geoscience workflows (often cited alongside commercial interpretation tools).



- **[JutulDarcy.jl](https://github.com/sintefmath/JutulDarcy.jl)**  

  Julia-based, fully differentiable porous-media / reservoir simulator built on the Jutul framework, suited for research, optimization, and modern scientific computing workflows.



- **[OPM ecosystem components](https://github.com/OPM)**  

  Supporting libraries for common data structures, upscaling, tests, and Eclipse-compatible workflows that underpin OPM Flow and related tools.



- **[Other reservoir simulation & modeling projects](https://github.com/search?q=reservoir+simulation+OR+porous+media+OR+black-oil)**  

  Academic and community codes for specialized physics, unstructured grids, and experimental simulators.



- **[Visualization & post-processing tools](https://github.com/search?q=reservoir+visualization+OR+ResInsight+OR+Eclipse+viewer)**  

  Open viewers and analysis utilities for simulation output and geological models.



### Additional Strong Open-Source Options



- **Grid generation & upscaling**: OPM and MRST modules for corner-point, unstructured, and fractured-media grids.

- **Ensemble & uncertainty workflows**: Scripts and frameworks built on MRST or OPM for history matching and forecasting.

- **CO₂ / geothermal extensions**: Open modules supporting energy-transition use cases within the same simulation frameworks.

- **Python / Julia wrappers**: Community interfaces that embed OPM or MRST-style engines in modern data-science pipelines.

- **Seismic-to-simulation bridges**: Open interpretation tools (OpendTect and plugins) feeding models into open simulators.

- Fully open stacks combining OpendTect (interpretation) → geological modeling scripts → OPM Flow / MRST (simulation) → ResInsight (visualization).



**Frameworks for building custom systems**:  

The strongest open-source foundation is the **OPM** stack (**OPM Flow** + **ResInsight** + supporting libraries) for production-style black-oil and storage simulation, complemented by **MRST** for research, rapid prototyping, and advanced numerics.  

**OpendTect** provides an open entry point for seismic interpretation.  

**JutulDarcy.jl** offers a modern, differentiable alternative for optimization-heavy workflows.  

Commercial platforms (Petrel, DecisionSpace, Roxar RMS, tNavigator, CMG, Kingdom, etc.) deliver integrated geology-to-simulation environments, vendor support, and validated workflows required by many operators.  

Research groups, national laboratories, and increasingly some operators use OPM/MRST for simulation while retaining commercial tools for interpretation and geomodeling; fully open pipelines are feasible for many study and CO₂-storage applications.



## How to Contribute



1. Fork the repo.

2. Add/edit entries in `README.md` (follow existing format).

3. Include: name, link, 1–2 sentence description, and whether it's commercial/SaaS or open-source.

4. Submit PR with a short explanation.



Star the repo if you find it useful!



## Disclaimer



- This is a **community-curated** list — not exhaustive and not an endorsement.

- Reservoir management decisions have significant safety, environmental, and economic consequences. Simulation results must be properly validated, and regulatory or corporate standards for model quality and uncertainty handling apply.

- Open-source simulators (especially OPM Flow) have reached industrial maturity and are used on real assets, yet organizations remain responsible for verification, validation, and appropriate use. Evaluate licensing, support options, and fitness for purpose carefully.



---



**Made for reservoir engineers, geoscientists, simulation specialists, and subsurface digital teams.**  

Let's advance open, high-quality tools for understanding and managing the subsurface while recognizing the continuing importance of integrated commercial platforms in operational decision-making.
