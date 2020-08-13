import json
import sys


def reader(file='./files/original_comment.json'):
    try:
        data = None
        with open(file) as f:
            data = json.load(f)
            f.close()
        return data if not None else False
    except OSError as err:
        print(f'OS error: {err}')
    except TypeError as err:
        print(f'TypeError: {err}')
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
