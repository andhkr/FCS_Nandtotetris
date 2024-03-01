#include "Code.h"

std::vector<BITS*> DEST {
Creation("null","000"),
Creation("M","001"),
Creation("D","010"),
Creation("DM","011"),
Creation("MD","011"),
Creation("A","100"),
Creation("AM","101"),
Creation("MA","101"),
Creation("DA","110"),
Creation("AD","110"),
Creation("ADM","111")
};

std::vector<BITS*> COMP{
Creation("0","0101010"),
Creation("1","0111111"),
Creation("-1","0111010"),
Creation("D","0001100"),
Creation("A","0110000"),
Creation("M","1110000"),
Creation("!D","0001101"),
Creation("!A","0110001"),
Creation("!M","1110001"),
Creation("-D","0001111"),
Creation("-A","0110011"),
Creation("-M","1110011"),
Creation("D+1","0011111"),
Creation("A+1","0110111"),
Creation("M+1","1110111"),
Creation("D-1","0001110"),
Creation("A-1","0110010"),
Creation("M-1","1110010"),
Creation("D+A","0000010"),
Creation("A+D","0000010"),
Creation("D+M","1000010"),
Creation("M+D","1000010"),
Creation("D-A","0010011"),
Creation("D-M","1010011"),
Creation("A-D","0000111"),
Creation("M-D","1000111"),
Creation("A&D","0000000"),
Creation("D&A","0000000"),
Creation("M&D","1000000"),
Creation("D&M","1000000"),
Creation("D|A","0010101"),
Creation("A|D","0010101"),
Creation("D|M","1010101"),
Creation("M|D","1010101"),

};

std::vector<BITS*> JUMP{
Creation("null","000"),
Creation("JGT","001"),
Creation("JEQ","010"),
Creation("JGE","011"),
Creation("JLT","100"),
Creation("JNE","101"),
Creation("JLE","110"),
Creation("JMP","111")
};

std::string get_value(std::string& c_part, std::vector<BITS*>& C_INSTRN){

    size_t k = C_INSTRN.size();
    int i {0};
    std::string bits;
    while(i<k){
        if (C_INSTRN[i]->C_part == c_part){
            bits = C_INSTRN[i]->str_Bits;
            break;
        }
        i++;
    }
    return bits; 
}

std::string Dest(std::string c_part){
    return get_value(c_part,DEST);
}

std::string Comp(std::string c_part){
    return get_value(c_part,COMP);
}

std::string Jump(std::string c_part){
    return get_value(c_part,JUMP);
}

void Code_obj_delete(){
    size_t i = 0;
    size_t k= DEST.size();
    while(i<k){
        delete DEST[i];
        i++;
    }
    i = 0;
    k = COMP.size();
    while(i<k){
        delete COMP[i];
        i++;
    }
    i = 0;
    k = JUMP.size();
    while(i<k){
        delete JUMP[i];
        i++;
    }
}



