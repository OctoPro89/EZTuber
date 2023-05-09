from pytube import YouTube
from sys import argv
import tkinter
from tkinter import simpledialog
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import sv_ttk

root = tkinter.Tk()
root.geometry("500x500")
root.title("EZTuber")

sv_ttk.set_theme("dark")

def callLink():
    global link 
    link = simpledialog.askstring("EZTuber", "Enter the URL of the YouTube video")

def downloadVid():
    yt = YouTube(link)
    print("Title: ", yt.title)
    print("View: ", yt.views)
    done = ttk.Label(root, text="Done!")
    label2 = ttk.Label(root, text="Title: " + yt.title)
    label2.pack()
    yd = yt.streams.get_highest_resolution()
    label3 = ttk.Label(root, text="File Size: " + str(yd.filesize_mb) + " MB")
    label3.pack()
    yd.download(directory)
    yd

def openDirectory():
    global directory
    directory = askdirectory()

label = ttk.Label(root, text="EZTuber YouTube Downloader", font=("Comic Sans MS", 18))
label.pack(pady=20, padx=20)

Directory = ttk.Button(root, text="Save Directory", command=openDirectory)
Directory.pack(pady=10)

linkbutton = ttk.Button(root, text="Add Link", command=callLink)
linkbutton.pack(padx=20)

download = ttk.Button(root, text="Download", command=downloadVid) 
download.pack(pady=25)

root.mainloop()