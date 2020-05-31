import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            ref, namee,cause, created = line.strip().split(";")
            self.users[ref] = (namee,cause, created)

        self.file.close()

    def get_user(self, ref):
        if ref in self.users:
            return self.users[ref]
        else:
            return -1

    def add_user(self, ref, namee, cause):
        if ref.strip() not in self.users:
            self.users[ref.strip()] = (namee.strip(),cause.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            return -1

    def validate(self, ref, namee,cause):
        if self.get_user(ref) != -1:
            return self.users[ref][0] == namee
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";"+ self.users[user][2] +"\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]