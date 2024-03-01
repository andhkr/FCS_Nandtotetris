objects: Assembler.o Parser.o Symbol.o Bits.o Code.o
	g++ Assembler.o Parser.o Symbol.o Bits.o Code.o -o Hack_Assembler
Assembler.o: Assembler.cpp 

Parser.o: Parser.cpp

Symbol.o: Symbol.cpp

Bits.o: Bits.cpp

Code.o: Code.cpp

clean:
	rm -rf *.o
	rm -rf Hack_Assembler
