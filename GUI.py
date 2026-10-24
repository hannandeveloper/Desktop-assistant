"""Desktop Assistant - Swiss-style GUI by Hannan Mudassar.

Layout
  blue sidebar (brand mark, navigation, author) | yellow stripe | light content area
  with a dark terminal-style status strip along the bottom.
Colours come from the brand banner: blue #2B4CFF and yellow #FFD84D.
"""
import base64
import io
import threading

import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image, ImageTk

from fileTask import mAFolder, mAFile, multipleFinFol
from chatBot import askAI
from brand import MARK_WHITE_B64, ICON_B64

# ---------------------------------------------------------------------------
# Design tokens
# ---------------------------------------------------------------------------
BRAND = "#2B4CFF"        # banner blue
BRAND_DARK = "#1F38D6"   # hover state of the blue
SIGNAL = "#FFD84D"       # banner yellow
BG = "#F4F5F8"           # page background
INK = "#0B0D14"          # text and heavy rules
MUTED = "#545A6B"        # captions
PANEL = "#E6E9F2"
WHITE = "#FFFFFF"
SOFT_WHITE = "#C9D2FF"   # secondary text on the blue sidebar

DISPLAY_FONT = "Arial Black"
BODY_FONT = "Arial"
MONO_FONT = "Consolas"

SIDEBAR_WIDTH = 270
STRIPE_WIDTH = 12
SIDEBAR_PAD = 28
PAGE_PAD = 40

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1120x740")
app.minsize(1000, 700)
app.title("Desktop Assistant")
app.configure(fg_color=BG)

# Fonts must be created after the root window exists
f_display_xl = ctk.CTkFont(family=DISPLAY_FONT, size=30)
f_display_md = ctk.CTkFont(family=DISPLAY_FONT, size=22)
f_heading = ctk.CTkFont(family=BODY_FONT, size=20, weight="bold")
f_body = ctk.CTkFont(family=BODY_FONT, size=14)
f_body_bold = ctk.CTkFont(family=BODY_FONT, size=14, weight="bold")
f_mono = ctk.CTkFont(family=MONO_FONT, size=13)
f_mono_bold = ctk.CTkFont(family=MONO_FONT, size=13, weight="bold")
f_mono_small = ctk.CTkFont(family=MONO_FONT, size=11)


# ---------------------------------------------------------------------------
# Brand mark
# ---------------------------------------------------------------------------
def load_image(b64_data):
    return Image.open(io.BytesIO(base64.b64decode(b64_data))).convert("RGBA")


mark_image = load_image(MARK_WHITE_B64)
mark = CTkImage(light_image=mark_image, dark_image=mark_image, size=(88, 88))

try:
    # CustomTkinter sets its own icon after ~200 ms on Windows, so set ours later
    icon_photo = ImageTk.PhotoImage(load_image(ICON_B64))
    app.after(300, lambda: app.iconphoto(False, icon_photo))
except Exception:
    pass


# ---------------------------------------------------------------------------
# Window frame: sidebar | stripe | main
# ---------------------------------------------------------------------------
app.grid_columnconfigure(0, weight=0)
app.grid_columnconfigure(1, weight=0)
app.grid_columnconfigure(2, weight=1)
app.grid_rowconfigure(0, weight=1)

sidebar = ctk.CTkFrame(app, width=SIDEBAR_WIDTH, fg_color=BRAND, corner_radius=0)
sidebar.grid(row=0, column=0, sticky="ns")
sidebar.grid_propagate(False)
sidebar.grid_columnconfigure(0, weight=1)
sidebar.grid_rowconfigure(4, weight=1)

stripe = ctk.CTkFrame(app, width=STRIPE_WIDTH, fg_color=SIGNAL, corner_radius=0)
stripe.grid(row=0, column=1, sticky="ns")

main = ctk.CTkFrame(app, fg_color=BG, corner_radius=0)
main.grid(row=0, column=2, sticky="nsew")
main.grid_columnconfigure(0, weight=1)
main.grid_rowconfigure(2, weight=1)


