"""
Instagram Account Manager - Python Desktop 3D Edition
======================================================
Pure Python Tkinter application (Zero external web/pip dependencies required).

Core Requirements:
1. Store Instagram credentials as a Python dictionary: {username: password}.
2. Username acts as unique Key, password acts as Value.
3. If duplicate username (key) is entered, trigger a proper error message.
4. Integrated 3D Three.js Concept Engine: Real-time 3D projection, depth sorting,
   directional lighting, orbiting particles, and interactive mouse controls.
"""

import math
import random
import tkinter as tk
from tkinter import ttk, messagebox


class ThreeJsViewport(tk.Canvas):
    """
    3D Three.js Concept Engine implemented natively in Tkinter Canvas.
    - 3D Vector Geometry & Matrix Rotations
    - Real-time Perspective Projection
    - Lambertian Lighting & Depth Sorting (Painter's Algorithm)
    - 3D Instagram Emblem with Lens, Flash, and Orbit Rings
    - 60 Floating 3D Star Particles with depth scaling
    - Full Interactive Mouse Controls (Click & Drag to rotate, Scroll to zoom)
    """

    def __init__(self, parent, width=380, height=620, **kwargs):
        super().__init__(
            parent,
            width=width,
            height=height,
            bg="#07080E",
            highlightthickness=1,
            highlightbackground="#1E2235",
            **kwargs
        )
        self.w = width
        self.h = height

        # Camera & Projection setup
        self.fov = 340
        self.camera_dist = 4.5
        self.rot_x = 0.25
        self.rot_y = 0.55
        self.rot_z = 0.0
        self.auto_speed_y = 0.015
        self.is_dragging = False
        self.last_mx = 0
        self.last_my = 0

        # Normalized Directional Light Source (Top-Right-Front)
        self.light = self._norm((0.55, 0.75, -0.85))

        # 3D Instagram Body Mesh (Chamfered Prism)
        bw, bh, bd = 0.92, 0.92, 0.35
        self.base_vertices = [
            [-bw, -bh, -bd], [ bw, -bh, -bd], [ bw,  bh, -bd], [-bw,  bh, -bd],  # Front: 0..3
            [-bw, -bh,  bd], [ bw, -bh,  bd], [ bw,  bh,  bd], [-bw,  bh,  bd],  # Back:  4..7
        ]

        # 6 Polygonal Faces with Instagram Brand Gradients
        self.faces = [
            ([0, 1, 2, 3], "#E1306C", "Front"),   # Front - Magenta
            ([5, 4, 7, 6], "#833AB4", "Back"),    # Back - Deep Purple
            ([4, 5, 1, 0], "#FD1D1D", "Top"),     # Top - Red-Orange
            ([3, 2, 6, 7], "#405DE6", "Bottom"),  # Bottom - Royal Blue
            ([4, 0, 3, 7], "#5851DB", "Left"),    # Left - Indigo
            ([1, 5, 6, 2], "#FCB045", "Right"),   # Right - Gold
        ]

        # 3D Camera Lens Geometry (16-vertex circle projected on front surface)
        self.lens_ring_3d = []
        for i in range(16):
            rad = 2 * math.pi * i / 16
            self.lens_ring_3d.append([0.42 * math.cos(rad), 0.42 * math.sin(rad), -bd - 0.02])

        self.lens_inner_3d = []
        for i in range(16):
            rad = 2 * math.pi * i / 16
            self.lens_inner_3d.append([0.24 * math.cos(rad), 0.24 * math.sin(rad), -bd - 0.04])

        self.flash_dot = [0.55, -0.55, -bd - 0.02]

        # 3D Orbiting Wireframe Rings (Gyroscopic 3D Accents)
        self.ring1_pts = []
        for i in range(24):
            rad = 2 * math.pi * i / 24
            self.ring1_pts.append([1.45 * math.cos(rad), 0.35 * math.sin(rad), 1.45 * math.sin(rad)])

        # 3D Star Particles Field
        random.seed(1337)
        self.particles = []
        for _ in range(50):
            self.particles.append([
                random.uniform(-2.5, 2.5),
                random.uniform(-2.8, 2.8),
                random.uniform(-2.5, 2.5),
                random.choice(["#E1306C", "#FD1D1D", "#FCB045", "#833AB4", "#FFFFFF"])
            ])

        # Mouse Event Listeners (Three.js Orbit Controls)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<B1-Motion>", self._on_drag)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<MouseWheel>", self._on_zoom)

        # Start animation frame loop (~45-50 FPS)
        self._loop()

    def _norm(self, v):
        mag = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
        return (v[0]/mag, v[1]/mag, v[2]/mag) if mag > 1e-6 else (0, 0, 1)

    def _on_press(self, e):
        self.is_dragging = True
        self.last_mx, self.last_my = e.x, e.y

    def _on_drag(self, e):
        if self.is_dragging:
            dx = e.x - self.last_mx
            dy = e.y - self.last_my
            self.rot_y += dx * 0.012
            self.rot_x += dy * 0.012
            self.last_mx, self.last_my = e.x, e.y

    def _on_release(self, _):
        self.is_dragging = False

    def _on_zoom(self, e):
        # Mouse wheel zoom in/out
        if e.delta > 0:
            self.camera_dist = max(2.6, self.camera_dist - 0.25)
        else:
            self.camera_dist = min(7.5, self.camera_dist + 0.25)

    def _rot(self, pt):
        x, y, z = pt
        # Pitch (X axis)
        cx, sx = math.cos(self.rot_x), math.sin(self.rot_x)
        y1 = y * cx - z * sx
        z1 = y * sx + z * cx
        # Yaw (Y axis)
        cy, sy = math.cos(self.rot_y), math.sin(self.rot_y)
        x2 = x * cy + z1 * sy
        z2 = -x * sy + z1 * cy
        # Roll (Z axis)
        cz, sz = math.cos(self.rot_z), math.sin(self.rot_z)
        x3 = x2 * cz - y1 * sz
        y3 = x2 * sz + y1 * cz
        return x3, y3, z2

    def _proj(self, x, y, z):
        dist = z + self.camera_dist
        if dist <= 0.1:
            dist = 0.1
        f = self.fov / dist
        sx = self.w / 2 + x * f
        sy = self.h / 2 + y * f
        return sx, sy, f

    def _shade(self, hex_c, light_factor):
        lf = max(0.28, min(1.25, light_factor))
        hex_c = hex_c.lstrip("#")
        r = min(255, int(int(hex_c[0:2], 16) * lf))
        g = min(255, int(int(hex_c[2:4], 16) * lf))
        b = min(255, int(int(hex_c[4:6], 16) * lf))
        return f"#{r:02x}{g:02x}{b:02x}"

    def _loop(self):
        if not self.is_dragging:
            self.rot_y += self.auto_speed_y
            self.rot_x = 0.22 + 0.14 * math.sin(self.rot_y * 0.6)

        self.delete("all")
        cx, cy = self.w / 2, self.h / 2

        # 1. Background Nebula Gradients
        self.create_oval(cx - 150, cy - 150, cx + 150, cy + 150, fill="#121020", outline="")
        self.create_oval(cx - 90, cy - 90, cx + 90, cy + 90, fill="#181329", outline="")

        # 2. Render 3D Floating Particles
        for p in self.particles:
            rx, ry, rz = self._rot((p[0], p[1], p[2]))
            sx, sy, scale = self._proj(rx, ry, rz)
            sz = max(1.0, min(3.5, scale * 0.035))
            self.create_oval(sx - sz, sy - sz, sx + sz, sy + sz, fill=p[3], outline="")

        # 3. Orbiting Gyro Ring (Wireframe 3D)
        ring_2d = []
        for pt in self.ring1_pts:
            rx, ry, rz = self._rot(pt)
            sx, sy, _ = self._proj(rx, ry, rz)
            ring_2d.extend([sx, sy])
        if len(ring_2d) >= 4:
            self.create_polygon(ring_2d, fill="", outline="#833AB4", width=1, dash=(3, 3))

        # 4. Transform Cube Vertices
        trans_v = [self._rot(v) for v in self.base_vertices]

        # 5. Face Depth Sorting & Normal Lighting
        render_queue = []
        for indices, col, name in self.faces:
            p0, p1, p2 = trans_v[indices[0]], trans_v[indices[1]], trans_v[indices[2]]
            vA = (p1[0] - p0[0], p1[1] - p0[1], p1[2] - p0[2])
            vB = (p2[0] - p0[0], p2[1] - p0[1], p2[2] - p0[2])
            normal = (
                vA[1] * vB[2] - vA[2] * vB[1],
                vA[2] * vB[0] - vA[0] * vB[2],
                vA[0] * vB[1] - vA[1] * vB[0]
            )
            norm = self._norm(normal)

            # Backface culling
            if norm[2] > 0.05:
                continue

            # Lambertian Shading
            dot = -(norm[0] * self.light[0] + norm[1] * self.light[1] + norm[2] * self.light[2])
            intensity = 0.5 + 0.65 * max(0.0, dot)
            shaded_color = self._shade(col, intensity)
            avg_z = sum(trans_v[i][2] for i in indices) / 4.0
            render_queue.append((avg_z, indices, shaded_color, name))

        render_queue.sort(key=lambda item: item[0], reverse=True)

        # Draw faces
        front_seen = False
        for _, indices, fcol, name in render_queue:
            pts = []
            for i in indices:
                sx, sy, _ = self._proj(*trans_v[i])
                pts.extend([sx, sy])
            self.create_polygon(pts, fill=fcol, outline="#0E101A", width=2, joinstyle=tk.ROUND)
            if name == "Front":
                front_seen = True

        # 6. Lens & Flash details on Front Face
        if front_seen:
            # Outer lens
            lens_pts = []
            for pt in self.lens_ring_3d:
                rx, ry, rz = self._rot(pt)
                sx, sy, _ = self._proj(rx, ry, rz)
                lens_pts.extend([sx, sy])
            if len(lens_pts) >= 6:
                self.create_polygon(lens_pts, fill="#161524", outline="#FFFFFF", width=2)

            # Inner lens aperture
            inner_pts = []
            for pt in self.lens_inner_3d:
                rx, ry, rz = self._rot(pt)
                sx, sy, _ = self._proj(rx, ry, rz)
                inner_pts.extend([sx, sy])
            if len(inner_pts) >= 6:
                self.create_polygon(inner_pts, fill="#FD1D1D", outline="#FCB045", width=1.5)

            # Flash dot
            frx, fry, frz = self._rot(self.flash_dot)
            fsx, fsy, fscale = self._proj(frx, fry, frz)
            frad = max(2.5, fscale * 0.038)
            self.create_oval(fsx - frad, fsy - frad, fsx + frad, fsy + frad, fill="#FFFFFF", outline="#FCB045")

        # 7. 3D Viewport HUD
        self.create_text(
            16, 20,
            text="THREE.JS 3D ENGINE",
            anchor="w",
            font=("Segoe UI", 9, "bold"),
            fill="#FCB045"
        )
        self.create_text(
            16, 38,
            text="Interactive WebGL Simulation",
            anchor="w",
            font=("Segoe UI", 8),
            fill="#8088A8"
        )
        self.create_text(
            self.w - 16, self.h - 22,
            text="DRAG: Orbit 3D  |  SCROLL: Zoom",
            anchor="e",
            font=("Consolas", 8),
            fill="#717894"
        )

        self.after(22, self._loop)


class InstagramAuthApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Instagram Account Manager - 3D Python Studio")
        self.root.geometry("980x660")
        self.root.minsize(920, 620)
        self.root.configure(bg="#08090E")

        # Core Data Model: Python Dictionary {username: password}
        self.user_database = {}

        # Visual Design Palette
        self.bg_color = "#08090E"
        self.card_bg = "#11131C"
        self.card_border = "#202538"
        self.accent_pink = "#E1306C"
        self.accent_purple = "#833AB4"
        self.accent_orange = "#FD1D1D"
        self.accent_gold = "#FCB045"
        self.text_primary = "#FFFFFF"
        self.text_secondary = "#8F96B2"
        self.input_bg = "#171A27"
        self.input_border = "#272C42"
        self.success_color = "#00E676"
        self.error_color = "#FF3366"

        self._setup_theme()
        self._build_layout()

    def _setup_theme(self):
        style = ttk.Style()
        style.theme_use("clam")

        # Notebook tab styling
        style.configure("TNotebook", background=self.card_bg, borderwidth=0)
        style.configure(
            "TNotebook.Tab",
            background="#161826",
            foreground=self.text_secondary,
            padding=[16, 9],
            font=("Segoe UI", 9, "bold"),
            borderwidth=0
        )
        style.map(
            "TNotebook.Tab",
            background=[("selected", self.accent_pink)],
            foreground=[("selected", "#FFFFFF")]
        )

        # Accounts Treeview
        style.configure(
            "Treeview",
            background=self.input_bg,
            foreground=self.text_primary,
            fieldbackground=self.input_bg,
            rowheight=32,
            font=("Segoe UI", 9),
            borderwidth=0
        )
        style.configure(
            "Treeview.Heading",
            background="#1C2033",
            foreground="#FFFFFF",
            font=("Segoe UI", 9, "bold"),
            borderwidth=0
        )
        style.map(
            "Treeview",
            background=[("selected", self.accent_purple)],
            foreground=[("selected", "#FFFFFF")]
        )

    def _build_layout(self):
        # Master horizontal layout: Left = 3D Three.js Viewport, Right = Application Card
        master_frame = tk.Frame(self.root, bg=self.bg_color)
        master_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # ================= LEFT: 3D THREE.JS VIEWPORT =================
        left_panel = tk.Frame(master_frame, bg=self.bg_color, width=380)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 16))

        self.viewport_3d = ThreeJsViewport(left_panel, width=380, height=620)
        self.viewport_3d.pack(fill=tk.BOTH, expand=True)

        # ================= RIGHT: INTERACTIVE CONTROL PANEL =================
        right_panel = tk.Frame(
            master_frame,
            bg=self.card_bg,
            highlightthickness=1,
            highlightbackground=self.card_border
        )
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Header with Gradient Title
        header = tk.Frame(right_panel, bg=self.card_bg, padx=28, pady=20)
        header.pack(fill=tk.X)

        badge_row = tk.Frame(header, bg=self.card_bg)
        badge_row.pack(anchor="w")

        tk.Label(
            badge_row,
            text="● PYTHON DICTIONARY ENGINE",
            font=("Segoe UI", 8, "bold"),
            fg=self.accent_gold,
            bg=self.card_bg
        ).pack(side=tk.LEFT)

        tk.Label(
            header,
            text="Instagram Account Manager",
            font=("Segoe UI", 20, "bold"),
            fg=self.text_primary,
            bg=self.card_bg
        ).pack(anchor="w", pady=(3, 2))

        tk.Label(
            header,
            text="Key: Username  |  Value: Password  |  Duplicate Key Protection",
            font=("Segoe UI", 9),
            fg=self.text_secondary,
            bg=self.card_bg
        ).pack(anchor="w")

        # Tabs: Register, Login, Dictionary
        self.notebook = ttk.Notebook(right_panel)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=24, pady=(0, 14))

        # Tab 1: Create Account
        self.tab_reg = tk.Frame(self.notebook, bg=self.card_bg)
        self.notebook.add(self.tab_reg, text="  Create Account  ")
        self._build_register_tab()

        # Tab 2: Login
        self.tab_login = tk.Frame(self.notebook, bg=self.card_bg)
        self.notebook.add(self.tab_login, text="  Login  ")
        self._build_login_tab()

        # Tab 3: Dictionary Explorer
        self.tab_dict = tk.Frame(self.notebook, bg=self.card_bg)
        self.notebook.add(self.tab_dict, text="  Dictionary Data  ")
        self._build_dict_tab()

        # Bottom Status Bar
        status_bar = tk.Frame(right_panel, bg="#0D0F17", padx=24, pady=10)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.status_label = tk.Label(
            status_bar,
            text="Ready. 0 accounts registered in dictionary.",
            font=("Segoe UI", 9),
            fg=self.text_secondary,
            bg="#0D0F17"
        )
        self.status_label.pack(side=tk.LEFT)

    # ------------------ TAB 1: CREATE ACCOUNT ------------------
    def _build_register_tab(self):
        container = tk.Frame(self.tab_reg, bg=self.card_bg, padx=20, pady=16)
        container.pack(fill=tk.BOTH, expand=True)

        # Username Field
        tk.Label(
            container,
            text="Username (Dictionary Key):",
            font=("Segoe UI", 9, "bold"),
            fg=self.text_primary,
            bg=self.card_bg
        ).pack(anchor="w", pady=(0, 4))

        self.reg_user_var = tk.StringVar()
        reg_user_entry = tk.Entry(
            container,
            textvariable=self.reg_user_var,
            font=("Segoe UI", 11),
            bg=self.input_bg,
            fg=self.text_primary,
            insertbackground="#FFFFFF",
            relief=tk.FLAT,
            bd=7,
            highlightthickness=1,
            highlightbackground=self.input_border,
            highlightcolor=self.accent_pink
        )
        reg_user_entry.pack(fill=tk.X, pady=(0, 12))

        # Password Field
        tk.Label(
            container,
            text="Password (Dictionary Value):",
            font=("Segoe UI", 9, "bold"),
            fg=self.text_primary,
            bg=self.card_bg
        ).pack(anchor="w", pady=(0, 4))

        self.reg_pass_var = tk.StringVar()
        self.reg_pass_entry = tk.Entry(
            container,
            textvariable=self.reg_pass_var,
            font=("Segoe UI", 11),
            bg=self.input_bg,
            fg=self.text_primary,
            insertbackground="#FFFFFF",
            show="*",
            relief=tk.FLAT,
            bd=7,
            highlightthickness=1,
            highlightbackground=self.input_border,
            highlightcolor=self.accent_pink
        )
        self.reg_pass_entry.pack(fill=tk.X, pady=(0, 6))

        # Show password toggle
        self.reg_show_var = tk.BooleanVar(value=False)
        toggle_cb = tk.Checkbutton(
            container,
            text="Show Password",
            variable=self.reg_show_var,
            command=lambda: self._toggle_show(self.reg_pass_entry, self.reg_show_var),
            font=("Segoe UI", 8),
            fg=self.text_secondary,
            bg=self.card_bg,
            selectcolor=self.input_bg,
            activebackground=self.card_bg,
            activeforeground=self.text_primary
        )
        toggle_cb.pack(anchor="w", pady=(0, 14))

        # Create Account Button
        create_btn = tk.Button(
            container,
            text="Create Account",
            command=self.create_account,
            font=("Segoe UI", 10, "bold"),
            bg=self.accent_pink,
            fg="#FFFFFF",
            activebackground=self.accent_purple,
            activeforeground="#FFFFFF",
            relief=tk.FLAT,
            cursor="hand2",
            pady=9
        )
        create_btn.pack(fill=tk.X, pady=(0, 12))

        # Dynamic Notification Box
        self.reg_banner = tk.Label(
            container,
            text="💡 Enter username and password to store into dictionary.",
            font=("Segoe UI", 9),
            bg="#161824",
            fg=self.text_secondary,
            relief=tk.FLAT,
            padx=12,
            pady=10,
            wraplength=460,
            justify=tk.LEFT
        )
        self.reg_banner.pack(fill=tk.X, pady=(4, 0))

    # ------------------ TAB 2: LOGIN ------------------
    def _build_login_tab(self):
        container = tk.Frame(self.tab_login, bg=self.card_bg, padx=20, pady=16)
        container.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            container,
            text="Username:",
            font=("Segoe UI", 9, "bold"),
            fg=self.text_primary,
            bg=self.card_bg
        ).pack(anchor="w", pady=(0, 4))

        self.login_user_var = tk.StringVar()
        login_user_entry = tk.Entry(
            container,
            textvariable=self.login_user_var,
            font=("Segoe UI", 11),
            bg=self.input_bg,
            fg=self.text_primary,
            insertbackground="#FFFFFF",
            relief=tk.FLAT,
            bd=7,
            highlightthickness=1,
            highlightbackground=self.input_border,
            highlightcolor="#3897F0"
        )
        login_user_entry.pack(fill=tk.X, pady=(0, 12))

        tk.Label(
            container,
            text="Password:",
            font=("Segoe UI", 9, "bold"),
            fg=self.text_primary,
            bg=self.card_bg
        ).pack(anchor="w", pady=(0, 4))

        self.login_pass_var = tk.StringVar()
        self.login_pass_entry = tk.Entry(
            container,
            textvariable=self.login_pass_var,
            font=("Segoe UI", 11),
            bg=self.input_bg,
            fg=self.text_primary,
            insertbackground="#FFFFFF",
            show="*",
            relief=tk.FLAT,
            bd=7,
            highlightthickness=1,
            highlightbackground=self.input_border,
            highlightcolor="#3897F0"
        )
        self.login_pass_entry.pack(fill=tk.X, pady=(0, 6))

        self.login_show_var = tk.BooleanVar(value=False)
        toggle_cb = tk.Checkbutton(
            container,
            text="Show Password",
            variable=self.login_show_var,
            command=lambda: self._toggle_show(self.login_pass_entry, self.login_show_var),
            font=("Segoe UI", 8),
            fg=self.text_secondary,
            bg=self.card_bg,
            selectcolor=self.input_bg,
            activebackground=self.card_bg,
            activeforeground=self.text_primary
        )
        toggle_cb.pack(anchor="w", pady=(0, 14))

        login_btn = tk.Button(
            container,
            text="Log In",
            command=self.login_account,
            font=("Segoe UI", 10, "bold"),
            bg="#3897F0",
            fg="#FFFFFF",
            activebackground="#2678C8",
            activeforeground="#FFFFFF",
            relief=tk.FLAT,
            cursor="hand2",
            pady=8
        )
        login_btn.pack(fill=tk.X, pady=(0, 12))

        self.login_banner = tk.Label(
            container,
            text="Authenticate username and password against dictionary.",
            font=("Segoe UI", 9),
            bg="#161824",
            fg=self.text_secondary,
            relief=tk.FLAT,
            padx=12,
            pady=10,
            wraplength=460,
            justify=tk.LEFT
        )
        self.login_banner.pack(fill=tk.X, pady=(4, 0))

    # ------------------ TAB 3: DICTIONARY DATA EXPLORER ------------------
    def _build_dict_tab(self):
        container = tk.Frame(self.tab_dict, bg=self.card_bg, padx=16, pady=12)
        container.pack(fill=tk.BOTH, expand=True)

        header_box = tk.Frame(container, bg=self.card_bg)
        header_box.pack(fill=tk.X, pady=(0, 6))

        tk.Label(
            header_box,
            text="Stored Accounts [Key : Value]",
            font=("Segoe UI", 9, "bold"),
            fg=self.text_primary,
            bg=self.card_bg
        ).pack(side=tk.LEFT)

        clear_btn = tk.Button(
            header_box,
            text="Clear Dictionary",
            command=self.clear_all,
            font=("Segoe UI", 8, "bold"),
            bg="#2A161E",
            fg=self.error_color,
            activebackground="#3D1C28",
            activeforeground="#FFFFFF",
            relief=tk.FLAT,
            cursor="hand2",
            padx=8
        )
        clear_btn.pack(side=tk.RIGHT)

        # Treeview Table
        cols = ("Username (Key)", "Password (Value)")
        self.tree = ttk.Treeview(container, columns=cols, show="headings", height=6)
        self.tree.heading("Username (Key)", text="Username [Dict Key]")
        self.tree.heading("Password (Value)", text="Password [Dict Value]")
        self.tree.column("Username (Key)", width=210, anchor="w")
        self.tree.column("Password (Value)", width=210, anchor="w")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=(0, 8))

        # Raw Dictionary String Box
        tk.Label(
            container,
            text="Raw Python Dictionary State:",
            font=("Consolas", 8, "bold"),
            fg=self.accent_gold,
            bg=self.card_bg
        ).pack(anchor="w", pady=(0, 3))

        self.dict_text = tk.Text(
            container,
            height=3,
            bg="#0B0D14",
            fg="#00E676",
            font=("Consolas", 9),
            relief=tk.FLAT,
            bd=6,
            highlightthickness=1,
            highlightbackground="#1E2336"
        )
        self.dict_text.insert("1.0", "{}")
        self.dict_text.configure(state="disabled")
        self.dict_text.pack(fill=tk.X)

    # ------------------ METHODS & CORE LOGIC ------------------
    def _toggle_show(self, entry, var):
        entry.config(show="" if var.get() else "*")

    def _refresh_ui(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for u, p in self.user_database.items():
            masked = "•" * len(p)
            self.tree.insert("", tk.END, values=(f"@{u}", f"{masked} ({p})"))

        self.dict_text.configure(state="normal")
        self.dict_text.delete("1.0", tk.END)
        self.dict_text.insert("1.0", repr(self.user_database))
        self.dict_text.configure(state="disabled")

        count = len(self.user_database)
        self.status_label.config(text=f"Ready. {count} accounts stored in dictionary.")


    def clear_all(self):
        if not self.user_database:
            return
        if messagebox.askyesno("Confirm Clear", "Clear all accounts from dictionary?"):
            self.user_database.clear()
            self._refresh_ui()
            self.reg_banner.config(
                text="🗑️ Dictionary cleared.",
                fg=self.text_secondary,
                bg="#161824"
            )

    def create_account(self):
        """
        1. Takes username and password.
        2. Validates duplicate username in dictionary.
        3. If duplicate, displays proper error message.
        4. If new, stores username as key and password as value.
        """
        username = self.reg_user_var.get().strip()
        password = self.reg_pass_var.get().strip()

        if not username or not password:
            self.reg_banner.config(
                text="⚠️ Please enter both username and password!",
                fg="#FFAA00",
                bg="#261E10"
            )
            messagebox.showwarning("Input Missing", "Username and password cannot be empty.")
            return

        # CRITICAL TASK: Duplicate Key Detection in Dictionary
        if username in self.user_database:
            err_msg = f"❌ Error: Username '{username}' already exists!\nDuplicate keys are not allowed in Python dictionaries."
            self.reg_banner.config(
                text=err_msg,
                fg=self.error_color,
                bg="#2A1018"
            )
            # Display prominent popup error dialog
            messagebox.showerror(
                "Duplicate Username Error",
                f"The username '{username}' is already taken!\n\n"
                f"In Python dictionaries, keys must be unique.\n"
                f"Please choose a different username."
            )
            return

        # Store username as key and password as value
        self.user_database[username] = password

        # Success message
        success_msg = f"✅ Account successfully created for @{username}!\nStored as key '{username}' in user dictionary."
        self.reg_banner.config(
            text=success_msg,
            fg=self.success_color,
            bg="#0E2319"
        )
        messagebox.showinfo(
            "Account Created",
            f"Success! Account for @{username} has been registered."
        )

        self.reg_user_var.set("")
        self.reg_pass_var.set("")
        self._refresh_ui()

    def login_account(self):
        """
        Validates login against dictionary keys and values.
        """
        username = self.login_user_var.get().strip()
        password = self.login_pass_var.get().strip()

        if not username or not password:
            self.login_banner.config(
                text="⚠️ Please enter both username and password.",
                fg="#FFAA00",
                bg="#261E10"
            )
            messagebox.showwarning("Input Missing", "Please fill in all fields.")
            return

        if username not in self.user_database:
            msg = f"Username '{username}' not found. Please create an account first."
            self.login_banner.config(
                text=f"❌ {msg}",
                fg=self.error_color,
                bg="#2A1018"
            )
            messagebox.showerror("User Not Found", msg)
            return

        if self.user_database[username] != password:
            msg = "Incorrect password! Please try again."
            self.login_banner.config(
                text=f"❌ {msg}",
                fg=self.error_color,
                bg="#2A1018"
            )
            messagebox.showerror("Authentication Failed", msg)
            return

        msg = f"Login successful! Welcome back, @{username}."
        self.login_banner.config(
            text=f"✅ {msg}",
            fg=self.success_color,
            bg="#0E2319"
        )
        messagebox.showinfo("Welcome", f"Welcome back, @{username}!")

        self.login_user_var.set("")
        self.login_pass_var.set("")


def main():
    root = tk.Tk()
    app = InstagramAuthApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
