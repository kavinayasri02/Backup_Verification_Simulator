import customtkinter as ctk
from tkinter import filedialog
from datetime import datetime
import os

# =====================================
# APP SETTINGS
# =====================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Enterprise Backup Verification System")
app.geometry("1400x800")

original_file = ""
backup_file = ""

# =====================================
# FUNCTIONS
# =====================================

def upload_original():
    global original_file

    file = filedialog.askopenfilename(
        title="Select Original File"
    )

    if file:
        original_file = file
        original_label.configure(
            text=f"Original: {os.path.basename(file)}"
        )


def upload_backup():
    global backup_file

    file = filedialog.askopenfilename(
        title="Select Backup File"
    )

    if file:
        backup_file = file
        backup_label.configure(
            text=f"Backup: {os.path.basename(file)}"
        )


def verify_backup():

    if not original_file or not backup_file:

        result_label.configure(
            text="⚠ Upload Both Files First"
        )

        return

    original_size = os.path.getsize(original_file)
    backup_size = os.path.getsize(backup_file)

    if original_size == backup_size:

        result_label.configure(
            text="🟢 MATCHED"
        )

        status.configure(
            text="🟢 SYSTEM HEALTHY"
        )

        progress.set(1)

    else:

        result_label.configure(
            text="🔴 MISMATCH FOUND"
        )

        status.configure(
            text="🔴 ATTENTION REQUIRED"
        )

        progress.set(0.5)


def clear_content():
    for widget in content.winfo_children():
        widget.destroy()


# =====================================
# PAGES
# =====================================

def show_dashboard():

    clear_content()

    frame = ctk.CTkFrame(content)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    ctk.CTkLabel(
        frame,
        text="🏠 Dashboard Overview",
        font=("Arial", 28, "bold")
    ).pack(pady=20)

    ctk.CTkLabel(
        frame,
        text="Backup Monitoring Service Running",
        font=("Arial", 18)
    ).pack(pady=10)

    dashboard_progress = ctk.CTkProgressBar(
        frame,
        width=600
    )

    dashboard_progress.pack(pady=20)
    dashboard_progress.set(0.97)

    ctk.CTkLabel(
        frame,
        text="Current System Uptime : 99.9%",
        font=("Arial", 16)
    ).pack(pady=10)


def show_backups():

    clear_content()

    frame = ctk.CTkFrame(content)
    frame.pack(fill="both", expand=True)

    ctk.CTkLabel(
        frame,
        text="📁 Backup Repository",
        font=("Arial", 28, "bold")
    ).pack(pady=20)

    box = ctk.CTkTextbox(frame)
    box.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    if original_file:
        box.insert(
            "end",
            f"Original File:\n{original_file}\n\n"
        )

    if backup_file:
        box.insert(
            "end",
            f"Backup File:\n{backup_file}\n\n"
        )

    if not original_file and not backup_file:
        box.insert(
            "end",
            "No files uploaded yet."
        )


def show_analytics():

    clear_content()

    frame = ctk.CTkFrame(content)
    frame.pack(fill="both", expand=True)

    ctk.CTkLabel(
        frame,
        text="📊 Analytics Dashboard",
        font=("Arial", 28, "bold")
    ).pack(pady=20)

    analytics = ctk.CTkTextbox(frame)
    analytics.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    analytics.insert(
        "end",
        """
Total Backups : 128

Verified Backups : 125

Failed Backups : 3

Success Rate : 97.6%

Average Verification Time : 3.2 Seconds

Storage Usage : 74%

Weekly Growth : 8%
"""
    )


def show_alerts():

    clear_content()

    frame = ctk.CTkFrame(content)
    frame.pack(fill="both", expand=True)

    ctk.CTkLabel(
        frame,
        text="⚠ Alert Center",
        font=("Arial", 28, "bold")
    ).pack(pady=20)

    alerts = ctk.CTkTextbox(frame)

    alerts.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    alerts.insert(
        "end",
        """
✅ Backup Verification Successful

⚠ Delayed Backup Detected

⚠ Storage Usage Above 70%

✅ Database Integrity Check Passed

✅ Monitoring Service Running

✅ Last Scan Completed Successfully
"""
    )

# =====================================
# SIDEBAR
# =====================================

sidebar = ctk.CTkFrame(
    app,
    width=250,
    corner_radius=0
)

sidebar.pack(
    side="left",
    fill="y"
)

logo = ctk.CTkLabel(
    sidebar,
    text="🛡 BackupGuard",
    font=("Arial", 24, "bold")
)

logo.pack(pady=30)

