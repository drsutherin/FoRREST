class Infer:
    def __init__(self, forrest):
        self.forrest = forrest

    def _get_file(self):
        return self.forrest.get_file()
