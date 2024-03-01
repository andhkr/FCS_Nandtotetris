from SymbolTable import SymbolTabel
from VMwriter import VMwriter
class compileEngine:
    def __init__(self,file):
        self.flag=0
        self.tokenfile=file
        self.i=0
        self.tokens=[]
        self.type=["int","char","boolean","void"]
        self.keywordconstant = ["true","false","null","this"]
        self.subroutine = ["constructor","function","method"]
        self.st=["let","if","while","do","return"]
        self.op = ['=','+','-','*','/','&amp;','|','&lt;','&gt;']
        self.Parsed=["<class>\n"]
        self.obj=SymbolTabel()
        self.objvm=VMwriter(self.tokenfile)
        self.symbol=[]
        self.subr_type=""
        self.type_name=""
        self.subr_name=""
        self.op1=[]
        self.f=0
        self.k=0
        self.arithmetic={"+":"add","-":"sub","!":"not","&lt;":"lt","&gt;":"gt","=":"eq","&amp;":"and","|":"or"}
        self.c=0
        self.osmethod=""
        self.osclass=""
        self.os=["Output","Screen","Array","Keyboard","Memory","Sys","String","Math"]
        self.fileclass=""
        self.letosclass=""
        self.letosmethod=""
        self.letfileclass=""
        
        with open(self.tokenfile,"r") as f:
            self.tokens = f.readlines()
            
        
    def CurrentToken(self):
        self.i = self.i +1
        self.xml = self.tokens[self.i]
        self.currentoken =self.xml[self.xml.find(' ')+1:self.xml.rfind(' ')]
        
    
    def nexttoken(self):
        self.xml1 = self.tokens[(self.i)+1]
        self.next =self.xml1[self.xml1.find(' ')+1:self.xml1.rfind(' ')]

    def CompileClass(self):
            self.CurrentToken()
            self.SyntaxChecker("class") 
            self.className=self.tokenfile[self.tokenfile.find('/')+1:self.tokenfile.find('.')-1]
            
            self.SyntaxChecker(self.className)
            
            self.SyntaxChecker("{") 
            self.symbol.clear()
            

            if self.currentoken == "static" or self.currentoken == "field":
                while self.currentoken == "static" or self.currentoken == "field":
                    self.CompileClassVarDec()
                    self.SyntaxChecker(";")
                
                self.symbol.append("end")
            
                self.obj.class_var(self.symbol)
                
                self.symbol.clear()

            while  self.currentoken == "method" or self.currentoken == "constructor" or self.currentoken == "function":
                
                self.CompileSubroutine()
            
            self.SyntaxChecker("}")
            
            
            self.objvm.VM()
            self.tokens.clear()
            self.symbol.clear()
            
        
        
    def CompileClassVarDec(self):
            
            self.SyntaxChecker(self.currentoken)
            
            while self.currentoken != ";":
                
                self.SyntaxChecker(self.type)
                
                self.SyntaxChecker(self.currentoken)
                if self.currentoken == ",":
                    while self.currentoken != ";":
                        self.SyntaxChecker(self.currentoken)

            

    def CompileSubroutine(self):
        
            self.subr_type=self.currentoken
            
            self.SyntaxChecker(self.currentoken)
            self.type_name=self.currentoken
            self.SyntaxChecker(self.type)
            self.subr_name=self.currentoken

            self.SyntaxChecker(self.currentoken) 
            self.SyntaxChecker("(") 
            self.CompileParameterList()
            self.SyntaxChecker(")")
            self.CompileSubroutineBody()
            
      

    def CompileParameterList(self):
            
            self.symbol.clear()
            if self.currentoken != ")":
                
                self.SyntaxChecker(self.type)
                self.SyntaxChecker(self.currentoken)
                if self.currentoken == ",":
                    while self.currentoken != ")":
                        self.SyntaxChecker(",")
                        self.SyntaxChecker(self.type)
                        self.SyntaxChecker(self.currentoken)

            
        

    def CompileSubroutineBody(self):
        
            self.SyntaxChecker("{")
            self.symbol.append(self.subr_type)
            self.obj.subroutin_sym1(self.symbol)
            
           
            self.symbol.clear()
            
            if self.currentoken == "var":
                self.CompileVarDec()

            if self.subr_type == "constructor":
                 
                 func=self.type_name+"."+self.subr_name
                 self.objvm.writeFunction(func,self.obj.index_local)
                 self.objvm.wriePush("constant",self.obj.index_field)
                 self.objvm.writeCall("Memory.alloc",1)
                 self.objvm.writePop("pointer",0)

            elif self.subr_type == "method":
                 func=self.className+"."+self.subr_name
                 self.objvm.writeFunction(func,self.obj.index_local)
                 self.objvm.wriePush("argument",0)
                 self.objvm.writePop("pointer",0)

            elif self.subr_type == "function":
                 func=self.className+"."+self.subr_name
                 self.objvm.writeFunction(func,self.obj.index_local)
                 

            while self.currentoken in self.st:
                self.CompileStatements()
            
            self.SyntaxChecker("}")
            

    def CompileVarDec(self):
        
            while self.currentoken not in self.st:
                self.SyntaxChecker("var")
                while self.currentoken != ";":
                    self.SyntaxChecker(self.currentoken)
                self.SyntaxChecker(";")

            self.symbol.append("end")
            self.obj.subroutin_sym(self.symbol)
            self.symbol.clear()
            
        
        
    def CompileStatements(self):
        
            self.symbol.clear()
            while self.currentoken in self.st:

                if self.currentoken == "let":
                    self.CompileLet()
                    self.symbol.clear()
                elif self.currentoken == "if":
                    self.Compileif() 
                    self.symbol.clear()
                elif self.currentoken == "while":
                    self.CompileWhile()
                    self.symbol.clear()
                elif self.currentoken == "do":
                    self.CompileDo()
                    self.symbol.clear()
                elif self.currentoken == "return":
                    self.CompileReturn()
                    self.symbol.clear()

            
        

    def CompileLet(self):

            while self.currentoken == "let":
                
                self.SyntaxChecker(self.currentoken)
                var1=self.currentoken
                self.SyntaxChecker(self.currentoken)
                sym=self.currentoken

                if self.currentoken == "[":
            
                    self.SyntaxChecker("[")
                    self.CompileExpression()
                    self.objvm.wriePush(self.obj.kindof(var1),self.obj.indexof(var1))
                    self.SyntaxChecker("]")
                    self.objvm.writeArithmetic("add")

                self.SyntaxChecker("=")

                if self.obj.key_rem(self.symbol[-2]) == "]":
            
                  self.CompileExpression()
                
                  self.objvm.writePop("temp",0)
                  self.objvm.writePop("pointer",1)
                  self.objvm.wriePush("temp",0)
                  self.objvm.writePop("that",0)
                else:
                    self.CompileExpression() 
                self.SyntaxChecker(";")
                if sym != "[": 
                    
                    self.objvm.writePop(self.obj.kindof(var1),self.obj.indexof(var1))
                
        

    def Compileif(self):
            currentIfCounter=self.f
            self.f=self.f+1
            
            self.SyntaxChecker("if")
            self.SyntaxChecker("(")
            self.CompileExpression()
            self.objvm.writeArithmetic("not")
            self.objvm.writeIf(f"Else_Part{currentIfCounter}")
            self.SyntaxChecker(")")
            self.SyntaxChecker("{")
            self.CompileStatements()
            self.SyntaxChecker("}")
            sym = self.currentoken

            if self.currentoken == "else":

                self.objvm.writeGoto(f"IF_else_end{currentIfCounter}")
                self.objvm.writeLabel(f"Else_Part{currentIfCounter}")
                self.SyntaxChecker("else")
                self.SyntaxChecker("{")
                self.CompileStatements()
                self.SyntaxChecker("}")

            if sym == "else":
               self.objvm.writeLabel(f"IF_else_end{currentIfCounter}")

            else:
                self.objvm.writeLabel(f"Else_Part{currentIfCounter}") 
            
        
    def CompileWhile(self):
        
            whilecounter=self.k
            self.k=self.k+1
            self.SyntaxChecker("while")
            self.SyntaxChecker("(")
            self.objvm.writeLabel(f"WHILE_EXP{whilecounter}")
            self.CompileExpression()
            
            self.objvm.writeArithmetic("not")
            self.objvm.writeIf(f"WHILE_END{whilecounter}")
            self.SyntaxChecker(")")

            self.SyntaxChecker("{")

            self.CompileStatements()
            self.objvm.writeGoto(f"WHILE_EXP{whilecounter}")
            self.objvm.writeLabel(f"WHILE_END{whilecounter}")
            self.SyntaxChecker("}")
           
        
    def CompileDo(self):

            while self.currentoken == "do":
                
                self.SyntaxChecker("do")
                self.Compilesubroutinecall()
                self.objvm.writePop("temp",0)
                self.SyntaxChecker(";")
                
        
    def CompileReturn(self):
            
            self.SyntaxChecker("return")
            if self.currentoken != ";":
                self.CompileExpression()
                self.objvm.writeReturn()
            else:
               self.objvm.wriePush("constant",0) 
               self.objvm.writeReturn()
            self.SyntaxChecker(";")
            

    def CompileExpression(self):
            
            self.CompileTerm()

            if self.currentoken in self.op:
                self.op1.append(self.currentoken)
                self.SyntaxChecker(self.currentoken)
                
                self.CompileTerm()
            self.operonstatck()
            


    def CompileTerm(self):
       
            if self.currentoken == "(":
                self.SyntaxChecker("(")
                self.CompileExpression()             
                self.SyntaxChecker(")")

            elif self.currentoken == "~":
                self.Aterm()

            elif self.currentoken == "-":
                self.Unaryop()

            elif self.currentoken != ")":
                    
                    if self.currentoken.isnumeric():
                            self.objvm.wriePush("constant",self.currentoken)
                    
                            self.SyntaxChecker(self.currentoken)
                    
                    
                    if self.currentoken.isalpha():
                            if self.obj.kindof(self.currentoken) != None:
                                self.objvm.wriePush(self.obj.kindof(self.currentoken),self.obj.indexof(self.currentoken))
                            if self.currentoken=="null" or self.currentoken=="false":
                                 self.objvm.wriePush("constant",0)
                            elif self.currentoken=="true":
                                 self.objvm.wriePush("constant",1)
                                 self.objvm.writeArithmetic("neg")
                            elif self.currentoken == "this":
                                 self.objvm.wriePush("pointer",0)
                            
                            
                            self.SyntaxChecker(self.currentoken)
                    
                    if " " in self.currentoken:
                        
                         self.string1(self.currentoken)  
                         self.SyntaxChecker(self.currentoken)
                   
                    if self.currentoken == "[":
                        self.SyntaxChecker("[")
                        self.CompileExpression()
                        
                        self.objvm.writeArithmetic("add")
                        
                        self.SyntaxChecker("]")
                       
                        if self.currentoken != "=":
                            
                            self.objvm.writePop("pointer",1)
                            self.objvm.wriePush("that",0)
                             
                
                    
                    if self.currentoken == ".":
                        self.letosclass=self.obj.key_rem(self.symbol[-1])
                        self.SyntaxChecker(".")
                        if self.letosclass[0].islower():
                            
                             self.letosclass=self.obj.typeof(self.letosclass)
                             self.letfileclass=self.letosclass
                             
                             
                        self.letosmethod=self.currentoken
                        self.SyntaxChecker(self.currentoken)
                        self.SyntaxChecker("(")
                        self.CompileExpressionList()
                        self.SyntaxChecker(")")
                        
                        if self.letosclass  in self.os:
                            a = self.letosclass+"."+self.letosmethod
                            self.objvm.writeCall(a,self.c)
                        elif self.letosclass == self.letfileclass:
                            a = self.letosclass+"."+self.letosmethod 
                            ar=((self.c)+1)
                            self.objvm.writeCall(a,ar)
                        else:
                            a = self.letosclass+"."+self.letosmethod
                            self.objvm.writeCall(a,self.c)
                        
                    
            


    def Aterm(self):
        self.SyntaxChecker("~")
        self.CompileTerm()
        self.objvm.writeArithmetic("not")


    def Unaryop(self):
        self.SyntaxChecker("-")
        self.CompileTerm()
        self.objvm.writeArithmetic("neg")

    def operonstatck(self):
        if self.op1 != []:
                self.nexttoken()
                
                if self.currentoken !="]" and self.currentoken not in self.op and self.next != ")":
                    
                    if self.op1[-1] == "*":
                        self.objvm.writeCall("Math.multiply",2)
                        self.op1.remove("*")
                    elif self.op1[-1]=="/":
                        self.objvm.writeCall("Math.divide",2)
                        self.op1.remove("/")
                    else:
                        self.objvm.writeArithmetic(self.arithmetic[self.op1[-1]])
                        p = self.op1[-1]
                        self.op1.remove(p)

                elif  (self.currentoken =="]" or self.currentoken ==")") and (self.obj.key_rem(self.symbol[-2]) in self.op):

                    if self.op1[-1] == "*":
                        self.objvm.writeCall("Math.multiply",2)
                        self.op1.remove("*")
                    elif self.op1[-1]=="/":
                        self.objvm.writeCall("Math.divide",2)
                        self.op1.remove("/")
                    else:
                        self.objvm.writeArithmetic(self.arithmetic[self.op1[-1]])
                        p = self.op1[-1]
                        self.op1.remove(p)
        self.nexttoken()
        if self.next == "{" and self.op1 != []:
             
             self.operonstatck()
             


    def CompileExpressionList(self):
        
            self.c=0
            if self.currentoken != ")":
                self.c=self.c+1
                self.CompileExpression()
                if self.currentoken == ",":
                    
                    while self.currentoken != ")":
                        self.c=self.c+1
                        self.SyntaxChecker(",")
                        self.CompileExpression()
                    
           


    def Compilesubroutinecall(self):
        
            self.c=0
            self.osclass=self.currentoken

            self.SyntaxChecker(self.currentoken)
            
            if self.currentoken == ".":
                self.SyntaxChecker(".")
                if self.osclass[0].islower():
                     
                     self.objvm.wriePush(self.obj.kindof(self.osclass),self.obj.indexof(self.osclass))
                     
                     self.osclass=self.obj.typeof(self.osclass)
                     
                     self.fileclass=self.osclass
                self.osmethod=self.currentoken
                self.SyntaxChecker(self.currentoken)
                
                self.SyntaxChecker("(")
                
                if self.currentoken != ")":
                    self.CompileExpressionList()
                    self.SyntaxChecker(")")

                else:
                    self.SyntaxChecker(")")
                
            elif self.currentoken == "(":

                if self.osclass[0].islower():
                    self.objvm.wriePush("pointer",0)
                self.SyntaxChecker("(")

                if self.currentoken != ")":
                    self.CompileExpressionList()
                    self.SyntaxChecker(")")
                    
                else:
                    
                    self.SyntaxChecker(")")
            
            if self.osclass[0].isupper():

                if self.osclass  in self.os:
                    a = self.osclass+"."+self.osmethod
                    self.objvm.writeCall(a,self.c)
                elif self.osclass == self.fileclass:
                    a = self.osclass+"."+self.osmethod 
                    ar=((self.c)+1)
                    self.objvm.writeCall(a,ar)
                else:
                    a = self.osclass+"."+self.osmethod
                    self.objvm.writeCall(a,self.c)

            elif self.osclass[0].islower():
                 a = self.className + "." +self.osclass
                 self.objvm.writeCall(a,self.c+1)
                
                    
            
            
                
            
            
    
    def SyntaxChecker(self,tokens):
        
        if self.currentoken == tokens:
            
            self.symbol.append(self.xml)
            self.CurrentToken()
            
        elif self.currentoken in tokens:
            self.symbol.append(self.xml)
            
            self.CurrentToken()

        elif self.currentoken == self.className:
            self.symbol.append(self.xml)
            
            self.CurrentToken()

        elif self.currentoken[0]==self.currentoken[0].upper():
            self.symbol.append(self.xml)
            
            self.CurrentToken()

        else:
            print(tokens)
            print(self.currentoken)
            print(f"{self.xml}")
            print(self.i)
            print("syntax error")

    def string1(self,strt):
         a = len(strt)
         self.objvm.wriePush("constant",a)
         self.objvm.writeCall("String.new",1)
         for i in range(a):
              self.objvm.wriePush("constant",ord(strt[i]))
              self.objvm.writeCall("String.appendChar",2)

        





    
        
    


