class Contextable(object):
    def get_context_key(self):
        raise NotImplementedError

    def get_context_value(self):
        raise NotImplementedError