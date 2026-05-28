# Inflation Monitoring Dashboard (Argentina)

An interactive data visualization application built in Python to monitor and analyze Argentine macroeconomic inflation metrics (IPC) using official datasets.

*Note: This project is currently under active development (Work in Progress).*

## 🛠️ Tech Stack & Core Concepts
- **Language:** Python
- **Libraries:** Pandas (Data Cleaning & Processing), Streamlit (Web Dashboard Framework).
- **Data Engineering:** Automated ingestion and pipeline structuring of INDEC/official datasets.
- **Analytics:** Calculation of monthly, inter-annual, and accumulated inflation metrics.

## 📂 Current Features (Implemented)
- **Data Pipeline:** Automated parsing, cleaning, and structural transformation of raw inflation datasets using Pandas.
- **Metric Computation:** Core logic to accurately calculate and aggregate inflation trends over time.
- **Interactive Framework:** Basic Streamlit dashboard architecture setup for data rendering.

## 🚀 Future Features & Roadmap (In Progress)
- [ ] Implement dynamic data fetching directly from external APIs (DolarAPI / INDEC).
- [ ] Add advanced interactive charts and visual filtering by region/category.
- [ ] Optimize caching mechanisms to improve dashboard loading speeds.


curl basico https://apis.datos.gob.ar/series/api/search/?q=salarios
