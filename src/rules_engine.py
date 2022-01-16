from lark import Lark
from corek_transformer import CorekTransformer

class RulesEngine():

    def __init__(self):
        with open('corek_grammar.lark','r') as cgfd:
            self.corek_grammar = cgfd.read()

    def test(self, input_values):
        parser = Lark(self.corek_grammar, parser='lalr', transformer=CorekTransformer(input_values=input_values))
        comparator = parser.parse
        print(comparator("(a + b) > 20"))


