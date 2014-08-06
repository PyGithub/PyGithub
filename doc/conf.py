# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

# @todoAlpha In the doc of each method, link to the tests that use it (good examples for the doc)

# The _templates/layout.html file has been copied from a part sphinx/themes/basic/layout.html and modified to include Disqus

import sys
import os
import shutil
import glob

sys.path.insert(0, os.path.abspath('..'))
import PyGithub

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage', 'sphinx.ext.mathjax']
templates_path = ['_templates']
source_suffix = '.rst'
source_encoding = 'utf-8'
master_doc = 'index'

project = u'PyGithub'
copyright = u'2013-2014, Vincent Jacques'
version = PyGithub.Version
release = PyGithub.Version

exclude_patterns = []

pygments_style = 'sphinx'

html_theme = 'default'
# html_static_path = ['_static']

autodoc_default_flags = []
autodoc_member_order = "bysource"
autoclass_content = "both"
