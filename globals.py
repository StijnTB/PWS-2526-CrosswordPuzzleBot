from pygame import Color, display
from typing import Literal


class Globals:
    #TILE_SIZE: the base dimension of a tile and button. should be divisible by 2 and 10
    TILE_SIZE: int = 2 * 2 * 10
    # BUTTON_SIZE: the size of a button, width is standard due to the maximum text size
    BUTTON_SIZE: tuple[int, int] = (
        148,
        TILE_SIZE,
    ) 
    # EMPTY_TILE: a set containing the possible values the text of a BoardTile can be if it is not occupied
    EMPTY_TILE: set[None | str] = {None, "DW", "DL", "TW", "TL", "", "MI"}
    # BORDER_BETWEEN_TILES_WIDTH: the amount of pixels between 2 tiles
    BORDER_BETWEEN_TILES_WIDTH: int = 2
    # OFFSET_BETWEEN_SCREEN_CATEGORIES: the amount of pixels between different areas of the screen (the board, the buttons, the tilerow etc.)
    OFFSET_BETWEEN_SCREEN_CATEGORIES: int = 10
    # amount_of_passes: every time the player or the bot passes, increase by 1. after 3, stop game
    amount_of_passes: int = 0
    # RANDOM_SEED: the seed to use for every random generator to improve bugfixing
    RANDOM_SEED: int = 111
    # BINGO_BONUS_SCORE_MULTIPLIER: a multiplier for the bingo bonus score to vary its influence
    BINGO_BONUS_SCORE_MULTIPLIER: float = 0.5
    # BOARDPOSITION_FACTORS: a group of factors used for calculating the boardposition degradation factor
    BOARDPOSITION_FACTORS: dict[str, float] = {  
            "TW": 22.5, # The base multiplication factor used for a TW-tile in the expected multiplication calculation
            "TL": 2, # The base multiplication factor used for a DW-tile in the expected multiplication calculation
            "DW": 15,
            "DL": 1.3333,
            "Vowel": 2,
            "Consonant": 1,
            "Addition_Danger": 0.1,  # The value per available letter in bag - own letters
            "danger_word_played_alongside": 1, # The base danger used for the calculation of a word being played alongside the current word
            "multiplication_danger_base": 0.1,
    }
    # BOARDPOSITION_FACTOR_DISTANCE_REDUCTOR: a factor used to define the reduction of influence a tile has in the degradation score
    BOARDPOSITION_FACTOR_DISTANCE_REDUCTOR: float = 0.87
    # SCREEN_WIDTH: the screen width, dependent mainly on the tile size
    SCREEN_WIDTH: int = (
        TILE_SIZE * 15
        + 14 * BORDER_BETWEEN_TILES_WIDTH
        + OFFSET_BETWEEN_SCREEN_CATEGORIES
        + BUTTON_SIZE[0]
    )
    # SCREEN_HEIGHT: the screen height, dependent mainly on the tile size
    SCREEN_HEIGHT: int = (
        TILE_SIZE * 15
        + 15 * BORDER_BETWEEN_TILES_WIDTH
        + OFFSET_BETWEEN_SCREEN_CATEGORIES
        + BUTTON_SIZE[1]
    )
    # TEXT_SIZE_TILE: the size of text used for the pygame font definition
    TEXT_SIZE_TILE: int = int(TILE_SIZE / 2)
    # TILE_COLOR_DICT: The different colors a tile can take depending on its function and occupation
    TILE_COLOR_DICT: dict[str, Color] = {
        "TW": Color(22, 57, 157), #122, 57, 57
        "TL": Color(172, 91, 45), #72, 91, 145
        "DW": Color(91, 120, 132), #191, 120, 32
        "DL": Color(13, 157, 201), #133, 157, 101
        "MI": Color(197, 72, 254), #97, 72, 99
        "Empty_tile": Color(84, 84, 84),  # grey
        "Played_tilerow_letter": Color(44, 47, 54),  # grey, same as empty_tile
        "Set_board/Base_tilerow": Color(209, 210, 205),  # greyish white
        "Try_board/Selected_tilerow": Color(255, 255, 255),  # white
    }
    # global_should_recompute: a variable which tells the program to do a full visual recomputation. used sparingly, only when a visual element has to fully disappear
    global_should_recompute: bool = True
    # BOARD_LAYOUT_LIST: a list of lists which contains the original layout of the board with special and normal tiles
    BOARD_LAYOUT_LIST: list[list[Literal["TL", "TW", "DL", "DW", "MI", None]]] = [
        ["TL",None,None,None,"TW",None,None,"DL",None,None,"TW",None,None,None,"TL",],
        [None,"DL",None,None,None,"TL",None,None,None,"TL",None,None,None,"DL",None,],
        [None,None,"DW",None,None,None,"DL",None,"DL",None,None,None,"DW",None,None,],
        [None,None,None,"TL",None,None,None,"DW",None,None,None,"TL",None,None,None,],
        ["TW",None,None,None,"DW",None,"DL",None,"DL",None,"DW",None,None,None,"TW",],
        [None,"TL",None,None,None,"TL",None,None,None,"TL",None,None,None,"TL",None,],
        [None,None,"DL",None,"DL",None,None,None,None,None,"DL",None,"DL",None,None,],
        ["DL",None,None,"DW",None,None,None,"MI",None,None,None,"DW",None,None,"DL",],
        [None,None,"DL",None,"DL",None,None,None,None,None,"DL",None,"DL",None,None,],
        [None,"TL",None,None,None,"TL",None,None,None,"TL",None,None,None,"TL",None,],
        ["TW",None,None,None,"DW",None,"DL",None,"DL",None,"DW",None,None,None,"TW",],
        [None,None,None,"TL",None,None,None,"DW",None,None,None,"TL",None,None,None,],
        [None,None,"DW",None,None,None,"DL",None,"DL",None,None,None,"DW",None,None,],
        [None,"DL",None,None,None,"TL",None,None,None,"TL",None,None,None,"DL",None,],
        ["TL",None,None,None,"TW",None,None,"DL",None,None,"TW",None,None,None,"TL",],
    ]
    # TILE_LETTER_DICT: a dictionary with every possible letter in the tilebag with the total amount and the number of points it gives
    TILE_LETTER_DICT: dict[str, dict[str, int]] = {
        "A": {"amount": 7, "value": 1},
        "B": {"amount": 2, "value": 4},
        "C": {"amount": 2, "value": 5},
        "D": {"amount": 5, "value": 2},
        "E": {"amount": 18, "value": 1},
        "F": {"amount": 2, "value": 4},
        "G": {"amount": 3, "value": 3},
        "H": {"amount": 2, "value": 4},
        "I": {"amount": 4, "value": 2},
        "J": {"amount": 2, "value": 4},
        "K": {"amount": 3, "value": 3},
        "L": {"amount": 3, "value": 3},
        "M": {"amount": 3, "value": 3},
        "N": {"amount": 11, "value": 1},
        "O": {"amount": 6, "value": 1},
        "P": {"amount": 2, "value": 4},
        "Q": {"amount": 1, "value": 10},
        "R": {"amount": 5, "value": 2},
        "S": {"amount": 5, "value": 2},
        "T": {"amount": 5, "value": 2},
        "U": {"amount": 3, "value": 2},
        "V": {"amount": 2, "value": 4},
        "W": {"amount": 2, "value": 5},
        "X": {"amount": 1, "value": 8},
        "Y": {"amount": 1, "value": 8},
        "Z": {"amount": 2, "value": 5},
        " ": {"amount": 0, "value": 0},
    }
    # SCREEN_TILES_STARTING_HEIGHT: the offset from the top of the display at which the tiles start
    SCREEN_TILES_STARTING_HEIGHT: int = OFFSET_BETWEEN_SCREEN_CATEGORIES * 0
    # ROW_TILES_SCREEN_HEIGHT: the center y-coordinate on the screen of the players row of tiles
    ROW_TILES_SCREEN_HEIGHT: int = (
        SCREEN_TILES_STARTING_HEIGHT
        + TILE_SIZE * 15
        + 15 * BORDER_BETWEEN_TILES_WIDTH
        + int(TILE_SIZE / 2)
        + OFFSET_BETWEEN_SCREEN_CATEGORIES
    )
    # players_tilerows: contains both players tilerows to use for the Chance bot calculations
    players_tilerows: dict[int, list[str]] = {1: [], 2: []}
    scores: list[int] = [0,0]




screen = display.set_mode((Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT))
display.set_caption("WordFeud")
