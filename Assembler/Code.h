#ifndef CODE_H
#define CODE_H
#include "CinstructionTable.h"

std::string get_value(std::string& c_part, std::vector<BITS*>& C_INSTRN);

std::string Dest(std::string c_part);

std::string Comp(std::string c_part);

std::string Jump(std::string c_part);

void Code_obj_delete();
#endif