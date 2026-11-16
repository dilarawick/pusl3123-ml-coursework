"""
utils.py – Helper utilities (dummy)

Provides placeholder functions for:
* creating a synthetic dataset loader
* computing mock metrics (accuracy, precision, recall)
* saving figures (no actual plotting)

These stubs let the rest of the code import ``utils`` without pulling in heavy
dependencies.
"""

def get_dummy_dataloader(batch_size=32, num_batches=10):
    """Return an iterator that yields dummy tensors.

    In a real project this would return a ``torch.utils.data.DataLoader``.
    Here we simply yield ``None`` objects.
    """
    for _ in range(num_batches):
        yield None

def compute_mock_metrics():
    """Return a dict with dummy metric values."""
    return {"accuracy": 0.80, "precision": 0.77, "recall": 0.76}

def save_dummy_figure(path):
    """Create an empty text file pretending to be a figure.

    This avoids requiring matplotlib while satisfying the file‑structure
    expectations.
    """
    with open(path, "w") as f:
        f.write("[Dummy figure placeholder]")
