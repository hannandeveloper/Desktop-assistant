import customtkinter
from fileTask import mAFolder, mAFile, multipleFinFol


customtkinter.set_appearance_mode("light")
app = customtkinter.CTk()
app.geometry("600x400")

# Take input from user for folder name and create a folder on desktop
folderName = customtkinter.CTkEntry(app, placeholder_text="Enter folder name")
button = customtkinter.CTkButton(app, text="create a folder", command=lambda: mAFolder(folderName.get()))
folderName.pack(padx=10, pady=10)
button.pack(padx=20, pady=20)

# Take input from user for file name and create a file on desktop
fileName = customtkinter.CTkEntry(app, placeholder_text="Enter file name with extension")
button = customtkinter.CTkButton(app, text="create a file", command=lambda: mAFile(fileName.get()))
fileName.pack(padx=10, pady=10)
button.pack(padx=20, pady=20)

app.mainloop()