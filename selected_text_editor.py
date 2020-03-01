"""
A simple program to allow editing of selected text before copy/pasting

This program must be run with python3, and requires xclip. The program can be
bound to a keyboard shortcut, and once in the text editor ctrl+c will copy the
text and close the window.

Author: David Chen
"""

import tkinter as tk
import os


def get_selected_text():
    text = os.popen('xsel').read()
    return text


def set_clipboard(text):
    with os.popen('xclip -selection c', 'w') as outf:
        outf.write(text)


def copy_text(event):
    text = entry.get('1.0', 'end-1c')  # select all text in entry box
    set_clipboard(text)
    window.destroy()


if __name__ == '__main__':
    window = tk.Tk()
    entry = tk.Text(window, width=400, height=40, font=('Calibri 16'))
    entry.insert('end', get_selected_text())
    entry.focus()
    window.bind('<Control-c>', copy_text)
    entry.pack()

    window.mainloop()
