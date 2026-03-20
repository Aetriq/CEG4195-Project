# CEG4195 Project
# Author: Alex Gordon
# Last revision: 3-19-26

# ===== 1.0 DEPENDENCIES & MACROS ===== 
#!/usr/bin/env python3
import serial
import time
import requests
import sys

# ===== 2.0 CONFIG AND GLOBALS ===== 
SERIAL_PORT = '/dev/ttyUSB0' # Verify this on your klipper host!
BAUD_RATE = 115200
MOONRAKER_URL = "http://localhost:7125/printer/print/pause"
TIMEOUT_SECONDS = 10

# ===== 3.0 FUNCTIONS ===== 
def trigger_pause():
    try:
        response = requests.post(MOONRAKER_URL)
        if response.status_code == 200:
            print("PRINT PAUSED SUCCESSFULLY.")
        else:
            print(f"FAILED TO PAUSE: {response.status_code}")
    except Exception as e:
        print(f"CONNECTION ERR: {e}")

def main():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
        time.sleep(2)
        
        ser.write(b"CHECK_NOZZLE\n")
        
        start_time = time.time()
        
        while (time.time() - start_time) < TIMEOUT_SECONDS:
            if ser.in_waiting > 0:
                response = ser.readline().decode('utf-8').strip()
                
                if response in ["CLEAN", "EXTRUDED"]:
                    print(f"SAFE STATE CONFIRMED: {response}")
                    sys.exit(0)
                    
                elif response == "BLOB":
                    print("CRITICAL: BLOB DETECTED! Pausing...")
                    trigger_pause()
                    sys.exit(1)
                    
                elif response in ["CAM_FAIL", "CAP_FAIL", "ML_ERR"]:
                    print(f"HW ERR: {response}. PLEASE CHECK CAMERA")
                    sys.exit(2)
                    
        print("HW ERR: ESP32 TIMED OUT")
        sys.exit(3)
        
    except serial.SerialException as e:
        print(f"HW ERR: SERIAL PORT CONNECTION, {e}")
        sys.exit(4)

if __name__ == "__main__":
    main()