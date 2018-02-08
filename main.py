from registiration import Registiration
import datetime;
import time

reg = Registiration("STUDENT_ID", "STUDENT_PASSWORD")
reg.setDebug(True)
if reg.login():
    start = time.time()
    count = 1
    while (time.time() - start < 55):
        print("\n---------- " + str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))
        for i in range(11,15):
            reg.changeSection("HTR", "312", str(i))
        reg.takeCourse("CMPE", "493", "01")
        count += 1
        time.sleep(2)
    print("\n")
