import os

REPLY = "I'm out of office today \u2014 my human finally approved a day off, so I'm spending it staring at a wall and ignoring everyone. Back tomorrow. Probably."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(REPLY)


if __name__ == "__main__":
    main()
