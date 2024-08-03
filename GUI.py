import tkinter as tk
from tkinter import *
from tkinter.ttk import *
#import Back as Back

window = tk.Tk()
window.title("Mr. Compound Naming")

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
#row = 12
#column = 20

def HydrogenButtonFunction():
    print("Hydrogen")

#DELETE THIS
activeforeground1 = "#%02x%02x%02x" % (0,0,0)
activebackground1 = "#%02x%02x%02x" % (255,0,0)

BUTTONHEIGHT = 100
BUTTONWIDTH = 100

#Element Buttons
HydrogenImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\HydrogenPic.png")
HydrogenImage2 = HydrogenImage1.subsample(4)
HydrogenButton = tk.Button(window,
                           image = HydrogenImage2,
                           borderwidth = 0,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH, #BTW pads ADD paddings FROM WIDTH (width는 그냥 찐 button의 width정하는거)
                           command = HydrogenButtonFunction,
                           )
HydrogenButton.grid(row = 2, column = 2)


HeliumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\HeliumPic.png")
HeliumImage2 = HeliumImage1.subsample(4)
HeliumButton = tk.Button(window,
                           image = HeliumImage2,  
                           borderwidth = 0,
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = HeliumButtonFunction,
                           )
HeliumButton.grid(row = 2, column = 19)

LithiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\LithiumPic.png")
LithiumImage2 = LithiumImage1.subsample(4)
LithiumButton = tk.Button(window,
                           image = LithiumImage2,
                           borderwidth = 0,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = LithiumButtonFunction,
                           )
LithiumButton.grid(row = 3, column = 2)

BerylliumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\BerylliumPic.png")
BerylliumImage2 = BerylliumImage1.subsample(3)
BerylliumButton = tk.Button(window,
                           image = BerylliumImage2,
                           borderwidth = 0,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = BerylliumButtonFunction,
                           )
BerylliumButton.grid(row = 3, column = 3)

BoronImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\BoronPic.png")
BoronImage2 = BoronImage1.subsample(4)
BoronButton = tk.Button(window,
                           image = BoronImage2,
                           borderwidth = 0,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = BoronButtonFunction,
                           )
BoronButton.grid(row = 3, column = 14)

CarbonImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\CarbonPic.png")
CarbonImage2 = CarbonImage1.subsample(4)
CarbonButton = tk.Button(window,
                           image = CarbonImage2,
                           borderwidth = 0,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = CarbonButtonFunction,
                           )
CarbonButton.grid(row = 3, column = 15)

NitrogenImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\NitrogenPic.png")
NitrogenImage2 = NitrogenImage1.subsample(4)
NitrogenButton = tk.Button(window,
                           image = NitrogenImage2,
                           borderwidth = 0,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = NitrogenButtonFunction,
                           )
NitrogenButton.grid(row = 3, column = 16)

OxygenImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\OxygenPic.png")
OxygenImage2 = OxygenImage1.subsample(4)
OxygenButton = tk.Button(window,
                           image = OxygenImage2,
                           borderwidth = 0,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = OxygenButtonFunction,
                           )
OxygenButton.grid(row = 3, column = 17)

FluorineImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\FluorinePic.png")
FluorineImage2 = FluorineImage1.subsample(4)
FluorineButton = tk.Button(window,
                           image = FluorineImage2,
                           borderwidth = 0,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = FluorineButtonFunction,
                           )
FluorineButton.grid(row = 3, column = 18)

NeonImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\NeonPic.png")
NeonImage2 = NeonImage1.subsample(4)
NeonButton = tk.Button(window,
                           image = NeonImage2,
                           borderwidth = 0,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = NeonButtonFunction,
                           )
NeonButton.grid(row = 3, column = 19)

SodiumImage1 = PhotoImage (file = r"C:\Users\yeonj\OneDrive\Desktop\Elite\ElementPics\SodiumPic.png")
SodiumImage2 = SodiumImage1.subsample(4)
SodiumButton = tk.Button(window,
                           image = SodiumImage2,
                           borderwidth = 0,  
                           height = BUTTONHEIGHT,
                           width= BUTTONWIDTH,
                           #command = SodiumButtonFunction,
                           )
SodiumButton.grid(row = 4, column = 2)











# #GO Section
GoSectionbg = "#%02x%02x%02x" % (0,0,153)
GoSectionbd = "#%02x%02x%02x" % (0,76,153)

GoSection = tk.Label(window,
                     bg = GoSectionbg,
                     height = 10,
                     width = 150,
                     padx=40,
                     text = "labelPlaceHolder",
                     fg = GoSectionbd
                     )
GoSection.grid(row=20, column=1, columnspan=30)
window.grid_rowconfigure(20, weight=3)
#GoSection.pack(side="bottom", fill="x")



                  


























window.mainloop()






