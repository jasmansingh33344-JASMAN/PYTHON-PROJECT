
import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import pandas as pd
import numpy as np

from main import initialize

# ================= CONFIG =================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

BG = "#080D18"
SIDEBAR = "#0D1525"
CARD = "#111D30"
CARD2 = "#16243A"
BLUE = "#38BDF8"
CYAN = "#22D3EE"
GREEN = "#4ADE80"
RED = "#FB7185"
WHITE = "#F1F5F9"
MUTED = "#8293AA"
PURPLE = "#A78BFA"

# ================= BACKEND =================

project = initialize()

data = project["data"]
X = project["X"]
y = project["y"]

lr = project["lr"]
rf = project["rf"]

lr_pred = project["lr_pred"]
rf_pred = project["rf_pred"]

y_test = project["y_test"]

best_model = project["best_model"]
best_model_name = project["best_model_name"]

lr_metrics = project["lr_metrics"]
rf_metrics = project["rf_metrics"]

history_records = []
history_table = None
content = None

# ================= WINDOW =================

root = ctk.CTk()

root.title("FRAUDSHIELD AI | Intelligence Center")
root.geometry("1450x850")
root.minsize(1100, 700)
root.configure(fg_color=BG)

# ================= HELPERS =================

def label(parent, text, size=13, color=WHITE, weight="normal"):
    return ctk.CTkLabel(
        parent,
        text=text,
        font=("Segoe UI", size, weight),
        text_color=color
    )


def clear_content():
    global history_table

    for widget in content.winfo_children():
        widget.destroy()

    history_table = None


def heading(title, subtitle):
    label(content, title, 27, WHITE, "bold").pack(
        anchor="w", pady=(5, 3)
    )

    label(content, subtitle, 12, MUTED).pack(
        anchor="w", pady=(0, 22)
    )


def card(parent, title, value, color=BLUE, subtitle=None):
    frame = ctk.CTkFrame(
        parent,
        fg_color=CARD,
        corner_radius=16,
        border_width=1,
        border_color="#20334D"
    )

    label(frame, title, 11, MUTED, "bold").pack(
        anchor="w", padx=18, pady=(17, 5)
    )

    label(frame, value, 27, color, "bold").pack(
        anchor="w", padx=18, pady=3
    )

    if subtitle:
        label(frame, subtitle, 10, MUTED).pack(
            anchor="w", padx=18, pady=(2, 15)
        )
    else:
        ctk.CTkFrame(
            frame, fg_color="transparent", height=12
        ).pack()

    return frame


def section(parent, title):
    frame = ctk.CTkFrame(
        parent,
        fg_color=CARD,
        corner_radius=16,
        border_width=1,
        border_color="#20334D"
    )

    label(frame, title, 15, WHITE, "bold").pack(
        anchor="w", padx=20, pady=18
    )

    return frame


# ================= SIDEBAR =================

sidebar = ctk.CTkFrame(
    root,
    width=245,
    corner_radius=0,
    fg_color=SIDEBAR
)

sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

ctk.CTkLabel(
    sidebar,
    text="◆  FRAUDSHIELD",
    font=("Segoe UI", 21, "bold"),
    text_color=CYAN
).pack(anchor="w", padx=22, pady=(35, 4))

label(
    sidebar, "FINANCIAL INTELLIGENCE", 9, MUTED, "bold"
).pack(anchor="w", padx=24, pady=(0, 35))


label(
    sidebar, "WORKSPACE", 9, MUTED, "bold"
).pack(anchor="w", padx=24, pady=(0, 10))


# ================= MAIN CONTENT =================

content = ctk.CTkFrame(
    root,
    fg_color=BG,
    corner_radius=0
)

content.pack(
    side="left",
    fill="both",
    expand=True,
    padx=25,
    pady=20
)


# ================= NAVIGATION =================

nav_buttons = {}


def navigate(name, function):

    for button_name, button in nav_buttons.items():

        button.configure(
            fg_color="#142238" if button_name == name else "transparent",
            text_color=CYAN if button_name == name else MUTED
        )

    function()


