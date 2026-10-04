import tkinter as tk
from tkinter import filedialog, messagebox
from core import organize_folder

class OrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple File Organizer")
        self.root.geometry("500x250")
        self.root.resizable(False, False)

        # Variables
        self.selected_path = tk.StringVar()

        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        # Header Label
        header = tk.Label(self.root, text="File Organizer", font=("Arial", 16, "bold"))
        header.pack(pady=15)

        # Directory Selection Frame
        frame = tk.Frame(self.root)
        frame.pack(pady=10, fill="x", padx=20)


        self.entry = tk.Entry(frame, textvariable=self.selected_path, width=40)
        self.entry.pack(side="left", padx=5, ipady=3)

        browse_btn = tk.Button(frame, text="Browse", command=self.browse_directory)
        browse_btn.pack(side="left", padx=5)

        # Action Button
        organize_btn = tk.Button(
            self.root, 
            text="Organize Files", 
            command=self.run_organization, 
            bg="#4CAF50", 
            fg="white", 
            font=("Arial", 11, "bold"),
            padx=10,
            pady=5
        )
        organize_btn.pack(pady=20)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.selected_path.set(directory)

    def run_organization(self):
        target = self.selected_path.get()
        if not target:
            messagebox.showwarning("Warning", "Please select a directory first!")
            return

        try:
            results = organize_folder(target)
            
            # Format results message
            moved_items = [f"{cat}: {count}" for cat, count in results.items() if count > 0]
            if moved_items:
                msg = "Successfully organized:\n" + "\n".join(moved_items)
            else:
                msg = "No files needed organizing!"

            messagebox.showinfo("Success", msg)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
