import sys
import traceback
class Redirect:
    def __init__(self, stdout=sys.stdout, stderr=sys.stderr):
        self.__stdout = sys.stdout
        self.__stderr = sys.stderr
        self.stdout = stdout
        self.stderr = stderr

    def __enter__(self):
        sys.stderr = self.stderr
        sys.stdout = self.stdout
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        traceback.print_exc()
        sys.stderr = self.__stderr
        sys.stdout = self.__stderr
        return self
