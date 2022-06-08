from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pytesseract
import pyautogui
import cv2

reliclist = []
namepresetlist = ["Axi", "Lith", "Meso", "Neo"]
scanletterlist = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
axilist = []
lithlist = []
mesolist = []
neolist = []
onoffdict = {
    "green": "red",
    "red": "green",
    "ON": "OFF",
    "OFF": "ON",
    RAISED: SUNKEN,
    SUNKEN: RAISED
}

#Klasse für die Relikte
class Relics:

    def __init__(self, name, amount, master):
        self.name = str(name)
        self.amount = amount
        self.deletecounter = 0
        self.displayamount = StringVar()
        self.displayamount.set(self.amount)
        self.relicframe = Frame(master)
        self.amountframe = LabelFrame(self.relicframe, text="Amount")
        self.nameframe = LabelFrame(self.relicframe, text="Name")
        self.plusbtn = Button(self.amountframe, text="+", command=lambda: self.addamount())
        self.minusbtn = Button(self.amountframe, text="-", command=lambda: self.removeamount())
        self.deletebtn = Button(self.relicframe, text="DELETE", command=lambda: self.deleteentry())
        self.relicname = Label(self.nameframe, text=self.name)
        self.relicamount = Label(self.amountframe, textvariable=self.displayamount)
        self.upbtn = Button(self.relicframe, text="^", command=lambda: self.moveup())
        self.downbtn = Button(self.relicframe, text="v", command=lambda: self.movedown())
        reliclist.append(self)
        self.relicframe.grid(row=reliclist.index(self), column=0, pady=2)
        self.upbtn.grid(row=0, column=0, padx=2)
        self.downbtn.grid(row=0, column=1, padx=2)
        self.nameframe.grid(row=0, column=2)
        self.relicname.grid(row=0, column=0, pady=5, padx=8)
        self.amountframe.grid(row=0, column=3, padx=6)
        self.minusbtn.grid(row=0, column=0, padx=2, pady=2)
        self.relicamount.grid(row=0, column=1, padx=2, pady=2)
        self.plusbtn.grid(row=0, column=2, padx=2, pady=2)
        self.deletebtn.grid(row=0, column=4)

    def moveup(self):
        if reliclist.index(self) > 0:
            pos = reliclist.index(self)
            reliclist.remove(self)
            reliclist.insert(pos - 1, self)
            self.relicframe.forget()
            otherrelic = reliclist[reliclist.index(self) + 1]
            otherrelic.relicframe.forget()
            self.redraw()
            otherrelic.redraw()

    def movedown(self):
        if reliclist.index(self) < len(reliclist) - 1:
            pos = reliclist.index(self)
            reliclist.remove(self)
            reliclist.insert(pos + 1, self)
            self.relicframe.forget()
            otherrelic = reliclist[reliclist.index(self) - 1]
            otherrelic.relicframe.forget()
            self.redraw()
            otherrelic.redraw()

    def addamount(self):
        self.amount += 1
        self.displayamount.set(self.amount)

    def removeamount(self):
        self.amount -= 1
        self.displayamount.set(self.amount)

    def deleteentry(self):
        self.deletecounter += 1
        if self.deletecounter == 1:
            self.deletebtn.config(background="red")
        elif self.deletecounter >= 2:
            self.relicframe.grid_remove()
            reliclist.remove(self)
            del self

    def redraw(self):
        self.relicframe.grid(row=reliclist.index(self), column=0, pady=2)
        self.upbtn.grid(row=0, column=0, padx=2)
        self.downbtn.grid(row=0, column=1, padx=2)
        self.nameframe.grid(row=0, column=2)
        self.relicname.grid(row=0, column=0, pady=5, padx=8)
        self.amountframe.grid(row=0, column=3, padx=6)
        self.minusbtn.grid(row=0, column=0, padx=2, pady=2)
        self.relicamount.grid(row=0, column=1, padx=2, pady=2)
        self.plusbtn.grid(row=0, column=2, padx=2, pady=2)
        self.deletebtn.grid(row=0, column=4)


