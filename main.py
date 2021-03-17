import sys

import valheimlog



def main():
    death_count = {}

    # read line from STDIN until EOF
    while line := sys.stdin.readline():
        # parse line
        entry: valheimlog.LogEntry = valheimlog.parse(line)

        if entry:
            if not entry.is_alive:
                try:
                    death_count[entry.char_name] += 1
                except KeyError:
                    death_count[entry.char_name] = 1
            print(f"At {entry.time} {entry.char_name} {'was alive' if entry.is_alive else 'died'}", file=sys.stdout)

    print(death_count)
    return

if __name__ == "__main__":
    main()
