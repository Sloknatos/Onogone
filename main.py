from files.env import start_urls
import sys
from tools.scrapper import scrap
from tools.writer import writer
from tools.reader import reader


def get_comment():
    url = start_urls
    writer(scrap(url))
    return True


def convert_comment(**kwargs):
    from tools.spelling import respelling

    converted_comment = {}

    file_name = kwargs.get('file_name', None)
    dict = reader() if file_name is None else reader(file=file_name)
    for index, comment in dict.items():
        converted_comment[index] = respelling(comment)
    writer(converted_comment, file_name='results.json')


def execute_error():
    print(f'usage : main.py [command]\n'
          '\t write \t to get comments\n'
          '\t read \t to convert comments')


if __name__ == "__main__":
    try:
        command = str(sys.argv[1])
        if command == 'write':
            get_comment()
        elif command == "read":
            convert_comment()
        else:
            execute_error()
    except IndexError:
        execute_error()
