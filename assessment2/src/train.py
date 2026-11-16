"""
train.py – Dummy training script

Usage:
    python -m src.train --config <config.yaml>

The script parses a configuration file, builds the model defined in `model.py`,
creates dummy data loaders, and runs a mock training loop that prints epoch
information.  No real training is performed – this is only a placeholder to
show the expected file layout.
"""

import argparse
import yaml

def main():
    parser = argparse.ArgumentParser(description="Dummy training script")
    parser.add_argument("--config", type=str, required=True, help="Path to config YAML")
    args = parser.parse_args()

    # Load config (dummy – just prints it)
    with open(args.config, "r") as f:
        cfg = yaml.safe_load(f)
    print("Loaded config:")
    print(cfg)

    print("\n[Dummy] Building model ...")
    # Normally you would import and instantiate the model here

    print("[Dummy] Starting mock training loop …")
    for epoch in range(1, cfg.get("epochs", 1) + 1):
        print(f"Epoch {epoch}/{cfg.get('epochs', 1)} – loss: 0.123 (mock)")
    print("Training finished (dummy).")

if __name__ == "__main__":
    main()
