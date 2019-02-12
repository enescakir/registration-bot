import requests
from enum import Enum
import datetime
from bs4 import BeautifulSoup


def change_style(string, style):
    if style == "green":
        return "\033[92m{}\033[00m".format(string)
    elif style == "red":
        return "\033[31m{}\033[00m".format(string)
    elif style == "blue":
        return "\033[36m{}\033[00m".format(string)
    elif style == "info":
        return "\033[92m \033[01m{}\033[00m".format(string)
    elif style == "bold":
        return "\033[01m{}\033[00m".format(string)
    elif style == "tag":
        return "\033[97m\033[104m{}\033[00m".format(string)
    elif style == "time":
        return "\033[01m\033[97m\033[101m{}\033[00m".format(string)
    return str


class RegistrationError(Enum):
    """ Represents type of error """
    UNKNOWN = 1
    WRONG_CREDENTIALS = 2
    TOO_MANY_LOGIN = 3
    SESSION_EXPIRED = 4
    NOT_TAKEN = 5
    WRONG_USER = 6


class Registration:
    username = ""
    password = ""
    debug = False
    session = requests.Session()
    error = None
    base_url = "https://registration.boun.edu.tr/scripts/"

    def __init__(self, u, p):
        self.username = u
        self.password = p

    def set_debug(self, d):
        self.debug = d

    def error_log(self, message, tag):
        self.log(change_style(message, 'red'), tag)

    def success_log(self, message, tag):
        self.log(change_style(message, 'green'), tag)

    def info_log(self, message, tag):
        self.log(change_style(message, 'blue'), tag)

    def log(self, message, tag):
        if self.debug:
            print(
                "{}{} {}".format(
                    change_style(
                        (" [{}] ".format(str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))).ljust(20),
                        'time'),
                    change_style((" " + tag + " ").ljust(13), 'tag'),
                    message
                )
            )

    def full_url(self, url):
        return self.base_url + url

    def login(self):
        self.info_log("Start login", "LOGIN")
        r = self.session.post(self.full_url("loginst.asp"),
                              data={'user_id': self.username, 'user_pass': self.password}).text
        if "hatakullanici" in r:
            self.error_log("Wrong credentials", "LOGIN")
            self.error = RegistrationError.WRONG_CREDENTIALS
            return False
        elif "Wrong User" in r:
            self.error_log("Wrong user ID and password", "LOGIN")
            self.error = RegistrationError.WRONG_USER
            return False
        elif "multiple times" in r:
            self.error_log("Too many login in 30 seconds", "LOGIN")
            self.error = RegistrationError.TOO_MANY_LOGIN
            return False

        self.success_log("Successfully login", "LOGIN")
        return True

    def change_section(self, abbr, code, section):
        section = str(section).zfill(2)
        course = str(abbr) + " " + str(code) + "." + str(section)
        r = self.session.post(self.full_url("secchaact.asp"), data={'R1': course}).text
        if "You cannot take this course" in r:
            self.error_log("Not taken", course)
            self.error = RegistrationError.NOT_TAKEN
            return False
        elif "Session Expired" in r:
            self.error_log("Session expired. Please login again", course)
            self.error = RegistrationError.SESSION_EXPIRED
            return False
        else:
            self.success_log("TAKEN", course)
            return True

    def take_course(self, abbr, code, section, non_credit=False, repeat_with=None):
        section = str(section).zfill(2)
        course = str(abbr) + " " + str(code) + "." + str(section)

        data = {
            'abbr1': str(abbr),
            'code1': str(code),
            'section1': str(section),
            'rnc1': 'NC' if non_credit else 'N',
            'rcourse1': repeat_with if repeat_with else '',
            'B1': 'Quick Add'
        }

        r = self.session.post(self.full_url("studentaction.asp"), data=data).text

        if "course couldn't be added to your list" in r:
            self.error_log("Not taken", course)
            self.error = RegistrationError.NOT_TAKEN
            return False
        elif "Session Expired" in r:
            self.error_log("Session expired. Please login again", course)
            self.error = RegistrationError.SESSION_EXPIRED
            return False
        else:
            self.success_log("TAKEN", course)
            return True

    def get_quota(self, abbr, code, section):
        quotas = {"departmental": [], "class": []}
        section = str(section).zfill(2)
        course = str(abbr) + " " + str(code) + "." + str(section)

        data = {
            'abbr': str(abbr),
            'code': str(code),
            'section': str(section)
        }

        r = self.session.post(self.full_url("quotasearch.asp"), data=data).text
        soup = BeautifulSoup(r, 'html.parser')
        tables = soup.find_all('table')[:2]
        departments = tables[0].find_all(class_='schtd')
        for department in departments:
            columns = department.find_all('td')
            quotas['departmental'].append({
                "department": columns[0].text.encode('ascii', errors='ignore').decode(),
                "statu": columns[1].text.encode('ascii', errors='ignore').decode(),
                "quota": int(columns[2].text),
                "current": int(columns[3].text)
            })
        grades = tables[1].find_all(class_='schtd')
        for grade in grades:
            columns = grade.find_all('td')
            quotas['class'].append({
                "class": int(columns[0].text),
                "quota": int(columns[1].text),
                "current": int(columns[2].text)
            })

        return quotas
