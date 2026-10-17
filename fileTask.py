from pathlib import Path

def mAFolder(folderName):
    # FolderName = input("Enter the name of folder ")
    desktop = Path.home() / "Desktop"
    folderPath= Path(f"{desktop}/{folderName}")
    folderPath.mkdir(parents=True , exist_ok=True)
    return f"{folderName} folder created successfully on Desktop"

def mAFile(fileName):
    
    desktop = Path.home() / "Desktop"
    filePath = desktop/fileName
    if filePath.exists():
        return f"{fileName} already exists on Desktop"
    else:
        filePath.touch()
        return f"{fileName} created successfully on Desktop"

def multipleFinFol():
    fileName = input("Enter the name of file with extension ")
    folderName = input("Enter the name of folder ")
    n = int(input("Enter number of file "))
    desktop = Path.home() / "Desktop"
    for i in range(1,n+1):
        mulFile = Path(f"{desktop}/{folderName}/{i}_{fileName}")
        mulFile.parent.mkdir(parents=True , exist_ok=True)
        mulFile.touch()
