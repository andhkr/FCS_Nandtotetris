import sys
from Parser import parser
from os import walk

class main:
    sardar=[]



    def __init__(self):
        self.mypath=sys.argv[1]
        self.f = []
        self.sardar=[]
        self.medlist=[]
        if ".vm" in self.mypath:
            self.parserobj=parser(self.mypath)

            self.finallist=self.parserobj.VMT()

            with open(self.mypath[:self.mypath.find(".")]+".asm","w") as t:
                for i in self.finallist:
                    t.write(i)
        else :



            for (dirpath,dirnames,filenames) in walk(self.mypath):
                self.f.extend(filenames)
                break
            
            
            self.medlist.append("@256\nD=A\n@SP\nM=D\n")
            self.Writecall("Sys.init",0)
            for i in self.f:
                if ".vm" in i:
                    self.parserobj=parser(i)
                    self.sardar=self.parserobj.VMT()

                if self.sardar != []: 
                    for j in self.sardar:
                        self.medlist.append(j)
                    del self.sardar

            with open(self.mypath+".asm","w") as k:
                    for i in self.medlist:
                        k.write(i)

            
        # self.parserobj=parser(self.mypath)

        # self.finallist=self.parserobj.VMT()

        # with open(self.file[:self.file.find(".")]+".asm","w") as f:
        #     for i in self.finallist:
        #         f.write(i)
    def Writecall(self,f_name,nArgs):
        self.l = 0
        a = f_name 
        b = (f"@$ret.{self.l}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@LCL\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"+
             "@ARG\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"+
             f"@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@5\nD=A\n@{nArgs}\nD=D+A\n"+
             f"@SP\nD=M-D\n@ARG\nM=D\n@SP\nD=M\n@LCL\nM=D\n@{a}\n0;JMP\n($ret.{self.l})\n"
             )
        self.l = self.l+1
        self.medlist.append(b)

if __name__ == '__main__':
    main()