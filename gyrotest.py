from pyjoycon import GyroTrackingJoyCon, get_R_id
import time
import math
joycon_id = get_R_id()
joycon = GyroTrackingJoyCon(*joycon_id)
joycon.calibrate(seconds=10)
time.sleep(10)  # Allow time for calibration
for i in range(300):
    print("joycon pointer:  ", joycon.pointer)
    print("joycon rotation: ", (math.degrees(joycon.rotation.x), math.degrees(joycon.rotation.y), math.degrees(joycon.rotation.z)))
    print("joycon direction:", (math.degrees(joycon.direction.x), math.degrees(joycon.direction.y), math.degrees(joycon.direction.z)))
    print()
    time.sleep(3)