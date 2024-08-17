import tkinter as tk
from tkinter import *
#from tkinter.ttk import *
from tkinter import ttk
import Back as backinfo

window = tk.Tk()
window.title("Mr. Compound Naming")
window.configure(background="black")

#window.geometry("400x200+200+200")

# width, height = window.winfo_screenwidth(), window.winfo_screenheight()

# window.geometry('%dx%d+0+0' % (width,height))

# frame1 = Frame(window)
# window = Frame(window)
# frame1.pack(fill = BOTH, expand = True)
# window = Frame(window, width = 450, height=50)
#window.pack(fill="both",expand=True)

# #GO Section
# GoSectionbg = "#%02x%02x%02x" % (0,0,153)
# GoSectionbd = "#%02x%02x%02x" % (0,76,153)

# GoSection = tk.Label(window,
#                      bg = GoSectionbg,
#                      height = 15,
#                      width = 15,
#                      text = "labelPlaceHolder",
#                      fg = GoSectionbd
#                      )
# GoSection.pack(side="bottom", fill="x")
# window.pack(side="top", fill="both", expand = TRUE)

#def button
#row = 14
#column = 20


#Element Button Functions
def HydrogenButtonFunction():
    if  backinfo.UserElement1== "NONE":
        backinfo.UserElement1 = "Hydrogen"
        print(backinfo.UserElement1)
    elif backinfo.UserElement2 == "NONE":
        backinfo.UserElement2 = "Hydrogen"
        print(backinfo.UserElement2)
    else:
        print("You can only choose up to 2 elements")

def HeliumButtonFunction():
    if  backinfo.UserElement1== "NONE":
        backinfo.UserElement1 = "Helium"
    elif backinfo.UserElement2 == "NONE":
        backinfo.UserElement2 = "Helium"
    else:
        print("You can only choose up to 2 elements")

def LithiumButtonFunction():
    if  backinfo.UserElement1== "NONE":
        backinfo.UserElement1 = "Lithium"
        print(backinfo.UserElement1)
    elif backinfo.UserElement2 == "NONE":
        backinfo.UserElement2 = "Lithium"
        print(backinfo.UserElement2)
    else:
        print("You can only choose up to 2 elements")


#DELETE THIS
activeforeground1 = "#%02x%02x%02x" % (0,0,0)
activebackground1 = "#%02x%02x%02x" % (255,0,0)

BUTTONHEIGHT = 90
BUTTONWIDTH = 90
SUBSAMPLESIZE = 4



# style = ttk.Style()
# style.configure("ButtonColor", foreground ="white", background="black")

#Element Buttons
HydrogenImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\HydrogenPic.png")
HydrogenImage2 = HydrogenImage1.subsample(SUBSAMPLESIZE)
HydrogenButton = tk.Button(window,
                           image = HydrogenImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH, #BTW pads ADD paddings FROM WIDTH (width는 그냥 찐 button의 width정하는거)
                           #style = "ButtonColor",
                           command = HydrogenButtonFunction,
                           )
HydrogenButton.grid(row = 2, column = 2)


HeliumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\HeliumPic.png")
HeliumImage2 = HeliumImage1.subsample(SUBSAMPLESIZE)
HeliumButton = tk.Button(window,
                           image = HeliumImage2,  
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500                             ,
pady = 500,
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           command = HeliumButtonFunction,
                           )
HeliumButton.grid(row = 2, column = 19)

LithiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\LithiumPic.png")
LithiumImage2 = LithiumImage1.subsample(SUBSAMPLESIZE)
LithiumButton = tk.Button(window,
                           image = LithiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           command = LithiumButtonFunction,
                           )
LithiumButton.grid(row = 3, column = 2)

BerylliumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\BerylliumPic.png")
BerylliumImage2 = BerylliumImage1.subsample(SUBSAMPLESIZE)
BerylliumButton = tk.Button(window,
                           image = BerylliumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = BerylliumButtonFunction,
                           )
BerylliumButton.grid(row = 3, column = 3)

BoronImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\BoronPic.png")
BoronImage2 = BoronImage1.subsample(SUBSAMPLESIZE)
BoronButton = tk.Button(window,
                           image = BoronImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = BoronButtonFunction,
                           )
BoronButton.grid(row = 3, column = 14)

CarbonImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\CarbonPic.png")
CarbonImage2 = CarbonImage1.subsample(SUBSAMPLESIZE)
CarbonButton = tk.Button(window,
                           image = CarbonImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = CarbonButtonFunction,
                           )
CarbonButton.grid(row = 3, column = 15)

NitrogenImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\NitrogenPic.png")
NitrogenImage2 = NitrogenImage1.subsample(SUBSAMPLESIZE)
NitrogenButton = tk.Button(window,
                           image = NitrogenImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = NitrogenButtonFunction,
                           )
NitrogenButton.grid(row = 3, column = 16)

OxygenImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\OxygenPic.png")
OxygenImage2 = OxygenImage1.subsample(SUBSAMPLESIZE)
OxygenButton = tk.Button(window,
                           image = OxygenImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = OxygenButtonFunction,
                           )
OxygenButton.grid(row = 3, column = 17)

FluorineImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\FluorinePic.png")
FluorineImage2 = FluorineImage1.subsample(SUBSAMPLESIZE)
FluorineButton = tk.Button(window,
                           image = FluorineImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = FluorineButtonFunction,
                           )
FluorineButton.grid(row = 3, column = 18)

NeonImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\NeonPic.png")
NeonImage2 = NeonImage1.subsample(SUBSAMPLESIZE)
NeonButton = tk.Button(window,
                           image = NeonImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = NeonButtonFunction,
                           )
NeonButton.grid(row = 3, column = 19)

SodiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\SodiumPic.png")
SodiumImage2 = SodiumImage1.subsample(SUBSAMPLESIZE)
SodiumButton = tk.Button(window,
                           image = SodiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = SodiumButtonFunction,
                           )
SodiumButton.grid(row = 4, column = 2)

MagnesiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\MagnesiumPic.png")
MagnesiumImage2 = MagnesiumImage1.subsample(SUBSAMPLESIZE)
MagnesiumButton = tk.Button(window,
                           image = MagnesiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = MagnesiumButtonFunction,
                           )
MagnesiumButton.grid(row = 4, column = 3)

AluminumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\AluminumPic.png")
AluminumImage2 = AluminumImage1.subsample(SUBSAMPLESIZE)
AluminumButton = tk.Button(window,
                           image = AluminumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = AluminumButtonFunction,
                           )
AluminumButton.grid(row = 4, column = 14)

SiliconImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\SiliconPic.png")
SiliconImage2 = SiliconImage1.subsample(SUBSAMPLESIZE)
SiliconButton = tk.Button(window,
                           image = SiliconImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = SiliconButtonFunction,
                           )
SiliconButton.grid(row = 4, column = 15)

PhosphorusImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\PhosphorusPic.png")
PhosphorusImage2 = PhosphorusImage1.subsample(SUBSAMPLESIZE)
PhosphorusButton = tk.Button(window,
                           image = PhosphorusImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = PhosphorusButtonFunction,
                           )
PhosphorusButton.grid(row = 4, column = 16)

SulfurImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\SulfurPic.png")
SulfurImage2 = SulfurImage1.subsample(SUBSAMPLESIZE)
SulfurButton = tk.Button(window,
                           image = SulfurImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = SulfurButtonFunction,
                           )
SulfurButton.grid(row = 4, column = 17)

ChlorineImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\ChlorinePic.png")
ChlorineImage2 = ChlorineImage1.subsample(SUBSAMPLESIZE)
ChlorineButton = tk.Button(window,
                           image = ChlorineImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = ChlorineButtonFunction,
                           )
ChlorineButton.grid(row = 4, column = 18)

ArgonImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\ArgonPic.png")
ArgonImage2 = ArgonImage1.subsample(SUBSAMPLESIZE)
ArgonButton = tk.Button(window,
                           image = ArgonImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = ArgonButtonFunction,
                           )
ArgonButton.grid(row = 4, column = 19)

PotassiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\PotassiumPic.png")
PotassiumImage2 = PotassiumImage1.subsample(SUBSAMPLESIZE)
PotassiumButton = tk.Button(window,
                           image = PotassiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = PotassiumButtonFunction,
                           )
PotassiumButton.grid(row = 5, column = 2)

CalciumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\CalciumPic.png")
CalciumImage2 = CalciumImage1.subsample(SUBSAMPLESIZE)
CalciumButton = tk.Button(window,
                           image = CalciumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = CalciumButtonFunction,
                           )
CalciumButton.grid(row = 5, column = 3)

ScandiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\ScandiumPic.png")
ScandiumImage2 = ScandiumImage1.subsample(SUBSAMPLESIZE)
ScandiumButton = tk.Button(window,
                           image = ScandiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = ScandiumButtonFunction,
                           )
ScandiumButton.grid(row = 5, column = 4)

TitaniumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\TitaniumPic.png")
TitaniumImage2 = TitaniumImage1.subsample(SUBSAMPLESIZE)
TitaniumButton = tk.Button(window,
                           image = TitaniumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = TitaniumButtonFunction,
                           )
TitaniumButton.grid(row = 5, column = 5)

VanadiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\VanadiumPic.png")
VanadiumImage2 = VanadiumImage1.subsample(SUBSAMPLESIZE)
VanadiumButton = tk.Button(window,
                           image = VanadiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = VanadiumButtonFunction,
                           )
VanadiumButton.grid(row = 5, column = 6)

ChromiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\ChromiumPic.png")
ChromiumImage2 = ChromiumImage1.subsample(SUBSAMPLESIZE)
ChromiumButton = tk.Button(window,
                           image = ChromiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = ChromiumButtonFunction,
                           )
ChromiumButton.grid(row = 5, column = 7)

ManganeseImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\ManganesePic.png")
ManganeseImage2 = ManganeseImage1.subsample(SUBSAMPLESIZE)
ManganeseButton = tk.Button(window,
                           image = ManganeseImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = ManganeseButtonFunction,
                           )
ManganeseButton.grid(row = 5, column = 8)

IronImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\IronPic.png")
IronImage2 = IronImage1.subsample(SUBSAMPLESIZE)
IronButton = tk.Button(window,
                           image = IronImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = IronButtonFunction,
                           )
IronButton.grid(row = 5, column = 9)

CobaltImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\CobaltPic.png")
CobaltImage2 = CobaltImage1.subsample(SUBSAMPLESIZE)
CobaltButton = tk.Button(window,
                           image = CobaltImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = CobaltButtonFunction,
                           )
CobaltButton.grid(row = 5, column = 10)

NickelImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\NickelPic.png")
NickelImage2 = NickelImage1.subsample(SUBSAMPLESIZE)
NickelButton = tk.Button(window,
                           image = NickelImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = NickelButtonFunction,
                           )
NickelButton.grid(row = 5, column = 11)

CopperImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\CopperPic.png")
CopperImage2 = CopperImage1.subsample(SUBSAMPLESIZE)
CopperButton = tk.Button(window,
                           image = CopperImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = CopperButtonFunction,
                           )
CopperButton.grid(row = 5, column = 12)

ZincImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\ZincPic.png")
ZincImage2 = ZincImage1.subsample(SUBSAMPLESIZE)
ZincButton = tk.Button(window,
                           image = ZincImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = ZincButtonFunction,
                           )
ZincButton.grid(row = 5, column = 13)

GalliumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\GalliumPic.png")
GalliumImage2 = GalliumImage1.subsample(SUBSAMPLESIZE)
GalliumButton = tk.Button(window,
                           image = GalliumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = GalliumButtonFunction,
                           )
GalliumButton.grid(row = 5, column = 14)

GermaniumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\GermaniumPic.png")
GermaniumImage2 = GermaniumImage1.subsample(SUBSAMPLESIZE)
GermaniumButton = tk.Button(window,
                           image = GermaniumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = GermaniumButtonFunction,
                           )
GermaniumButton.grid(row = 5, column = 15)

ArsenicImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\ArsenicPic.png")
ArsenicImage2 = ArsenicImage1.subsample(SUBSAMPLESIZE)
ArsenicButton = tk.Button(window,
                           image = ArsenicImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = ArsenicButtonFunction,
                           )
ArsenicButton.grid(row = 5, column = 16)

SeleniumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\SeleniumPic.png")
SeleniumImage2 = SeleniumImage1.subsample(SUBSAMPLESIZE)
SeleniumButton = tk.Button(window,
                           image = SeleniumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = SeleniumButtonFunction,
                           )
SeleniumButton.grid(row = 5, column = 17)

BromineImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\BrominePic.png")
BromineImage2 = BromineImage1.subsample(SUBSAMPLESIZE)
BromineButton = tk.Button(window,
                           image = BromineImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = BromineButtonFunction,
                           )
BromineButton.grid(row = 5, column = 18)

KryptonImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\KryptonPic.png")
KryptonImage2 = KryptonImage1.subsample(SUBSAMPLESIZE)
KryptonButton = tk.Button(window,
                           image = KryptonImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = KryptonButtonFunction,
                           )
KryptonButton.grid(row = 5, column = 19)

RubidiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\RubidiumPic.png")
RubidiumImage2 = RubidiumImage1.subsample(SUBSAMPLESIZE)
RubidiumButton = tk.Button(window,
                           image = RubidiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = RubidiumButtonFunction,
                           )
RubidiumButton.grid(row = 6, column = 2)

StrontiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\StrontiumPic.png")
StrontiumImage2 = StrontiumImage1.subsample(SUBSAMPLESIZE)
StrontiumButton = tk.Button(window,
                           image = StrontiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = StrontiumButtonFunction,
                           )
StrontiumButton.grid(row = 6, column = 3)

YttriumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\YttriumPic.png")
YttriumImage2 = YttriumImage1.subsample(SUBSAMPLESIZE)
YttriumButton = tk.Button(window,
                           image = YttriumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = YttriumButtonFunction,
                           )
YttriumButton.grid(row = 6, column = 4)

ZirconiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\ZirconiumPic.png")
ZirconiumImage2 = ZirconiumImage1.subsample(SUBSAMPLESIZE)
ZirconiumButton = tk.Button(window,
                           image = ZirconiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = ZirconiumButtonFunction,
                           )
ZirconiumButton.grid(row = 6, column = 5)

NiobiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\NiobiumPic.png")
NiobiumImage2 = NiobiumImage1.subsample(SUBSAMPLESIZE)
NiobiumButton = tk.Button(window,
                           image = NiobiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = NiobiumButtonFunction,
                           )
NiobiumButton.grid(row = 6, column = 6)

MolybdenumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\MolybdenumPic.png")
MolybdenumImage2 = MolybdenumImage1.subsample(SUBSAMPLESIZE)
MolybdenumButton = tk.Button(window,
                           image = MolybdenumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = MolybdenumButtonFunction,
                           )
MolybdenumButton.grid(row = 6, column = 7)

TechnetiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\TechnetiumPic.png")
TechnetiumImage2 = TechnetiumImage1.subsample(SUBSAMPLESIZE)
TechnetiumButton = tk.Button(window,
                           image = TechnetiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = TechnetiumButtonFunction,
                           )
TechnetiumButton.grid(row = 6, column = 8)

RutheniumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\RutheniumPic.png")
RutheniumImage2 = RutheniumImage1.subsample(SUBSAMPLESIZE)
RutheniumButton = tk.Button(window,
                           image = RutheniumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = RutheniumButtonFunction,
                           )
RutheniumButton.grid(row = 6, column = 9)

RhodiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\RhodiumPic.png")
RhodiumImage2 = RhodiumImage1.subsample(SUBSAMPLESIZE)
RhodiumButton = tk.Button(window,
                           image = RhodiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = RhodiumButtonFunction,
                           )
RhodiumButton.grid(row = 6, column = 10)

PalladiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\PalladiumPic.png")
PalladiumImage2 = PalladiumImage1.subsample(SUBSAMPLESIZE)
PalladiumButton = tk.Button(window,
                           image = PalladiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = PalladiumButtonFunction,
                           )
PalladiumButton.grid(row = 6, column = 11)

SilverImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\SilverPic.png")
SilverImage2 = SilverImage1.subsample(SUBSAMPLESIZE)
SilverButton = tk.Button(window,
                           image = SilverImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = SilverButtonFunction,
                           )
