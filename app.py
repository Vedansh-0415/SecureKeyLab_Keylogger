
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from event_processor import create_event_record
from local_logger import LocalLogger
from tkinter import messagebox

class SecureKeyLab:
    def __init__(self, root):
        self.root = root
        self.root.title("SecureKeyLab - Keyboard Event Lab")
        self.root.geometry("750x520")
        self.root.minsize(600, 400)

        self.monitoring = False
        self.event_count = 0
        self.logger = LocalLogger()

        title = ttk.Label(
            root,
            text="SecureKeyLab",
            font=("Segoe UI", 20, "bold")
        )
        title.pack(pady=(15, 3))

        subtitle = ttk.Label(
            root,
            text="Keyboard event monitoring in a dedicated test area"
        )
        subtitle.pack(pady=(0, 12))

        ttk.Label(
            root,
            text="Type sample text in the box below:"
        ).pack(anchor="w", padx=20)

        self.input_box = tk.Text(
            root,
            height=5,
            font=("Consolas", 12),
            wrap="word"
        )
        self.input_box.pack(fill="x", padx=20, pady=8)

        controls = ttk.Frame(root)
        controls.pack(pady=5)

        self.start_button = ttk.Button(
            controls,
            text="Start Monitoring",
            command=self.start_monitoring
        )
        self.start_button.pack(side="left", padx=5)

        self.stop_button = ttk.Button(
            controls,
            text="Stop Monitoring",
            command=self.stop_monitoring,
            state="disabled"
        )
        self.stop_button.pack(side="left", padx=5)

        self.clear_button = ttk.Button(
            controls,
            text="Clear Events",
            command=self.clear_events
        )
        self.clear_button.pack(side="left", padx=5)

        self.status = ttk.Label(
            root,
            text="Status: Stopped",
            foreground="red"
        )
        self.status.pack(pady=5)
        
        self.counter_label = ttk.Label(
            root,
            text="Events recorded: 0"
        )
        self.counter_label.pack(pady=3)

        ttk.Label(
            root,
            text="Captured events:"
        ).pack(anchor="w", padx=20, pady=(5, 0))

        columns = ("time", "key", "event")
        self.event_table = ttk.Treeview(
            root,
            columns=columns,
            show="headings",
            height=9
        )

        self.event_table.heading("time", text="Timestamp")
        self.event_table.heading("key", text="Key")
        self.event_table.heading("event", text="Event")

        self.event_table.column("time", width=150)
        self.event_table.column("key", width=150)
        self.event_table.column("event", width=250)

        self.event_table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(5, 15)
        )

        # Capture keyboard events only inside our test input.
        self.input_box.bind(
            "<KeyPress>",
            self.handle_keypress
        )

    def start_monitoring(self):
        self.monitoring = True
        self.status.config(
            text="Status: Monitoring test input",
            foreground="green"
        )
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.input_box.focus_set()

    def stop_monitoring(self):
        self.monitoring = False
        self.status.config(
            text="Status: Stopped",
            foreground="red"
        )
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def handle_keypress(self, event):
        if not self.monitoring:
            return

        record = create_event_record(event.keysym)

        try:
            self.logger.write_event(record)
        except RuntimeError as exc:
            self.stop_monitoring()
            messagebox.showerror(
                "Logging Error",
                str(exc)
            )
            return

        self.event_count += 1

        self.event_table.insert(
            "",
            "end",
            values=(
                record["timestamp"],
                record["key"],
                record["event_type"]
            )
        )

        self.counter_label.config(
            text=f"Events recorded: {self.event_count}"
        )

    def clear_events(self):
        try:
            self.logger.clear()
        except RuntimeError as exc:
            messagebox.showerror(
                "Clear Error",
                str(exc)
            )
            return

        for item in self.event_table.get_children():
            self.event_table.delete(item)

        self.event_count = 0
        self.counter_label.config(
            text="Events recorded: 0"
        )

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    window = tk.Tk()
    app = SecureKeyLab(window)
    app.run()
