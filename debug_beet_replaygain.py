from __future__ import division, absolute_import, print_function
from beets.ui import main
import time

if __name__ == "__main__":
    t = time.time()

    main(
        [
            '-c', 'config.yaml', '-vv',
            'replaygain', '-a', '-fw',
        ]
    )

    print(f"\n\n Elapsed time: {time.time() - t} s.")
