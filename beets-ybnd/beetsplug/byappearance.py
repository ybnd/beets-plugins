# -*- coding: utf-8 -*-
# This file is part of beets.
# Copyright 2020, Yury Bondarenko
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

"""If the track number is not set, go by order of appearance
"""
from __future__ import division, absolute_import, print_function

from beets import plugins
from beets.util import displayable_path
import os
import re
import six


class ByAppearancePlugin(plugins.BeetsPlugin):
	def __init__(self):
		super(ByAppearancePlugin, self).__init__()
		self.register_listener('import_task_start', by_appearance)


def by_appearance(task, session):
	if task.is_album:
		items = task.items
		missing_tracks = all(i.track == 0 for i in items)
		
		# todo: doesn't work @ "Use as-is""
        # todo: but track numbers are correct in "eDit"
        # todo: workaround: "eDit" track 1 to e.g. 666, fix afterwards
        # todo: ...messy, but faster than entering numbers manually
		
		if missing_tracks:
			for i, item in enumerate(items):
				item.track = i+1  # Python counts from 0
