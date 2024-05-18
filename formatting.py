import os

levels = [d for d in os.listdir() if "Level" in d]

problemnum = 1

for num, level in enumerate(levels):
    problems = [d for d in os.listdir(f"{level}") if "Problem" in d]
    for n, problem in enumerate(problems):
        with open(f"{level}\{problem}", "r") as f:
            title = f.readline().strip()[2:]
        os.rename(f"{level}/{problem}", f"{level}/{problem[:7]} {25 * num + n + 1} - {title}.py")
    if num == len(levels) - 1:
        problemnum = 25 * num + len(problems)
        print(f"Up to problem {problemnum}.")
with open("README.md", "w") as f:
    f.write(f"# James' Project Euler Repository\nHere is my Project Euler files.\nDone up to and including Problem {problemnum}!")