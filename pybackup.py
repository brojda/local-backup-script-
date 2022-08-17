import json, os, datetime, shutil
class backup:
    def __init__(self):
        self.data = self.get_config()
        self.path = self.data["path"]
        self.repeat = self.data['repeat']
        self.schedule = self.data['schedule']
        self.today = datetime.datetime.today()
        self.backups = os.listdir(self.path)
        self.backup_path = os.path.join(self.path, str(datetime.date.today()))
        if len(self.backups) > 0:
            self.last_backup = datetime.datetime.strptime(self.backups[-1], '%Y-%m-%d')
    def get_config(self):
        with open("config.json", "r") as config:
            data = json.loads(config.read())
            return data
    def check(self):
        if len(self.backups) > 0:
            if (self.today - self.last_backup).days >= self.schedule:
                self.backup()
            else:
                input("No backup today ^ ^")
        else:
            self.backup()
    def remove(self, path):
        if os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
    def backup(self):
        if len(self.backups) > 0:
            if self.repeat <= len(self.backups):
                path = os.path.join(self.path, self.backups[0])
                self.remove(path)
        self.creat()
        input("Backuped.....")
    def copy(self, path, to):
        if os.path.isfile(path):
            self.remove(to)
            shutil.copy(path, to)
        elif os.path.isdir(path):
            self.remove(to)
            shutil.copytree(path, to)
    def creat(self):
        os.mkdir(self.backup_path)
        with open("paths.text", 'r') as paths:
            for line in paths:
                path = line.rstrip()
                if path:
                    path_name = path.split("\\")[-1]
                    new_path = os.path.join(self.backup_path, path_name)
                    self.copy(path, new_path)
backup = backup()
backup.check()
