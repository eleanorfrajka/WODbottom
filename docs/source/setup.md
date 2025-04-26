# 📦 Getting Started

This guide walks you through setting up the `verticalnn` project. It includes instructions for both terminal users and those using GitHub Desktop.

---

## Step 1: Get the Repository

You have two choices, depending on whether you're making a copy for your own use or contributing to the project.

### Option A: Clone for Your Own Use

#### a. Clone the repository to your computer
From a **terminal**:
```bash
git clone https://github.com/eleanorfrajka/verticalnn.git
```

Or using **GitHub Desktop**:
1. Navigate to [https://github.com/eleanorfrajka/verticalnn](https://github.com/eleanorfrajka/verticalnn)
2. Click the green `<> Code` button.
3. Choose **Open with GitHub Desktop**.

> 💡 You can rename the folder after cloning if you wish.

#### b. (Optional) Change the remote origin
If you want to push to your own GitHub repository, create a new repo on [GitHub.com](https://github.com) and set it as the remote:
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/new-repo-name.git
git push -u origin main
```

### Option B: Contribute to This Project
If you plan to contribute back, fork the repository first, then clone your fork. See [Git Collaboration](https://eleanorfrajka.github.io/template-project/gitcollab.html) for detailed instructions.

---

## Step 2: Set Up a Python Environment

We recommend using a clean Python environment with `venv`, `micromamba`, or `conda`. Here's how to use `venv`:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For development tools and testing
```

> ♻️ These commands install both runtime and development dependencies.

---

## Step 3: Install the Package (Editable Mode)

To use the code as an importable package:
```bash
pip install -e .
```
This installs `verticalnn` in *editable* mode, meaning changes you make to `.py` files immediately affect the environment without needing to reinstall.

---

## Step 4: Verify Installation

Run the tests to make sure everything works:
```bash
pytest
```
This runs the unit tests inside the `tests/` directory.

---

## Optional: Use GitHub Desktop Instead of Terminal

If you prefer not to use the terminal:
- Clone the repo using GitHub Desktop.
- Set up your Python environment using tools like Anaconda or built-in venv.
- Open the project folder in VSCode.
- Install the Python extension and select the correct interpreter.
- Run notebooks or Python scripts from the VSCode terminal panel.

See also [faq.md](faq.md) for common troubleshooting tips.

---

## Git Workflows

Depending on how you’re working:

- For **solo development** using `verticalnn`, see: [Solo Git Workflow](https://eleanorfrajka.github.io/template-project/gitworkflow_solo.html)
- For **collaborative development**, see: [Git Collaboration Workflow](https://eleanorfrajka.github.io/template-project/gitcollab.html)

Each guide covers typical workflows using Terminal, VSCode, and GitHub Desktop.

---

## You're All Set!

From here, you can start editing code, training neural networks, writing documentation, or expanding the testing suite. Happy coding! 🚀

