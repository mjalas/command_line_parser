from optparse import OptionParser


class CommandLineOptionParser(object):
    """
    Command-line parser for usual network options.
    """

    def __init__(self, options, usage, version):
        self.parser = OptionParser(usage=usage,
                                   version=version)
        for option in options:
            self.parser.add_option(option.short, option.long,
                                   dest=option.dest, help=option.help)
        self.input_options = options

    def parseArguments(self, args):
        (options, args) = self.parser.parse_args(args)
        for option in self.input_options:
            attr = getattr(options, option.dest)
            if attr is not None:
                setattr(self, option.dest, attr)

        self.args = args
        self.options = options
