from pytube import YouTube
import tkinter
from tkinter import simpledialog
from tkinter import ttk
from tkinter.filedialog import askdirectory
import sv_ttk

root = tkinter.Tk()
root.geometry("500x500")
root.title("EZTuber")
res = tkinter.StringVar(root)
res.set('Lowest')

sv_ttk.set_theme("dark")

def callLink():
    global link 
    link = simpledialog.askstring("EZTuber", "Enter the URL of the YouTube video")

def downloadVid():
    yt = YouTube(link)
    done = ttk.Label(root, text="Done!")
    label2 = ttk.Label(root, text="Title: " + yt.title)
    label2.pack()
    yd = yt.streams.get_highest_resolution() if res.get() == "Highest" else yt.streams.get_lowest_resolution()
    label3 = ttk.Label(root, text="File Size: " + str(yd.filesize_mb) + " MB")
    label3.pack()
    yd.download(directory)
    done = ttk.Label(root, text="Done! Downloaded to: " + directory)
    done.pack()

def openDirectory():
    global directory
    directory = askdirectory()

label = ttk.Label(root, text="EZTuber YouTube Downloader", font=("Comic Sans MS", 18))
label.pack(pady=20, padx=20)

Directory = ttk.Button(root, text="Save Directory", command=openDirectory)
Directory.pack(pady=10)

linkbutton = ttk.Button(root, text="Add Link", command=callLink)
linkbutton.pack(padx=20)

restxt = ttk.Label(root, text="Resolution:")
restxt.pack(padx=5,pady=10)
resolution = ttk.OptionMenu(root, res, "Lowest", "Lowest", "Highest")
resolution.pack(padx=20, pady=10)

download = ttk.Button(root, text="Download", command=downloadVid) 
download.pack(pady=25)

root.mainloop()
