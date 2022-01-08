# importing all modules that we need

import os
from tkinter import *
from tkinter import messagebox as msg

# Made this function in order to clean folder
def clean():
    # ------------------------------------------------------------------------------------------------------------------
    from tkinter import filedialog as filr
    new_path_to_work = filr.askdirectory()
    os.chdir(new_path_to_work)

    def make_folder_and_move(folder, filex):
        if not os.path.exists(folder):
            os.makedirs(folder)

        for file in filex:
            os.replace(file, f"{folder}/{file}")

    # ------------------------------------------------------------------------------------------------------------------
    if __name__ == "__main__":
        # Getting all files list
        files = os.listdir()
        try:
            files.remove('File organizer.pyw')
        except ValueError:
            pass
        if not checkbutton1.get() and not checkbutton2.get() and not checkbutton3.get() and not checkbutton4.get() and not checkbutton5.get():
            msg.showerror('Error to clean', 'Please Select Something!')
            return 0
        else:
            pass
        if checkbutton1.get():
            imgxts = [".png", ".jpg", ".jpeg"]
            images = [file for file in files if os.path.splitext(file)[1].lower() in imgxts]
            make_folder_and_move('Images', images)

        if checkbutton2.get():
            docxts = [".txt", ".docx", "doc", ".pdf"]
            docs = [file for file in files if os.path.splitext(file)[1].lower() in docxts]
            make_folder_and_move('Docs', docs)

        if checkbutton3.get():
            mediaxts = [".mp4", ".mp3"]
            medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaxts]
            make_folder_and_move('Media', medias)

        if checkbutton4.get():
            software = [file for file in files if os.path.splitext(file)[1].lower() == ".exe"]
            make_folder_and_move('Software', software)

        if checkbutton5.get():
            listr = [".png", ".jpg", ".jpeg", ".txt", ".docx", "doc", ".pdf", ".mp4", ".mp3", "exe"]
            others = []
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if (ext not in listr) and os.path.isfile(file):
                    others.append(file)
            make_folder_and_move('Others', others)

        msg.showinfo('Success', 'Folder Cleaned Successfully')


# ----------------------------------------------------------------------------------------------------------------------


def make_exit():
    sure = msg.askokcancel(':(', ' Really Want To Exit!')

    if sure:
        root.destroy()
    else:
        return 0


# ----------------------------------------------------------------------------------------------------------------------


# Making Gui

cwd = os.getcwd()

root = Tk()

f = Frame(root)
Button(f, text="Clean", font="SegoeUI 10 bold", command=clean).pack(padx=4, pady=5)
Button(f, text="Exit", font="SegoeUI 10 bold", command=make_exit).pack(padx=4, pady=5)
f.pack(fill=BOTH, expand=True, side='right', anchor="center")

f = Frame(root)
checkbutton1 = BooleanVar()
checkbutton2 = BooleanVar()
checkbutton3 = BooleanVar()
checkbutton4 = BooleanVar()
checkbutton5 = BooleanVar()

Button1 = Checkbutton(root, text="Images",
                      variable=checkbutton1,
                      onvalue=1,
                      offvalue=0,
                      height=4,
                      width=20).pack()
Button2 = Checkbutton(root, text="Documents",
                      variable=checkbutton2,
                      onvalue=1,
                      offvalue=0,
                      height=4,
                      width=20).pack()
Button3 = Checkbutton(root, text="Media",
                      variable=checkbutton3,
                      onvalue=1,
                      offvalue=0,
                      height=4,
                      width=20).pack()
Button4 = Checkbutton(root, text="Software",
                      variable=checkbutton4,
                      onvalue=1,
                      offvalue=0,
                      height=4,
                      width=20).pack()

Button5 = Checkbutton(root, text="Others",
                      variable=checkbutton5,
                      onvalue=1,
                      offvalue=0,
                      height=4,
                      width=20).pack()
f.pack()

root.title(f"{cwd} | File Organizer")
root.geometry("600x500")


mainloop()

# ----------------------------------------------------------------------------------------------------------------------
