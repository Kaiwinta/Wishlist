import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry("1280x720")

    root.resizable(False,False)
    root.bind('<Escape>',root.destroy)

    root.mainloop()


if __name__ == "__main__":
    main()