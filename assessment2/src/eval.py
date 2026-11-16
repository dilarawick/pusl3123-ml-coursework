"""
 eval.py – Dummy evaluation script

Usage:
    python -m src.eval --model <model_path> --config <config.yaml>

Loads a model checkpoint (placeholder) and prints mock accuracy, precision, and recall
values. No real inference is performed.
"""

import argparse
import yaml
import json

def main():
    parser = argparse.ArgumentParser(description="Dummy evaluation script")
    parser.add_argument("--model", type=str, required=True, help="Path to model checkpoint")
    parser.add_argument("--config", type=str, required=True, help="Config YAML used for training")
    args = parser.parse_args()

    with open(args.config, "r") as f:
        cfg = yaml.safe_load(f)
    print("Loaded config:")
    print(cfg)

    print(f"[Dummy] Loading model from {args.model} (no real loading)")
    # Mock metrics
    metrics = {"accuracy": 0.78, "precision": 0.75, "recall": 0.74}
    print("[Dummy] Evaluation metrics:")
    print(metrics)
    # Save metrics to results folder (based on config name)
    import os
    variant = os.path.splitext(os.path.basename(args.config))[0]
    out_dir = os.path.join("results", variant)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"Metrics saved to {out_dir}/metrics.json")

if __name__ == "__main__":
    main()
