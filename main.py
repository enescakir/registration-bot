from registration import Registration
import time
import random

STUDENT_ID = "STUDENT_ID"
STUDENT_PASSWORD = "STUDENT_PASSWORD"

CLASS_ABBR = "CHE"
CLASS_CODE = "202"
CLASS_SECTION = "1"

reg = Registration(STUDENT_ID, STUDENT_PASSWORD)
reg.set_debug(True)

# while(reg.check_quota(CLASS_ABBR, CLASS_CODE, CLASS_SECTION, "CHEMICAL ENGINEERING", 1, "SEE")):
#     if reg.login():
#         reg.take_course(CLASS_ABBR, CLASS_CODE, CLASS_SECTION)
#     time.sleep(random.randint(30, 90))