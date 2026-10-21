from pathlib import Path


# make a folder on desktop
def mAFolder(folderName , label):
    desktop = Path.home() / "Desktop"
    folderPath= Path(f"{desktop}/{folderName}")
    folderPath.mkdir(parents=True , exist_ok=True)
    label.configure(text=f"Folder '{folderName}' created successfully!")

# make a file on desktop
def mAFile(fileName,label):
    desktop = Path.home() / "Desktop"
    filePath = desktop/fileName
    if filePath.exists():
        label.configure(text=f"File '{fileName}' already exists!")
    else:
        filePath.touch()
        label.configure(text=f"Folder '{fileName}' created successfully!")

# make multiple files in a folder on desktop
def multipleFinFol(fileName_, folderName_, numFiles ):
    desktop = Path.home() / "Desktop"
    for i in range(1, numFiles + 1):
        mulFile = Path(f"{desktop}/{folderName_}/{i}_{fileName_}")
        mulFile.parent.mkdir(parents=True , exist_ok=True)
        mulFile.touch()
