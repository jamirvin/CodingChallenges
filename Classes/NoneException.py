class NoneError(Exception):
    def __index__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
