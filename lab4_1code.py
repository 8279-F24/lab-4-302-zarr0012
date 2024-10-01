import time
from adafruit_circuitplayground import cp

# Set initial brightness and auto write to False
cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

def set_color(color):
    max_val = 255  # Maximum intensity for the color
    while max_val > 0:
        for i in range(10):
            if color == 1:
                cp.pixels[i] = (max_val, 0, 0)  # Red
            elif color == 2:
                cp.pixels[i] = (0, max_val, 0)  # Green
            elif color == 3:
                cp.pixels[i] = (0, 0, max_val)  # Blue
        cp.pixels.show()
        time.sleep(0.3)
        max_val -= 1  # Decrease brightness

def show_menu():
    print("\nSelect an option:")
    print("1. Red")
    print("2. Green")
    print("3. Blue")
    print("Press 'q' to quit.")

# Main loop to keep the program running until the user decides to quit
while True:
    show_menu()
    user_input = input("Enter your choice: ").strip()

    # If the user chooses to quit
    if user_input.lower() == 'q':
        print("Exiting program...")
        cp.pixels.fill((0, 0, 0))  # Turn off all LEDs when exiting
        cp.pixels.show()
        break

    # Try to cast input to an integer and handle invalid input
    try:
        choice = int(user_input)
        if choice in [1, 2, 3]:
            set_color(choice)
        else:
            print("Invalid choice! Please select 1, 2, or 3.")
    except ValueError:
        print("Invalid input! Please enter a number or 'q' to quit.")
