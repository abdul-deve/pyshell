import sys
import shutil
import subprocess

EXIT = False

def find(cmd):
    return shutil.which(cmd)

def _exit(*args):
    global EXIT
    EXIT = True


def _echo(*agrs):
    output = " ".join(agrs)
    sys.stdout.write(f"{output}\n")



def _type(*cmds):
    for cmd in cmds:
        if cmd in COMMANDS:
            sys.stdout.write(f"{cmd} is a shell builtin\n")
        elif path:=find(cmd):
            sys.stdout.write(f"{cmd} is {path}\n")
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

def subprocess_call(cmd, path, *args):
    result = subprocess.run([cmd, *args], executable=path, capture_output=True,text=True)
    if result.returncode == 0:
         sys.stdout.write(result.stdout)
    else:
        sys.stderr.write(f"{cmd}: command not found\n")


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
        elif cmd_full_path:=find(command):
            subprocess_call(command,cmd_full_path, *args)
        else:
            sys.stderr.write(f"{user_input}: command not found\n")


if __name__ == "__main__":
    main()
