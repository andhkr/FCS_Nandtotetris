#ifndef BITS_H
#define BITS_H
#include <iostream>
#include <vector>
#include <string>

class BITS{
    public:
        std::string C_part;
        std::string str_Bits;

    public:
        BITS()=default;
        BITS(std::string& C_part, std::string& str_Bits);
        ~BITS(){}
};

BITS* Creation(std::string c_part, std::string str_bit);

#endif