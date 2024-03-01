class jackTokeniser:
    def __init__(self,filename):
        self.file = filename
        self.XML=["<tokens>"]
        self.symbol = ['{','}','(',')','[',']','.',',',';','=','+','-','*',
                       '/','&','|','<','>','~']
        
        self.keyword = ["class","constructor","function","method","field","static",
               "var","int","char","boolean","void","true","false",
               "null","this","let","do","if","else","while","return"
                ]
        
        
        with open(self.file,"r") as f:
            self.codeline = f.readlines()

    def HasMorelines(self):
        if len(self.codeline) == 0:
            return False
        else :
            return True
        
    
    def Advance(self):
        f_codeline = self.codeline[0].strip()
        
        if f_codeline.strip()=="":
            del self.codeline[0]
        elif f_codeline[0] == "/" or f_codeline[0] == "*":
            del self.codeline[0]
        else:
            if "//" in f_codeline:
                code = f_codeline[:f_codeline.find('//')].strip()
                self.token_list = []
                self.token_desider(code)
                del self.codeline[0]
            else:
                self.token_list = []
                self.token_desider(f_codeline)
                del self.codeline[0]

    def token_desider(self,code):
        d = [i for i in code]
        b = ""
        i=0
        while (i<len(d)):
            if d[i].isalpha() == True:
                b = b+d[i]
            
            elif d[i] == ' ':
                if b != "":     
                    self.token_list.append(b)
                    del b
                    b = ""

            elif d[i].isnumeric() :
                b= b+d[i]
                

            elif d[i] in self.symbol:
                if b!="":
                    self.token_list.append(b)
                    del b
                    b = ""
                self.token_list.append(d[i])
                
            elif d[i] == '"':
                self.token_list.append([code[code.find('"')+1:code.rfind('"')]])
                i = int(code.rfind('"'))
            i = i+1
                
        self.XML_input(self.token_list)

    def XML_input(self,tokenlist):
        for i in tokenlist:
            
            if i in self.keyword:
                xml = f"<keyword> {i} </keyword>"
                self.XML.append(xml)
                continue

            elif i in self.symbol:

                if i == "<":
                    xml = f"<symbol> &lt; </symbol>"
                    self.XML.append(xml)
                    continue
                elif i == ">":
                    xml = f"<symbol> &gt; </symbol>"
                    self.XML.append(xml)
                    continue
                elif i == "&":
                    xml = f"<symbol> &amp; </symbol>"
                    self.XML.append(xml)
                    continue
                else:
                    xml = f"<symbol> {i} </symbol>"
                    self.XML.append(xml)
                    continue
            
            try:
                
                if isinstance(int(i),int):
                    xml= f"<integerConstant> {int(i)} </integerConstant>"
                    self.XML.append(xml)
                    

            except:
                pass
            try:
                if isinstance(i,list):
                    xml = f"<stringConstant> {i[0]} </stringConstant>"
                    
                    self.XML.append(xml)
            except:
                pass
            try:
                if i.isalpha() :
                    xml = f"<identifier> {i} </identifier>"
                    
                    self.XML.append(xml)
            except:
                pass
                
            
    def Tokeniser(self):
        while(self.HasMorelines()==True):
            self.Advance()
        self.XML.append("</tokens>")
        return self.XML


            

            