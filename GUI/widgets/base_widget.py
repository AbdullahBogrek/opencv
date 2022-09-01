import tkinter as tk
import tkinter.ttk as ttk
from pygubu.widgets.scrolledframe import ScrolledFrame


class BaseWidget(ttk.Panedwindow):
    def __init__(self, master=None, **kw):
        ttk.Panedwindow.__init__(self, master, **kw)
        self.frame2 = ttk.Frame(self)
        self.button1 = tk.Button(self.frame2)
        self.button1.configure(cursor='hand1', font='TkDefaultFont', text='Record')
        self.button1.pack(padx='10', side='left')
        self.button1.configure(command=self.record)
        self.button2 = tk.Button(self.frame2)
        self.button2.configure(text='Save')
        self.button2.pack(padx='10', pady='10', side='left')
        self.button2.configure(command=self.save)
        self.button3 = tk.Button(self.frame2)
        self.button3.configure(text='Stop')
        self.button3.pack(padx='10', pady='10', side='left')
        self.button3.configure(command=self.stop)
        self.frame2.configure(height='200', relief='groove', width='200')
        self.frame2.pack(side='top')
        self.add(self.frame2, weight='1')
        self.panedwindow2 = ttk.Panedwindow(self, orient='horizontal')
        self.scrolledframe1 = ScrolledFrame(self.panedwindow2, scrolltype='both')
        self.canvas1 = tk.Canvas(self.scrolledframe1.innerframe)
        self.canvas1.pack(expand='true', fill='both', side='top')
        self.scrolledframe1.configure(usemousewheel=False)
        self.scrolledframe1.pack(side='top')
        self.panedwindow2.add(self.scrolledframe1, weight='1')
        self.scrolledframe2 = ScrolledFrame(self.panedwindow2, scrolltype='both')
        self.frame6 = ttk.Frame(self.scrolledframe2.innerframe)
        self.label_thresh = tk.Label(self.frame6)
        self.label_thresh.configure(text='Threshold')
        self.label_thresh.pack(padx='5', pady='5', side='left')
        self.label_scale_thresh = ttk.Scale(self.frame6)
        self.label_scale_thresh.configure(from_='0', length='150', orient='horizontal', to='255')
        self.label_scale_thresh.pack(padx='5', pady='5', side='left')
        self.label_scale_thresh.bind('<B1- Motion>', self.get_thresh_val, add='')
        self.label_thresh_res = ttk.Label(self.frame6)
        self.label_thresh_res.configure(text='0', width='3')
        self.label_thresh_res.pack(padx='5', pady='5', side='left')
        self.frame6.configure(height='200', width='200')
        self.frame6.pack(side='top')
        self.frame7 = ttk.Frame(self.scrolledframe2.innerframe)
        self.label_colorspace = ttk.Label(self.frame7)
        self.label_colorspace.configure(text='Colorspace')
        self.label_colorspace.pack(padx='5', pady='5', side='left')
        self.combobox_colorspace = ttk.Combobox(self.frame7)
        self.combobox_colorspace.configure(cursor='hand1', state='readonly', width='20')
        self.combobox_colorspace.pack(padx='5', pady='5', side='left')
        self.combobox_colorspace.bind('<<ComboboxSelected>>', self.select_colorspace, add='')
        self.frame7.configure(height='200', width='200')
        self.frame7.pack(side='top')
        self.frame8 = ttk.Frame(self.scrolledframe2.innerframe)
        self.frame8.configure(height='200', width='200')
        self.frame8.pack(side='top')
        self.scrolledframe2.configure(usemousewheel=False)
        self.scrolledframe2.pack(pady='10', side='top')
        self.panedwindow2.add(self.scrolledframe2, weight='1')
        self.panedwindow2.configure(height='200', width='200')
        self.panedwindow2.pack(side='top')
        self.add(self.panedwindow2, weight='12')
        self.notebook1 = ttk.Notebook(self)
        self.text1 = tk.Text(self.notebook1)
        self.text1.configure(background='#2b2b2b', foreground='#ff6700', height='10', width='50')
        _text_ = '''text1'''
        self.text1.insert('0.0', _text_)
        self.text1.pack(side='top')
        self.notebook1.add(self.text1, text='Message Log')
        self.frame5 = ttk.Frame(self.notebook1)
        self.frame5.configure(height='200', width='200')
        self.frame5.pack(side='top')
        self.notebook1.add(self.frame5, text='Live Histogram')
        self.notebook1.configure(height='200', width='200')
        self.notebook1.pack(side='top')
        self.add(self.notebook1, weight='1')

    def record(self):
        pass

    def save(self):
        pass

    def stop(self):
        pass

    def get_thresh_val(self, event=None):
        pass

    def select_colorspace(self, event=None):
        pass

