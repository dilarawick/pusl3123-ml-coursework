"""
 inference.py – Dummy real‑time inference script

Usage:
    python -m src.inference --model <model_path>

Loads the (placeholder) model and starts a mock webcam loop that prints a random
expression label every second. No actual OpenCV or camera access is performed –
this file only demonstrates the expected command‑line interface for the final
assessment.
"""

import argparse, time, random

EXPRESSIONS = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

def main():
    parser = argparse.ArgumentParser(description="Dummy inference script")
    parser.add_argument("--model", type=str, required=True, help="Path to model checkpoint")
    args = parser.parse_args()
    print(f"[Dummy] Loading model from {args.model} (no real loading)")
    print("[Dummy] Starting mock webcam feed – press Ctrl+C to stop")
    try:
        while True:
            expr = random.choice(EXPRESSIONS)
            confidence = round(random.uniform(0.6, 0.99), 2)
            print(f"Detected: {expr} (confidence {confidence})")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[Dummy] Inference stopped.")

if __name__ == "__main__":
    main()
