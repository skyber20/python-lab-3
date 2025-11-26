import shlex
from sys import stdin
from src.cli import CLIState, CommandHandler


def main():
    state = CLIState()
    handler = CommandHandler(state)

    while stdin:
        try:
            user_inp = input('> ').lower()

            if not user_inp:
                continue

            user_inp = user_inp.replace("[", "'[").replace("]", "]'")
            command = shlex.split(user_inp)

            res = handler.handle_command(command)
            if not res:
                break
        except (KeyboardInterrupt, EOFError):
            print('Пока')
            break
        except Exception as e:
            print(f'Ошибка: {e}')


if __name__ == '__main__':
    main()
