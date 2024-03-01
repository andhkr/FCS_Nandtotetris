class VMwriter:
    def __init__(self,file):
        self.file_name= file
        self.vmcode=[]
        

    def wriePush(self,x,y):
        self.vmcode.append("push"+" "+f"{x}"+" "+f"{y}")
        

    def writePop(self,x,y):
        self.vmcode.append("pop"+" "+f"{x}"+" "+f"{y}")
        

    def writeArithmetic(self,x):
        self.vmcode.append(x)
        

    def writeLabel(self,x):
        self.vmcode.append(f"label {x}")

    def writeGoto(self,x):
        self.vmcode.append(f"goto {x}")

    def writeIf(self,x):
        self.vmcode.append(f"if-goto {x}")

    def writeCall(self,x,y):
        self.vmcode.append("call"+" "+f"{x}"+" "+f"{y}")

    def writeFunction(self,x,y):
        self.vmcode.append("function"+" "+f"{x}"+" "+f"{y}")

    def writeReturn(self):
        self.vmcode.append("return")

    def VM(self):
        
        with open(self.file_name[:self.file_name.find("T.")]+".vm","w") as f:
            for i in self.vmcode:
                f.write(i+"\n")
        self.vmcode.clear()
