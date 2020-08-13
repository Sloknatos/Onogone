import json
import sys


def writer(dict, **kwargs):
    file_name = f"./files/{kwargs.get('file_name', 'original_comment.json')}"
    try:
        with open(file_name, 'w+') as f:
            json.dump(dict, f)
            f.close()
        return True
    except OSError as err:
        print(f'OS error: {err}')
    except TypeError as err:
        print(f'TypeError: {err}')
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
