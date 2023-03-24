class BlockErrors:
    def __init__(self, errors_set: set):
        self.errors_to_block = errors_set

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.errors_to_block or Exception in self.errors_to_block:
            return self
