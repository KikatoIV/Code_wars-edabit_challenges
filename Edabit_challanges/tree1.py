class Expr:
    pass

class Times (Expr):
    def __init__(self, l, r):
        self.l = l
        self.r = r

class Plus (Expr):
    def __init__(self, l, r):
        self.l = l
        self.r = r

class Const(Expr):
    def __init__(self, val):
        self.val = val

class Var (Expr):
    def __init__(self,name):
        self.name = name
 n  e1 = Times(Const(3),Plus(Var("y"),Var("x")))

