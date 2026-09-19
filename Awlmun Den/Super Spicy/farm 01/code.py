import time
import usb_hid

# Safety net: Ensure boot.py worked before trying to grab the gamepad
try:
    gamepad = usb_hid.devices[0]
except IndexError:
    print("Gamepad not found. Check boot.py!")
    while True:
        time.sleep(1)

# Helper function to tap buttons cleanly
def tap_button(btn_0=0, btn_1=0, dpad=8, lx=128, ly=128, rx=128, ry=128, press_time=0.1, release_time=0.1):
    report = bytearray(8)
    report[0] = btn_0
    report[1] = btn_1
    report[2] = dpad    # (0=Up, 2=Right, 4=Down, 6=Left, 8=Neutral)
    report[3] = lx      # Left Stick X (0=Left, 128=Center, 255=Right)
    report[4] = ly      # Left Stick Y (0=Up, 128=Center, 255=Down)
    report[5] = rx      # Right Stick X (0=Left, 128=Center, 255=Right)
    report[6] = ry      # Right Stick Y (0=Up, 128=Center, 255=Down)
    
    # Press
    gamepad.send_report(report)
    time.sleep(press_time)
    
    # Release everything
    report[0] = 0
    report[1] = 0
    report[2] = 8
    report[3] = 128
    report[4] = 128
    report[5] = 128
    report[6] = 128
    gamepad.send_report(report)
    time.sleep(release_time)

# =====================
# Buttons
# =====================
# For btn_0 (0=Release)
Y  = 1
B  = 2
A  = 4
X  = 8
L  = 16
R  = 32
ZL = 64
ZR = 128

# For btn_1 (0=Release)
MINUS = 1
PLUS  = 2
L3    = 4
R3    = 8

# For dpad
DPAD_UP    = 0
DPAD_RIGHT = 2
DPAD_DOWN  = 4
DPAD_LEFT  = 6
DPAD_NONE  = 8

# ==========================================
# 1. THE PLUG-IN DELAY
# Wait 5 seconds to ensure the Nintendo Switch has fully 
# registered the USB device before sending inputs.
# ==========================================
time.sleep(5.0)

# ==========================================
# 2. CONNECTION WAKE-UP SEQUENCE
# ==========================================
# Press A to connect the controller
tap_button(btn_0=A, release_time=1.5)
# Press A again to confirm/close the prompt
tap_button(btn_0=A, release_time=3.0)
# Press A again to confirm/close the prompt
tap_button(btn_0=A, release_time=3.0)
# Press A again to confirm/close the prompt
tap_button(btn_0=A, release_time=1.0)
tap_button(btn_0=A, release_time=1.0)


# ============================================================
# 3. INFINITE FARM
# ============================================================
while True:
    # Raid on Super Spicy!
    tap_button(btn_0=A, release_time=2)
    
    # Skip intro
    tap_button(btn_0=A, release_time=7)


    
    # Jump
    tap_button(btn_0=B)
    
    # Armor jump
    tap_button(btn_0=B, ly=0)
    
    # Jump Bomb 1
    tap_button(btn_0=L, ly=0)

    # Keep floating forward
    tap_button(ly=0, press_time=1)

    # Dash Bomb 1
    tap_button(btn_0=R, ly=0)

    # Keep floating forward
    tap_button(ly=0, press_time=1)

    # Air jump
    tap_button(btn_0=B, ly=0)
    
    # Jump Bomb 2
    tap_button(btn_0=L, ly=0)

    # Keep floating forward
    tap_button(ly=0, press_time=1)

    # Dash Bomb 2
    tap_button(btn_0=R, ly=0)

    # Keep floating forward
    tap_button(ly=0, press_time=1)

    # Jump Bomb 3
    tap_button(btn_0=L, ly=0)

    # Keep floating forward
    tap_button(ly=0, press_time=1)

    # Dash Bomb 3
    tap_button(btn_0=R, ly=0)

    # Keep floating forward
    tap_button(ly=0, press_time=3)

    # Walk right shooting till ends (Ensure the enemy is finished off)
    tap_button(btn_0=ZR, lx=255, press_time=3)

    # Walk left shooting till ends (Ensure the enemy is finished off)
    tap_button(btn_0=ZR, lx=0, press_time=5)

    # Walk right shooting (find treasure position)
    tap_button(btn_0=ZR, lx=255, press_time=2.5)

    # Walk forward shooting (collect golden eggs)
    tap_button(btn_0=ZR, ly=0, press_time=3.5)

    # Walk right shooting (collect golden eggs)
    tap_button(btn_0=ZR, lx=255, press_time=3.5)

    # Walk left shooting (go back)
    tap_button(btn_0=ZR, lx=0, press_time=3.5)

    # Walk backward shooting (touch treasure)
    tap_button(btn_0=ZR, ly=255, press_time=3.5)



    # Wait for victory scene
    time.sleep(10)

    # Next (Clear! screen)
    tap_button(btn_0=A, release_time=1.5)

    # Open (Treasure! 10s if relic)
    tap_button(btn_0=A, release_time=10)

    # Next (reveal treasure item. 8s if relic combine)
    tap_button(btn_0=A, release_time=8)
    
    # Back (What you got / relic collection if relic)
    tap_button(btn_0=B, release_time=1.5)

    # Back (jump/ What you got if relic)
    tap_button(btn_0=B, release_time=1.5)

    # Open Menu
    tap_button(btn_0=X, release_time=1)

    # Select Treasure Map
    tap_button(btn_0=A, release_time=1)

    # Select Awlmun Den
    tap_button(btn_0=A, release_time=1)
