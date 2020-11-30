from sys import *
from tkinter import *
from os import *
import tkinter.filedialog as tkfd
import asyncio
import subprocess

root = Tk()
root.title("FLAC converter(experimental)")

#初期化
encode = StringVar()
encode.set("normal")
decode = StringVar()
decode.set("normal")
CLevel = IntVar()
CLevel.set(0)
file1 = StringVar()
decode_check = 0
FullPass = [None]
FullPass2 = [None]


def Convert(event):
        global FullPass
        CLevel = CompScale.get()
        for fpass in FullPass:
                cmd = ["flac"]
                if decode_check :
                        cmd.append("-d")
                else :
                        cmd.append(f"-{CLevel}")
                cmd.append("\""+ str(fpass) +"\"")
                cmd = " ".join(cmd)
                #print(cmd)
                subprocess.call(cmd)
        path_ = path.normpath(path.join(FullPass[0],'..'))
        subprocess.call(f"explorer {path_}")
        #print(path)

def Browse1():
        global FullPass,FileEntry
        if decode_check :
                FullPass = tkfd.askopenfilenames(filetypes=[('Music Files', '.flac')])
        else :
                FullPass = tkfd.askopenfilenames(filetypes=[('Music Files', '.wav')])
        FileEntry.delete(0,END)
        FileEntry.insert(END,(";".join(FullPass)))

def ChangeStateE():
        CompScale.configure(state="active", fg="black")
        StartButton.configure(text="Encode")
        global decode_check
        decode_check = 0
def ChangeStateD():
        CompScale.configure(state="disabled", fg="gray64")
        StartButton.configure(text="Decode")
        global decode_check
        decode_check = 1

EncodeCheck = Button(text="Encode", command=ChangeStateE)
EncodeCheck.pack(side="left") #encode/decode切り替え
DecodeCheck = Button(text="Decode", command=ChangeStateD)
DecodeCheck.pack(side="left") #encode/decode切り替え

CompScale = Scale(root, label="Comp Level", from_=0, to=8, orient="h", variable=CLevel,
        showvalue=1)
CompScale.pack() #圧縮レベルのスライダー

LabelAskFile = Label(root, text="File:")
LabelAskFile.pack()
FileEntry = Entry(root, text="", width=50)
FileEntry.pack()
AskFileButton = Button(root, text="Browse", command=Browse1)
AskFileButton.pack()         #入力ファイル参照

StartButton = Button(root, text="Start Encode")
StartButton.bind("<Button-1>", Convert)
StartButton.pack(side="bottom", anchor="s") #最後に押すボタン



root.mainloop()