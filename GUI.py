import customtkinter
import customtkinter as ctk
from fileTask import mAFolder, mAFile, multipleFinFol
from chatBot import askAI
import threading


app = ctk.CTk()
customtkinter.set_appearance_mode("light")
app.geometry("1000x800")
app.title("Desktop Assistant")



# 1. Create the tab container
tabview = ctk.CTkTabview(app, width=900, height=650)
tabview.pack(padx=20, pady=20)

# 2. Add tabs (the name is the title shown on the tab)
tabview.add("Folders")
tabview.add("AI Chat")
aiTab = tabview.tab("AI Chat")

#----------- code for file tasks -----------------

# Take input from user for folder name and create a folder on desktop

folderName = customtkinter.CTkEntry(tabview.tab("Folders"),placeholder_text="Enter folder name")
button = customtkinter.CTkButton(tabview.tab("Folders"), text="create a folder", command=lambda: mAFolder(folderName.get(),label))
folderName.pack(padx=10, pady=10)
button.pack(padx=20, pady=20)


# Take input from user for file name and create a file on desktop
fileName = customtkinter.CTkEntry(tabview.tab("Folders"),placeholder_text="Enter file name with extension")
button = customtkinter.CTkButton(tabview.tab("Folders"),text="create a file", command=lambda: mAFile(fileName.get(),label))
fileName.pack(padx=10, pady=10)
button.pack(padx=20, pady=20)


# Take input from user for multiple files and create them in a folder on desktop
fileNameEntry = customtkinter.CTkEntry(tabview.tab("Folders"),placeholder_text="File Name")
fileNameEntry.pack(pady=10)

folderNameEntry = customtkinter.CTkEntry(tabview.tab("Folders"), placeholder_text="Folder Name")
folderNameEntry.pack(pady=10)

numFilesEntry = customtkinter.CTkEntry(tabview.tab("Folders"),placeholder_text="Number of Files")
numFilesEntry.pack(pady=10)


def on_click():
    try:
        f_name = fileNameEntry.get()
        f_fol = folderNameEntry.get()
        n_files = int(numFilesEntry.get())
        
        if not f_name or not f_fol:
            label.configure(tabview.tab("Folders"),text="Please enter valid file and folder names.")
            return
            
        multipleFinFol(f_name, f_fol, n_files)
        label.configure(tabview.tab("Folders"),text=f"Folder created successfully!")
    except ValueError:
        label.configure(tabview.tab("Folders"),text=f"Please enter a valid number")


button = customtkinter.CTkButton(tabview.tab("Folders"),text="create multiple files", command=on_click)
button.pack(pady=20)


label = ctk.CTkLabel(tabview.tab("Folders"),text="", font=("Arial", 14))
label.pack(pady=30)

#-------------- code for chat bot ---------------

# Where the conversation is shown
chatBox = ctk.CTkTextbox(aiTab, width=800, height=400, wrap="word")
chatBox.pack(padx=10, pady=10)
chatBox.configure(state="disabled")  # read-only

# Where the user types
chatEntry = ctk.CTkEntry(aiTab, width=650, placeholder_text="Ask something...")
chatEntry.pack(side="left", padx=(10, 5), pady=10)

def addMessage(text):
    chatBox.configure(state="normal")
    chatBox.insert("end", text)
    chatBox.see("end")
    chatBox.configure(state="disabled")

def showReply(answer):
    addMessage(f"Bot: {answer}\n\n")
    sendButton.configure(state="normal")

def sendMessage(event=None):
    user = chatEntry.get().strip()
    if not user:
        return
    chatEntry.delete(0, "end")
    addMessage(f"You: {user}\n")
    sendButton.configure(state="disabled")

    def worker():
        answer = askAI(user)
        app.after(0, lambda: showReply(answer))

    threading.Thread(target=worker, daemon=True).start()

sendButton = ctk.CTkButton(aiTab, text="Send", width=100, command=sendMessage)
sendButton.pack(side="left", padx=5, pady=10)

chatEntry.bind("<Return>", sendMessage)  # Enter key also sends

app.mainloop()