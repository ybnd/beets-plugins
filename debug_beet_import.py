from __future__ import division, absolute_import, print_function

import shutil
from beets.ui import main

if __name__ == "__main__":
    try:
        shutil.rmtree('library/soundtracks/2010 - S.E.N.S. Project - 君に届け オリジナル・サウンドトラック')
        main(
            [
                '-c', 'config.yaml',
                'update'
            ]
        )
    except FileNotFoundError:
        pass

    main(
        [
            '-c', 'config.yaml',
            'import', 'import'
        ]
    )
