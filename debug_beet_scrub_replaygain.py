from __future__ import division, absolute_import, print_function
from beets.ui import main

if __name__ == "__main__":
    main(
        [
            '-c', 'config.yaml', '-vv',
            'modify',
            'rg_album_gain=""', 'rg_album_peak=""',
            'rg_track_gain=""', 'rg_track_peak=""',
        ]
    )
