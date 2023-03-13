import sys


def decrypt(line):
    line_split = list(line)
    while line.find("..") >= 0:
        index = line.find("..")
        line_split[index - 1:index + 2] = ''
        line = ''.join(line_split)
        if line.count(".") == len(line):
            line = ""
    line = line.replace('.', '')
    return line

# line = sys.stdin.readline()
# if __name__ == '__main__':
#     print(decrypt(line))
