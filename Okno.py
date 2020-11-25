from tkinter import *

root = Tk()
root.title("Определение направления векторов по правилу левой руки")
#root.geometry('850x400')
root.resizable(0, 0)
w = 16
h = 8

bg_color = '#FBB96A'
bg_color = "white"


BtnH = 160
wB = 120
limit = 6
curB = 0
curJ = 0
curLawF = 0
curAmpF = 0
curVelP = 0
curVelE = 0

curCalc = 0
IsElectron = False
Mode = "empty"

indexes = [1, 2, 3, 4, 5, 6]

Bimg = PhotoImage(file="imgs/B.png")
Jimg = PhotoImage(file="imgs/I.png")
FAmperimg = PhotoImage(file="imgs/FAmper.png")
FLawrenceimg = PhotoImage(file="imgs/FLawrence.png")
alphaImg = PhotoImage(file = "imgs/sina.png")
Limg = PhotoImage(file = "imgs/L.png")
Qimg = PhotoImage(file = "imgs/Q.png")
vImg = PhotoImage(file = "imgs/v.png")
arrUp = PhotoImage(file="imgs/Arrow_up.png")
arrRight = PhotoImage(file="imgs/Arrow_right.png")
arrDown = PhotoImage(file="imgs/Arrow_down.png")
arrLeft = PhotoImage(file="imgs/Arrow_left.png")
dot = PhotoImage(file="imgs/dot.png")
cross = PhotoImage(file="imgs/cross.png")
question = PhotoImage(file="imgs/Question.png")

images = [question, arrUp, arrDown, arrRight, arrLeft, dot, cross]

CalcJV = [Jimg, vImg]
CalcFF = [FAmperimg, FLawrenceimg]
CalcLQ = [Limg, Qimg]

DicAmpF =  {36:2,45:2,53:2,64 : 2, 35:1,46:1,54:1,63:1,15:4,26:4,52:4,61:4,16:3,25:3,51:3,62:3,14:6,23:6, 31:6, 42:6,13:5,24:5,32:5,41:5}
DicJ = {35:2,46:2,54:2,63:2,36:1,45:1,53:1,64:1,16:4,25:4,51:4,62:4,15:3,26:3,52:3,61:3,13:6,24:6,32:6,41:6,14:5,23:5,31:5,42:5}


curB_Image = images[curB]
curJ_Image = images[curJ]
curLawF_Image = images[curLawF]
curAmpF_Image = images[curAmpF]
curVelP_Image = images[curVelP]
curVelE_Image = images[curVelE]

Ind_Text = StringVar()
AmperF_Text = StringVar()
LawrenceF_Text = StringVar()
J_Text = StringVar()
VelP_Text = StringVar()
VelE_Text = StringVar()
ChangerL = StringVar()
Rules = StringVar()
BorderText = StringVar()

Rules.set("Справка:\nПрограмма используется для опеределения направления векторов физических величин по правилу левой руки.\n\nАлгоритм работы с программой:\n 1. С помощью кнопок установите направления уже известных величин.\n 2. Нажмите на кнопку, соответствующую неизвестной величине, для того чтобы узнать её направление.\n3. Нажмите на кнопку 'Сброс', чтобы вернуть все значения к статусу непоределённых.\n\nВ случае, если вы определяете силу Лоренца, действующую на электрон, перед началом работы выставьте значение 'Скорость Электрона', нажав на кнопку 'Скорость Протона'");
Ind_Text.set(curB)
AmperF_Text.set(curAmpF)
LawrenceF_Text.set(curLawF)
J_Text.set(curJ)
VelP_Text.set(curVelP)
VelE_Text.set(curVelE)
BorderText.set("Калькулятор")
ChangerL.set("Скорость Протона")


def CalcChange():
    global curCalc
    curCalc += 1
    if (curCalc > 1):
        curCalc = 0
    CalcFF_L.configure(image = CalcFF[curCalc])
    CalcJV_L.configure(image = CalcJV[curCalc])
    CalcLQ_L.configure(image = CalcLQ[curCalc])
def BtnClick(Original, Alt, Alt2, Dic):
    if (Alt > 0 and Alt2 > 0):
        keyword = int(str(Alt) + str(Alt2))
        print(keyword)
        return Dic[keyword]
    else:
      AltExtra = 0
      AltExtra2 = 0
      if (Alt % 2 == 0):
          AltExtra = Alt - 1
      else: AltExtra = Alt + 1
      if (Alt2 % 2 == 0):
          AltExtra2 = Alt2 - 1
      else: AltExtra2 = Alt2 + 1
      if (Original == limit):
          Original = 0
          print ('original is limit')
      else: Original += 1;
      while (Original == Alt or Original == AltExtra or Original == AltExtra2 or Original == Alt2):
          Original+=1;
          if (Original >= limit):
              Original = 0
              print ("Doint while shit")
              break
      return Original
def ResetF():
    global curB
    global curJ
    global curAmpF
    global curLawF
    global curVelP
    global curLawF_Image
    global curB_Image
    global curJ_Image
    global curAmpF_Image
    global curVelP_Image
    global curVelE_Image
    global Mode
    curB = 0
    curJ = 0
    curLawF = 0
    curAmpF = 0
    curVelP = 0
    curB_Image = images[curB]
    curJ_Image = images[curJ]
    curLawF_Image = images[curLawF]
    curAmpF_Image = images[curAmpF]
    curVelP_Image = images[curVelP]
    Induction.configure(image = curB_Image, state = NORMAL)
    AmperF.configure(image = curAmpF_Image, state = NORMAL)
    J.configure(image = curJ_Image, state = NORMAL)
    LawrenceF.configure(image = curLawF_Image, state = NORMAL)
    VelP.configure(image = curVelP_Image, state = NORMAL)
    Mode = "empty"

