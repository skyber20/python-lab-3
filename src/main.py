import shlex
from sys import stdin
from typing import Optional

from constants import ALGORITHMS, STRUCTURS, MATH_FUNCS
from benchmarks.benchmark import timeit_once
from generators.genetators import rand_int_array
from structurs.stack import Stack
from structurs.queue import Queue
from src.exceptions import EmptyStack, EmptyQueue


class CLIState:
    def __init__(self):
        self.stack: Optional[Stack] = None
        self.queue: Optional[Queue] = None


def help_cmd():
    print('Список поддерживаемых команд:')
    print('gen', *MATH_FUNCS.keys(), *ALGORITHMS.keys(), *STRUCTURS.keys(), sep='\n')


def parse_arr(arr: str) -> list[int]:
    cleaned = arr.strip('[] ')
    if not cleaned:
        return []
    return [int(i.strip()) for i in cleaned.split(',')]


def generate_array(inp: list[str]) -> list[int] | None:
    if len(inp) != 4:
        print('Для генерации данных введите размер массива, нижнюю и верхнюю границы')
        return
    try:
        n = int(inp[1])
        low = int(inp[2])
        high = int(inp[3])
    except ValueError:
        raise ValueError('Вводимые данные должны быть числами')

    arr = rand_int_array(n, low, high)

    print(arr)
    return arr


def fib_fact(inp: list[str]) -> None:
    if len(inp) < 2:
        print('Чтобы вывести число Фибоначчи, введите порядковый номер члена последовательности')
        return
    try:
        n = int(inp[1])
    except ValueError:
        raise ValueError('Размер массива - число')

    if '-t' in inp:
        res, time = timeit_once(MATH_FUNCS[inp[0]], n)
        print(res)
        print(f'Время выполнения: {time}')
    else:
        res = MATH_FUNCS[inp[0]](n)
        print(res)


def sorts(inp: list[str]) -> None:
    if len(inp) < 2:
        print('Для сортировки нужен массив')
        return
    try:
        data = parse_arr(inp[1])
    except ValueError:
        raise ValueError('Формат массива должен быть [1, 2, 3]')

    if '-t' in inp:
        res, time = timeit_once(ALGORITHMS[inp[0]], data)
        print(res)
        print(f'Время выполнения: {time}')
    else:
        res = ALGORITHMS[inp[0]](data)
        print(res)


def stack_cmd(inp: list[str], state: CLIState) -> None:
    if len(inp) == 1:
        state.stack = Stack()
        print('Стек создан')
        return

    if inp[1].startswith('['):
        data = parse_arr(inp[1])
        state.stack = Stack(data)
        print('Стек создан')
        return

    if state.stack is None:
        print('Сначала создайте Стек')
        return

    if inp[1] == 'push':
        if len(inp) == 3:
            try:
                n = int(inp[2])
                state.stack.push(n)
            except ValueError:
                print('Введите число, чтобы добавить его в стек')
        else:
            print('Введите число, чтобы добавить его в стек')

    elif inp[1] == 'pop':
        try:
            value = state.stack.pop()
            print(value)
        except EmptyStack:
            print('Стек пуст')

    elif inp[1] == 'peek':
        try:
            value = state.stack.peek()
            print(value)
        except EmptyStack as e:
            print(str(e))

    elif inp[1] == 'is_empty':
        print(state.stack.is_empty())

    elif inp[1] == 'len':
        print(len(state.stack))

    elif inp[1] == 'min':
        try:
            value = state.stack.min()
            print(value)
        except EmptyStack:
            print('Стек пуст')

    else:
        print('Неизвестная команда стека')


def queue_cmd(inp: list[str], state: CLIState):
    if len(inp) == 1:
        state.queue = Queue()
        print('Очередь создана')
        return

    if inp[1].startswith('['):
        data = parse_arr(inp[1])
        state.queue = Queue(data)
        print('Очередь создана')
        return

    if state.queue is None:
        print('Сначала создайте Очередь')
        return

    if inp[1] == 'enqueue':
        if len(inp) == 3:
            try:
                n = int(inp[2])
                state.queue.enqueue(n)
            except ValueError:
                print('Введите число, чтобы добавить его в очередь')
        else:
            print('Введите число, чтобы добавить его в очередь')

    elif inp[1] == 'dequeue':
        try:
            value = state.queue.dequeue()
            print(value)
        except EmptyQueue:
            print('Очередь пуста')

    elif inp[1] == 'front':
        try:
            value = state.queue.front()
            print(value)
        except EmptyQueue:
            print('Очередь пуста')

    elif inp[1] == 'is_empty':
        print(state.queue.is_empty())

    elif inp[1] == 'len':
        print(len(state.queue))

    else:
        print('Неизвестная команда очереди')


def main():
    state = CLIState()

    while stdin:
        user_inp = input('> ').lower()
        user_inp = user_inp.replace("[", "'[").replace("]", "]'")
        command = shlex.split(user_inp)

        if not command:
            continue

        if command[0] in 'help':
            help_cmd()
        elif command[0] in 'exit':
            print('Пока')
            break
        elif command[0] in 'gen':
            generate_array(command)
        elif command[0] in 'stack':
            stack_cmd(command, state)
        elif command[0] in 'queue':
            queue_cmd(command, state)
        elif command[0] in MATH_FUNCS.keys():
            fib_fact(command)
        elif command[0] in ALGORITHMS.keys():
            sorts(command)
        else:
            print(f'Неизвестная команда {command[0]}')


if __name__ == '__main__':
    main()
