"""
backgrounds module.
This module contains data and functions relating to backgrounds. Its
public module functions are to be used primarily during the character
creation process.

Classes:

    `Background`: base class for all backgrounds
    `Farmer`: farmer background
    `Gypsy`: gypsy background
    `Noble`: noble background
    `Nomad`: nomad background
    `Tradesman`: tradesman background
    `Urchin`: urchin background
    

Module Functions

    - `load_background(str)`:
       loads an instance of the named Background class

    - `apply_background(character, background)`:
        have a character "become" a member of the specified background with
        the specified background ability
    """

from evennia import Command


class CmdBackground(Command):
    """This is the command string that will assign a background onto a character,
     and the cooresponding command set."""

    key = "choose"
    locks = "cmd:all()"

    def func(self):
        caller = self.caller
        args = self.args.strip().lower

        apply_background(caller, args)


class BackgroundException(Exception):
    """Base exception class for races module."""

    def __init__(self, msg):
        self.msg = msg


ALL_BACKGROUNDS = ("Farmer", "Gypsy", "Noble", "Nomad", "Tradesman", "Urchin")


def load_background(background):
    """Returns an instance of the named race class.
    Args:
        background (str): case-insensitive name of background to load
    Returns:
        (Background): instance of the appropriate subclass of `Background`
    """

    background = background.strip().capitalize()

    if background in ALL_BACKGROUNDS:
        return globals()[background]()
    else:
        raise BackgroundException("Invalid background specified.")


def apply_background(character, background):
    """Causes a Character to "have" a named background.
    Args: 
        character: the character object having a background
        background (str, Background): the name of the background to apply
    """
    if isinstance(background, Background):
        background = background.name

    background = load_background(background)

    character.db.background = background.name
    character.message('Your background has been set to {}.' .format(background.name))


class Background(object):
    def __init__(self):
        self.name = ""


class Urchin(Background):
    def __init__(self):
        super(Urchin, self).__init__()
        self.name = "Urchin"
        # self.cmdset.add(CmdSetUrchin, permanent=True)


class Noble(Background):
    def __init__(self):
        super(Noble, self).__init__()
        self.name = 'Noble'
        # self.cmdset.add(CmdSetNoble, permanent=True)


class Nomad(Background):
    def __init__(self):
        super(Nomad, self).__init__()
        self.name = "Nomad"
        # self.cmdset.add(CmdSetNoble, permanent=True)


class Gypsy(Background):
    def __init__(self):
        super(Gypsy, self). __init__()
        self.name = 'Gypsy'
        # self.cmdset.add(CmdSetGpysy, permanent=True)


class Farmer(Background):
    def __init__(self):
        super(Farmer, self). __init__()
        self.name = 'Farmer'
        # self.cmdset.add(CmdSetFarmer, permanent=True)


class Tradesman(Background):
    def __init__(self):
        super(Tradesman, self). __init__()
        self.name = 'Tradesman'
        # self.cmdset.add(CmdSetTradesman, permanent=True)
