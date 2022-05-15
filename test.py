from token_type import Token
from node import Node
from lexer import lex
from parser import parse


class Number(Token):
    rule = '\d+'

    def value(self):
        return int(self.text)

class Plus(Token):
    rule = '\+'

class LBrace(Token):
    rule = '{'

class RBrace(Token):
    rule = '}'

class LParen(Token):
    rule = '\('

class RParen(Token):
    rule = '\)'

class Minus(Token):
    rule = '\-'

class Hash(Node):
    @staticmethod
    def rules():
        return [[LBrace, RBrace]]

    def value(self):
        return {}

class FunctionDefinition(Node):
    @staticmethod
    def rules():
        return [[LParen, RParen, LBrace, RBrace]]

    def value(self):
        return lambda:None

class AddExpression(Node):
    @staticmethod
    def rules():
        return [[Number, Plus, Number], [AddExpression, Plus, Number]]

    def value(self):
        return self.tokens[0].value() + self.tokens[2].value()

class Root(Node):
    @staticmethod
    def rules():
        return [[AddExpression], [Hash], [FunctionDefinition]]

    @staticmethod
    def is_root():
        return True

    def value(self):
        return self.tokens[0].value()


text = '(){}'

token_chain = lex(text)
print(token_chain)
ast = parse(token_chain)
print(ast)
print(ast.value())
