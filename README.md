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

## Repository File Structure
```
.
├─ README.md                     # This file
├─ assessment1/                  # Assessment 1 code & data
│   ├─ data/
│   │   └─ train.csv            # Dummy dataset placeholder
│   ├─ src/
│   │   └─ __init__.py          # Package init (add scripts here)
│   ├─ requirements.txt          # Python dependencies for assessment 1
│   └─ SAMPLE.txt                # Example file (optional)
├─ assessment2/                  # Assessment 2 (model improvement & ablation)
│   ├─ data/
│   │   └─ train.csv            # Placeholder data for assessment 2
│   ├─ src/
│   │   ├─ __init__.py
│   │   ├─ train.py
│   │   ├─ eval.py
│   │   ├─ model.py
│   │   ├─ utils.py
│   │   └─ inference.py
│   ├─ configs/
│   │   └─ baseline.yaml
│   ├─ requirements.txt
│   ├─ README.md                 # Overview for assessment 2
│   └─ ... (notebooks, results, etc.)
├─ .gitignore                    # Git ignore patterns
└─ other project files as needed
```

The structure separates data, source code, configuration, and results for each assessment, making it easy to run experiments and generate the required reports.
