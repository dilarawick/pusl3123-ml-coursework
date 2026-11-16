"""
model.py – Dummy model definitions

Provides a simple PyTorch-like placeholder class `BaseCNN` that could be extended
with dropout, batch‑norm, etc. No real torch dependency is imported – this file
only contains illustrative docstrings and a fake `forward` method.
"""

class BaseCNN:
    """Placeholder CNN model.

    In a real implementation this would inherit from `torch.nn.Module` and
    define `conv`, `relu`, `pool`, and `fc` layers. Here we only store the
    configuration dictionary for demonstration purposes.
    """

    def __init__(self, config=None):
        self.config = config or {}
        print("[Dummy Model] Initialized with config:", self.config)

    def forward(self, x):  # pragma: no cover
        """Fake forward pass – returns the input unchanged."""
        return x