class Scanner:

    def __init__(self):
        global scancooldown
        self.minlenght = int(pyautogui.size()[0] * 0.45)
        self.minheight = int(pyautogui.size()[1] * 0.7)
        self.maxheight = int(pyautogui.size()[1] * 0.74)
        self.scanimg = pyautogui.screenshot()
        #self.scanimg.save(r"scanpic.png")
        self.scanimg = cv2.imread(r"relic coords.png")
        self.scanimg = cv2.imread(r"scanpic.png")
        self.scan(self.transformpic())
        del self


    def transformpic(self):
        self.scanimg = self.scanimg[self.minheight:self.maxheight, self.minlenght:pyautogui.size()[0]]
        cv2.fastNlMeansDenoisingColored(self.scanimg, None, 10, 10, 7, 21)
        self.scanimg = cv2.convertScaleAbs(self.scanimg, alpha=2.0)
        #self.scanimg = cv2.cvtColor(self.scanimg, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("heyagain", self.scanimg)
        return self.scanimg

    def scan(self, pic):
        self.scanpicstring = pytesseract.image_to_string(pic)

        for x in allrelicslist:
            self.scanfor = x
            if self.scanfor + " " in self.scanpicstring:  # relikt wird gefunden auf screen
                self.skip = False
                if len(reliclist) > 0:
                    for a in reliclist:
                        if a.name == self.scanfor:
                            a.amount += 1
                            a.displayamount.set(a.amount)  # relikt schon drin deshalb ein mehr
                            lastaddedvar.set(self.scanfor)
                            self.skip = True
                            break
                if not self.skip:
                    inst = Relics(self.scanfor, 1, listframe)  # relikt ist neu deshalb neu hinzufügen
                    lastaddedvar.set(self.scanfor)


#Settings sind WiP
class Settings:

    def __init__(self, master):
        self.top = Toplevel()
        self.top.transient(master)


def addnewrelic():
    global listframe
    global relicaddvar
    global listcanvas
    if relicaddvar.get() != "":
        name = str(relicaddvar.get()[0].upper()) + str(relicaddvar.get()[1])
        inst = Relics(namepresetvar.get() + " " + name, 1, listframe)
        relicaddvar.set("")
    listcanvas.configure(scrollregion=(0, 0, 1000, 100 + (len(reliclist) * 50) ))


def toggleonoff():
    global togglebtn
    global onoffvar
    togglebtn.config(background=onoffdict[togglebtn.cget("background")])
    togglebtn.config(relief=onoffdict[togglebtn.cget("relief")])
    onoffvar.set(onoffdict[onoffvar.get()])


def timertick():
    global timerdelay
    global foundbool
    global scancooldown

    if onoffvar.get() == "ON" and scancooldown <= 0:
        if int(timervar.get()) <= 1:
            timervar.set(timerdelay)
            inst = Scanner()
            scancooldown = 30
            scancooldownvar.set(str(scancooldown))
        else:
            timervar.set(str(int(timervar.get()) - 1))

    elif scancooldown > 0:
        scancooldown -= 1
        scancooldownvar.set(str(scancooldown))

    root.after(1000, timertick)


def save():
    global reliclist
    global savebtn
    savelist = []

    for i in range(len(reliclist)):
        if i < len(reliclist) - 1:
            savelist.append(str(reliclist[i].amount) + "\n")
            savelist.append(reliclist[i].name + "\n")
        elif i == len(reliclist) - 1:
            savelist.append(str(reliclist[i].amount) + "\n")
            savelist.append(reliclist[i].name)

    savefile = open("relicsave.txt", "w")
    savefile.writelines(savelist)
    savefile.close()


def load():
    global listframe
    savefile = open("relicsave.txt", "r")
    loadlist = savefile.readlines()
    for i in range(0, len(loadlist), 2):
        if i < len(loadlist) - 2:
            loadamount = loadlist[i][0:len(loadlist[i])-1]
            loadname = loadlist[i+1][0:len(loadlist[i+1])-1]
        elif i == len(loadlist) - 2:
            loadamount = loadlist[i][0:len(loadlist[i])-1]
            loadname = loadlist[i + 1]
        inst = Relics(loadname, loadamount, listframe)
    listcanvas.configure(scrollregion=(0, 0, 1000, 100 + (len(reliclist) * 50)))


def sortrelics(type):
    if type == "axi":
        for i in axilist:
            for x in reliclist:
                if i == x.name:
                    reliclist.insert(0, reliclist.pop(reliclist.index(x)))

    if type == "lith":
        for i in lithlist:
            for x in reliclist:
                if i == x.name:
                    reliclist.insert(0, reliclist.pop(reliclist.index(x)))

    if type == "meso":
        for i in mesolist:
            for x in reliclist:
                if i == x.name:
                    reliclist.insert(0, reliclist.pop(reliclist.index(x)))

    if type == "neo":
        for i in neolist:
            for x in reliclist:
                if i == x.name:
                    reliclist.insert(0, reliclist.pop(reliclist.index(x)))

    for x in reliclist:
        x.redraw()


def settimerdelay():
    global timerdelay
    timerdelay = timerdelayvar.get()
    timerdelayvar.set("")


def opensettings():
    global root
    inst = Settings(root)


