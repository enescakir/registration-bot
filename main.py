from registration import Registration
import time
import random

STUDENT_ID = "STUDENT_ID"
STUDENT_PASSWORD = "STUDENT_PASSWORD"

reg = Registration(STUDENT_ID, STUDENT_PASSWORD)
reg.set_debug(True)

reg.get_quota("HUM", "102", 11)

if reg.login():
    while True:
        reg.take_course("CMPE", "493", 1)

        for i in range(11, 14):
            reg.change_section("HTR", "312", i)

        time.sleep(random.randint(30, 90))
