from __future__ import division, absolute_import, print_function
from beets.ui import main
import shutil
import os


if __name__ == '__main__':
    try:
        shutil.rmtree('library')
        main(
            [
                '-c', 'config.yaml',
                'update'
            ]
        )
    except FileNotFoundError:
        pass

    os.mkdir('library')

    main(
        [
            '-c', 'config.yaml',
            'import', 'import'
        ]
    )
