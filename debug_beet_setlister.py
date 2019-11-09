from __future__ import division, absolute_import, print_function

import shutil
from beets.ui import main

if __name__ == "__main__":
    main(
        [
            '-c', 'config.yaml',
            '-l', 'library/library.db',
            'setlister', 'Rosetta'
        ]
    )
