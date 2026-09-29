import tkinter as tk
from tkinter import messagebox, ttk

class PersonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Person Data Entry")
        self.root.geometry("450x520")
        self.root.resizable(False, False)

        self.total_persons = 0
        self.current_count = 1
        self.records = []

        self._build_ui()

    def _build_ui(self):
        # Setup Section: Total count
        self.setup_frame = ttk.LabelFrame(self.root, text="Step 1: Number of Persons", padding=10)
        self.setup_frame.pack(fill="x", padx=15, pady=10)

        ttk.Label(self.setup_frame, text="How many persons?").pack(side="left", padx=5)
        self.entry_total = ttk.Entry(self.setup_frame, width=8)
        self.entry_total.pack(side="left", padx=5)
        self.btn_start = ttk.Button(self.setup_frame, text="Start", command=self.start_entry)
        self.btn_start.pack(side="left", padx=5)

        # Input Section: Person details
        self.form_frame = ttk.LabelFrame(self.root, text="Step 2: Enter Details", padding=10)
        self.form_frame.pack(fill="x", padx=15, pady=5)

        self.lbl_person_no = ttk.Label(self.form_frame, text="Person 1", font=("Segoe UI", 10, "bold"))
        self.lbl_person_no.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")

        ttk.Label(self.form_frame, text="First Name:").grid(row=1, column=0, sticky="w", pady=4)
        self.entry_first = ttk.Entry(self.form_frame, width=28)
        self.entry_first.grid(row=1, column=1, pady=4, padx=5)

        ttk.Label(self.form_frame, text="Middle Name (optional):").grid(row=2, column=0, sticky="w", pady=4)
        self.entry_middle = ttk.Entry(self.form_frame, width=28)
        self.entry_middle.grid(row=2, column=1, pady=4, padx=5)

        ttk.Label(self.form_frame, text="Last Name:").grid(row=3, column=0, sticky="w", pady=4)
        self.entry_last = ttk.Entry(self.form_frame, width=28)
        self.entry_last.grid(row=3, column=1, pady=4, padx=5)

        self.btn_add = ttk.Button(self.form_frame, text="Submit Person", command=self.add_person, state="disabled")
        self.btn_add.grid(row=4, column=0, columnspan=2, pady=10)

        # Results Section
        self.display_frame = ttk.LabelFrame(self.root, text="Saved Persons", padding=10)
        self.display_frame.pack(fill="both", expand=True, padx=15, pady=10)

        self.listbox = tk.Listbox(self.display_frame, height=8)
        self.listbox.pack(fill="both", expand=True)

    def start_entry(self):
        val = self.entry_total.get().strip()
        if not val.isdigit() or int(val) <= 0:
            messagebox.showerror("Invalid Input", "Please enter a valid positive number.")
            return

        self.total_persons = int(val)
        self.current_count = 1
        self.records.clear()
        self.listbox.delete(0, tk.END)

        self.btn_start.config(state="disabled")
        self.entry_total.config(state="disabled")
        self.btn_add.config(state="normal")
        self.lbl_person_no.config(text=f"Person {self.current_count} of {self.total_persons}")
        self.entry_first.focus_set()

    def add_person(self):
        first = self.entry_first.get().strip()
        middle = self.entry_middle.get().strip()
        last = self.entry_last.get().strip()

        if not first or not last:
            messagebox.showwarning("Missing Information", "First Name and Last Name are required.")
            return

        if middle == "":
            full_name = f"{first} {last}"
        else:
            full_name = f"{first} {middle} {last}"

        self.records.append(full_name)
        self.listbox.insert(tk.END, f"{self.current_count}. {full_name}")

        # Clear input fields
        self.entry_first.delete(0, tk.END)
        self.entry_middle.delete(0, tk.END)
        self.entry_last.delete(0, tk.END)

        self.current_count += 1
        if self.current_count <= self.total_persons:
            self.lbl_person_no.config(text=f"Person {self.current_count} of {self.total_persons}")
            self.entry_first.focus_set()
        else:
            messagebox.showinfo("Completed", f"Successfully entered data for all {self.total_persons} person(s).")
            self.btn_add.config(state="disabled")
            self.btn_start.config(state="normal")
            self.entry_total.config(state="normal")
            self.lbl_person_no.config(text="Entry Complete")


if __name__ == "__main__":
    root = tk.Tk()
    app = PersonApp(root)
    root.mainloop()
