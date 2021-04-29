#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0
    for y in range(1, len(sys.argv)):
        res += int((sys.argv[y]))
    print(res)
