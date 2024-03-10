#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

#include "split_string.h"

int card_number(int i) {
    std::unordered_map<int, int> card_val (
            {
                {65, 0},
                {75, 1},
                {81, 2},
                {84, 3},
                {57, 4},
                {56, 5},
                {55, 6},
                {54, 7},
                {53, 8},
                {52, 9},
                {51, 10},
                {50, 11},
                {49, 12},
                {48, 13},
                {74, 14}
            }
            );
    return card_val[i];
}

int label_hand(std::string hand) {
    std::unordered_map <char, int> counter;
    for (char &h : hand) {
        if (counter.find(h) == counter.end()) {
            counter[h] = 1;
        }
        else {
            counter[h] += 1;
        }
    }
    for (auto x : counter) {
        std::cout << x.first << "," << x.second << std::endl;
    }
    std::cout << "=======" << std::endl;

    // Here process J's
    int j_num = counter['J'];
    int min = 1;
    char card = 0;
    for (auto card_type : counter) {
        // find the card with the most
        if (card_type.first == 'J') continue;
        if (card_type.second > min) {
            card = card_type.first;
            min = card_type.second;
        }
        else if (card_type.second == min) {
            // Find highest card in card type.
            if (card == 0) {
                card = card_type.first;
            }
            else if (card_number(card_type.first) < card_number(card)) {
                card = card_type.first;
            }
        }
    }

    std::cout << hand << " : " << card << std::endl;

    // Add j num to highest card and remove J
    if (counter['J'] == 5) {  // We don't have card set if 5 J.
        counter['A'] = 5;
    }
    else {
        counter[card] += counter['J'];
    }
    counter.erase('J');
    enum hand_enum {nothing, one, two, three, full, four, five};
    hand_enum state;
    state = nothing;
    for (auto kv : counter) {
        std::cout << kv.first << "," << kv.second << std::endl;
        if (kv.second != 1) {
            if (state == nothing) {
                if (kv.second == 5) {
                    return 6;
                }
                else if (kv.second == 4) {
                    return 5;
                }
                else if (kv.second == 3) {
                    state = three;
                }
                else if (kv.second == 2) {
                    state = one;
                }
            }
            else if (state == one) {
                if (kv.second == 2) {
                    return 2;
                }
                else if (kv.second == 3) {
                    return 4;
                }
            }
            else if (state == three) {
                return 4;
            }
        }
    }
    return state;
}

bool compare_hands (std::pair<std::string, int> a, std::pair<std::string, int> b){

    if (a.second < b.second) {
        return true;
    }
    else if (a.second > b.second ) {
        return false;
    }
    else {
        for(int i = 0; i < a.first.size(); i++) {
            int a_val = card_number(a.first[i]);
            int b_val = card_number(b.first[i]);
            // order reverses because I return higher card = lower value.
            if (a_val > b_val) {
                return true;
            }
            else if(a_val < b_val) {
                return false;
            }
        }
    }
    return true;
}

void do_1(std::string input) {
    std::ifstream f;
    std::string line;
    f.open(input);
    std::vector<std::string> lines;
    while(std::getline(f, line)) {
        //std::cout << line << std::endl;
        lines.push_back(line);
    }
    //std::vector<std::string> temp;
    std::vector<std::string> hands;
    std::vector<std::string> bids;
    std::vector<std::string> temp;
    std::unordered_map<std::string, int> hands_to_bids;
    for (auto l : lines) {
        temp = split_string(l, ' ');
        hands.push_back(temp[0]);
        bids.push_back(temp[1]);
        hands_to_bids[temp[0]] = std::stoi(temp[1]);
    }
    //std::map<std::string, int> final_map;
    std::vector<std::pair<std::string, int>> final_map;
    for (auto h : hands) {
        //final_map[h] = label_hand(h);
        final_map.push_back({h, label_hand(h)});
        std::cout << "+++++++++++++" << std::endl;
    }


    std::sort(final_map.begin(), final_map.end(), compare_hands);

    long sum = 0;
    for (int i = 0; i < final_map.size(); i++) {
    //for (auto h : final_map) {
        std::cout << final_map[i].first << "," << final_map[i].second << std::endl;
        std::cout << hands_to_bids[final_map[i].first] << std::endl;
        sum += hands_to_bids[final_map[i].first] * (i + 1);  // +1 so no multiplication by 0
    }
    std::cout << sum << std::endl;
}

int main(int argc, char * argv[]) {
    if (argc < 2) {
        std::cout << "Need file" << std::endl;
        return 0;
    }
    do_1(std::string(argv[1]));

    return 0;
}