def nav_button(name, function):

    button = ctk.CTkButton(
        sidebar,
        text="   " + name,
        height=47,
        corner_radius=10,
        anchor="w",
        fg_color="transparent",
        hover_color="#1B2C45",
        text_color=MUTED,
        font=("Segoe UI", 13),
        command=lambda: navigate(name, function)
    )

    button.pack(fill="x", padx=12, pady=4)

    nav_buttons[name] = button


# ================= DASHBOARD =================

def dashboard():

    clear_content()

    heading(
        "Security Overview",
        "Real-time financial fraud intelligence and model monitoring"
    )

    total = len(data)
    fraud = int(data["is_fraud"].sum())
    safe = total - fraud

    stats = ctk.CTkFrame(content, fg_color="transparent")
    stats.pack(fill="x")

    stats.grid_columnconfigure((0, 1, 2, 3), weight=1)

    items = [
        ("TOTAL TRANSACTIONS", f"{total:,}", BLUE, "Dataset volume"),
        ("FRAUD DETECTED", f"{fraud:,}", RED, "Simulated fraud records"),
        ("LEGITIMATE", f"{safe:,}", GREEN, "Safe records"),
        ("MODEL ACCURACY", f"{rf_metrics['accuracy']*100:.1f}%", PURPLE, "Random Forest")
    ]

    for i, (title, value, color, sub) in enumerate(items):

        box = card(stats, title, value, color, sub)
        box.grid(row=0, column=i, sticky="nsew", padx=6, pady=5)

    middle = ctk.CTkFrame(content, fg_color="transparent")
    middle.pack(fill="both", expand=True, pady=18)

    middle.grid_columnconfigure((0, 1), weight=1)
    middle.grid_rowconfigure(0, weight=1)

    # System status
    status = section(middle, "SYSTEM STATUS")
    status.grid(row=0, column=0, sticky="nsew", padx=6)

    statuses = [
        ("●", "Dataset loaded successfully", GREEN),
        ("●", "Preprocessing completed", GREEN),
        ("●", "Logistic Regression trained", GREEN),
        ("●", "Random Forest trained", GREEN),
        ("●", f"{best_model_name} selected", CYAN)
    ]

    for symbol, text, color in statuses:

        row = ctk.CTkFrame(status, fg_color="transparent")
        row.pack(fill="x", padx=20, pady=10)

        label(row, symbol, 15, color, "bold").pack(side="left")
        label(row, text, 12, WHITE).pack(side="left", padx=10)

    label(
        status,
        "FraudShield AI monitoring active",
        11, MUTED
    ).pack(anchor="w", padx=20, pady=20)

    # Fraud distribution
    distribution = section(middle, "TRANSACTION DISTRIBUTION")
    distribution.grid(row=0, column=1, sticky="nsew", padx=6)

    for title, count, color in [
        ("Legitimate transactions", safe, GREEN),
        ("Potential fraud transactions", fraud, RED)
    ]:

        label(
            distribution,
            f"{title}  |  {count:,}",
            12, WHITE
        ).pack(anchor="w", padx=20, pady=(12, 5))

        bar = ctk.CTkProgressBar(
            distribution,
            height=12,
            corner_radius=10,
            progress_color=color,
            fg_color="#25364D"
        )

        bar.pack(fill="x", padx=20, pady=(0, 12))

        bar.set(count / total if total else 0)

    # Bottom model status
    bottom = card(
        content,
        "ACTIVE DETECTION ENGINE",
        best_model_name,
        CYAN,
        "Selected automatically using F1 score"
    )

    bottom.pack(fill="x", padx=6, pady=5)


# ================= FRAUD ANALYSIS =================