# ---------------------------------------------------------------------------
# Sidebar: brand, navigation, author
# ---------------------------------------------------------------------------
ctk.CTkLabel(sidebar, text="", image=mark, fg_color="transparent").grid(
    row=0, column=0, sticky="w", padx=SIDEBAR_PAD, pady=(SIDEBAR_PAD + 6, 18))

ctk.CTkLabel(
    sidebar, text="DESKTOP\nASSISTANT", font=f_display_md, text_color=WHITE,
    justify="left", anchor="w",
).grid(row=1, column=0, sticky="w", padx=SIDEBAR_PAD)

ctk.CTkLabel(
    sidebar, text="v2.0", font=f_mono_bold, text_color=SIGNAL, anchor="w",
).grid(row=2, column=0, sticky="w", padx=SIDEBAR_PAD, pady=(8, 0))

nav = ctk.CTkFrame(sidebar, fg_color="transparent", corner_radius=0)
nav.grid(row=3, column=0, sticky="ew", pady=(44, 0))

NAV_INDENT = "    "


def make_nav_button(text, key):
    return ctk.CTkButton(
        nav, text=NAV_INDENT + text, anchor="w", height=48, corner_radius=0,
        font=f_mono_bold, fg_color="transparent", text_color=WHITE,
        hover_color=BRAND_DARK, command=lambda: show_page(key),
    )


files_nav = make_nav_button("//  FILES & FOLDERS", "files")
files_nav.pack(fill="x")
chat_nav = make_nav_button("//  AI CHAT", "chat")
chat_nav.pack(fill="x", pady=(2, 0))

author = ctk.CTkFrame(sidebar, fg_color="transparent", corner_radius=0)
author.grid(row=5, column=0, sticky="ew", padx=SIDEBAR_PAD, pady=(0, SIDEBAR_PAD))
ctk.CTkFrame(author, height=2, fg_color=WHITE, corner_radius=0).pack(fill="x", pady=(0, 14))
ctk.CTkLabel(author, text="$ whoami", font=f_mono_bold, text_color=SIGNAL, anchor="w").pack(anchor="w")
ctk.CTkLabel(author, text="Hannan Mudassar", font=f_body_bold, text_color=WHITE, anchor="w").pack(anchor="w", pady=(2, 0))
ctk.CTkLabel(author, text="github.com/hannandeveloper", font=f_mono_small, text_color=SOFT_WHITE, anchor="w").pack(anchor="w", pady=(2, 0))


# ---------------------------------------------------------------------------
# Main: page heading, rule, content, status strip
# ---------------------------------------------------------------------------
head = ctk.CTkFrame(main, fg_color="transparent", corner_radius=0)
head.grid(row=0, column=0, sticky="ew", padx=PAGE_PAD, pady=(34, 20))
page_kicker = ctk.CTkLabel(head, text="", font=f_mono_bold, text_color=BRAND, anchor="w")
page_kicker.pack(anchor="w")
page_title = ctk.CTkLabel(head, text="", font=f_display_xl, text_color=INK, anchor="w")
page_title.pack(anchor="w", pady=(6, 0))

ctk.CTkFrame(main, height=3, fg_color=INK, corner_radius=0).grid(
    row=1, column=0, sticky="ew", padx=PAGE_PAD)

content = ctk.CTkFrame(main, fg_color="transparent", corner_radius=0)
content.grid(row=2, column=0, sticky="nsew", padx=PAGE_PAD, pady=(28, 28))
content.grid_columnconfigure(0, weight=1)
content.grid_rowconfigure(0, weight=1)

