import sys
import shutil


EXIT = False

def find(cmd):
    return shutil.which(cmd)

def _exit(*args):
    global EXIT
    EXIT = True


def _echo(text):
    sys.stdout.write(f"{text}\n")


def _type(*cmds):
    for cmd in cmds:
        if cmd in COMMANDS:
            sys.stdout.write(f"{cmd} is a shell builtin\n")
        elif path:=find(cmd):
            sys.stdout.write(f"{path}\n")
        else:
            sys.stderr.write(f"{cmd}: not found\n")

def parser(user_input):
    parts = user_input.split(" ")
    command = parts[0]
    args = parts[1:]

    return command, args

COMMANDS = {
    "exit": _exit,
    "echo": _echo,
    "type": _type
}




def main():
    while not EXIT:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        user_input = sys.stdin.readline()
        if not user_input:
            break

        user_input = user_input.strip()
        if not user_input:
            continue

        command, args = parser(user_input)

        if command in COMMANDS:
            COMMANDS[command](*args)

        else:
            sys.stderr.write(f"{user_input}: command not found\n")


if __name__ == "__main__":
    main()





