
class Option(object):
    """Generic user created option."""

    def __init__(self, shortname, longname, dest, help_text):
        self.short = shortname
        self.long = longname
        self.dest = dest
        self.help = help_text


class NetworkAddressOption(object):
    """Default network address option."""

    def __init__(self):
        self.short = "-a"
        self.long = "--address"
        self.dest = "address"
        self.help = "Address of remote host."


class PortNumberOption(object):
    """Default port number option."""

    def __init__(self):
        self.short = "-p"
        self.long = "--port"
        self.dest = "port"
        self.help = "Port of the remote application."


class FileOption(object):
    """Default file option."""

    def __init__(self):
        self.short = "-f"
        self.long = "--file"
        self.dest = "file"
        self.help = "Path to file."

class OutputOption(object):
    """Default output option."""

    def __init__(self):
        self.short = "-o"
        self.long = "--output"
        self.dest = "output"
        self.help = "Output path."
