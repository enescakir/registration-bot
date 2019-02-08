import requests


class Registration:
    username = ""
    password = ""
    debug = False
    session = requests.Session()

    def __init__(self, u, p):
        self.username = u
        self.password = p

    def set_debug(self, d):
        self.debug = d

    def log(self, message):
        if self.debug:
            print(message)

    def login(self):
        self.log("-- LOGIN")
        r = self.session.post('https://registration.boun.edu.tr/scripts/loginst.asp',
                              data={'user_id': self.username, 'user_pass': self.password}).text
        if "hatakullanici" in r:
            self.log("---- Hatali giris bilgisi")
            return False
        elif "multiple times" in r:
            self.log("---- 30 saniyede birden fazla giris denemesi")
            return False
        else:
            self.log("---- Giris basarili")
            return True

    def change_section(self, abbr, code, section):
        course = str(abbr) + " " + str(code) + "." + str(section)
        r = self.session.post('https://registration.boun.edu.tr/scripts/secchaact.asp', data={'R1': course}).text
        if "You cannot take this course" in r:
            self.log(course + " - Alinamadi")
            return False
        elif "Session Expired" in r:
            self.log(course + " - Tekrar giris gerekiyor")
            return False
        else:
            self.log("!!!! " + course + " - Aldi")
            return True

    def take_course(self, abbr, code, section, non_credit=False):
        rnc1 = 'N'
        if non_credit:
            rnc1 = 'NC'
        course = str(abbr) + " " + str(code) + "." + str(section)
        r = self.session.post('https://registration.boun.edu.tr/scripts/studentaction.asp', data={
            'abbr1': str(abbr),
            'code1': str(code),
            'section1': str(section),
            'rnc1': str(rnc1),
            'B1': 'Quick Add'
        }).text
        if "course couldn't be added to your list" in r:
            self.log(course + " - Alinamadi")
            return False
        elif "Session Expired" in r:
            self.log(course + " - Tekrar giris gerekiyor")
            return False
        else:
            self.log("!!!! " + course + " - Aldi")
            return True
