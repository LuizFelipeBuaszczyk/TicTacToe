#ifndef VALIDATE_H
#define VALIDATE_H

#include <stdbool.h>

static bool valid_play(int x, int y, int game[3][3]){
    if (x>=3 || y>=3 || x<0 || y<0) return false;
    if (game[x][y] != 0) return false;

    return true;
}

static bool is_winner(int player, int game[3][3]){
    
    // Horizontal
    if (game[0][0] == player && game[0][1] == player && game[0][2] == player) return true;
    if (game[1][0] == player && game[1][1] == player && game[1][2] == player) return true;
    if (game[2][0] == player && game[2][1] == player && game[2][2] == player) return true;

    // Verticle
    if (game[0][0] == player && game[1][0] == player && game[2][0] == player) return true;
    if (game[0][1] == player && game[1][1] == player && game[2][1] == player) return true;
    if (game[0][2] == player && game[1][2] == player && game[2][2] == player) return true;

    // Diagonally
    if (game[0][0] == player && game[1][1] == player && game[2][2] == player) return true;
    if (game[0][2] == player && game[1][1] == player && game[2][0] == player) return true;

    return false;
}

#endif
