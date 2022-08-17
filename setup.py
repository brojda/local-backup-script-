import os, datetime, json
def setup():
    path = input("->> Enter the path to backup: ")
    if not(os.path.exists(path)):
        print("Path error")
        setup()
        return
    schedule = int(input("->> Enter the number of days between each backup to schedule: "))
    repeat = int(input("->> Enter the number of copy you want to have: "))
    data = {
    "path" : path,
    "schedule" : schedule,
    "repeat" : repeat
    }
    data = json.dumps(data)
    with open("config.json", "w") as config:
        config.write(data)
    startup_path = os.getcwd() + "\\pybackup.py"
    startup_command = "start " + startup_path
    with open("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\pybackup.bat","w") as f:
        f.write(startup_command)
def get_config():
    with open("config.json", "r") as config:
        data = json.loads(config.read())
        return data
def add_path():
    path = input('->> Enter your path: ')
    if os.path.exists(path):
        with open('paths.text', 'r') as paths:
            if path in paths:
                print("Your path is already exists !")
            else:
                with open('paths.text', 'a') as f:
                    f.write("\n")
                    f.write(path)
    else:
        print("Path error")
def schedule():
    schedule = int(input("->> Enter the number of days between each backup to schedule: "))
    data = get_config()
    data["schedule"] = schedule
    data = json.dumps(data)
    with open("config.json", "w") as config:
        config.write(data)
def set_repeat():
    repeat = int(input("->> Enter the number of copy you want to have: "))
    data = get_config()
    data["repeat"] = repeat
    data = json.dumps(data)
    with open("config.json", "w") as config:
        config.write(data)
def set_path():
    path = input("->> Enter the path to backup: ")
    data = get_config()
    data["path"] = path
    data = json.dumps(data)
    with open("config.json", "w") as config:
        config.write(data)

def main_loop():
    os.system("cls")
    print("""
    /////////// WELCOME TO PYBACKUP ///////////
    .                                         .
    .        __AUTHER__: IBRAHIM_JADAAN       .
    .        __LASTUPDAT__: 2022/5/15         .
    .        V: 0.1                           .
    ...........................................

    1) Add new path
    2) Schedule backup
    3) Set copy repeat
    4) set backup path
    5) Exit
    """)
    cmd = input('->> cmd: ')
    while cmd != "5":
        if cmd == "1":
            add_path()
        elif cmd == "2":
            schedule()
        elif cmd == "3":
            set_repeat()
        elif cmd == "4":
            set_path()
        cmd = input('->> cmd: ')
if not(os.path.exists("config.json")):
    setup()
main_loop()
