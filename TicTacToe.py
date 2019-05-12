
class TicTacToe:
    def __init__(self):
        self.line1 = [" ", " ", " "] 
        self.line2 = [" ", " ", " "] 
        self.line3 = [" ", " ", " "]
        self.conversion = {"top left": 0}
        self.board = [None] * 9

    def game(self):
        while True:
            self.player = "Player 1"
            self.move = self.choose_move(self.player)
            self.move = self.is_it_a_valid_move(self.move)
            self.move = self.check_board(self.move)
            self.update_board(self.player, self.move)
            self.game_over()
            self.cats_game()

            self.player = "Player 2"
            self.move = self.choose_move(self.player)
            self.move = self.is_it_a_valid_move(self.move)
            self.move = self.check_board(self.move)
            self.update_board(self.player, self.move)
            #checks to see if the game is over
            self.game_over()
            #checks to see if their is a cats game
            self.cats_game()



    def update_board(self, player, move):
        #updating player 1's moves
        if player == "Player 1":    
            if move == "top left":
                self.line1[0] = "x"
                self.printboard()
            if move == "top mid":
                self.line1[1] = "x"
                self.printboard()
            if move == "top right":
                self.line1[2] = "x"
                self.printboard()


            #updating the middle line of the board
            if move == "mid left":
                self.line2[0] = "x"
                self.printboard()
            if move == "middle":
                self.line2[1] = "x"
                self.printboard()
            if move == "mid right":
                self.line2[2] = "x"
                self.printboard()
            #updating the bottom line of the board
            if move == "bot left":
                self.line3[0] = "x"
                self.printboard()
            if move == "bot mid":
                self.line3[1] = "x"
                self.printboard()
            if move == "bot right":
                self.line3[2] = "x"
                self.printboard()
          
            
            

           
        
        #updating player 2's moves
        if player == "Player 2":        
        #updating the top line of the board            
            if move == "top left":
                self.line1[0] = "o"
                self.printboard()
            if move == "top mid":
                self.line1[1] = "o"
                self.printboard()
            if move == "top right":
                self.line1[2] = "o"
                self.printboard()

            #updating the middle line of the board
            if move == "mid left":
                self.line2[0] = "o"
                self.printboard()
            if move == "middle":
                self.line2[1] = "o"
                self.printboard()
            if move == "mid right":
                self.line2[2] = "o"
                self.printboard()

            #updating the bottom line of the board
            if move == "bot left":
                self.line3[0] = "o"
                self.printboard()
            if move == "bot mid":
                self.line3[1] = "o"
                self.printboard()
            if move == "bot right":
                self.line3[2] = "o"
                self.printboard()
           

            

    def printboard(self):
        print(self.line1[0] + "|" + self.line1[1] + "|" + self.line1[2])
        print("-----")
        print(self.line2[0] + "|" + self.line2[1] + "|" + self.line2[2])
        print("-----")
        print(self.line3[0] + "|" + self.line3[1] + "|" + self.line3[2])

    def game_over(self):
        #player 1 win conditions
        if self.line1[0] == "x" and self.line1[1] == "x" and self.line1[2] == "x":
            print("Player 1 wins!")
            exit()
        if self.line2[0] == "x" and self.line2[1] == "x" and self.line2[2] == "x":
            print("Player 1 wins!")
            exit()
        if self.line3[0] == "x" and self.line3[1] == "x" and self.line3[2] == "x":
            print("Player 1 wins!")
            exit()
        if self.line1[0] == "x" and self.line2[0] == "x" and self.line3[0] == "x":
            print("Player 1 wins!")
            exit()
        if self.line1[1] == "x" and self.line2[1] == "x" and self.line3[1] == "x":
            print("Player 1 wins!")
            exit()  
        if self.line1[2] == "x" and self.line2[2] == "x" and self.line3[2] == "x":
            print("Player 1 wins!")
            exit() 
        if self.line1[0] == "x" and self.line2[1] == "x" and self.line3[2] == "x":
            print("Player 1 wins!")
            exit()
        if self.line1[2] == "x" and self.line2[1] == "x" and self.line3[0] == "x":
            print("Player 1 wins!")
            exit()
            #player 2 win conditions
        if self.line1[0] == "o" and self.line1[1] == "o" and self.line1[2] == "o":
            print("Player 2 wins!")
            exit()
        if self.line2[0] == "o" and self.line2[1] == "o" and self.line2[2] == "o":
            print("Player 2 wins!")
            exit()
        if self.line3[0] == "o" and self.line3[1] == "o" and self.line3[2] == "o":
            print("Player 2 wins!")
            exit()
        if self.line1[0] == "o" and self.line2[0] == "o" and self.line3[0] == "o":
            print("Player 2 wins!")
            exit()
        if self.line1[1] == "o" and self.line2[1] == "o" and self.line3[1] == "o":
            print("Player 2 wins!")
            exit()  
        if self.line1[2] == "o" and self.line2[2] == "o" and self.line3[2] == "o":
            print("Player 2 wins!")
            exit() 
        if self.line1[0] == "o" and self.line2[1] == "o" and self.line3[2] == "o":
            print("Player 2 wins!")
            exit()
        if self.line1[2] == "o" and self.line2[1] == "o" and self.line3[0] == "o":
            print("Player 2 wins!")
            exit()

    def cats_game(self):
        if self.line1[0] != " " and self.line1[1] != " " and self.line1[2] != " " and self.line2[0] != " " and self.line2[1] != " " and self.line2[2] != " " and self.line3[0] != " " and self.line3[1] != " " and self.line3[2] != " ":
            print("Cats game...")
            exit()

    def choose_move(self, player):
        move = input(str(player) + " " + "move? ")
        #return self.conversion[move]
        return move
    def is_it_a_valid_move(self, move):
        #if self.board[move] is not None:
        #    self.chooseNewMove()
        while True:
            if move == "top left":
                return move
            if move == "top mid":
                return move
            if move == "top right":
                return move
            if move == "mid left":
                return move
            if move == "middle":
                return move
            if move == "mid right":
                return move
            if move == "bot left":
                return move
            if move == "bot mid":
                return move
            if move == "bot right":
                return move
            else:
                move = input("Select new move: ")
    def check_board(self, move):
        #checking top row for repeat move
        if move == "top left" and self.line1[0] != " ":
            while move == "top left":
                move = input("Choose new move: ")

        if move == "top mid" and self.line1[1] != " ":
            while move == "top mid":
                move = input("Choose new move: ")

        if move == "top right" and self.line1[2] != " ":
            while move == "top right":
                move = input("Choose new move: ")
                         
         #checking middle row for repeat move
        if move == "mid left" and self.line2[0] != " ":
            while move == "mid left":
                move = input("Choose new move: ")
        
        if move == "middle" and self.line2[1] != " ":
            while move == "middle":
                move = input("Choose new move: ")
           
        if move == "mid right" and self.line2[2] != " ":
            while move == "mid right":
                move = input("Choose new move: ")
            
        #checking bottom row for repeat move
        if move == "bot left" and self.line3[0] != " ":
            while move == "bot left":
                move = input("Choose new move: ")
            
        if move == "bot mid" and self.line3[1] != " ":
            while move == "bot mid":
                move = input("Choose new move: ")
            
        if move == "bot right" and self.line3[2] != " ":
            while move == "bot right":
                move = input("Choose new move: ")
        return move
            
        
    



        
if __name__ == '__main__':
    board = TicTacToe()
    board.game()
 


