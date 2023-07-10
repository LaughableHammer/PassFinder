# Code heavily inspired from https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python?rq=3

import tkinter as tk


class ToolTip(object):
    """Allows creation of tooltips for input fields

    Args:
        widget (Tkinter widget): The widget to which the tooltip will be attached
        text (str): The text to be displayed in the tooltip
    """

    def __init__(self, widget, text):
        """Initialize the ToolTip instance

        Args:
            widget (Tkinter widget): The widget to which the tooltip will be attached
            text (str): The text to be displayed in the tooltip
        """
        self.widget = widget
        self.text = text
        self.tooltipwindow = None
        self.tooltip_id = None  # To store the tooltip timer ID

        def enter(event):
            """Handle the mouse entering the widget

            Args:
                event (Tkinter event): The event object
            """
            self.tooltip_id = self.widget.after(
                1500, self.show_tooltip
            )  # Delay of 1500 milliseconds

        def leave(event):
            """Handle the mouse leaving the widget

            Args:
                event (Tkinter event): The event object
            """
            self.hide_tooltip()
            if self.tooltip_id is not None:
                self.widget.after_cancel(self.tooltip_id)  # Cancel the tooltip timer

        widget.bind("<Enter>", enter)
        widget.bind("<Leave>", leave)

    def show_tooltip(self):
        """Display the tooltip window"""
        if self.tooltipwindow is not None:
            return

        y, _, _ = (
            self.widget.winfo_rooty(),
            self.widget.winfo_width(),
            self.widget.winfo_height(),
        )

        cursor_x = (
            self.widget.winfo_pointerx()
        )  # Add an offset to avoid overlap with the cursor
        cursor_y = y - 20

        self.tooltipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(
            1
        )  # window without border and no normal means of closing
        tw.wm_geometry(f"+{cursor_x}+{cursor_y}")

        label = tk.Label(
            tw, text=self.text, background="#757575", relief="solid", borderwidth=1
        )
        label.pack(ipadx=1)

    def hide_tooltip(self):
        """Hide the tooltip window"""
        if self.tooltipwindow is None:
            return

        tipwin = self.tooltipwindow
        tipwin.destroy()
        self.tooltipwindow = None
