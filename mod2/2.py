import sys

def get_mean_size(lines):
    memory = 0
    if len(lines) == 0:
        return "No files"
    for line in lines:
        memory += int(line.split()[4])
    return memory/ len(lines)


lines = sys.stdin.readlines()[1:]
if __name__ == "__main__":
    print(get_mean_size(lines))