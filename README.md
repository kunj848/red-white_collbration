# 🚀 Red & White Collaboration - Python Projects & Practice

Welcome to the **Red & White Collaboration** repository! This repository contains a curated collection of Python programs, pattern designs, homework tasks, and graphical user interface (GUI) applications developed collaboratively.

---

## 📂 Project Structure

```text
├── pattern1.py       # 🦋 Interactive Butterfly Pattern generator
├── program1.py       # 🖥️ Tkinter GUI for Person Data Entry & Management
├── Homework3.py      # 🔢 Even Number Validator & Checker
└── README.md         # 📖 Project Documentation
```

---

## 🌟 Modules & Features

### 1. 🦋 Butterfly Pattern (`pattern1.py`)
An interactive terminal application that prints a symmetrical **Butterfly Pattern** using asterisks (`*`) and dynamic whitespace calculation.

- **How it works:**
  - Asks the user to enter the number of rows ($n$).
  - Dynamically computes stars and space padding for $2n - 1$ lines.
  - Generates the upper half ($1 \le i \le n$) and mirrors it to form the lower half.

#### Example Usage:
```bash
python pattern1.py
```

#### Sample Output:
```text
Enter rows: 5

✨ Butterfly Pattern ✨

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
```

---

### 2. 🖥️ Person Data Entry Desktop App (`program1.py`)
A modern desktop GUI application built using Python's `tkinter` and `ttk` modules.

- **Key Highlights:**
  - **Step 1:** Specify the total number of persons to record.
  - **Step 2:** Form entry fields for *First Name*, *Middle Name* (optional), and *Last Name*.
  - **Step 3:** Live listbox view displaying formatted, indexed full names.
  - **Validation:** Input validation with alerts for empty mandatory fields or invalid person counts.

#### Running the App:
```bash
python program1.py
```

---

### 3. 🔢 Even Number Checker (`Homework3.py`)
A straightforward console script to test and identify even numbers.

- Prompts the user for how many numbers they want to check.
- Loops through each entered number and determines if it is divisible by 2.

#### Running the Script:
```bash
python Homework3.py
```

---

## ⚙️ Requirements & Prerequisites

- **Python 3.8+**
- Standard Python libraries (`tkinter`, `sys`, `math` — included with Python installations).

---

## 🤝 Collaboration & Contribution

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/new-pattern`
3. Commit your changes: `git commit -m "Add new pattern"`
4. Push to your branch: `git push origin feature/new-pattern`
5. Open a Pull Request

---

*Maintained by the Red & White Collaboration Team.*
