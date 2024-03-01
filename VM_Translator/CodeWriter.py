class code:
    def __init__(self,filename):
        self.filename=filename
        self.output=[]
        self.i=0
        self.j=0
        self.k=0
        self.l=0
        self.fnctn = ""
        # self.output.append(
            # "@256\nD=A\n@SP\nM=D\n"
        # )
        # self.Writecall("Sys.init",0)

    Pointer_Table={"local":"LCL","argument":"ARG","this":"THIS","that":"THAT"}
    
    Aritmetic_cmds=[["add"],["sub"],["neg"],["lt"],["eq"],["gt"],["and"],["or"],["not"]]

    def codeArithmetic(self,cmd):
        
        if cmd == "add":
            a="@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M+D\n@SP\nM=M+1\n"
            self.output.append(a)

        elif cmd == "sub":
            a="@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M-D\n@SP\nM=M+1\n"
            self.output.append(a)

        elif cmd == "neg":
            a="@SP\nM=M-1\nA=M\nM=-M\n@SP\nM=M+1\n"
            self.output.append(a)

        elif cmd == "eq":
            a=f"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\nM=0\n@EQ{self.i}\nD;JNE\n@SP\nA=M\nM=-1\n(EQ{self.i})\n@SP\nM=M+1\n"
            self.output.append(a)
            self.i = self.i+1

        elif cmd == "lt":
            a=f"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\nM=0\n@LT{self.j}\nD;JGE\n@SP\nA=M\nM=-1\n(LT{self.j})\n@SP\nM=M+1\n"
            self.output.append(a)
            self.j = self.j+1

        elif cmd == "gt":
            a=f"@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\nM=0\n@GT{self.k}\nD;JLE\n@SP\nA=M\nM=-1\n(GT{self.k})\n@SP\nM=M+1\n"
            self.output.append(a)
            self.k = self.k +1

        elif cmd == "and":
            a="@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M&D\n@SP\nM=M+1\n"
            self.output.append(a)

        elif cmd == "or":
            a="@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M|D\n@SP\nM=M+1\n"
            self.output.append(a)

        elif cmd == "not":
            a="@SP\nM=M-1\nA=M\nM=!M\n@SP\nM=M+1\n"
            self.output.append(a)
        
    def codepushpop(self,cmd,arg1,arg2):
        
        if cmd == "push":
            if arg1 != "temp" and arg1 != "pointer" and arg1 != "static" and arg1 != "constant":
                a = self.Pointer_Table[arg1]   
                b = f"@{a}\nD=M\n@{arg2}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
                self.output.append(b)

            elif arg1 == "temp":
                a = 5+int(arg2)
                b=f"@{a}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
                self.output.append(b)

            elif arg1 == "pointer":
                
                if arg2 == "0":
                    b="@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
                    self.output.append(b)
                elif arg2 == "1":
                    b="@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
                    self.output.append(b)

            elif arg1 == "constant":
                b=f"@{arg2}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
                self.output.append(b)

            elif arg1 == "static":
                a = self.filename[:self.filename.find(".")]+f".{arg2}"
                b=f"@{a}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
                self.output.append(b)

        elif cmd == "pop":
            
            if arg1 != "temp" and arg1 != "pointer" and arg1 != "static" and arg1 != "constant":
                a = self.Pointer_Table[arg1]   
                b = f"@SP\nM=M-1\nA=M\nD=M\n@R13\nM=D\n@{arg2}\nD=A\n@{a}\nD=D+M\n@R14\nM=D\n@R13\nD=M\n@R14\nA=M\nM=D\n"
                self.output.append(b)

            elif arg1 == "temp":
                a = 5+int(arg2)
                b=f"@SP\nM=M-1\nA=M\nD=M\n@{a}\nM=D\n"
                self.output.append(b)

            elif arg1 == "pointer":
                
                if arg2 == "0":
                    b="@SP\nM=M-1\nA=M\nD=M\n@THIS\nM=D\n"
                    self.output.append(b)
                elif arg2 == "1":
                    b="@SP\nM=M-1\nA=M\nD=M\n@THAT\nM=D\n"
                    self.output.append(b)

            elif arg1 == "static":
                a = self.filename[:self.filename.find(".")]+f".{arg2}"
                
                b=f"@SP\nM=M-1\nA=M\nD=M\n@{a}\nM=D\n"
                self.output.append(b)
    
    
    
    def Writelabel(self,label):
        a = self.fnctn+label
        b = f"({a})\n"
        self.output.append(b)


    def Writegoto(self,label):
        a = self.fnctn+label
        b = f"@{a}\n0;JMP\n"
        self.output.append(b)

    def Writeif(self,label):
        a = self.fnctn+label
        b = f"@SP\nM=M-1\nA=M\nD=M\n@{a}\nD;JNE\n"
        self.output.append(b)

    def WriteFunction(self,f_name,nVars):
        self.fnctn = f_name
        b = f"({self.fnctn})\n"
        for i in range(int(nVars)):
            b=b+f"@SP\nA=M\nM=0\n@SP\nM=M+1\n"
        self.l=0
        self.output.append(b)

    
    

    def WriteReturn(self):
        b = ("@LCL\nD=M\n@endframe\nM=D\n"+
             "@5\nD=A\n@endframe\nA=M-D\nD=M\n@retaddr\nM=D\n@SP\nA=M-1\nD=M\n@ARG\nA=M\nM=D\n@ARG\nD=M\n@SP\nM=D+1\n"+
             "@endframe\nM=M-1\nA=M\nD=M\n@THAT\nM=D\n@endframe\nM=M-1\nA=M\nD=M\n@THIS\nM=D\n"+
             "@endframe\nM=M-1\nA=M\nD=M\n@ARG\nM=D\n@endframe\nM=M-1\nA=M\nD=M\n@LCL\nM=D\n"+
             "@retaddr\nA=M\n0;JMP\n"
             )
        self.output.append(b)


    
    def Writecall(self,f_name,nArgs):
        a = f_name 
        b = (f"@{self.fnctn}$ret.{self.l}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@LCL\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"+
             "@ARG\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"+
             f"@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@5\nD=A\n@{nArgs}\nD=D+A\n"+
             f"@SP\nD=M-D\n@ARG\nM=D\n@SP\nD=M\n@LCL\nM=D\n@{a}\n0;JMP\n({self.fnctn}$ret.{self.l})\n"
             )
        self.l = self.l+1
        self.output.append(b)

        

        










        
        
        