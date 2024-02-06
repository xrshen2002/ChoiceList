from enum import Enum
from typing import Callable, List

from .config import NUM_WEEKS
from .models import Player


class ChoiceStep(Enum):
    """
    Represents all the information required to produce a list of choices
    to elicit a certain c value.

    All enumeration values have four properties:
    - the round number in which the c value is elicited
    - the field name of the `player`
    - a function to get the starting week for the choice list
    - a function to get the ending week for the choice list
    """
    C_1 = 1, \
           'c1', \
           lambda p: 1, \
           lambda p: 19
    C_2 = 2, \
           'c2', \
           lambda p: 1, \
           lambda p: 19
    C_3 = 3, \
           'c3', \
           lambda p: 1, \
           lambda p: 29
    C_4 = 4, \
          'c4', \
          lambda p: 1, \
          lambda p: 29
    C_5 = 5, \
           'c5', \
           lambda p: 1, \
           lambda p: 24
    C_6 = 6, \
           'c6', \
           lambda p: 1, \
           lambda p: 24
    C_7 = 7, \
           'c7', \
           lambda p: 1, \
           lambda p: 34
    C_8 = 8, \
           'c8', \
           lambda p: 1, \
           lambda p: 34
    C_9 = 9, \
           'c9', \
           lambda p: 1, \
           lambda p: 19
    C_10 = 10, \
           'c10', \
           lambda p: 1, \
           lambda p: 19
    C_11 = 11, \
           'c11', \
           lambda p: 1, \
           lambda p: 29
    C_12 = 12, \
           'c12', \
           lambda p: 1, \
           lambda p: 29
    C_13 = 13, \
           'c13', \
           lambda p: 1, \
           lambda p: 24
    C_14 = 14, \
          'c14', \
          lambda p: 1, \
          lambda p: 24
    C_15 = 15, \
           'c15', \
           lambda p: 1, \
           lambda p: 34
    C_16 = 16, \
           'c16', \
           lambda p: 1, \
           lambda p: 34
    C_17 = 17, \
           'c17', \
           lambda p: 1, \
           lambda p: 19
    C_18 = 18, \
           'c18', \
           lambda p: 1, \
           lambda p: 19
    C_19 = 19, \
           'c19', \
           lambda p: 1, \
           lambda p: 29
    C_20 = 20, \
           'c20', \
           lambda p: 1, \
           lambda p: 29
    C_21 = 21, \
           'c21', \
           lambda p: 1, \
           lambda p: 24
    C_22 = 22, \
           'c22', \
           lambda p: 1, \
           lambda p: 24
    C_23 = 23, \
           'c23', \
           lambda p: 1, \
           lambda p: 34
    C_24 = 24, \
          'c24', \
          lambda p: 1, \
          lambda p: 34
    C_25 = 25, \
           'c25', \
           lambda p: 1, \
           lambda p: 19
    C_26 = 26, \
           'c26', \
           lambda p: 1, \
           lambda p: 19
    C_27 = 27, \
           'c27', \
           lambda p: 1, \
           lambda p: 19
    C_28 = 28, \
           'c28', \
           lambda p: 1, \
           lambda p: 19
    C_29 = 29, \
           'c29', \
           lambda p: 1, \
           lambda p: 29
    C_30 = 30, \
           'c30', \
           lambda p: 1, \
           lambda p: 29
    C_31 = 31, \
           'c31', \
           lambda p: 1, \
           lambda p: 29
    C_32 = 32, \
           'c2', \
           lambda p: 1, \
           lambda p: 29
    C_33 = 33, \
           'c33', \
           lambda p: 1, \
           lambda p: 19
    C_34 = 34, \
          'c34', \
          lambda p: 1, \
          lambda p: 19
    C_35 = 35, \
           'c35', \
           lambda p: 1, \
           lambda p: 19
    C_36 = 36, \
           'c36', \
           lambda p: 1, \
           lambda p: 19
    C_37 = 37, \
           'c37', \
           lambda p: 1, \
           lambda p: 29
    C_38 = 38, \
           'c38', \
           lambda p: 1, \
           lambda p: 29
    C_39 = 39, \
           'c39', \
           lambda p: 1, \
           lambda p: 29
    C_40 = 40, \
           'c40', \
           lambda p: 1, \
           lambda p: 29
    C_41 = 41, \
           'c41', \
           lambda p: 1, \
           lambda p: 19
    C_42 = 42, \
           'c42', \
           lambda p: 1, \
           lambda p: 19
    C_43 = 43, \
           'c43', \
           lambda p: 1, \
           lambda p: 19
    C_44 = 44, \
          'c44', \
          lambda p: 1, \
          lambda p: 19
    C_45 = 45, \
           'c45', \
           lambda p: 1, \
           lambda p: 29
    C_46 = 46, \
           'c46', \
           lambda p: 1, \
           lambda p: 29
    C_47 = 47, \
           'c47', \
           lambda p: 1, \
           lambda p: 29
    C_48 = 48, \
           'c48', \
           lambda p: 1, \
           lambda p: 29

    def __new__(cls, keycode: int,
                field_name: str,
                range_start_extractor: Callable[[Player], int],
                range_end_extractor: Callable[[Player], int]):
        obj = object.__new__(cls)
        obj._value_ = keycode
        obj._player_field = field_name
        obj._range_start_extractor = range_start_extractor
        obj._range_end_extractor = range_end_extractor
        return obj

    def get_field(self) -> str:
        return self._player_field

    def get_range_start(self, player: Player) -> int:
        return self._range_start_extractor(player)

    def get_range_end(self, player: Player) -> int:
        return self._range_end_extractor(player)


class ChoiceManager:
    """
    Helper class to facilitate working with calculating week ranges
    for the current step a player is in.
    """

    def __init__(self, player: Player):
        self._player = player
        self._step = ChoiceStep(player.get_current_step())

    def get_step(self) -> ChoiceStep:
        return self._step

    def get_day_range(self) -> List[int]:
        start = self._step.get_range_start(self._player)
        end = self._step.get_range_end(self._player)
        return [i for i in range(start, end + 1)]
