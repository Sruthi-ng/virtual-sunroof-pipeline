# src/sunroof_controller.py
import time

class SunroofController:
    """
    A Virtual ECU for a Sunroof.
    Simulates the hardware behavior without physical motors.
    """
    
    def __init__(self):
        # Initial State
        self.status = "CLOSED"
        self.is_locked = False
        print("[ECU] System Initialized. Sunroof is CLOSED.")

    def get_status(self):
        return self.status

    def lock_vehicle(self):
        self.is_locked = True
        print("[ECU] Vehicle Locked.")

    def unlock_vehicle(self):
        self.is_locked = False
        print("[ECU] Vehicle Unlocked.")

    def open_sunroof(self):
        """Simulates sending a signal to the motor to OPEN"""
        print("[ECU] Signal Received: OPEN")
        
        if self.is_locked:
            print("[ECU] Error: Cannot open while vehicle is locked.")
            return "ERROR_LOCKED"
        
        if self.status == "OPEN":
            print("[ECU] Warning: Already open.")
            return "ALREADY_OPEN"

        # Simulate the time it takes for a motor to move (Virtual Hardware Lag)
        # In real HIL, this might be 5 seconds. In vHIL, we can make it fast (0.1s)
        time.sleep(0.1) 
        
        self.status = "OPEN"
        print("[ECU] Action Complete: Sunroof is now OPEN.")
        return "SUCCESS"

    def close_sunroof(self):
        """Simulates sending a signal to the motor to CLOSE"""
        print("[ECU] Signal Received: CLOSE")
        
        time.sleep(0.1)
        self.status = "CLOSED"
        print("[ECU] Action Complete: Sunroof is now CLOSED.")
        return "SUCCESS"