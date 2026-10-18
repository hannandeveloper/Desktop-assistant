import customtkinter
from fileTask import mAFolder, mAFile, multipleFinFol


customtkinter.set_appearance_mode("light")
app = customtkinter.CTk()
app.geometry("1000x800")

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


# Take input from user for multiple files and create them in a folder on desktop
fileNameEntry = customtkinter.CTkEntry(app, placeholder_text="File Name")
fileNameEntry.pack(pady=10)

folderNameEntry = customtkinter.CTkEntry(app, placeholder_text="Folder Name")
folderNameEntry.pack(pady=10)

numFilesEntry = customtkinter.CTkEntry(app, placeholder_text="Number of Files")
numFilesEntry.pack(pady=10)

# 3. Define the click handler taking ZERO arguments
def on_click():
    try:
        f_name = fileNameEntry.get()
        f_fol = folderNameEntry.get()
        n_files = int(numFilesEntry.get())
        
        if not f_name or not f_fol:
            print("Please fill all fields")
            return
            
        multipleFinFol(f_name, f_fol, n_files)
        print("Files and folder created successfully!")
    except ValueError:
        print("Please enter a valid number")

# 4. Bind the command directly with NO lambda
button = customtkinter.CTkButton(app, text="create multiple files", command=on_click)
button.pack(pady=20)

app.mainloop()