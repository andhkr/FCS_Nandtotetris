from CodeWriter import code

class parser:
    def __init__(self,file):
        self.filename=file
        self.codeobj=code(self.filename)

        with open(self.filename,"r") as f:
            self.list = f.readlines()

    def HasMorelines(self):
        if len(self.list)==0:
            return False
        else:
            return True

    def Advance(self):
        self.a = self.list[0].strip()
        self.b=self.a.split()

        if self.a == "":
            del self.list[0]

        elif self.a[0] == "/":
            del self.list[0]

        else:
            if "/" in self.a:
                s = self.a.rfind("/")
                r = self.a[:(s-1)].strip()
                self.b = r.split()
                self.commandType()
                del self.list[0]
            else:
                self.commandType()
                del self.list[0]
        
    def commandType(self):
        if "push" in self.b:
            cmd = "push"
            arg1 = self.Arg1()
            arg2 = self.Arg2()

            self.codeobj.codepushpop(cmd,arg1,arg2)

        elif "pop" in self.b:
            cmd = "pop"
            arg1 = self.Arg1()
            arg2 = self.Arg2()

            self.codeobj.codepushpop(cmd,arg1,arg2)

        elif self.b in self.codeobj.Aritmetic_cmds:
            
            self.codeobj.codeArithmetic(self.b[0])

        elif self.b[0] == "label":
            self.codeobj.Writelabel(self.b[1])

        elif self.b[0] == "goto":
            self.codeobj.Writegoto(self.b[1])

        elif self.b[0] == "if-goto":
            self.codeobj.Writeif(self.b[1])
        
        elif self.b[0] == "function":
            self.codeobj.WriteFunction(self.b[1],self.b[2])
        
        elif self.b == ["return"]:
            self.codeobj.WriteReturn()

        elif self.b[0] == "call":
            self.codeobj.Writecall(self.b[1],self.b[2])
        

    def Arg1(self):
        return self.b[1]

    def Arg2(self):
        return self.b[2]
    
    def VMT(self):
        while (self.HasMorelines()):
            self.Advance()
        return self.codeobj.output    
    


    

