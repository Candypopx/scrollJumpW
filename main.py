from pynput import mouse, keyboard

# Global variable to keep track of the current scroll position
current_scroll_position = 0

def on_scroll(x, y, dx, dy):
    global current_scroll_position

    # Update the current scroll position
    current_scroll_position += dy

    # Check if scrolling down
    if dy > 0:
        # Simulate pressing the SPACE key
        keyboard.Controller().press('w')
        keyboard.Controller().release('w')

# Set up the listener for mouse scroll events
mouse_listener = mouse.Listener(on_scroll=on_scroll)
mouse_listener.start()

print("start simulate w when scroll up to tap strafe!")

# Keep the script running
mouse_listener.join()