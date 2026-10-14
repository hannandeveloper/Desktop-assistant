from pathlib import Path

def mAFolder():
    FolderName = input("Enter the name of folder ")
    desktop = Path.home() / "Desktop"
    folderPath= Path(f"{desktop}/{FolderName}")
    folderPath.mkdir(parents=True , exist_ok=True)

def mAFile():
    FileName = input("Enter the name of file with extension ")
    desktop = Path.home() / "Desktop"
    filePath = desktop/FileName
    if filePath.exists():
        print(f"{FileName} already exists")
    else:
         filePath.touch()
  
def multipleFinFol():
    fileName = input("Enter the name of file with extension ")
    folderName = input("Enter the name of folder ")
    n = int(input("Enter number of file "))
    desktop = Path.home() / "Desktop"
    for i in range(1,n+1):
        mulFile = Path(f"{desktop}/{folderName}/{i}_{fileName}")
        mulFile.parent.mkdir(parents=True , exist_ok=True)
        mulFile.touch()
