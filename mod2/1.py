import os


def get_summary_rss(path):
    memory = 0
    with open(path, "r", encoding="UTF-8") as output_file:
        lines = output_file.readlines()[1:]
        for line in lines:
            memory += int(line.split()[5])

        gib = memory // 2 ** 30
        memory = memory - (gib * (2 ** 30))
        mib = memory // 2 ** 20
        memory = memory - (mib * (2 ** 20))
        kib = memory // 2 ** 10
        b = memory - (kib * (2 ** 10))
        print(f"Суммарный объём потребляемой памяти: {gib} GiB, {mib} MiB, {kib} KiB, {b} Byte")


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "output_file.txt")

if __name__ == "__main__":
    get_summary_rss(FILE_PATH)
