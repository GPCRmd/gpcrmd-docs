# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'gpcrmd-docs'
copyright = '2023, GPCRmd, GPCR drug discovery group'
author = 'GPCRmd'
version = '2.0'
release = '2.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.extlinks']

templates_path = ['_templates']
exclude_patterns = ['_build']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'GPCRmddoc'

# URL
extlinks = {'link': ('https://gpcrmd.org/%s',
                      'link %s')}