ctk.CTkButton(
    sidebar,
    text="🏠 Dashboard",
    command=show_dashboard,
    height=45
).pack(fill="x", padx=20, pady=8)

ctk.CTkButton(
    sidebar,
    text="📁 Backups",
    command=show_backups,
    height=45
).pack(fill="x", padx=20, pady=8)

ctk.CTkButton(
    sidebar,
    text="📊 Analytics",
    command=show_analytics,
    height=45
).pack(fill="x", padx=20, pady=8)

ctk.CTkButton(
    sidebar,
    text="⚠ Alerts",
    command=show_alerts,
    height=45
).pack(fill="x", padx=20, pady=8)

# =====================================
# MAIN AREA
# =====================================

main = ctk.CTkFrame(app)
main.pack(
    side="right",
    fill="both",
    expand=True
)

# =====================================
# HEADER
# =====================================

header = ctk.CTkFrame(main)
header.pack(
    fill="x",
    padx=15,
    pady=15
)

title = ctk.CTkLabel(
    header,
    text="Backup Verification Dashboard",
    font=("Arial", 30, "bold")
)

title.pack(
    side="left",
    padx=20
)

status = ctk.CTkLabel(
    header,
    text="🟢 SYSTEM HEALTHY",
    font=("Arial", 18, "bold")
)

status.pack(
    side="right",
    padx=20
)

# =====================================
# UPLOAD SECTION
# =====================================

upload_frame = ctk.CTkFrame(main)
upload_frame.pack(
    fill="x",
    padx=15,
    pady=10
)

ctk.CTkLabel(
    upload_frame,
    text="Database Verification",
    font=("Arial", 22, "bold")
).pack(pady=10)

button_frame = ctk.CTkFrame(upload_frame)
button_frame.pack(
    fill="x",
    padx=10,
    pady=10
)

ctk.CTkButton(
    button_frame,
    text="📂 Upload Original",
    command=upload_original
).pack(
    side="left",
    padx=10
)

ctk.CTkButton(
    button_frame,
    text="📂 Upload Backup",
    command=upload_backup
).pack(
    side="left",
    padx=10
)

ctk.CTkButton(
    button_frame,
    text="✅ Verify",
    command=verify_backup
).pack(
    side="right",
    padx=10
)

original_label = ctk.CTkLabel(
    upload_frame,
    text="Original : Not Selected"
)

original_label.pack(
    anchor="w",
    padx=20
)

backup_label = ctk.CTkLabel(
    upload_frame,
    text="Backup : Not Selected"
)

backup_label.pack(
    anchor="w",
    padx=20
)

result_label = ctk.CTkLabel(
    upload_frame,
    text="Waiting For Verification",
    font=("Arial", 24, "bold")
)

result_label.pack(pady=10)

# =====================================
# KPI CARDS
# =====================================

cards = ctk.CTkFrame(main)
cards.pack(
    fill="x",
    padx=15
)

for title_text, value in [
    ("Total Backups", "128"),
    ("Verified", "125"),
    ("Failed", "3"),
    ("Success Rate", "97.6%")
]:

    card = ctk.CTkFrame(cards)

    card.pack(
        side="left",
        expand=True,
        fill="both",
        padx=10
    )

    ctk.CTkLabel(
        card,
        text=title_text
    ).pack(pady=10)

    ctk.CTkLabel(
        card,
        text=value,
        font=("Arial", 30, "bold")
    ).pack(pady=10)

# =====================================
# PROGRESS BAR
# =====================================

progress_frame = ctk.CTkFrame(main)
progress_frame.pack(
    fill="x",
    padx=15,
    pady=15
)

ctk.CTkLabel(
    progress_frame,
    text="Verification Progress",
    font=("Arial", 18, "bold")
).pack(
    anchor="w",
    padx=20
)

progress = ctk.CTkProgressBar(
    progress_frame
)

progress.pack(
    fill="x",
    padx=20,
    pady=10
)

progress.set(0)

# =====================================
# DYNAMIC CONTENT AREA
# =====================================

content = ctk.CTkFrame(main)
content.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)

# =====================================
# FOOTER
# =====================================

footer = ctk.CTkFrame(main)

footer.pack(
    fill="x",
    padx=15,
    pady=10
)

ctk.CTkLabel(
    footer,
    text=f"Last Scan : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
).pack(
    side="left",
    padx=20
)

ctk.CTkButton(
    footer,
    text="▶ Run Verification",
    command=verify_backup,
    width=180
).pack(
    side="right",
    padx=20
)

show_dashboard()

app.mainloop()