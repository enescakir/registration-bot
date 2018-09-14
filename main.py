from registration import Registration
import datetime
import time

STUDENT_ID = "STUDENT_ID"
STUDENT_PASSWORD = "STUDENT_PASSWORD"

reg = Registration(STUDENT_ID, STUDENT_PASSWORD)
reg.set_debug(True)
if reg.login():
    start = time.time()
    count = 1
    while time.time() - start < 55:
        print("\n---------- " + str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')) + "---------- " + STUDENT_ID)
        for i in range(11,15):
            reg.change_section("HTR", "312", str(i))
        reg.take_course("CMPE", "493", "01")
        count += 1
        time.sleep(2)
    print("\n")
