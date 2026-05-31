#include "validate.h"

int game[3][3];
int current_player;

int start_game(){

    // Reseta o jogo
    for (int i=0; i<3; i++){
        for (int j=0; j<3; j++){
            game[i][j] = 0;
        }
    }

    current_player = 1;

    return 0;
}

int play(int x, int y){
    if (!valid_play(x, y, game)) {
        return 1;
    }
    
    game[x][y] = current_player;

    current_player *= -1;
    return 0;
}

bool check_winner(char player) {
    int player_to_check = (player == 'X' || player == 'x') ? 1 : -1;
    return is_winner(player_to_check, game);
}
