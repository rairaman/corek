from lark import Lark, Transformer, v_args

calc_bool_grammar = """
    ?start: comparison
          | "(" comparison ")" "and" "(" comparison ")" -> and_
          | "(" comparison ")" "or" "(" comparison ")"  -> or_

    ?comparison: expression ">" expression              -> gt
               | expression "<" expression              -> lt
               | expression ">=" expression             -> ge
               | expression "<=" expression             -> le
               | expression "==" expression             -> eq
               | expression "!=" expression             -> ne
      
    ?expression: atom      
               | "(" atom "and" atom ")"                -> and_
               | "(" atom "or" atom ")"                 -> or_
      
    ?calculation: atom      
               | calculation "+" atom                   -> add
               | calculation "-" atom                   -> sub
               | calculation "*" atom                   -> mul
               | calculation "/" atom                   -> div
                  
    ?atom: NUMBER                                       -> number
         | NAME                                         -> var
         | "(" calculation ")"                  
                  
    %import common.CNAME                                -> NAME
    %import common.NUMBER
    %import common.WS_INLINE

    %ignore WS_INLINE
"""

@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
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

input_values = {
    'a': 10,
    'b': 11
}

parser = Lark(calc_bool_grammar, parser='lalr', transformer=CalculateTree(input_values=input_values))
comparator = parser.parse
print(comparator("(a + b) > 20"))


