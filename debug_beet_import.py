from __future__ import division, absolute_import, print_function

import shutil
from beets.ui import main

if __name__ == "__main__":
    try:
        shutil.rmtree('library/Elder')
        main(['update'])
    except FileNotFoundError:
        pass

    main(
        [
            '-c', 'config.yaml',
            '-l', 'library/library.db',
            'import', 'import'
        ]
    )
