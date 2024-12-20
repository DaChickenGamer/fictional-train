import time
from pynput.keyboard import Controller
import pygetwindow as gw

keyboard = Controller()


def check_if_active_window(window_title):
    active_window = gw.getActiveWindow()
    if active_window and window_title in active_window.title:
        return True
    return False


program_running = True

while program_running:
    try:
        target_window_title = input("What application do you want to check: ")

        if not target_window_title:
            raise ValueError("Window title cannot be empty.")

        if not any(window.title and target_window_title in window.title for window in gw.getAllWindows()):
            raise ValueError(f"No window with title containing '{target_window_title}' is currently open.")

        time_to_run = input("How many seconds do you want to check: ")
        time_to_run = float(time_to_run)

        if time_to_run <= 0:
            raise ValueError("Time to run must be a positive number.")

        start_time = time.time()

        while time.time() - start_time < time_to_run:
            active_window = gw.getActiveWindow()
            if check_if_active_window(target_window_title):
                keyboard.press(' ')
                keyboard.release(' ')
            time.sleep(0.0001)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
