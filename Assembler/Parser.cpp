
#include "Parser.h"


Parser::Parser(std::string filename){
    file_name = filename;
    file.open(file_name,std::ios::in);
    current_instruction = "";
    linenumber = 0;
    times_parsing = 0;
    instruction = 1;
    symbol_value = "";
}

bool Parser::hasMoreLines(){
    bool lines{false};
    if(!file.eof()){
        lines = true;
    }
    return lines;
        
}

void Parser::strip_space(){
    if(current_instruction.find(32)==0){
        int i {0};
        while(current_instruction[i]==32){
            current_instruction.erase(0,1);
        }
    }
    current_instruction = current_instruction.substr(0,current_instruction.length()-1);
            if(current_instruction.find(32)!=-1){
                int i = 0;
                std::string striped_instruction {};
                int num;
                while(current_instruction[i]!='\0'){
                    if(current_instruction[i]==32){
                        break;
                    }
                    striped_instruction=striped_instruction+current_instruction[i];

                    i++;
                }
                current_instruction = striped_instruction;

            }
}

void Parser::advance(){
    std::getline(file,current_instruction);
    strip_space();
    instruction = 1;
    if(times_parsing == 0){
        if( (current_instruction.find("//")==0)||
            (current_instruction.empty())      ){
                instruction = 0;
            }
        else{
            
            if(current_instruction[0]!='('){
                linenumber++;
                instruction = 0;
            }
        } 
    }
    else {
        if( (current_instruction.find("//")==0)||
            (current_instruction.empty())      ||
            (current_instruction[0]=='(')){
                instruction = 0;
        }
    }
}

void Parser::instruction_type(){
    switch (current_instruction[0])
    {
    case '@':
        A_C_L_instruction.A_INSTRUCTION = 1;
        A_C_L_instruction.L_INSTRUCTION = 0;
        A_C_L_instruction.C_INSTRUCTION = 0;
        break;
    case '(':
        A_C_L_instruction.A_INSTRUCTION = 0;
        A_C_L_instruction.L_INSTRUCTION = 1;
        A_C_L_instruction.C_INSTRUCTION = 0;
        break;
    default:
        A_C_L_instruction.A_INSTRUCTION = 0;
        A_C_L_instruction.L_INSTRUCTION = 0;
        A_C_L_instruction.C_INSTRUCTION = 1;
        break;
    }
} 

void Parser::symbol(){
    if(A_C_L_instruction.L_INSTRUCTION){
        symbol_value =  current_instruction.substr(
                        current_instruction.find('(')+1,
                        current_instruction.find(')')-1);
    }
    else if(A_C_L_instruction.A_INSTRUCTION){
        symbol_value =  current_instruction.substr(1);
    }

}

int Parser::dest(){
    int check{0};
    int index_eq = current_instruction.find('=');
    if(index_eq!=-1){
        symbol_value =  current_instruction.substr(0,index_eq);
        check = 1;
    }
    return check;     
}

void Parser::comp(){
    int index_eq     = current_instruction.find('=');
    int index_semico = current_instruction.find(';');
    if(index_eq!=-1){
            symbol_value =  current_instruction.substr(index_eq+1);

    }
    else
        symbol_value =  current_instruction.substr(0,index_semico);
}

int Parser::jump(){
    int check{0};
    int index_semico = current_instruction.find(';');
    if(index_semico!=-1){
        symbol_value =  current_instruction.substr(index_semico+1);
        check = 1;
    }
    return check;
}


    
        
