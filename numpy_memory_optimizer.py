# mem_analyzer.py
# A small, nerdy tool to check how much memory your NumPy arrays are actually eating.

import numpy as np
import os
import time
import sys
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path


YES = ["yes", "y"]
NO = ["no", "n"]
ERROR_LOG = {}
END_MSG = "\nProgram finished."


def clear_screen():
    """Clears the screen for a cleaner look. Works on Windows and Linux."""
    os.system("cls" if os.name == "nt" else "clear")


def current_time():
    """Returns the current time in Nigeria (UTC+1)."""
    nigeria_time = datetime.now(timezone.utc) + timedelta(hours=1)
    return nigeria_time.strftime("%Y-%m-%d %H:%M:%S")


def save_error(error_data):
    """
    Saves all collected errors into a JSON file.
    If the file doesn't exist, creates one. If it does, appends to it.
    """
    if error_data:
        path = Path("error_log.json")
        with path.open("a", encoding="utf-8") as fp:
            fp.write(json.dumps(error_data, indent=4) + "\n")


def show_saved_mem(num, current_bytes):
    """
    Shows how much memory was saved by using the chosen dtype.
    Compares current array memory with NumPy's default int64.
    """
    default_arr = np.arange(num)
    default_bytes = default_arr.nbytes
    saved_bytes = default_bytes - current_bytes
    saved_percent = (saved_bytes / default_bytes) * 100

    print(f"\nMemory saved: {saved_bytes} bytes ({saved_percent:.2f}%) compared to int64.")


def mem_req(r):
    """
    Runs a quick memory check on a NumPy array with `r` elements.
    It auto-picks the smallest unsigned int type (uint8, uint16, etc.)
    that can fit the values in the array.
    """
    arr = np.arange(r).astype(np.uint8)
    max_val = int(r - 1)
    min_dtype = np.min_scalar_type(max_val)

    print("\nAnalyzing..")
    time.sleep(2)
    clear_screen()

    print("=" * 40)
    print("🧠 NUMPY MEMORY ANALYZER (BEGINNER EDITION)")
    print("=" * 40)

    print(f"\nArray up to {max_val} needs min dtype: {min_dtype}.")
    print(f"Total bytes used: {arr.nbytes} bytes")
    print(f"Allocated dtype: uint{arr.itemsize * 8}")

    # Send the byte size back to whoever called this function
    return arr.nbytes


def again():
    """Asks if the user wants to run another test."""
    while True:
        print("\nWould you like to perform another memory analysis?")
        choice = input("(y/n): ").lower().strip()

        if not choice:
            print("\nInput field cannot be empty!")
            continue
        if choice in YES:
            return True
        elif choice in NO:
            return False
        else:
            print("\nDid you mean 'yes' or 'no'? Try again.")


def main():
    """
    This is the main entry point of the script.
    Keeps the app running, handles user input, and logs any weird errors.
    """
    while True:
        clear_screen()
        print("=" * 5, "NUMPY MEMORY ANALYZER TOOL", "=" * 5)
        try:
            print("\nEnter your desired number of elements or 'q' to quit")
            num = input("No. of array elements:  ").strip()

            if not num:
                continue
            if num.lower() == "q":
                save_error(ERROR_LOG)
                print(END_MSG)
                sys.exit()

            n = int(num)
            current_bytes = mem_req(n)
            show_saved_mem(n, current_bytes)

            if again():
                continue
            else:
                print(END_MSG)
                save_error(ERROR_LOG)
                sys.exit()

        except KeyboardInterrupt:
            print(f"\n{END_MSG}")
            save_error(ERROR_LOG)
            sys.exit()

        except ValueError:
            print("\nOops! Please enter a valid integer.")
            time.sleep(1.5)

        except Exception as e:
            timestamp = current_time()
            error_info = {
                "type": type(e).__name__,
                "message": str(e),
                "time": timestamp,
            }
            ERROR_LOG[len(ERROR_LOG) + 1] = error_info


if __name__ == "__main__":
    main()