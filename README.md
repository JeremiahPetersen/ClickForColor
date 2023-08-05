# ClickForColor

## Overview:

This program is a simple color picker tool that allows users to capture the color under their mouse pointer using the F9 key. The captured color is shown in a GUI window with its hex value and is automatically copied to the clipboard. Additionally, the tool maintains a history of the last 10 colors picked and allows users to revisit and copy those colors to the clipboard.

## Required Libraries:

- **tkinter**: The standard Python GUI library. Used to create the graphical user interface.
- **pyperclip**: A module to access the clipboard, allowing the program to copy and paste text.
- **PIL (Pillow)**: A Python Imaging Library. Used to capture the screen and extract color data.
- **pynput**: Allows control and monitor of input devices (keyboard and mouse).

## Code Breakdown:

### Initialization and Main Window:

- **ColorPickerApp(tk.Tk)**: This class is derived from `tk.Tk` which represents the main window of a Tkinter GUI application.

    - Inside the `__init__` method:
        - We set the title and geometry for our main window.
        - `is_active`: This is a Boolean variable that keeps track of whether the color picker is active or not.
        - Various UI components are initialized and packed (like Checkbutton, Canvas, Label, Button).

### Keyboard Listener:

- `self.keyboard_listener`: A listener is set up to monitor keypress events. If F9 is pressed and the color picker is active, the color under the mouse pointer is captured, displayed, and copied to the clipboard.

### Capturing the Color:

- **on_keypress**: This function is triggered whenever a key is pressed. Inside this method:
    - We use `mouse.Controller().position` to get the current position of the mouse.
    - `ImageGrab.grab` captures a tiny portion of the screen where the mouse is.
    - The pixel color at that location is extracted and converted to a hex format.
    - The hex color is displayed in the GUI and passed to the `save_color` method.

### Storing and Copying the Color:

- **save_color**: This method takes the hex color, copies it to the clipboard, and adds it to the `color_history` list, which keeps a history of the last 10 colors.

- **copy_to_clipboard**: A utility method to copy a given color to the clipboard.

### Displaying Color History:

- **show_history**: When invoked, this method creates a new window (`Toplevel`) that displays all the colors in the `color_history` list. Each color is shown as a label with its hex value, and a button is provided next to each color. Clicking this button copies the respective color to the clipboard.

### Utility Functions:

- **text_color**: Determines whether the text color on a colored background should be white or black based on the brightness of the background color.

## How to Use the Tool:

1. Run the program to open the GUI.
2. Activate the color picker by checking the "Activate" checkbox.
3. Navigate to any screen or application. Press the F9 key to capture the color under the mouse pointer. This color will be displayed in the GUI and its hex code will be copied to the clipboard.
4. If you want to view the history of captured colors, click the "History" button in the GUI. This opens a new window with all your recent colors. Next to each color is a "Copy" button, which you can click to copy that particular color's hex code to the clipboard.

To run this tool, you need to have the mentioned libraries installed. You can install them using pip:

```bash
pip install tkinter pyperclip pillow pynput