# Terminal-style status strip. mAFolder and mAFile write their messages here.
status_bar = ctk.CTkFrame(main, height=46, fg_color=INK, corner_radius=0)
status_bar.grid(row=3, column=0, sticky="ew")
status_bar.pack_propagate(False)
ctk.CTkLabel(status_bar, text="$", font=f_mono_bold, text_color=SIGNAL).pack(side="left", padx=(PAGE_PAD, 10))
status_label = ctk.CTkLabel(status_bar, text="ready", font=f_mono, text_color="#E8EBF5", anchor="w")
status_label.pack(side="left", fill="x", expand=True)


def set_status(text):
    status_label.configure(text=text)


# ---------------------------------------------------------------------------
# Shared widget helpers
# ---------------------------------------------------------------------------
def make_entry(parent, placeholder, height=42):
    return ctk.CTkEntry(
        parent, placeholder_text=placeholder, height=height, corner_radius=0,
        border_width=2, border_color=INK, fg_color=WHITE, text_color=INK,
        placeholder_text_color=MUTED, font=f_body,
    )


def make_button(parent, text, command, height=46, width=140):
    return ctk.CTkButton(
        parent, text=text, command=command, height=height, width=width, corner_radius=0,
        font=f_mono_bold, fg_color=BRAND, hover_color=BRAND_DARK, text_color=WHITE,
    )


# ---------------------------------------------------------------------------
# Page 1: files and folders
# ---------------------------------------------------------------------------
files_page = ctk.CTkFrame(content, fg_color="transparent", corner_radius=0)
files_page.grid(row=0, column=0, sticky="nsew")
files_page.grid_columnconfigure(0, weight=1, uniform="cols")
files_page.grid_columnconfigure(1, weight=0, minsize=40)
files_page.grid_columnconfigure(2, weight=1, uniform="cols")
files_page.grid_rowconfigure(0, weight=1)


def make_column(col, kicker, heading):
    frame = ctk.CTkFrame(files_page, fg_color="transparent", corner_radius=0)
    frame.grid(row=0, column=col, sticky="nsew")
    frame.grid_columnconfigure(0, weight=1)
    ctk.CTkFrame(frame, height=3, fg_color=INK, corner_radius=0).grid(row=0, column=0, sticky="ew")
    ctk.CTkLabel(frame, text=kicker, font=f_mono_small, text_color=MUTED, anchor="w").grid(
        row=1, column=0, sticky="ew", pady=(12, 0))
    ctk.CTkLabel(frame, text=heading, font=f_heading, text_color=INK, anchor="w").grid(
        row=2, column=0, sticky="ew", pady=(2, 8))
    return frame


def add_field(frame, row, caption, placeholder):
    ctk.CTkLabel(frame, text=caption, font=f_mono_small, text_color=MUTED, anchor="w").grid(
        row=row, column=0, sticky="ew", pady=(14, 4))
    entry = make_entry(frame, placeholder)
    entry.grid(row=row + 1, column=0, sticky="ew")
    return entry


# Left column: single operations
single_col = make_column(0, "// SINGLE", "One folder or one file")

folderName = add_field(single_col, 3, "FOLDER NAME", "Enter folder name")


def create_folder():
    name = folderName.get().strip()
    if not name:
        set_status("enter a folder name first")
        return
    mAFolder(name, status_label)


make_button(single_col, "CREATE FOLDER  →", create_folder).grid(
    row=5, column=0, sticky="ew", pady=(16, 0))

fileName = add_field(single_col, 6, "FILE NAME", "Enter file name with extension")


def create_file():
    name = fileName.get().strip()
    if not name:
        set_status("enter a file name first")
        return
    mAFile(name, status_label)


make_button(single_col, "CREATE FILE  →", create_file).grid(
    row=8, column=0, sticky="ew", pady=(16, 0))

# Right column: batch generation
batch_col = make_column(2, "// BATCH", "A folder with many files")

fileNameEntry = add_field(batch_col, 3, "BASE FILE NAME", "Base file name")
folderNameEntry = add_field(batch_col, 5, "TARGET FOLDER", "Target folder name")
numFilesEntry = add_field(batch_col, 7, "NUMBER OF FILES", "Number of files")


