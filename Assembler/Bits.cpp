#include "Bits.h"

BITS::BITS(std::string& C_part, std::string& str_Bits){
    this->C_part = C_part;
    this->str_Bits = str_Bits;
}

BITS* Creation(std::string c_part, std::string str_bit){
    BITS* p_obj = new BITS(c_part,str_bit);
    return p_obj; 
}