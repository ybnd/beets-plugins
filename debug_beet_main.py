from __future__ import division, absolute_import, print_function
import beets.ui

if __name__ == '__main__':
    beets.ui.main(
        ['-c', 'config.yaml', '--help']
    )