class SymbolTabel:

    

    def __init__(self):
        self.index_static=0
        self.index_field=0
        self.index_local=0
        self.index_Argument=0
        self.list=[]
        self.class_sym={}
        self.subr_sym={}
        self.subtype=""

    def class_var(self,xml):
        j = 0
        while True :
            token = xml[j:][0]
            
            a = xml[j:][xml[j:].index(token):xml[j:].index("<symbol> ; </symbol>\n")]
            
            if "<symbol> , </symbol>\n" not in a:
                self.add_SYMBOL(a,2)
            else:

                k = len(a)-list(reversed(a)).index("<symbol> , </symbol>\n")-1
                i = 2
                while i<=k+1:
                    self.add_SYMBOL(a,i)
                    
                    i = i+2
                
            j = j+xml[j:].index("<symbol> ; </symbol>\n")+1
            
            if not(xml[j] == "<keyword> field </keyword>\n" or xml[j] =="<keyword> static </keyword>"):
                break
            
    def subroutin_sym1(self,xml_par):
        self.subr_sym.clear()
        self.index_Argument=0
        self.index_local=0
        self.subtype=xml_par[-1]
        xml_par.remove(self.subtype)
        
        if xml_par != ['<symbol> ) </symbol>\n', '<symbol> { </symbol>\n']:
            
            k = 0
            while xml_par[k] != "<symbol> { </symbol>\n":
                
                a = []
                for i in range(2):
                    a.append(xml_par[i+k])
                    
                k=k+3
                
                self.add_SYMBOL(a,1)
            del a
    def subroutin_sym(self,xml_var):
            
            j = 0
            while True :
                d = xml_var[j:][xml_var[j:].index("<keyword> var </keyword>\n"):xml_var[j:].index("<symbol> ; </symbol>\n")]
            
                if "<symbol> , </symbol>\n" not in d:
                    
                    self.add_SYMBOL(d,2)
                    
                else:
                    k = len(d)-1-list(reversed(d)).index("<symbol> , </symbol>\n")
                    i = 2
                    while i<=k+1:
                        self.add_SYMBOL(d,i)
                        i = i+2
                j = j+xml_var[j:].index("<symbol> ; </symbol>\n")+1
                if xml_var[j] != "<keyword> var </keyword>\n":
                    break
            del d


    def add_SYMBOL(self,a,i):
        if self.key_rem(a[0]) == "field":
            self.class_sym[self.key_rem(a[i])]=[self.key_rem(a[1]),"this",self.index_field]
            self.index_field = self.index_field + 1
        elif self.key_rem(a[0]) == "static":
            self.class_sym[self.key_rem(a[i])]=[self.key_rem(a[1]),self.key_rem(a[0]),self.index_static]
            self.index_static = self.index_static + 1
        elif self.key_rem(a[0]) == "var":
            self.subr_sym[self.key_rem(a[i])]=[self.key_rem(a[1]),"local",self.index_local]
            self.index_local = self.index_local + 1
        else:
            if self.subtype == "method":
                self.index_Argument = self.index_Argument + 1
                self.subr_sym[self.key_rem(a[i])]=[self.key_rem(a[0]),"argument",self.index_Argument]
                
            else:
                self.subr_sym[self.key_rem(a[i])]=[self.key_rem(a[0]),"argument",self.index_Argument]
                self.index_Argument = self.index_Argument + 1


    

    def key_rem(self,a):
        b = a[a.find(" ")+1:a.rfind(" ")]
        return b
    

    def typeof(self,name):
        if name in self.subr_sym:
            return self.subr_sym[name][0]
        elif name in self.class_sym:
            return self.class_sym[name][0]
        else:
            return None
        
    def kindof(self,name):
        if name in self.subr_sym:
            return self.subr_sym[name][1]
        elif name in self.class_sym:
            return self.class_sym[name][1]
        else:
            
            return None
        
    def indexof(self,name):
        if name in self.subr_sym:
            return self.subr_sym[name][2]
        elif name in self.class_sym:
            return self.class_sym[name][2]
        else:
            
            return None





