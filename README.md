# Command-line parser
[![Build Status](https://travis-ci.org/mjalas/command_line_parser.svg?branch=master)](https://travis-ci.org/mjalas/command_line_parser)
[![Coverage Status](https://coveralls.io/repos/github/mjalas/command_line_parser/badge.svg?branch=master)](https://coveralls.io/github/mjalas/command_line_parser?branch=master)
[![Code Health](https://landscape.io/github/mjalas/command_line_parser/master/landscape.svg?style=flat)](https://landscape.io/github/mjalas/command_line_parser/master)

The command-line parser includes default parsers for file and networking command-line options. 
The parser can be customized for users needs, by creating new option classes and injecting them into
the parser.

## Installation

There are currently two different ways of installing the application.

Through pip:
```
pip install command-line-parser
```

Manually:
```
git clone git@github.com:mjalas/command_line_parser.git
cd command-line-parser
python setup.py install
```