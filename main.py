"""
Chess playing program
Everything starts here


8 ║♜♞♝♛♚♝♞♜
7 ║♟♟♟♟♟♟♟♟
6 ║…………………………………
5 ║…………………………………
4 ║…………………………………
3 ║…………………………………
2 ║♙♙♙♙♙♙♙♙
1 ║♖♘♗♕♔♗♘♖
--╚═══════════════
——-a b c d e f g h

Copyright © 2016 Aubhro Sengupta. All rights reserved.
"""

from setup.board import Board
from setup.algebraic.location import Location


def main():
    """
    Main method
    """
    print("New game creating")

    # Creates new game with human players for both white and black.
    """
    new_game = game.Game(human.Player(color.Color(color.white)), human.Player(color.Color(color.black)))
    new_game.start()
    """
    position = Board.init_default()
    position.print()

    position.move_piece(Location(0, 0), Location(4, 4))
    position.move_piece(Location(7, 7), Location(4, 5))
    position.print()

    # print("This is the ghost symbol: " + position.piece_at_square(Location(3, 0)).symbol)

    for i in range(len(position.piece_at_square(Location(4, 4)).possible_moves(position))):
        position.piece_at_square(Location(4, 4)).possible_moves(position)[i].print()

    print()
    print(position.piece_at_square(Location(4, 4)).location.rank, " file", position.piece_at_square(Location(4, 4)).location.file)

    for j in range(len(position.piece_at_square(Location(4, 5)).possible_moves(position))):
        position.piece_at_square(Location(4, 5)).possible_moves(position)[j].print()

    print(position.piece_at_square(Location(4, 5)).location.rank, " file",
              position.piece_at_square(Location(4, 5)).location.file)

main()
