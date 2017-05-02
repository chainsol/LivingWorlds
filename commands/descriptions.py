from evennia import Command, CmdSet


class SetLong(Command):
    """
    allows for the player to set the desc of their character to be be what they want
    
    usage: long <text>
    
    """
    key = 'long'
    locks = "cmd:all()"

    def func(self):
        """
        implements the command
        """

        caller = self.caller
        args = self.args.strip().capitalize()
        caller.db.desc = args
        caller.msg('Your long description was set to %s' % args)


class SetHair(Command):
    """
    Allows for the player to set the hairdesc of their character to be what they want other to see
    
    usage: hair <text>
    
    """
    key = 'hair'
    locks = "cmd:all()"

    def func(self):
        """
        Implements the command
        
        """

        caller = self.caller
        args = self.args.strip().capitalize()
        caller.db.hairdesc = args
        caller.msg('Your hair description was set to %s' % args)


class SetEyes(Command):
    """
    Allows for the player to set the eyedesc of their character to be what they want other to see

    usage: eyes <text>

    """
    key = 'eyes'
    locks = "cmd:all()"

    def func(self):
        """
        Implements the command
        """

        caller = self.caller
        args = self.args.strip().capitalize()
        caller.db.eyedesc = args
        caller.msg('Your eyes description was set to %s' % args)


class DescCmdSet(CmdSet):
    """
    This stores the input command
    """
    key = "Chargen"

    def at_cmdset_creation(self):
        """called once at creation"""
        self.add(SetLong())
        self.add(SetHair())
        self.add(SetEyes())
