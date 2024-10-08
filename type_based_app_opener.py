import subprocess
import os
import keyboard
from datetime import datetime
import sys

# Dictionary to map application names to their commands
app_commands = {
    "notepad": "notepad",
    "calculator": "calc",
    "browser": "open brave",
    "file_explorer": "explorer",
    "valorant": "Valorant"
}

def greet_user():
    """Greet the user based on the time of day and tell the time."""
    current_time = datetime.now()
    hour = current_time.hour
    
    if 5 <= hour < 12:
        greeting = "Good morning!"
    elif 12 <= hour < 17:
        greeting = "Good afternoon!"
    elif 17 <= hour < 21:
        greeting = "Good evening!"
    else:
        greeting = "Good night!"
    
    time_str = current_time.strftime("%I:%M %p")  # Format time in HH:MM AM/PM
    print(f"{greeting} The current time is {time_str}.")

def open_application(app_type):
    # Convert the input to lowercase for consistent matching
    app_type = app_type.lower()
    
    # Look up the command based on the app_type
    if app_type in app_commands:
        try:
            subprocess.run(app_commands[app_type], shell=True)
            print(f"{app_type.capitalize()} opened successfully!")
        except Exception as e:
            print(f"Failed to open {app_type}: {str(e)}")
    else:
        print(f"Application type '{app_type}' not recognized.")

def restart_program():
    """Restart the current program."""
    print("Restarting the program...")
    python = sys.executable  # Path to the Python interpreter
    os.execl(python, python, *sys.argv)  # Restart the script

def main():
    # Greet the user with time
    greet_user()

    # Example usage
    while True:
        app_type = input("Enter the application to open (notepad, calculator, browser, file_explorer, valorant): ").lower()
        open_application(app_type)

# Set up a keyboard shortcut for restarting the program (Ctrl + R)
keyboard.add_hotkey('ctrl+r', restart_program)

if __name__ == "__main__":
    main()
