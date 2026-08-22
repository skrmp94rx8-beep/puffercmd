import random as rand
import numpy
import os
import sys
import time
import typing
import requests
puffercmd = type('pufferfish', (), {})()
puffercmd.version = "Jupyter v12.0-beta"
def k(*args,**kwargs):
    se = kwargs.get('sep', ' ')
    en = kwargs.get('end', '\n')
    fil = kwargs.get('file', None)
    print(*args,end=en,sep=se,file=fil)

def losc(value):
    try:
        output = str(value)
        output = output.replace("[", "").replace("]", "").replace("'", "")
        return output
    except Exception as e:
        print(f"bro think! {e}!")
        return None

def ni(v):
    try:
        v = int(v)
        return v
    except (ValueError, TypeError) as e:
        print(f"bro dont input string,if you input your code will: {e}")
        return None

def flt(v):
    try:
        v = float(v)
        return v
    except (ValueError, TypeError) as e:
        print(f"bro dont input string,if you input your code will: {e}")
        return None

def si(value,hint):
    if hint != "NH":
        value = input(hint)
        return value
    else:
        value = input()
        return value

def end():
    print("\r---------------------------------------------------")

def non():
    pass

def decl(list):
    listf = str(list)
    listf = listf.replace("{","").replace("}","").replace(":","=")
    return listf

def bug(name,reason,cell,line):
    k(f"=======================\nTraceBack(most recent call last):\nin cell{cell},line{line}:\n{name}:{reason}")

def wind(power, value):
    stop = f"{value:>{power}}"
    return stop

def idjt(o):
    if type(o) == str:
        return o.isdigit()
    else:
        return False

def iflt(o):
    if type(o) == float:
        return True
    else:
        return False

def istr(o):
    if type(o) == str:
        return True
    else:
        return False

def isl(o):
    if type(o) == list:
        return True
    else:
        return False

def isd(o):
    if type(o) == dict:
        return True
    else:
        return False

def title(t):
    print(">------{}------<".format(t))

def losd(list):
    listf = str(list)
    listf = listf.replace("{","").replace("}","").replace(":","")
    return listf

class EmptyError(Exception):
    pass
class Joke(Exception):
    pass
class EmptyDetect:
    @staticmethod
    def Detect():
        a = input()
        if len(a) == 0:
            raise EmptyError("Empty")
        else:
            print("Something")

class WrongInput(Exception):
    pass
def BeAdmin():
    raise Joke("bro got pranked lol this is not the real func to be admin lol")
class Op:
    def __init__(self):
        self.__Op = False
        self.__Acd = False
    def BeOperator(self):
        if self.__Acd:
            print("you already are the opreator.")
        pw = input("please input password")
        if pw == "RMAF,CEO/CTO,p͚u͚f͚f͚e͚r͚f͚i͚s͚h͚i͚s͚g͚o͚o͚d͚,pythoner":
            self.__Op = True
            self.__Acd = True
            print("you're opreator now!")
        else:
            raise PermissionError("Access Denied.")
    
    def UnInstall(self):
        if hasattr(self, '_Op__Acd') and not self.__Op:
            raise WrongInput("you are lying.")
        if self.__Op:
            
            import sys
            current_module = sys.modules[__name__]
            
            
            for name in ['k', 'vi', 'losc', 'decl', 'wind', 'ni', 'flt',
                         'check_vardefed', 'si', 'bug', 'end', 'non',
                         'idjt', 'iflt', 'istr', 'isl', 'isd', 'klang', 'title']:
                try:
                    delattr(current_module, name)
                except AttributeError:
                    pass
            
            print("fully uninstalled!")
        else:
            raise PermissionError("you have no permission to uninstall.")

