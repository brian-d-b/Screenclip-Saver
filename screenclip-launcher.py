import subprocess
import time
import os
from PIL import ImageGrab
from datetime import datetime

# Define the path to the PowerShell script
script_path = r'.\screenclip.ps1'

# Run the PowerShell script
subprocess.run(['powershell', '-File', script_path])

# Wait for a few seconds to allow the screenshot to be taken and placed on the clipboard
time.sleep(12)

# Check if there is an image on the clipboard
image = ImageGrab.grabclipboard()

if isinstance(image, ImageGrab.Image.Image):
    # Get the current date and time
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Define the path where the screenshot will be saved, with the date and time appended
    screenshot_path = rf'.\Screenshots\screenshot_{current_time}.png'
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    
    # Save the image from the clipboard to the desired location
    image.save(screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")
else:
    print("No image found on the clipboard.")
