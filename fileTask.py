from pathlib import Path

def mAFolder():
    FolderName = input("Enter the name of folder ")
    desktop = Path.home() / "Desktop"
    folderPath= Path(f"{desktop}/{FolderName}")
    folderPath.mkdir(parents=True , exist_ok=True)

def mAFile():
    FileName = input("Enter the name of file wiht extension ")
    desktop = Path.home() / "Desktop"
    filePath = desktop/FileName
    filePath.touch()

