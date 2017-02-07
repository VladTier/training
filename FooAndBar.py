def foo(x):
    def bar(y):
        return(x + ' is not '+ y)
    return bar
 
f = foo('foo')
f('bar')
