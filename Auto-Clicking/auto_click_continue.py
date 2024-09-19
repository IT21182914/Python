import pyautogui
import time
import keyboard  # For detecting key presses

# Define the coordinates for the "Continue" button at different possible locations
locations = [(1068, 583), (964, 566), (913, 525)]

# Function to click at each location


def click_locations():
    for location in locations:
        # Move the mouse to the specified location
        pyautogui.moveTo(location[0], location[1], duration=0.5)
        # Click at the current location
        pyautogui.click()
        # Wait for 1 second before moving to the next location
        time.sleep(1)


# Run the click loop every 5 seconds and allow stopping via hotkey
try:
    while True:
        # Activate the Ezviz window (make sure it is the active window)
        window = pyautogui.getWindowsWithTitle('Ezviz')
        if window:
            window[0].activate()

        # Check if 'q' is pressed to stop the script
        if keyboard.is_pressed('q'):
            print("Stopping the script...")
            break

        # Click through the defined locations
        click_locations()

        # Wait for 5 seconds before repeating the cycle
        time.sleep(5)
except KeyboardInterrupt:
    print("Script stopped.")