def fraud_analysis():

    clear_content()

    heading(
        "Transaction Intelligence",
        "Analyze a transaction using the trained machine-learning model"
    )

    form = ctk.CTkFrame(
        content,
        fg_color=CARD,
        corner_radius=16,
        border_width=1,
        border_color="#20334D"
    )

    form.pack(fill="x", padx=5)

    fields = [
        ("Transaction Amount", "amount", "2500"),
        ("Transaction Hour (0-23)", "hour", "14"),
        ("Account Age (days)", "account_age", "500"),
        ("Transaction Count", "transactions", "2"),
        ("Distance (km)", "distance", "10"),
        ("International (0/1)", "international", "0"),
        ("Failed PIN Attempts", "failed_pin", "0"),
        ("Device Changed (0/1)", "device_changed", "0")
    ]

    entries = {}

    for i, (title, key, default) in enumerate(fields):

        row, col = divmod(i, 2)

        label(form, title, 11, MUTED, "bold").grid(
            row=row * 2,
            column=col,
            sticky="w",
            padx=20,
            pady=(15, 5)
        )

        entry = ctk.CTkEntry(
            form,
            height=42,
            corner_radius=9,
            fg_color=CARD2,
            border_color="#304763",
            text_color=WHITE,
            placeholder_text=title
        )

        entry.insert(0, default)

        entry.grid(
            row=row * 2 + 1,
            column=col,
            sticky="ew",
            padx=20,
            pady=(0, 8)
        )

        entries[key] = entry

    form.grid_columnconfigure((0, 1), weight=1)

    output = ctk.CTkFrame(
        content,
        fg_color=CARD,
        corner_radius=16,
        border_width=1,
        border_color="#20334D"
    )

    output.pack(fill="x", padx=5, pady=18)

    result = label(
        output,
        "AWAITING ANALYSIS",
        21,
        CYAN,
        "bold"
    )

    result.pack(pady=(20, 5))

    probability = label(output, "", 14, WHITE)
    probability.pack(pady=5)

    recommendation = label(
        output, "", 12, MUTED
    )

    recommendation.pack(pady=(5, 20))

    def analyse():

        try:

            values = {
                key: float(entry.get())
                for key, entry in entries.items()
            }

            if not all(np.isfinite(v) for v in values.values()):
                raise ValueError("Enter valid finite numbers.")

            if values["amount"] < 0 or values["distance"] < 0:
                raise ValueError("Amount and distance cannot be negative.")

            if not 0 <= values["hour"] <= 23:
                raise ValueError("Hour must be between 0 and 23.")

            if not values["hour"].is_integer():
                raise ValueError("Hour must be a whole number.")

            if values["account_age"] < 1 or not values["account_age"].is_integer():
                raise ValueError("Account age must be a positive whole number.")

            for key in ["transactions", "failed_pin"]:

                if values[key] < 0 or not values[key].is_integer():
                    raise ValueError(f"{key} must be a non-negative whole number.")

            for key in ["international", "device_changed"]:

                if values[key] not in (0, 1):
                    raise ValueError(f"{key} must be 0 or 1.")

            transaction = pd.DataFrame([values], columns=X.columns)

            prediction = int(best_model.predict(transaction)[0])

            probability_value = float(
                best_model.predict_proba(transaction)[0][1]
            )

            if prediction == 1:

                result.configure(
                    text="⚠ POTENTIAL FRAUD DETECTED",
                    text_color=RED
                )

                recommendation.configure(
                    text="Additional verification and human review recommended."
                )

            else:

                result.configure(
                    text="✓ LIKELY LEGITIMATE",
                    text_color=GREEN
                )

                recommendation.configure(
                    text="No fraud signal detected by this model."
                )

            probability.configure(
                text=f"Estimated fraud probability: {probability_value:.2%}"
            )

            record = (
                f"{values['amount']:.2f}",
                values["hour"],
                "Potential fraud" if prediction else "Likely legitimate",
                f"{probability_value:.2%}"
            )

            history_records.append(record)

            if history_table is not None:

                history_table.insert("", "end", values=record)

        except ValueError as error:

            messagebox.showerror("Invalid Input", str(error))

        except Exception as error:

            messagebox.showerror("Analysis Error", str(error))

    ctk.CTkButton(
        content,
        text="RUN FRAUD ANALYSIS  →",
        height=48,
        corner_radius=10,
        fg_color="#087EB8",
        hover_color="#0369A1",
        font=("Segoe UI", 14, "bold"),
        command=analyse
    ).pack(fill="x", padx=5)


