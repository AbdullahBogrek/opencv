import tkinter as tk
import tkinter.ttk as ttk
import PIL.Image
import PIL.ImageTk

# Internals
from .base_widget import BaseWidget
from .cam import Camera

# We inherit all components and methods in "Basewidget"
class Base(BaseWidget):
    def __init__(self, *args, **kwargs):
        BaseWidget.__init__(self, *args, **kwargs)

        self.label_scale_thresh_var = tk.IntVar(self.frame6, value = 0)
        self.label_scale_thresh.configure(variable = self.label_scale_thresh_var)
        self.label_thresh_res['text'] = str(self.label_scale_thresh_var.get())

        colorspace = ['BGR', 'HSV', 'Gray']
        self.combobox_colorspace.configure(values = colorspace)

    def start(self):
        try:
            self.camera = Camera(0)
            self.capture()
        except Exception as exc:
            self.txt_log.insert('0.0', f"{exc}")

    def get_thresh_val(self, event = None):
        val = self.label_scale_thresh_var.get()
        self.label_thresh_res['text'] = str(val)

    def select_colorspace(self, event = None):
        print(self.combobox_colorspace.get())