def on_click():
    try:
        f_name = fileNameEntry.get().strip()
        f_fol = folderNameEntry.get().strip()
        n_files = int(numFilesEntry.get())

        if not f_name or not f_fol:
            set_status("please enter valid file and folder names")
            return
        if n_files < 1:
            set_status("number of files must be 1 or more")
            return

        multipleFinFol(f_name, f_fol, n_files)
        set_status("batch files created successfully!")
    except ValueError:
        set_status("please enter a valid number for files")


make_button(batch_col, "CREATE MULTIPLE FILES  →", on_click).grid(
    row=9, column=0, sticky="ew", pady=(16, 0))


# ---------------------------------------------------------------------------
# Page 2: AI chat
# ---------------------------------------------------------------------------
chat_page = ctk.CTkFrame(content, fg_color="transparent", corner_radius=0)
chat_page.grid(row=0, column=0, sticky="nsew")
chat_page.grid_columnconfigure(0, weight=1)
chat_page.grid_rowconfigure(0, weight=1)

chatBox = ctk.CTkTextbox(
    chat_page, wrap="word", corner_radius=0, border_width=2, border_color=INK,
    border_spacing=14, fg_color=WHITE, text_color=INK, font=f_body,
    scrollbar_button_color="#B8BECE", scrollbar_button_hover_color=BRAND,
)
chatBox.grid(row=0, column=0, sticky="nsew")
chatBox.tag_config("who_you", foreground=BRAND)
chatBox.tag_config("who_bot", foreground=MUTED)

input_row = ctk.CTkFrame(chat_page, fg_color="transparent", corner_radius=0)
input_row.grid(row=1, column=0, sticky="ew", pady=(14, 0))
input_row.grid_columnconfigure(0, weight=1)

chatEntry = make_entry(input_row, "Ask your assistant something...", height=46)
chatEntry.grid(row=0, column=0, sticky="ew", padx=(0, 10))


def addMessage(text, tag=None):
    chatBox.configure(state="normal")
    chatBox.insert("end", text, tag)
    chatBox.see("end")
    chatBox.configure(state="disabled")


def showReply(answer):
    addMessage("ASSISTANT\n", "who_bot")
    addMessage(f"{answer}\n\n")
    sendButton.configure(state="normal")
    set_status("ready")


def sendMessage(event=None):
    user = chatEntry.get().strip()
    if not user:
        return
    chatEntry.delete(0, "end")
    addMessage("YOU\n", "who_you")
    addMessage(f"{user}\n\n")
    sendButton.configure(state="disabled")
    set_status("waiting for reply...")

    def worker():
        answer = askAI(user)
        app.after(0, lambda: showReply(answer))

    threading.Thread(target=worker, daemon=True).start()


sendButton = make_button(input_row, "SEND  →", sendMessage, height=46, width=130)
sendButton.grid(row=0, column=1)
chatEntry.bind("<Return>", sendMessage)

# Opening message
addMessage("ASSISTANT\n", "who_bot")
addMessage("Ask anything. Replies use your own Gemini API key from the .env file.\n\n")


# ---------------------------------------------------------------------------
# Navigation
# ---------------------------------------------------------------------------
PAGES = {
    "files": (files_page, files_nav, "// FILES & FOLDERS", "Make files and folders."),
    "chat": (chat_page, chat_nav, "// AI CHAT", "Ask the assistant."),
}


def show_page(name):
    for key, (frame, button, _kicker, _title) in PAGES.items():
        if key == name:
            frame.grid()
            button.configure(fg_color=WHITE, text_color=BRAND, hover_color=WHITE)
        else:
            frame.grid_remove()
            button.configure(fg_color="transparent", text_color=WHITE, hover_color=BRAND_DARK)
    page_kicker.configure(text=PAGES[name][2])
    page_title.configure(text=PAGES[name][3])
    if name == "chat":
        chatEntry.focus()


show_page("files")

# Run application
app.mainloop()