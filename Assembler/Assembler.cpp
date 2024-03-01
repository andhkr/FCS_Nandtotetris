#include <fstream>
#include "Code.h"
#include "Parser.h"
#include "SymbolTable.h"


std::string binary(int num){
    std::string output{""};
    int r {0};
    while(num!=0){
        r = (num - 2*(num>>1));
        num = num>>1;
        output = std::to_string(r)+output;
    }
    int k = output.size();
    while(k<16){
        output = '0'+output;
        k++;
    }
    return output;
}

int main(int argc, char* argv[]){
    Parser parse(argv[1]);
    if(parse.file.is_open()){
        parse.times_parsing = 0;
        while(parse.hasMoreLines()){
            parse.advance();
            if(parse.instruction){
                parse.instruction_type();
                parse.symbol();
                add_Entryl(parse.symbol_value, parse.linenumber);
            }
        }
        parse.file.close();


        Parser pass2nd(argv[1]);
        std::string hackfile;
        if(pass2nd.file_name.find('/')==-1){
        hackfile =  pass2nd.file_name.substr(0,
                                pass2nd.file_name.find('.')) + ".hack";
        }
        else{
            int reverse_posn = pass2nd.file_name.rfind('/');
            hackfile =  pass2nd.file_name.substr(0,reverse_posn+1)+
                        pass2nd.file_name.substr(reverse_posn+1,
                        (pass2nd.file_name.rfind('.')-(reverse_posn+1)))
                        + ".hack";
        }
        
        std::fstream my_hack;
        my_hack.open(hackfile,std::ios::out);
        if(my_hack.is_open()){
                
            pass2nd.times_parsing = 1;
            int var_address {16};
            while(pass2nd.hasMoreLines()){
                pass2nd.advance();
                if(pass2nd.instruction){
                    pass2nd.instruction_type();
                    if(pass2nd.A_C_L_instruction.A_INSTRUCTION){
                        pass2nd.symbol();
                        if(contains(pass2nd.symbol_value)){
                            my_hack<<binary(get_address(pass2nd.symbol_value))
                            <<std::endl;
                        }
                        else{
                            try {
                                int i{std::stoi(pass2nd.symbol_value)};
                                my_hack<<binary(i)<<std::endl;
                            }
                            catch(std::invalid_argument const& ex)
                            {
                                add_Entryl(pass2nd.symbol_value,var_address);
                                my_hack<<binary(var_address)<<std::endl;
                                var_address = var_address + 1; 
                            }

                        }

                    }
                    else {
                        my_hack<<"111";
                        pass2nd.comp();
                        my_hack<<Comp(pass2nd.symbol_value);
                        if(pass2nd.dest()){
                            my_hack<<Dest(pass2nd.symbol_value);
                        }
                        else{
                            my_hack<<"000";
                        }

                        if(pass2nd.jump()){
                            my_hack<<Jump(pass2nd.symbol_value)<<std::endl;;
                        }
                        else{
                            my_hack<<"000"<<std::endl;
                        }
                    }
                }
            }

            pass2nd.file.close();
            my_hack.close();
        }
        else{
            std::cout<<"unable to open file to write output"<<std::endl;
        }
        delete_obj();
        Code_obj_delete();
    }
    else{
        std::cout<<"unable to open file:"<<
                    "may be given file is not available in folder"<<std::endl;
    }
    return 0;
}

