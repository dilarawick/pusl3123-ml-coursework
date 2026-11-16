# README for Assessment 2

This repository contains the code and resources for the model improvement and ablation study part of the facial expression recognition coursework.

## Structure
- `src/` – core training/evaluation/inference scripts
- `configs/` – YAML configuration files for each experiment
- `data/` – optional additional data (kept empty here)
- `results/` – generated metrics and plots
- `models/` – saved model checkpoints
- `notebooks/` – exploratory Jupyter notebooks
- `reports/` – tables/figures for the final report

## Quick start
```bash
# create a virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows PowerShell
pip install -r requirements.txt

# run baseline training
python -m src.train --config configs/baseline.yaml
```