root = Tk()
#root.geometry("250x800")
root.title("RelicScanner")
relicaddvar = StringVar()
onoffvar = StringVar()
timervar = StringVar()
namepresetvar = StringVar()
lastaddedvar = StringVar()
timerdelayvar = StringVar()
scancooldownvar = StringVar()
onoffvar.set("OFF")
timervar.set("8")
namepresetvar.set("Axi")
lastaddedvar.set("nothing yet")
timerdelayvar.set("")
scancooldownvar.set("0")
timerdelay = "8"
scancooldown = 0
foundbool = bool(True)
optframe = LabelFrame(root, text="Options")
pytesseract.pytesseract.tesseract_cmd = r"pytesseract\tesseract"
cogimg = ImageTk.PhotoImage(Image.open("cog.png"))

scrollframe = Frame(root)
listcanvas = Canvas(scrollframe, height=800)
listframe = Frame(listcanvas)
relicscrollbar = ttk.Scrollbar(scrollframe, orient=VERTICAL, command=listcanvas.yview)

timerframe = LabelFrame(optframe, text="timer", height=80, width=80)
togglebtn = Button(optframe, textvariable=onoffvar, background="red", font=("Times", "10", "bold"), command=lambda: toggleonoff())
addnewbtn = Button(optframe, text="Add New Relic", command=lambda: addnewrelic())
presetmenu = OptionMenu(optframe, namepresetvar, *namepresetlist)
addnewentry = Entry(optframe, textvariable=relicaddvar)
timerlabel = Label(timerframe, textvariable=timervar, font=("Times", "28", "bold"))
savebtn = Button(optframe, text="Save", command=lambda: save())
loadbtn = Button(optframe, text="Load", command=lambda: load())
axibtn = Button(optframe, text="Axi", command=lambda: sortrelics("axi"))
lithbtn = Button(optframe, text="Lith", command=lambda: sortrelics("lith"))
mesobtn = Button(optframe, text="Meso", command=lambda: sortrelics("meso"))
neobtn = Button(optframe, text="Neo", command=lambda: sortrelics("neo"))
setdelaybtn = Button(optframe, text="Set Delay", command=lambda: settimerdelay())
delayentry = Entry(optframe, textvariable=timerdelayvar)
lastscannedlabel = Label(optframe, textvariable=lastaddedvar)
scancooldownlabel = Label(optframe, textvariable=scancooldownvar)
#settingsbtn = Button(optframe, image=cogimg, command=lambda: opensettings())

listcanvas.configure(yscrollcommand=relicscrollbar.set)
listcanvas.bind("<Configure>", lambda e: listcanvas.configure(scrollregion=(0, 0, 1000, 800)))

optframe.grid(row=0, column=0, padx=4, pady=4, sticky=W)

scrollframe.grid(row=1, column=0, sticky=W)
listcanvas.grid(row=0, column=0, sticky=N)
listcanvas.create_window((0,0), window=listframe, anchor="nw")
relicscrollbar.grid(row=0, column=1, sticky=N+S+W)

togglebtn.grid(row=0, column=0, padx=4, pady=1, sticky=E)
addnewbtn.grid(row=1, column=0, padx=4, pady=4, sticky=E)
presetmenu.grid(row=2, column=0)
addnewentry.grid(row=2, column=1, padx=4, pady=4)
timerframe.grid(row=0, column=1, rowspan=2, columnspan=2)
timerframe.grid_propagate(0)
timerlabel.grid(row=0, column=0, padx=24, pady=6)
savebtn.grid(row=0, column=3, padx=3)
loadbtn.grid(row=0, column=4, padx=3)
axibtn.grid(row=0, column=5, padx=3, pady=1, sticky=E)
lithbtn.grid(row=0, column=6, padx=3, pady=1, sticky=W)
mesobtn.grid(row=1, column=5, padx=3, pady=1, sticky=E)
neobtn.grid(row=1, column=6, padx=3, pady=1, sticky=W)
setdelaybtn.grid(row=2, column=5, padx=3, pady=1)
delayentry.grid(row=2, column=6, padx=3, pady=1)
lastscannedlabel.grid(row=1, column=3, columnspan=2)
scancooldownlabel.grid(row=1, column=6, sticky=S+E)
#settingsbtn.grid(row=0, column=6)


for letter in scanletterlist:
    for number in range(1, 19):
        axilist.append("Axi " + letter + str(number))
for letter in scanletterlist:
    for number in range(1, 19):
        lithlist.append("Lith " + letter + str(number))
for letter in scanletterlist:
    for number in range(1, 19):
        mesolist.append("Meso " + letter + str(number))
for letter in scanletterlist:
    for number in range(1, 19):
        neolist.append("Neo " + letter + str(number))
allrelicslist = []
allrelicslist.extend(axilist)
allrelicslist.extend(lithlist)
allrelicslist.extend(mesolist)
allrelicslist.extend(neolist)
axilist.reverse()
lithlist.reverse()
mesolist.reverse()
neolist.reverse()
allrelicslist.reverse()

root.after(1000, timertick)

root.mainloop()
