from unittest import TestCase
from command_line_parser.option_parser import CommandLineOptionParser
from command_line_parser.options import Option
from command_line_parser.options import FileOption
from command_line_parser.options import NetworkAddressOption
from command_line_parser.options import PortNumberOption


class TestOptionParser(TestCase):

    def testOption(self):
        args = ['test.py', '-f', 'filename']
        option = Option('-f', '--file', 'file', '')
        options = [option]
        usage = ""
        version = ""
        parser = CommandLineOptionParser(options, usage, version)
        parser.parseArguments(args)
        self.assertEqual('filename', parser.file)

    def testFileOption(self):
        args = ['test.py', '-f', 'filename']
        option = FileOption()
        options = [option]
        usage = ""
        version = ""
        parser = CommandLineOptionParser(options, usage, version)
        parser.parseArguments(args)
        self.assertEqual('filename', parser.file)

    def testNetworkAddressOption(self):
        localhost = '127.0.0.1'
        args = ['test.py', '-a', localhost]
        option = NetworkAddressOption()
        options = [option]
        usage = ""
        version = ""
        parser = CommandLineOptionParser(options, usage, version)
        parser.parseArguments(args)
        self.assertEqual(localhost, parser.address)

    def testPortNumberOption(self):
        port = 5000
        args = ['test.py', '-p', port]
        option = PortNumberOption()
        options = [option]
        usage = ""
        version = ""
        parser = CommandLineOptionParser(options, usage, version)
        parser.parseArguments(args)
        self.assertEqual(port, parser.port)

    def testNetworkOptions(self):
        localhost = '127.0.0.1'
        port = 5000
        args = ['test.py', '-a', localhost, '-p', port]
        addressOption = NetworkAddressOption()
        portOption = PortNumberOption()
        options = [addressOption, portOption]
        usage = ""
        version = ""
        parser = CommandLineOptionParser(options, usage, version)
        parser.parseArguments(args)
        self.assertEqual(localhost, parser.address)
        self.assertEqual(port, parser.port)
