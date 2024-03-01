#ifndef PARSER_H_
#define PARSER_H_
#include <iostream>
#include <string>
#include <fstream>

typedef struct InstructionType{
    int A_INSTRUCTION  {0};
    int C_INSTRUCTION {0};
    int L_INSTRUCTION {0};
}Type;

class Parser{
    public:
        std::string file_name;
        std::fstream file;
        std::string current_instruction;
        int linenumber;
        int times_parsing;
        int instruction;
        Type A_C_L_instruction;
        std::string symbol_value;
    
    public:
        Parser()=default;

        Parser(std::string filename);

        bool hasMoreLines();

        void strip_space();

        void advance();

        void instruction_type();

        void symbol();

        int dest();

        void comp();
        
        int jump();
};

#endif