import sys

EXIT = False


def _exit():
    global EXIT
    EXIT = True


def _echo(text):
    sys.stdout.write(f"{text}\n")


def _type(*cmds):
    for cmd in cmds:
        if cmd in COMMANDS:
            sys.stdout.write(f"{cmd} is a shell builtin\n")
        else:
            sys.stderr.write(f"{cmd}: not found\n")


COMMANDS = {"exit":_exit,"echo":_echo,"type":_type}


def main():

    while not EXIT :
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_input = sys.stdin.readline().strip()
        user_inputs = user_input.split(" ",maxsplit=1)
        command = user_inputs[0]


        if command in COMMANDS :
            if command == "echo":
                COMMANDS[command](user_input[5:])
            else:
                COMMANDS[command]()
            if command == "type":
                _type(user_input[5:])


        else:
            sys.stderr.write(f"{user_input}: command not found \n")



if __name__ == "__main__":
    main()

