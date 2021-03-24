# 0
import os, subprocess, sys
number = __file__.split("_", 1)[1]
number = int(number[:len(number)-3])
messages = {
    0: "Loading",
    1: ".",
    2: ".",
    4: ".\n\n",
    7: "Welcome!\n",
    9: "Dont worry, ",
    10: "absolutely nothing bad is happening right now.\n",
    13: ".",
    14: ".",
    15: ".",
    16: ".",
    17: ".\n\n",
    19: "So, ",
    20: "how's your day been?\n",
    24: "Oh, ",
    25: "you can't answer.\n",
    28: "Well, ",
    29: "I guess maybe I should introduce myself.\n",
    31: "Hello! My name is 'mostly-harmless'.\n",
    34: "Why is my name 'mostly-harmless'?\n",
    36: "Well, ",
    37: "uhhh... ",
    38: "thats a good question.\n",
    40: "Honestly I'm not sure myself.\n",
    42: "Wait! ",
    43: "Don't close the window!\n",
    45: "Maybe I can tell you a story.\n",
    47: "Do you like stories?\n",
    49: "Anyway, ",
    50: "the story goes something like this:\n"
}
message = messages.get(number)
#if message != None:
#    print(message, end="")
number += 1
filePath = str(os.getcwd() + "\\mostly-harmless_%s.py" % number)
with open(filePath, "w") as file:
    lines = open(__file__).readlines()[1:]
    file.write("# %s\n" % number)
    for line in lines:
        file.write(line)
subprocess.Popen(["start", sys.executable, filePath], shell=True)