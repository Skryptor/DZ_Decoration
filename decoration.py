import os
from datetime import datetime

def logger(old_function):
    def new_function(*args, **kwargs):
        start = datetime.now()

        result = old_function(*args, **kwargs)

        end = datetime.now()

        print(f'function {old_function.__name__} works {end - start}')
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        with open('main.log', 'a', encoding='utf-8') as file:
            file.write(f'{now} \n')
            file.write(f'Name function{old_function.__name__}\n')
            if args or kwargs:
                file.write(f'Initial arguments: args={args}, kwargs={kwargs}\n')
            file.write(f'return arguments function {result}\n')
            file.write('-' * 40 + '\n')

        return result

    return new_function


def loggers(path):
    def logger_(old_function):
        def new_function(*args, **kwargs):
            start = datetime.now()

            result = old_function(*args, **kwargs)

            end = datetime.now()

            print(f'function {old_function.__name__} works {end - start}')
            now = datetime.now().strftime("%Y-%m-%d %H:%M")
            writers = (
                    f'{now} \n'
                    f'Name function{old_function.__name__}\n'
                    f'Initial arguments: args={args}, kwargs={kwargs}\n'
                    f'return arguments function {result}\n'
                    '-' * 40 + '\n'
            )
            with open(path, 'a', encoding='utf-8') as file:
                file.write(writers)

            return result

        return new_function

    return logger_