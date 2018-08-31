def decorator(fn):
    def _():
        print('hello')
        return fn
    return _


@decorator
def hello():
    pass


hello()