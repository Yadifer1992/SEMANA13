import tkinter as tk
from tkinter import ttk, messagebox

class AppGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación GUI Básica - Tarea")
        self.geometry("600x400")
        self.configure(padx=10, pady=10)

        # contador para IDs
        self.counter = 0

        # Crear los componentes
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta de título
        lbl_title = tk.Label(self, text="Gestor de Información", font=("Arial", 16, "bold"))
        lbl_title.pack(pady=10)

        # Frame de entrada
        frame_input = tk.Frame(self)
        frame_input.pack(fill="x", pady=5)

        self.entry = tk.Entry(frame_input, width=40)
        self.entry.pack(side="left", padx=5, pady=5)
        self.entry.bind("<Return>", lambda e: self.add_item())  # Enter también agrega

        btn_add = tk.Button(frame_input, text="Agregar", command=self.add_item)
        btn_add.pack(side="left", padx=5)

        btn_clear = tk.Button(frame_input, text="Limpiar", command=self.clear_action)
        btn_clear.pack(side="left", padx=5)

        # Tabla (Treeview)
        columns = ("ID", "Texto")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Texto", text="Texto")
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Texto", width=450, anchor="w")
        self.tree.pack(expand=True, fill="both", pady=10)

        # Scrollbar vertical para la tabla
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def add_item(self):
        """Agrega un ítem a la tabla"""
        text = self.entry.get().strip()
        if not text:
            messagebox.showwarning("Campo vacío", "Debes escribir algo antes de agregar.")
            return
        self.counter += 1
        self.tree.insert("", "end", values=(self.counter, text))
        self.entry.delete(0, tk.END)

    def clear_action(self):
        """Borra la selección o el campo de texto"""
        selected = self.tree.selection()
        if selected:
            for item in selected:
                self.tree.delete(item)
        else:
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    app = AppGUI()
    app.mainloop()