SilverButton.grid(row = 6, column = 12)

CadmiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\CadmiumPic.png")
CadmiumImage2 = CadmiumImage1.subsample(SUBSAMPLESIZE)
CadmiumButton = tk.Button(window,
                           image = CadmiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = CadmiumButtonFunction,
                           )
CadmiumButton.grid(row = 6, column = 13)

IndiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\IndiumPic.png")
IndiumImage2 = IndiumImage1.subsample(SUBSAMPLESIZE)
IndiumButton = tk.Button(window,
                           image = IndiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = IndiumButtonFunction,
                           )
IndiumButton.grid(row = 6, column = 14)

TinImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\TinPic.png")
TinImage2 = TinImage1.subsample(SUBSAMPLESIZE)
TinButton = tk.Button(window,
                           image = TinImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = TinButtonFunction,
                           )
TinButton.grid(row = 6, column = 15)

AntimonyImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\AntimonyPic.png")
AntimonyImage2 = AntimonyImage1.subsample(SUBSAMPLESIZE)
AntimonyButton = tk.Button(window,
                           image = AntimonyImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = AntimonyButtonFunction,
                           )
AntimonyButton.grid(row = 6, column = 16)

TelluriumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\TelluriumPic.png")
TelluriumImage2 = TelluriumImage1.subsample(SUBSAMPLESIZE)
TelluriumButton = tk.Button(window,
                           image = TelluriumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = TelluriumButtonFunction,
                           )
TelluriumButton.grid(row = 6, column = 17)

IodineImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\IodinePic.png")
IodineImage2 = IodineImage1.subsample(SUBSAMPLESIZE)
IodineButton = tk.Button(window,
                           image = IodineImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = IodineButtonFunction,
                           )
IodineButton.grid(row = 6, column = 18)

XenonImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\XenonPic.png")
XenonImage2 = XenonImage1.subsample(SUBSAMPLESIZE)
XenonButton = tk.Button(window,
                           image = XenonImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = XenonButtonFunction,
                           )
XenonButton.grid(row = 6, column = 19)

CesiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\CesiumPic.png")
CesiumImage2 = CesiumImage1.subsample(SUBSAMPLESIZE)
CesiumButton = tk.Button(window,
                           image = CesiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = CesiumButtonFunction,
                           )
CesiumButton.grid(row = 7, column = 2)

BariumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\BariumPic.png")
BariumImage2 = BariumImage1.subsample(SUBSAMPLESIZE)
BariumButton = tk.Button(window,
                           image = BariumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = BariumButtonFunction,
                           )
BariumButton.grid(row = 7, column = 3)

fiftyseventoseventyoneImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\57-71Pic.png")
fiftyseventoseventyoneImage2 = fiftyseventoseventyoneImage1.subsample(SUBSAMPLESIZE)
fiftyseventoseventyoneButton = tk.Button(window,
                           image = fiftyseventoseventyoneImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = fiftyseventoseventyoneButtonFunction,
                           )
fiftyseventoseventyoneButton.grid(row = 7, column = 4)

HafniumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\HafniumPic.png")
HafniumImage2 = HafniumImage1.subsample(SUBSAMPLESIZE)
HafniumButton = tk.Button(window,
                           image = HafniumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = HafniumButtonFunction,
                           )
HafniumButton.grid(row = 7, column = 5)

TantalumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\TantalumPic.png")
TantalumImage2 = TantalumImage1.subsample(SUBSAMPLESIZE)
TantalumButton = tk.Button(window,
                           image = TantalumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = TantalumButtonFunction,
                           )
TantalumButton.grid(row = 7, column = 6)

TungstenImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\TungstenPic.png")
TungstenImage2 = TungstenImage1.subsample(SUBSAMPLESIZE)
TungstenButton = tk.Button(window,
                           image = TungstenImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = TungstenButtonFunction,
                           )
TungstenButton.grid(row = 7, column = 7)

RheniumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\RheniumPic.png")
RheniumImage2 = RheniumImage1.subsample(SUBSAMPLESIZE)
RheniumButton = tk.Button(window,
                           image = RheniumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = RheniumButtonFunction,
                           )
RheniumButton.grid(row = 7, column = 8)

OsmiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\OsmiumPic.png")
OsmiumImage2 = OsmiumImage1.subsample(SUBSAMPLESIZE)
OsmiumButton = tk.Button(window,
                           image = OsmiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = OsmiumButtonFunction,
                           )
OsmiumButton.grid(row = 7, column = 9)

IridiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\IridiumPic.png")
IridiumImage2 = IridiumImage1.subsample(SUBSAMPLESIZE)
IridiumButton = tk.Button(window,
                           image = IridiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = IridiumButtonFunction,
                           )
IridiumButton.grid(row = 7, column = 10)

PlatinumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\PlatinumPic.png")
PlatinumImage2 = PlatinumImage1.subsample(SUBSAMPLESIZE)
PlatinumButton = tk.Button(window,
                           image = PlatinumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = PlatinumButtonFunction,
                           )
PlatinumButton.grid(row = 7, column = 11)

GoldImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\GoldPic.png")
GoldImage2 = GoldImage1.subsample(SUBSAMPLESIZE)
GoldButton = tk.Button(window,
                           image = GoldImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = GoldButtonFunction,
                           )
GoldButton.grid(row = 7, column = 12)

MercuryImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\MercuryPic.png")
MercuryImage2 = MercuryImage1.subsample(SUBSAMPLESIZE)
MercuryButton = tk.Button(window,
                           image = MercuryImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = MercuryButtonFunction,
                           )
MercuryButton.grid(row = 7, column = 13)

ThalliumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\ThalliumPic.png")
ThalliumImage2 = ThalliumImage1.subsample(SUBSAMPLESIZE)
ThalliumButton = tk.Button(window,
                           image = ThalliumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = ThalliumButtonFunction,
                           )
ThalliumButton.grid(row = 7, column = 14)

LeadImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\LeadPic.png")
LeadImage2 = LeadImage1.subsample(SUBSAMPLESIZE)
LeadButton = tk.Button(window,
                           image = LeadImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = LeadButtonFunction,
                           )
LeadButton.grid(row = 7, column = 15)

BismuthImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\BismuthPic.png")
BismuthImage2 = BismuthImage1.subsample(SUBSAMPLESIZE)
BismuthButton = tk.Button(window,
                           image = BismuthImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = BismuthButtonFunction,
                           )
BismuthButton.grid(row = 7, column = 16)

PoloniumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\PoloniumPic.png")
PoloniumImage2 = PoloniumImage1.subsample(SUBSAMPLESIZE)
PoloniumButton = tk.Button(window,
                           image = PoloniumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = PoloniumButtonFunction,
                           )
PoloniumButton.grid(row = 7, column = 17)

AstatineImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\AstatinePic.png")
AstatineImage2 = AstatineImage1.subsample(SUBSAMPLESIZE)
AstatineButton = tk.Button(window,
                           image = AstatineImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = AstatineButtonFunction,
                           )
AstatineButton.grid(row = 7, column = 18)

RadonImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\RadonPic.png")
RadonImage2 = RadonImage1.subsample(SUBSAMPLESIZE)
RadonButton = tk.Button(window,
                           image = RadonImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = RadonButtonFunction,
                           )
RadonButton.grid(row = 7, column = 19)

FranciumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\FranciumPic.png")
FranciumImage2 = FranciumImage1.subsample(SUBSAMPLESIZE)
FranciumButton = tk.Button(window,
                           image = FranciumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = FranciumButtonFunction,
                           )
FranciumButton.grid(row = 8, column = 2)

RadiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\RadiumPic.png")
RadiumImage2 = RadiumImage1.subsample(SUBSAMPLESIZE)
RadiumButton = tk.Button(window,
                           image = RadiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = RadiumButtonFunction,
                           )
RadiumButton.grid(row = 8, column = 3)

eightyninetohundredImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\89-103Pic.png")
eightyninetohundredImage2 = eightyninetohundredImage1.subsample(SUBSAMPLESIZE)
eightyninetohundredButton = tk.Button(window,
                           image = eightyninetohundredImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = eightyninetohundredButtonFunction,
                           )
eightyninetohundredButton.grid(row = 8, column = 4)

RutherfordiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\RutherfordiumPic.png")
RutherfordiumImage2 = RutherfordiumImage1.subsample(SUBSAMPLESIZE)
RutherfordiumButton = tk.Button(window,
                           image = RutherfordiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = RutherfordiumButtonFunction,
                           )
RutherfordiumButton.grid(row = 8, column = 5)

DubniumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\DubniumPic.png")
DubniumImage2 = DubniumImage1.subsample(SUBSAMPLESIZE)
DubniumButton = tk.Button(window,
                           image = DubniumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = DubniumButtonFunction,
                           )
DubniumButton.grid(row = 8, column = 6)

SeaborgiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\SeaborgiumPic.png")
SeaborgiumImage2 = SeaborgiumImage1.subsample(SUBSAMPLESIZE)
SeaborgiumButton = tk.Button(window,
                           image = SeaborgiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = SeaborgiumButtonFunction,
                           )
SeaborgiumButton.grid(row = 8, column = 7)

BohriumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\BohriumPic.png")
BohriumImage2 = BohriumImage1.subsample(SUBSAMPLESIZE)
BohriumButton = tk.Button(window,
                           image = BohriumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = BohriumButtonFunction,
                           )
BohriumButton.grid(row = 8, column = 8)

HassiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\HassiumPic.png")
HassiumImage2 = HassiumImage1.subsample(SUBSAMPLESIZE)
HassiumButton = tk.Button(window,
                           image = HassiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = HassiumButtonFunction,
                           )
HassiumButton.grid(row = 8, column = 9)

MeitneriumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\MeitneriumPic.png")
MeitneriumImage2 = MeitneriumImage1.subsample(SUBSAMPLESIZE)
MeitneriumButton = tk.Button(window,
                           image = MeitneriumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = MeitneriumButtonFunction,
                           )
MeitneriumButton.grid(row = 8, column = 10)

DarmstadtiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\DarmstadtiumPic.png")
DarmstadtiumImage2 = DarmstadtiumImage1.subsample(SUBSAMPLESIZE)
DarmstadtiumButton = tk.Button(window,
                           image = DarmstadtiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = DarmstadtiumButtonFunction,
                           )
DarmstadtiumButton.grid(row = 8, column = 11)

RoentgeniumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\RoentgeniumPic.png")
RoentgeniumImage2 = RoentgeniumImage1.subsample(SUBSAMPLESIZE)
RoentgeniumButton = tk.Button(window,
                           image = RoentgeniumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = RoentgeniumButtonFunction,
                           )
RoentgeniumButton.grid(row = 8, column = 12)

CoperniciumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\CoperniciumPic.png")
CoperniciumImage2 = CoperniciumImage1.subsample(SUBSAMPLESIZE)
CoperniciumButton = tk.Button(window,
                           image = CoperniciumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = CoperniciumButtonFunction,
                           )
CoperniciumButton.grid(row = 8, column = 13)

NihoniumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\NihoniumPic.png")
NihoniumImage2 = NihoniumImage1.subsample(SUBSAMPLESIZE)
NihoniumButton = tk.Button(window,
                           image = NihoniumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = NihoniumButtonFunction,
                           )
NihoniumButton.grid(row = 8, column = 14)

FleroviumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\FleroviumPic.png")
FleroviumImage2 = FleroviumImage1.subsample(SUBSAMPLESIZE)
FleroviumButton = tk.Button(window,
                           image = FleroviumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = FleroviumButtonFunction,
                           )
FleroviumButton.grid(row = 8, column = 15)

MoscoviumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\MoscoviumPic.png")
MoscoviumImage2 = MoscoviumImage1.subsample(SUBSAMPLESIZE)
MoscoviumButton = tk.Button(window,
                           image = MoscoviumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = MoscoviumButtonFunction,
                           )
MoscoviumButton.grid(row = 8, column = 16)

LivermoriumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\LivermoriumPic.png")
LivermoriumImage2 = LivermoriumImage1.subsample(SUBSAMPLESIZE)
LivermoriumButton = tk.Button(window,
                           image = LivermoriumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = LivermoriumButtonFunction,
                           )
LivermoriumButton.grid(row = 8, column = 17)

TennessineImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\TennessinePic.png")
TennessineImage2 = TennessineImage1.subsample(SUBSAMPLESIZE)
TennessineButton = tk.Button(window,
                           image = TennessineImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = TennessineButtonFunction,
                           )
TennessineButton.grid(row = 8, column = 18)

OganessonImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\OganessonPic.png")
OganessonImage2 = OganessonImage1.subsample(SUBSAMPLESIZE)
OganessonButton = tk.Button(window,
                           image = OganessonImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = OganessonButtonFunction,
                           )
OganessonButton.grid(row = 8, column = 19)

LanthanumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\LanthanumPic.png")
LanthanumImage2 = LanthanumImage1.subsample(SUBSAMPLESIZE)
LanthanumButton = tk.Button(window,
                           image = LanthanumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = LanthanumButtonFunction,
                           )
LanthanumButton.grid(row = 10, column = 4)

CeriumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\CeriumPic.png")
CeriumImage2 = CeriumImage1.subsample(SUBSAMPLESIZE)
CeriumButton = tk.Button(window,
                           image = CeriumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = CeriumButtonFunction,
                           )
CeriumButton.grid(row = 10, column = 5)

PraseodymiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\PraseodymiumPic.png")
PraseodymiumImage2 = PraseodymiumImage1.subsample(SUBSAMPLESIZE)
PraseodymiumButton = tk.Button(window,
                           image = PraseodymiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = PraseodymiumButtonFunction,
                           )
PraseodymiumButton.grid(row = 10, column = 6)

NeodymiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\NeodymiumPic.png")
NeodymiumImage2 = NeodymiumImage1.subsample(SUBSAMPLESIZE)
NeodymiumButton = tk.Button(window,
                           image = NeodymiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = NeodymiumButtonFunction,
                           )
NeodymiumButton.grid(row = 10, column = 7)

PromethiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\PromethiumPic.png")
PromethiumImage2 = PromethiumImage1.subsample(SUBSAMPLESIZE)
PromethiumButton = tk.Button(window,
                           image = PromethiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = PromethiumButtonFunction,
                           )
PromethiumButton.grid(row = 10, column = 8)

SamariumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\SamariumPic.png")
SamariumImage2 = SamariumImage1.subsample(SUBSAMPLESIZE)
SamariumButton = tk.Button(window,
                           image = SamariumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = SamariumButtonFunction,
                           )
SamariumButton.grid(row = 10, column = 9)

EuropiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\EuropiumPic.png")
EuropiumImage2 = EuropiumImage1.subsample(SUBSAMPLESIZE)
EuropiumButton = tk.Button(window,
                           image = EuropiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = EuropiumButtonFunction,
                           )
EuropiumButton.grid(row = 10, column = 10)

GadoliniumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\GadoliniumPic.png")
GadoliniumImage2 = GadoliniumImage1.subsample(SUBSAMPLESIZE)
GadoliniumButton = tk.Button(window,
                           image = GadoliniumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = GadoliniumButtonFunction,
                           )
GadoliniumButton.grid(row = 10, column = 11)

TerbiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\TerbiumPic.png")
TerbiumImage2 = TerbiumImage1.subsample(SUBSAMPLESIZE)
TerbiumButton = tk.Button(window,
                           image = TerbiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = TerbiumButtonFunction,
                           )
TerbiumButton.grid(row = 10, column = 12)

DysprosiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\DysprosiumPic.png")
DysprosiumImage2 = DysprosiumImage1.subsample(SUBSAMPLESIZE)
DysprosiumButton = tk.Button(window,
                           image = DysprosiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = DysprosiumButtonFunction,
                           )
DysprosiumButton.grid(row = 10, column = 13)

HolmiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\HolmiumPic.png")
HolmiumImage2 = HolmiumImage1.subsample(SUBSAMPLESIZE)
HolmiumButton = tk.Button(window,
                           image = HolmiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = HolmiumButtonFunction,
                           )
HolmiumButton.grid(row = 10, column = 14)

ErbiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\ErbiumPic.png")
ErbiumImage2 = ErbiumImage1.subsample(SUBSAMPLESIZE)
ErbiumButton = tk.Button(window,
                           image = ErbiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = ErbiumButtonFunction,
                           )
ErbiumButton.grid(row = 10, column = 15)

ThuliumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\ThuliumPic.png")
ThuliumImage2 = ThuliumImage1.subsample(SUBSAMPLESIZE)
ThuliumButton = tk.Button(window,
                           image = ThuliumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = ThuliumButtonFunction,
                           )
ThuliumButton.grid(row = 10, column = 16)

YtterbiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\YtterbiumPic.png")
YtterbiumImage2 = YtterbiumImage1.subsample(SUBSAMPLESIZE)
YtterbiumButton = tk.Button(window,
                           image = YtterbiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = YtterbiumButtonFunction,
                           )
YtterbiumButton.grid(row = 10, column = 17)


LutetiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\LutetiumPic.png")
LutetiumImage2 = LutetiumImage1.subsample(SUBSAMPLESIZE)
LutetiumButton = tk.Button(window,
                           image = LutetiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = LutetiumButtonFunction,
                           )
LutetiumButton.grid(row = 10, column = 18)

ActiniumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\ActiniumPic.png")
ActiniumImage2 = ActiniumImage1.subsample(SUBSAMPLESIZE)
ActiniumButton = tk.Button(window,
                           image = ActiniumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = ActiniumButtonFunction,
                           )
ActiniumButton.grid(row = 11, column = 4)

ThoriumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\ThoriumPic.png")
ThoriumImage2 = ThoriumImage1.subsample(SUBSAMPLESIZE)
ThoriumButton = tk.Button(window,
                           image = ThoriumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = ThoriumButtonFunction,
                           )
ThoriumButton.grid(row = 11, column = 5)

ProtactiniumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\ProtactiniumPic.png")
ProtactiniumImage2 = ProtactiniumImage1.subsample(SUBSAMPLESIZE)
ProtactiniumButton = tk.Button(window,
                           image = ProtactiniumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = ProtactiniumButtonFunction,
                           )
ProtactiniumButton.grid(row = 11, column = 6)

UraniumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\UraniumPic.png")
UraniumImage2 = UraniumImage1.subsample(SUBSAMPLESIZE)
UraniumButton = tk.Button(window,
                           image = UraniumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = UraniumButtonFunction,
                           )
UraniumButton.grid(row = 11, column = 7)

NeptuniumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\NeptuniumPic.png")
NeptuniumImage2 = NeptuniumImage1.subsample(SUBSAMPLESIZE)
NeptuniumButton = tk.Button(window,
                           image = NeptuniumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = NeptuniumButtonFunction,
                           )
NeptuniumButton.grid(row = 11, column = 8)

PlutoniumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\PlutoniumPic.png")
PlutoniumImage2 = PlutoniumImage1.subsample(SUBSAMPLESIZE)
PlutoniumButton = tk.Button(window,
                           image = PlutoniumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = PlutoniumButtonFunction,
                           )
PlutoniumButton.grid(row = 11, column = 9)

AmericiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\AmericiumPic.png")
AmericiumImage2 = AmericiumImage1.subsample(SUBSAMPLESIZE)
AmericiumButton = tk.Button(window,
                           image = AmericiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = AmericiumButtonFunction,
                           )
AmericiumButton.grid(row = 11, column = 10)

CuriumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\CuriumPic.png")
CuriumImage2 = CuriumImage1.subsample(SUBSAMPLESIZE)
CuriumButton = tk.Button(window,
                           image = CuriumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = CuriumButtonFunction,
                           )
CuriumButton.grid(row = 11, column = 11)

BerkeliumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\BerkeliumPic.png")
BerkeliumImage2 = BerkeliumImage1.subsample(SUBSAMPLESIZE)
BerkeliumButton = tk.Button(window,
                           image = BerkeliumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = BerkeliumButtonFunction,
                           )
BerkeliumButton.grid(row = 11, column = 12)

CaliforniumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\CaliforniumPic.png")
CaliforniumImage2 = CaliforniumImage1.subsample(SUBSAMPLESIZE)
CaliforniumButton = tk.Button(window,
                           image = CaliforniumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = CaliforniumButtonFunction,
                           )
CaliforniumButton.grid(row = 11, column = 13)

EinsteiniumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\EinsteiniumPic.png")
EinsteiniumImage2 = EinsteiniumImage1.subsample(SUBSAMPLESIZE)
EinsteiniumButton = tk.Button(window,
                           image = EinsteiniumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = EinsteiniumButtonFunction,
                           )
EinsteiniumButton.grid(row = 11, column = 14)

FermiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\FermiumPic.png")
FermiumImage2 = FermiumImage1.subsample(SUBSAMPLESIZE)
FermiumButton = tk.Button(window,
                           image = FermiumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = FermiumButtonFunction,
                           )
FermiumButton.grid(row = 11, column = 15)

MendeleviumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\MendeleviumPic.png")
MendeleviumImage2 = MendeleviumImage1.subsample(SUBSAMPLESIZE)
MendeleviumButton = tk.Button(window,
                           image = MendeleviumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = MendeleviumButtonFunction,
                           )
MendeleviumButton.grid(row = 11, column = 16)

NobeliumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\NobeliumPic.png")
NobeliumImage2 = NobeliumImage1.subsample(SUBSAMPLESIZE)
NobeliumButton = tk.Button(window,
                           image = NobeliumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = NobeliumButtonFunction,
                           )
NobeliumButton.grid(row = 11, column = 17)

LawrenciumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\LawrenciumPic.png")
LawrenciumImage2 = LawrenciumImage1.subsample(SUBSAMPLESIZE)
LawrenciumButton = tk.Button(window,
                           image = LawrenciumImage2,
                           borderwidth = -1,
                           highlightthickness= 0,
                           highlightbackground= "#007CEE",
                           padx = 500,
                           pady = 500,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = LawrenciumButtonFunction,
                           )
LawrenciumButton.grid(row = 11, column = 18)


# #GO Section
GoSectionbg = "#%02x%02x%02x" % (192,192,192)
GoSectionbd = "#%02x%02x%02x" % (192,192,192)

GoSection = tk.Label(window,
                     bg = GoSectionbg,
                     height = 10,
                     width = 150,
                     padx=40,
                     text = "labelPlaceHolder",
                     fg = GoSectionbd
                     )
GoSection.grid(row=20, column=1, columnspan=30, rowspan=3)
window.grid_rowconfigure(20, weight=100)
#GoSection.pack(side="bottom", fill="x")

#GO Button
def GoButtonFunction():
    backinfo.MatchElements
    backinfo.TestBondType

    backinfo.ChooseCharge
    
    backinfo.ionicbond_name(backinfo.UserElement1, backinfo.UserElement2, backinfo.Element1Type)
    backinfo.covalentbond_name(backinfo.UserElement1, backinfo.UserElement2)
    backinfo.metallicbond_name(backinfo.UserElement1, backinfo.UserElement2)

    backinfo.ionicbond_formula(backinfo.UserElement1, backinfo.UserElement2, backinfo.Element1Type)
    backinfo.covalentbond_formula(backinfo.UserElement1, backinfo.UserElement2)
    backinfo.metallicbond_formula(backinfo.UserElement1, backinfo.UserElement2)


GoButtonbg = "#%02x%02x%02x" % (204,0,0)
GoButton = tk.Button(window,
                     bg = GoButtonbg,
                     height = 10,
                     width = 10,
                     text = "GO",
                     command = GoButtonFunction
                     )
GoButton.grid(row=20, column=17, rowspan=3)

#Element1 and Element2 Label
UserElement1Labelbg = "#%02x%02x%02x" % (255,255,255)
UserElement1Label = tk.Label(window,
                             bg = UserElement1Labelbg,
                             height = 5,
                             width = 10,
                             text = "Element 1",
                             )
UserElement1Label.grid(row=20, column=6, columnspan=1, rowspan=3)

UserElement2Labelbg = "#%02x%02x%02x" % (255,255,255)
UserElement2Label = tk.Label(window,
                             bg = UserElement2Labelbg,
                             height = 5,
                             width = 10,
                             text = "Element 2",
                             )
UserElement2Label.grid(row=20, column=11, columnspan=1, rowspan=3)

#Add / Remove Buttons
UserElement1AddButtonImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\UpTriangle.png")
UserElement1AddButtonImage2 = UserElement1AddButtonImage1.subsample(20)
UserElement1AddButtonbg = "#%02x%02x%02x" % (192,192,192)
UserElement1AddButton = tk.Button(window,
                                  bg = UserElement1AddButtonbg,
                                  image = UserElement1AddButtonImage2,
                                  borderwidth = -1,
                                  highlightthickness= 0,
                                  highlightbackground= "#007CEE",
                                  padx = 500,
                                  pady = 500,  
                                  height = 30,
                                  width = 30,
                                  #command =  
                                  )
UserElement1AddButton.grid(row = 20, column = 7)

UserElement1RemoveButtonImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\DownTriangle.png")
UserElement1RemoveButtonImage2 = UserElement1RemoveButtonImage1.subsample(20)
UserElement1RemoveButtonbg = "#%02x%02x%02x" % (192,192,192)
UserElement1RemoveButton = tk.Button(window,
                                  bg = UserElement1RemoveButtonbg,
                                  image = UserElement1RemoveButtonImage2,
                                  borderwidth = -1,
                                  highlightthickness= 0,
                                  highlightbackground= "#007CEE",
                                  padx = 500,
                                  pady = 500,  
                                  height = 30,
                                  width = 30,
                                  #command =  
                                  )
UserElement1RemoveButton.grid(row = 22, column = 7)

UserElement2AddButtonImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\UpTriangle.png")
UserElement2AddButtonImage2 = UserElement2AddButtonImage1.subsample(20)
UserElement2AddButtonbg = "#%02x%02x%02x" % (192,192,192)
UserElement2AddButton = tk.Button(window,
                                  bg = UserElement2AddButtonbg,
                                  image = UserElement2AddButtonImage2,
                                  borderwidth = -1,
                                  highlightthickness= 0,
                                  highlightbackground= "#007CEE",
                                  padx = 500,
                                  pady = 500,  
                                  height = 30,
                                  width = 30,
                                  #command =  
                                  )
UserElement2AddButton.grid(row = 20, column = 12)

UserElement2RemoveButtonImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\DownTriangle.png")
UserElement2RemoveButtonImage2 = UserElement2RemoveButtonImage1.subsample(20)
UserElement2RemoveButtonbg = "#%02x%02x%02x" % (192,192,192)
UserElement2RemoveButton = tk.Button(window,
                                  bg = UserElement1RemoveButtonbg,
                                  image = UserElement2RemoveButtonImage2,
                                  borderwidth = -1,
                                  highlightthickness= 0,
                                  highlightbackground= "#007CEE",
                                  padx = 500,
                                  pady = 500,  
                                  height = 30,
                                  width = 30,
                                  #command =  
                                  )
UserElement2RemoveButton.grid(row = 22, column = 12)































window.mainloop()






