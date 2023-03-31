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


# print('Hello stdout')
# stdout_file = open('stdout.txt', 'w')
# stderr_file = open('stderr.txt', 'w')
#
#
# with Redirect(stdout=stdout_file, stderr=stderr_file):
#     print('Hello stdout.txt')
#     raise Exception('Hello stderr.txt')
#
#
# print('Hello stdout again') # почему красным пишется?
# raise Exception('Hello stderr')