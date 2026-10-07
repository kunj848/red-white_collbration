# Instagram Account Manager & 3D Studio (Pure Python Desktop App)

A 100% native Python desktop application (No web browser, No external dependencies).

## 📸 Screenshots

| 3D Viewport & Account Creation | Duplicate Key Error Validation | Dictionary Data & Login |
| :---: | :---: | :---: |
| ![3D Studio](imag1.png) | ![Duplicate Error](image2.png) | ![Dictionary Data](imag3.png) |

---

## Core Requirements Implemented
1. **Dictionary Storage**: Credentials stored as `{username: password}` where `username` is Key and `password` is Value.
2. **Duplicate Key Prevention**: Checks `if username in user_database:` and displays prominent error messages preventing duplicate keys.
3. **3D Three.js Concept in Python**: Real-time 3D projection, depth sorting, Lambertian face shading, orbiting particles, and interactive mouse controls.

---

## 🚀 How to Run

### 1. Launch the 3D Desktop Application:
```bash
python app.py
```

#### Features in `app.py`:
- **Left Panel**: 3D Three.js Concept Viewport
  - Click & Drag with mouse to orbit/rotate the 3D Instagram emblem in real time.
  - Scroll mouse wheel to zoom in and out.
  - 50 floating 3D particle stars with depth scaling.
- **Right Panel**: Management Studio
  - **Create Account**: Validates non-empty input & checks duplicate username keys.
  - **Login**: Authenticates against dictionary values.
  - **Dictionary Data**: Live visual table and raw Python dictionary representation.

---

### 2. Launch Pure Terminal Version:
```bash
python cli_program.py
```
Interactive terminal console menu for command-line use.
