import sys
from JackTokeniser import jackTokeniser 
from Engine import compileEngine
from os import walk,path

class JackAnalyser:
    def __init__(self):
        self.filename=sys.argv[1]
        self.files = []
        
        if ".jack" in self.filename: 
            self.tokeniser=jackTokeniser(self.filename)
            self.t = self.tokeniser.Tokeniser()
            with open(self.filename[:self.filename.find(".")]+"T.xml","w") as c:
                for i in self.t:
                    c.write(i+"\n")
            
            self.compileng=compileEngine(self.filename[:self.filename.find(".")]+"T.xml")
            
            self.compileng.CompileClass()

        else:

            for (dirpath,directory,filenames) in walk(self.filename):
                for name in filenames:
                    if ".jack" in name:
                        self.files.append(path.join(dirpath,name))
                        
            for j in self.files:
                if ".jack" in j: 
                    self.tokeniser=jackTokeniser(j)
                    self.t = self.tokeniser.Tokeniser()
                    with open(j[:j.find(".")]+"T.xml","w") as c:
                        for i in self.t:
                            c.write(i+"\n")
                    
                    self.compileng=compileEngine(j[:j.find(".")]+"T.xml")
                    
                    
                    self.compile = self.compileng.CompileClass()
                    


if __name__ == '__main__':
    JackAnalyser()


