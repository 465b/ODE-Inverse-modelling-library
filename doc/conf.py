# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'NEMF'
copyright = '2020, Laurin Steidle'
author = 'Laurin Steidle'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.


extensions = [
	# For conversion from markdown to html
	'recommonmark',
	# For auto generating documentation from docstrings
	'sphinx.ext.autodoc',
	# For numpy style docstrings
	'sphinx.ext.napoleon',
	# Linking source code to functions
	'sphinx.ext.viewcode',
]


# Add type of source files
source_suffix = ['.rst','.md']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

#html_theme = 'alabaster'
#html_theme = 'classic'
html_theme = 'sphinx_rtd_theme'
#import sphinx_bootstrap_theme
#html_theme = 'bootstrap'
#html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_logo = 'figures/logo.png'

# -- Laurin added this -------------------------------------------------------
 
# Sphinx error:master file 
# /home/docs/checkouts/readthedocs.org/user_builds/ ...
#  ... nemf/checkouts/latest/doc/
#  ... contents.rst not found
# to fix the error

master_doc = 'index'

autodoc_mock_imports = [
	'numpy',
	'seaborn',
	'pandas',
	'matplotlib',
	'networkx',
	'termcolor',
	'scipy',
	'yaml'
	]
