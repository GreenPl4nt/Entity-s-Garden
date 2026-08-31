from Gui_functionality import MainApp
from pathlib import Path
import shutil
import os

APP_VERSION = "v1.1.3"

appdata_path = os.getenv("LOCALAPPDATA") 
appdata_path = Path(appdata_path) / "DBD Challenge Tracking App" / "Saves"

if appdata_path.is_dir():
    pass
else:
    if Path("./Saves").is_dir():
        shutil.rmtree(Path("./Saves"))
    killersdir = appdata_path / "Killers"
    survivordir = appdata_path / "Survivors"
    appdata_path.mkdir(parents= True, exist_ok=True)
    killersdir.mkdir(parents=True,exist_ok=True)
    survivordir.mkdir(parents=True,exist_ok=True)

    

app = MainApp(app_version=APP_VERSION)

app.mainloop()