# ================= TRANSACTION HISTORY =================

def transaction_history():

    clear_content()

    heading(
        "Transaction Records",
        "Review all transactions analyzed during this session"
    )

    global history_table

    table_frame = ctk.CTkFrame(
        content,
        fg_color=CARD,
        corner_radius=16
    )

    table_frame.pack(fill="both", expand=True, padx=5)

    style = ttk.Style()

    style.theme_use("clam")

    style.configure(
        "Treeview",
        background=CARD,
        foreground=WHITE,
        fieldbackground=CARD,
        rowheight=38,
        borderwidth=0,
        font=("Segoe UI", 10)
    )

    style.configure(
        "Treeview.Heading",
        background=SIDEBAR,
        foreground=CYAN,
        font=("Segoe UI", 10, "bold"),
        relief="flat"
    )

    style.map(
        "Treeview",
        background=[("selected", "#164E63")]
    )

    history_table = ttk.Treeview(
        table_frame,
        columns=("amount", "hour", "status", "risk"),
        show="headings"
    )

    columns = [
        ("amount", "AMOUNT", 150),
        ("hour", "HOUR", 100),
        ("status", "PREDICTION", 250),
        ("risk", "FRAUD PROBABILITY", 180)
    ]

    for key, title, width in columns:

        history_table.heading(key, text=title)

        history_table.column(
            key,
            width=width,
            anchor="center"
        )

    history_table.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=15
    )

    for record in history_records:
        history_table.insert("", "end", values=record)

    label(
        content,
        "Session history is cleared when the application closes.",
        11, MUTED
    ).pack(anchor="w", padx=8, pady=12)


# ================= MODEL PERFORMANCE =================

def model_performance():

    clear_content()

    heading(
        "Model Intelligence",
        "Compare the performance of trained classification algorithms"
    )

    models = [
        ("LOGISTIC REGRESSION", lr_metrics, BLUE),
        ("RANDOM FOREST", rf_metrics, PURPLE)
    ]

    for name, metrics, color in models:

        panel = ctk.CTkFrame(
            content,
            fg_color=CARD,
            corner_radius=16,
            border_width=1,
            border_color="#20334D"
        )

        panel.pack(fill="x", padx=5, pady=10)

        label(
            panel, name, 16, color, "bold"
        ).pack(anchor="w", padx=20, pady=(18, 12))

        for metric in ["accuracy", "precision", "recall", "f1"]:

            value = metrics[metric]

            row = ctk.CTkFrame(
                panel,
                fg_color="transparent"
            )

            row.pack(fill="x", padx=20, pady=6)

            label(
                row,
                metric.upper(),
                11,
                MUTED,
                "bold"
            ).pack(side="left")

            label(
                row,
                f"{value:.4f}  ({value*100:.2f}%)",
                12,
                GREEN,
                "bold"
            ).pack(side="right")

            bar = ctk.CTkProgressBar(
                panel,
                height=8,
                progress_color=color,
                fg_color="#25364D"
            )

            bar.pack(fill="x", padx=20, pady=(0, 8))

            bar.set(value)

        label(
            panel,
            "Measured on the held-out synthetic test dataset.",
            10,
            MUTED
        ).pack(anchor="w", padx=20, pady=(8, 18))


# ================= NAVIGATION SETUP =================

nav_button("Dashboard", dashboard)
nav_button("Fraud Analysis", fraud_analysis)
nav_button("Transaction History", transaction_history)
nav_button("Model Performance", model_performance)

# Sidebar footer

ctk.CTkFrame(
    sidebar,
    fg_color="transparent"
).pack(fill="both", expand=True)

ctk.CTkFrame(
    sidebar,
    height=1,
    fg_color="#25364D"
).pack(fill="x", padx=18, pady=10)

label(
    sidebar, "FRAUDSHIELD AI", 12, CYAN, "bold"
).pack(anchor="w", padx=22, pady=3)

label(
    sidebar, "ML PROJECT  |  2026", 9, MUTED
).pack(anchor="w", padx=22, pady=(0, 20))

# ================= START =================

navigate("Dashboard", dashboard)

root.mainloop()