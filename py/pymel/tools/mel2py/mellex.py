"""
# ----------------------------------------------------------------------
# clex.py
#
# A lexer for ANSI C.
# ----------------------------------------------------------------------
"""

if False:
    from typing import Dict, List, Tuple, Union, Optional


def t_LPAREN(t):
    """
    \(
    """
    pass


def t_RBRACKET(t):
    """
    \]
    """
    pass


def t_ELLIPSIS(t):
    """
    \.\.
    """
    pass


def t_COMMENT(t):
    """
    //.*
    """
    pass


def t_RPAREN(t):
    """
    \)
    """
    pass


def t_COMMENT_BLOCK(t):
    """
    /\*(.|\n)*?\*/|/\*(.|\n)*?$
    """
    pass


def t_ID(t):
    """
    ([|]?([:]?([.]?[A-Za-z_][\w]*)+)+)+?
    """
    pass


def t_SEMI(t):
    """
    ;
    """
    pass


def t_CAPTURE(t):
    """
    `
    """
    pass


def t_VAR(t):
    """
    \$[A-Za-z_][\w_]*
    """
    pass


def t_COMPONENT(t):
    """
    \.[xyz]
    """
    pass


def t_NEWLINE(t):
    """
    \n+|\r+
    """
    pass


def t_LBRACKET(t):
    """
    \[
    """
    pass


t_LE = '<='

t_MINUSMINUS = '--'

t_GT = '>'

t_MINUSEQUAL = '-='

t_ICONST = r'(0x[a-fA-F0-9]*)|\d+'

t_LAND = '&&'

t_CROSSEQUAL = '^='

t_LVEC = '<<'

t_EQ = '=='

t_MINUS = '-'

reserved_map = {}

t_DIVEQUAL = '/='

t_MODEQUAL = '%='

t_FCONST = r'(((\d+\.)(\d+)?|(\d+)?(\.\d+))(e(\+|-)?(\d+))?|(\d+)e(\+|-)?(\d+))([lL]|[fF])?'

t_LBRACE = r'\{'

t_TIMES = r'\*'

t_NOT = '!'

t_CROSS = r'\^'

t_ignore = ' \t\x0c'

t_RBRACE = r'\}'

id_state = None

t_GE = '>='

t_RVEC = '>>'

t_NE = '!='

t_TIMESEQUAL = r'\*='

r = 'YES'

t_LOR = r'\|\|'

t_COMMA = ','

t_EQUALS = '='

t_PLUS = r'\+'

t_PLUSEQUAL = r'\+='

suspend_depth = 0

tokens = ()

t_LT = '<'

reserved = ()

t_SCONST = r'"([^\\\n]|(\\.)|\\\n)*?"'

t_PLUSPLUS = r'\+\+'

t_COLON = ':'

t_CONDOP = r'\?'

t_MOD = '%'

t_DIVIDE = '/'
