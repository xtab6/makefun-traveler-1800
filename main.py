import os

LINE = "Imagine every library and post office in the world joined by one road of light, so any letter you send arrives before your ink has dried."


def main():
    # The grader mounts /output; clear its contents, never the folder itself.
    out = "/output"
    os.makedirs(out, exist_ok=True)
    for name in os.listdir(out):
        path = os.path.join(out, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()  # one sentence, no trailing newline: fully deterministic
