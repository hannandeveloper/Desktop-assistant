import customtkinter
from pathlib import Path


customtkinter.set_appearance_mode("light")

def mAFolder(folderName):
    # FolderName = input("Enter the name of folder ")
    # folderName = customtkinter.CTkEntry(app, placeholder_text="Enter folder name")
    desktop = Path.home() / "Desktop"
    folderPath= Path(f"{desktop}/{folderName}")
    folderPath.mkdir(parents=True , exist_ok=True)
    # return f"{folderName} folder created successfully on Desktop"

app = customtkinter.CTk()
app.geometry("600x400")

button = customtkinter.CTkButton(app, text="create a folder", command=lambda: mAFolder(folderName.get()))
folderName = customtkinter.CTkEntry(app, placeholder_text="Enter folder name")
folderName.pack(padx=20, pady=20)
button.pack(padx=20, pady=20)

app.mainloop()