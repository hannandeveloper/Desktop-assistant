from pathlib import Path

# make a folder on desktop
def mAFolder(folderName):
    desktop = Path.home() / "Desktop"
    folderPath= Path(f"{desktop}/{folderName}")
    folderPath.mkdir(parents=True , exist_ok=True)

# make a file on desktop
def mAFile(fileName):
    desktop = Path.home() / "Desktop"
    filePath = desktop/fileName
    if filePath.exists():
        return f"{fileName} already exists on Desktop"
    else:
        filePath.touch()
        return f"{fileName} created successfully on Desktop"

# make multiple files in a folder on desktop
def multipleFinFol(fileName_, folderName_, numFiles):
    desktop = Path.home() / "Desktop"
    for i in range(1, numFiles + 1):
        mulFile = Path(f"{desktop}/{folderName_}/{i}_{fileName_}")
        mulFile.parent.mkdir(parents=True , exist_ok=True)
        mulFile.touch()