class assemble:
    def __init__(self):
        self.assembled_1 = False
        self.assembled_2 = False
        self.assembled_3 = False
        self.assembled_4 = False
    def assemble_MLM(self):
        if not self.assembled_1:
            class MLM: #Multi List Memory
                def __init__(self):
                    self.NL = []
                    self.DL = []
                def name(self,p,n):
                    if p==0:
                        raise ValueError("WTF are you doing")
                    if len(self.NL) >= p:
                        self.NL[p-1] = n
                    else:
                        while len(self.NL) < p:
                            self.NL.append("")
                        self.NL[p-1] = n
                def data(self,p,n):
                    if p==0:
                        raise ValueError("WTF are you doing")
                    if len(self.DL) >= p:
                        self.DL[p-1] = n
                    else:
                        while len(self.DL) < p:
                            self.DL.append("")
                        self.DL[p-1] = n
                def accessnad(self,np):
                    return self.DL[self.NL.index(np)]
            self.assembled_1 = True
        else:
            print("you silly boi,you already assembled MLM!")
    def assemble_loggingsys(self):
        if not self.assembled_2:
            class loggingsys:
                def __init__(self):
                    self.clog = []
                    self.celog = []
                    self.ceelog = []
                    self.elsm = "damn,"
                def nlog(self,lmsg):
                    self.clog.append(lmsg)
                def selog(self,lmsg):
                    self.celog.append(lmsg)
                def olbtt(self):
                    print(f"normal logs:{self.clog}")
                    print(f"slient err logs:{self.celog}")
                    print(f"err logs:{self.ceelog}")
                def elog(self,lmsg):
                    self.ceelog.append(self.elsm + lmsg)
                def ctlog(self,msg):
                    c = input(msg)
                    if bool(c):
                        self.olbtt()
                    else:
                        raise ValueError("Invalid choice.")
                self.nlog("assembled and started by puffercmd")
            self.assembled_2 = True
        else:
            print("silly,loggingsys is already assembled!")
    def assemble_pointer(self):
        if not self.assembled_3:
            class pointer:
                def __init__(self):
                    self.pointer_ = 0
                    self.step = 0
                def spawnpointeratlist(self,li):
                    if type(li) != list:
                        raise TypeError("LIST!!!")
                    self.lip = li
                    self.pointer_ = self.lip[self.step]
                def _R(self):
                    if self.step != len(self.lip) - 1:
                        self.step += 1
                        self.pointer_ = self.lip[self.step]
                def _L(self):
                    if self.step != 0:
                        self.step -= 1
                        self.pointer_ = self.lip[self.step]
                def getpointertext(self):
                    return self.pointer_
                def deletethispointer(self):
                    self.pointer_ = 0
                    self.step = 0
                    self.lip = None
                def search(self,target,returntype="p"):
                    if self.lip == [] or self.lip == None:
                        raise ValueError("wtf bro why search a empty list")
                    self.pointer_ = 0
                    self.step = 0
                    start_step = self.step
                    while self.step < len(self.lip):
                        if self.pointer_[0] == target:
                            if returntype == "p":
                                print("target found!")
                            elif returntype == "rt":
                                return True
                            else:
                                raise ValueError("invalid type of outputing.")
                        self._R()
                    self.step = start_step
                    while self.step > -1:
                        if self.pointer_ == target:
                            if returntype == "p":
                                print("target found!")
                            elif returntype == "rt":
                                return True
                            else:
                                raise ValueError("invalid type of returning.")
                        self._L()
                    if returntype == "p":
                        print("target not found!")
                    elif returntype == "rt":
                        return False
                    else:
                        raise ValueError("invalid type of returning.")
                def CR(self,steps):
                    for i in range(steps):
                        self._R()
                def CL(self,steps):
                    for i in range(steps):
                        self._L()
                def p_goto(self,place):
                    firstround = True
                    secondround = False
                    if place <= len(self.lip):
                        while firstround:
                            if self.step != place:
                                self.step -= 1
                                self.pointer_ = self.lip[self.step]
                            else:
                                firstround = False
                                secondround = True
                        while secondround:
                            if self.step < len(self.lip):
                                self.step += 1
                                self.pointer_ = self.lip[self.step]
                                if self.step == place:
                                    firstround = False
                                    secondround = False
                    else:
                        raise ValueError("invalid value.")
            
                def p_Restart(self):
                    self.p_goto(0)
            
                def p_End(self):
                    self.CL(len(lip) - 1)
            self.assembled_3 = True
        else:
            print("ay yo you silly,pointer is already assembled!")
    
    def assemble_randseed(self):
        if not self.assembled_4:
            def testseed(s):
                random.seed(s,mn,tt)
                test: list[int] = []
                maxval = int(mn)
                for i in range(0,int(tt)):
                    i = random.randint(0,maxval)
                    test.append(i)
                top = max(test)
                last = min(test)
                average = sum(test) / len(test)
                average2 = ((max(test) - min(test)) / 2) + min(test) #midpoint but im stupid
                print("numbers:" + str(test))
                print("max:" + str(top))
                print("min:" + str(last))
                print("average type 1:" + str(average))
                print("average type 2:" + str(average2))
                print("reached top:" + (str(maxval in test)))
                print("reached bottom:" + (str(0 in test)))
            self.assembled_4 = True
        else:
            print("bro you silly,seedtester is already assembled!")

    def fullassembled(self):
        if self.assembled_1 and self.assembled_2 and self.assembled_3 and self.assembled_4:
            return True
            try:
                self.firsttimealready = self.firsttimealready
            except(Exception):
                self.nlog("fully assembled!")
            self.firsttimealready = True

def b(i):
    return bin(i)
def h(i):
    return hex(i)

def ccipher(txt1,txt2): #EZ CIPHER BRO
    txt = []
    t1c = 0
    t2c = 0
    m = max(len(txt1),len(txt2))
    for i in range(m*2+1):
        if i % 2 == 0 and i != 0:
            if t2c < len(txt2):
                txt.append(txt2[t2c])
                t2c += 1
        else:
            if t1c < len(txt1) and i != 0:
                txt.append(txt1[t1c])
                t1c += 1
    fintext=""
    for l in range(len(txt)):
        fintext = fintext + txt[l]
    return fintext

def dccipher(cipher):
    o1 = []
    o2 = []
    c = []
    for i in range(len(cipher)):
        if i % 2 == 0:
            o1.append(cipher[i])
        else:
            if i % 1 == 0:
                o2.append(cipher[i])
    fin = ""
    for l in range(len(o1)):
        fin = fin + o1[l]
    for I in range(len(o2)):
        fin = fin + o2[I]
    return fin

def sendr(target,header: dict,ret="c"):
    resp = requests.get(target,headers=header)
    if ret == "c":
        return resp.content
    elif ret == "sc":
        return resp.status_code
    else:
        raise ValueError("bro what are you requesting for")

'''
from IPython.core.magic import register_line_magic

@register_line_magic
def klang(line):
    python_code = line
    exec(python_code)
@register_line_magic
def eat():
    print("JACKFRUITSSSZZZZZZZ")
@register_line_magic
def cmd(command,commandinput,commandmod=None):
    if commandmod == None:
        get_ipython().run_line_magic(command,commandinput)
    else:
        get_ipython().run_line_magic(command,commandmod,commandinput)
''' #disabled magic lines
