from __future__ import division, absolute_import, print_function
from beets.ui import main

if __name__ == "__main__":
    main(
        [
            '-c', 'config.yaml',
            '-l', 'library/library.db',
            'link', 'add'
        ]
    )
