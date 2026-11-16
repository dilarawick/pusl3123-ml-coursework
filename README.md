# pusl3123-ml-coursework
Coursework for PUSL3123 AI & Machine Learning: CIFAR-10 MLP/CNN experiments and a real-time facial expression recognition app (FER2013) built with PyTorch and OpenCV.

## Assessment 1 – Prerequisites & Libraries

### System requirements
- Python 3.9 or newer
- Windows (tested on Windows 10/11)
- Sufficient RAM (≥8 GB recommended) for loading the FER2013 dataset

### Python libraries
Install the required packages with:

```bash
pip install -r assessment1/requirements.txt
```

The `requirements.txt` should contain (example):

```
torch
torchvision
opencv-python
pandas
numpy
pyyaml
```

These libraries provide:
- **PyTorch** – model definition and training
- **torchvision** – transforms and data utilities
- **OpenCV** – webcam capture and face detection
- **pandas / numpy** – data handling
- **PyYAML** – configuration parsing

Make sure to activate a virtual environment before installing.
