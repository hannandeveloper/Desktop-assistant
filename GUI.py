import customtkinter
import customtkinter as ctk
from fileTask import mAFolder, mAFile, multipleFinFol



app = ctk.CTk()
customtkinter.set_appearance_mode("light")
app.geometry("1000x800")
app.title("Desktop Assistant")



# 1. Create the tab container
tabview = ctk.CTkTabview(app, width=900, height=650)
tabview.pack(padx=20, pady=20)

# 2. Add tabs (the name is the title shown on the tab)
tabview.add("Folders")
tabview.add("chat bot")

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
label = ctk.CTkLabel(tabview.tab("chat bot"),text="this tab contains the chat bot", font=("Arial", 14))
label.pack(pady=30)

app.mainloop()