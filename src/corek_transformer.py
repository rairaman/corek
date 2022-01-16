from lark import Transformer, v_args

@v_args(inline=True)    # Affects the signatures of the methods
class CorekTransformer(Transformer):
    from operator import add, sub, mul, truediv as div, neg, \
        gt, lt, ge, le, eq, ne, or_, and_
    number = float

    def __init__(self, input_values: dict):
        self.input_values = input_values

    def var(self, name):
        try:
            return self.input_values[name]
        except KeyError:
            raise Exception("Variable not found: %s" % name)
            