def BlockLawrence():
    global Mode
    Mode = "Amper"
    VelP.configure(state = DISABLED)
    LawrenceF.configure(state = DISABLED)

def BlockAmper():
    global Mode
    Mode = "Lawrence"
    J.configure(state = DISABLED)
    AmperF.configure(state = DISABLED)
    
def Opposite(orig):
    if (orig % 2 > 0):
        orig -= 1
    else: orig += 1
def B_click():
    global curB
    global curJ
    global curAmpF
    global curLawF
    global curVelP
    global Mode
    print (Mode)
    if (Mode == "Lawrence"):
        if (IsElectron):
            curB = BtnClick(curB, curVelP, curLawF, DicJ)
        else:
            curB = BtnClick(curB, curVelP, curLawF, DicAmpF)
    else:
        curB = BtnClick(curB, curJ, curAmpF, DicAmpF)
    curB_Image = images[curB]
    Induction.configure(image = curB_Image)
    Ind_Text.set(curB)
def J_click():
    global curB
    global curJ
    global curAmpF
    global IsElectron
    global Mode
    if (Mode == "empty"):
        BlockLawrence()
        
    curJ = BtnClick(curJ, curB, curAmpF, DicJ)
    curJ_Image = images[curJ]
    VelP.configure(image = curVelP_Image)
    J.configure(image = curJ_Image)
    J_Text.set(curJ)
def AmperF_click():
    global curB
    global curJ
    global curAmpF
    global Mode
    if (Mode == "empty"):
        BlockLawrence()
        
    curAmpF = BtnClick(curAmpF, curB, curJ, DicAmpF)
    curAmpF_Image = images[curAmpF]
    AmperF.config(image=curAmpF_Image)
    AmperF_Text.set(curAmpF)
def LawrenceF_click():
    global curLawF
    global curB
    global curVelP
    global Mode
    if (Mode == "empty"):
        BlockAmper()
        
    if (IsElectron):
        curLawF = BtnClick(curLawF, curB, curVelP, DicJ)
    else:
        curLawF = BtnClick(curLawF, curB, curVelP, DicAmpF)
    curLawF_Image = images[curLawF]
    LawrenceF.configure(image=curLawF_Image)
    LawrenceF_Text.set(curLawF)
def VelP_click():
    global curVelP
    global curB
    global curLawF
    global curJ
    global Mode
    if (Mode == "empty"):
        BlockAmper()
    if (IsElectron):
        curVelP = BtnClick(curVelP, curB, curLawF, DicAmpF)
    else:
        curVelP = BtnClick(curVelP, curB, curLawF, DicJ)
    curJ_Image = images[curJ]
    curVelP_Image = images[curVelP]
    J.configure(image = curJ_Image)
    J_Text.set(curJ)
    VelP.configure(image = curVelP_Image)
    VelP_Text.set(curVelP)


def Change():
    global IsElectron
    global ChangerL
    global curLawF
    global curJ
    global curAmpF
    IsElectron = not IsElectron
    print (IsElectron)
    if (IsElectron):
        ChangerL.set("Скорость Электрона")
    else:
        ChangerL.set("Скорость Протона")
        
ResetL = '_'

Induction = Button(width = BtnH, height = BtnH ,command = B_click, image = curB_Image,bg = bg_color)
AmperF = Button(width = BtnH, height = BtnH, command = AmperF_click, image = curAmpF_Image,bg = bg_color)
LawrenceF = Button(width = BtnH, height = BtnH, command = LawrenceF_click, image = curLawF_Image,bg = bg_color)
J = Button(width = BtnH, height = BtnH, command = J_click, image = curJ_Image,bg = bg_color)
VelP = Button(width = wB, height = wB, command = VelP_click, image = curVelP_Image,bg = bg_color)
Reset = Button(width = wB, textvariable = ResetL, height = wB, command = ResetF, image = question,bg = bg_color)
VelChanger = Button(textvariable = ChangerL,wraplength = 80,font = ("Calibri", 12), width = w, height = h, command = Change,bg = bg_color)

InductionL= Label(image = Bimg,relief = RAISED, bg = bg_color)
AmperFL= Label(image =FAmperimg,relief = RAISED, bg = bg_color)
LawrenceFL= Label(image = FLawrenceimg,relief = RAISED, bg = bg_color)
JL = Label(image = Jimg,relief = RAISED, bg = bg_color)
VelPL = Label(relief = RAISED,wraplength = 5,font = ("Calibri", 12),text = "Скорость Протона", width = w, height = h,bg = bg_color)
ResetL = Label(relief = RAISED,font = ("Calibri", 12),text = "Сброс", width = w, height = h, bg = bg_color)
RulesL = Label(font = ("Calibri",12), bd = 5,wraplength = wB * 3,textvariable = Rules,width = 3*w, height = 3 * h, bg = bg_color)
ButtonsL = [VelP, LawrenceF, Reset]
ButtonsA = [J, AmperF,Induction]
LabelsA = [JL, AmperFL,InductionL]
LabelsL = [VelChanger, LawrenceFL, ResetL]


for col in range(len(ButtonsA)):
  LabelsA[col].grid(column = 1, row = col, columnspan = 1, rowspan = 1, sticky = "NESW")
  ButtonsA[col].grid(column = 2, row = col, columnspan = 1, rowspan = 1, sticky = "NESW") 
  LabelsL[col].grid(column = 3, row = col,columnspan = 1, rowspan = 1, sticky = "NESW")
  ButtonsL[col].grid(column = 4,row = col, columnspan = 1, rowspan = 1, sticky = "NESW")

RulesL.grid(column = 5, row = 0, columnspan = 4, rowspan = 4, sticky= "NESW")

root.mainloop()
