"""
# ----------------------------------------------------------------------
# ctokens.py
#
# Token specifications for symbols in ANSI C and C++.  This file is
# meant to be used as a library in other tokenizers.
# ----------------------------------------------------------------------
"""

if False:
    from typing import Dict, List, Tuple, Union, Optional


def t_CPPCOMMENT(t):
    """
    //.*\n
    """
    pass


def t_COMMENT(t):
    """
    /\*(.|\n)*?\*/
    """
    pass


t_TIMESEQUAL = r'\*='

t_RSHIFTEQUAL = '>>='

t_INCREMENT = r'\+\+'

t_LOR = r'\|\|'

t_LE = '<='

t_RPAREN = r'\)'

t_SEMI = ';'

t_AND = '&'

t_MINUS = '-'

t_TIMES = r'\*'

t_MINUSEQUAL = '-='

t_LBRACKET = r'\['

t_DIVIDE = '/'

t_OR = r'\|'

t_OREQUAL = r'\|='

t_NOT = '~'

t_ARROW = '->'

t_RBRACKET = r'\]'

t_NE = '!='

t_CHARACTER = r"(L)?\'([^\\\n]|(\\.))*?\'"

t_PERIOD = r'\.'

tokens = []

t_LAND = '&&'

t_ID = '[A-Za-z_][A-Za-z0-9_]*'

t_RBRACE = r'\}'

t_LNOT = '!'

t_MODEQUAL = '%='

t_RSHIFT = '>>'

t_TERNARY = r'\?'

t_COMMA = ','

t_EQUALS = '='

t_LSHIFT = '<<'

t_INTEGER = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

t_FLOAT = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

t_LT = '<'

t_DIVEQUAL = '/='

t_ANDEQUAL = '&='

t_ELLIPSIS = r'\.\.\.'

t_XOREQUAL = '^='

t_LBRACE = r'\{'

t_XOR = r'\^'

t_STRING = r'\"([^\\\n]|(\\.))*?\"'

t_PLUS = r'\+'

t_GE = '>='

t_EQ = '=='

t_GT = '>'

t_PLUSEQUAL = r'\+='

t_MODULO = '%'

t_LPAREN = r'\('

t_COLON = ':'

t_DECREMENT = '--'

t_LSHIFTEQUAL = '<<='
