#include "SymbolTable.h"

std::vector<Symbol*> Table = {
Creation("R0",0),
Creation("R1",1),
Creation("R2",2),
Creation("R3",3),
Creation("R4",4),
Creation("R5",5),
Creation("R6",6),
Creation("R7",7),
Creation("R8",8),
Creation("R9",9),
Creation("R10",10),
Creation("R11",11),
Creation("R12",12),
Creation("R13",13),
Creation("R14",14),
Creation("R15",15),
Creation("SCREEN",16384),
Creation("KBD",24576),
Creation("SP",0),
Creation("LCL",1),
Creation("ARG",2),
Creation("THIS",3),
Creation("THAT",4)
};

Symbol::Symbol(std::string& name, int value){
    this->name = name;
    this->value = value;
}

Symbol* Creation(std::string symbol, int location){
    Symbol* p_obj = new Symbol(symbol,location);
    return p_obj;
}

void add_Entryl(std::string name, int value){
    Table.push_back(Creation(name,value));
}

void print(){
    for(Symbol* c:Table){
        std::cout<<c->name<<":"<<c->value<<std::endl;
    }
}

bool contains(std::string symbol){
    size_t k = Table.size();
    bool j{false};
    int i {0};
    while(i<k){
        if (Table[i]->name == symbol){
            j = true;
        }
        i++;
    }
    return j;

}

int get_address(std::string symbol){
    size_t k = Table.size();
     int i {0};
     int address{0};
    while(i<k){
        if (Table[i]->name == symbol){
            address = Table[i]->value;
            break;
        }
        i++;
    }
    return address;
}

void delete_obj(){
    size_t i {0};
    size_t k {Table.size()};
    while(i<k){
        delete Table[i];
        i++;
    }
}
