#ifndef SYMBOL_H
#define SYMBOL_H

#include <iostream>
#include <string>
#include <vector>

class Symbol{
    public:
        std::string name;
        int value;
    public:
        Symbol()=default;
        Symbol(std::string& name, int value);
        ~Symbol(){}

    
};

Symbol* Creation(std::string symbol, int location);

void add_Entryl(std::string name, int value);

void print();

bool contains(std::string symbol);

int get_address(std::string symbol);

void delete_obj();


#endif