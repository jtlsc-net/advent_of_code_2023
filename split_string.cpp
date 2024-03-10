#include "split_string.h"

std::vector<std::string> split_string(std::string input_str, char delim) {
    std::string temp; // Not efficient, will probably realloc a lot.
    std::vector<std::string> output;

    for (char &ch : input_str) {
        if (ch == delim) {
            if (temp.size() > 0){
                output.push_back(temp); 
            }
            temp = "";
        }
        else {
            temp.push_back(ch);
        }
    }

    // Do one last push to get last substr
    if (temp.size() > 0) {
        output.push_back(temp);
    }
    return output;
}
