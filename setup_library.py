from __future__ import division, absolute_import, print_function
from beets.ui import main
import shutil
import os


if __name__ == '__main__':
    try:
        shutil.rmtree('library')
        while os.path.isdir('library'):
            pass # todo: sometimes the dir gets removed *after* it is made!
        # todo: this still doesn't catch it, need to run this script twice...
        main(
            [
                '-c', 'config.yaml',
                'update', '--from-scratch'
            ]
        )
    except FileNotFoundError:
        pass

    if not os.path.isdir('library'):
        os.mkdir('library')
        # touch ~ https://stackoverflow.com/questions/1158076/implement-touch-using-python
        with open('library/library.db', 'a'):
            os.utime('library/library.db', None)

    main(
        [
            '-c', 'config.yaml',
            'import', 'import'
        ]
    )
