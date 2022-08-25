import tkinter


class LoginWindow(tkinter.Toplevel):

    # Constructor for Tkinter class
    def __init__(self, parent):
        super().__init__(self, parent)

        _width = 925
        _height = 500
        _pos_x = 200
        _pos_y = 200
        _bg_color = "#fff"

        # Set properties
        self.wm_title("Tkinter App")
        self.wm_geometry(f"{_width}x{_height}+{_pos_x}+{_pos_y}")
        self.configure(bg=_bg_color)
        self.wm_resizable(False, False)

        # Create an image object
        src_img = tkinter.PhotoImage(file="login.png")

        # Create the label image object
        bg_image = tkinter.Label(self, image=src_img, bg=_bg_color)

        # Put the image at the side of the container
        bg_image.place(x=50, y=50)

        self.create_form_frame(self)

    def create_form_frame(container):
        # Declare the properties for the frame
        _width = 350
        _height = 350
        _pos_x = 480
        _pos_y = 70
        _bg_color = "red"

        # Create the frame inside the container
        frame = tkinter.Frame(
            container, width=_width, height=_height, bg=_bg_color
        )
        # Place the frame at the coordinates x y
        frame.place(x=_pos_x, y=_pos_y)

        # Create the fields for this form frame
        heading_bg = "#fff"
        heading_fg = "#57a1f8"
        heading_text = "Sign in"
        heading = tkinter.Label(
            frame, text=heading_text, bg=heading_bg, fg=heading_fg
        )
