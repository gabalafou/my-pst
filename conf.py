# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'My PST'
copyright = '2024, Gabriel Fouasnon'
author = 'Gabriel Fouasnon'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_theme_options = {
    "use_edit_page_button": True,
    "show_toc_level": 1,
}
html_context = {
    "github_user": "gabalafou",
    "github_repo": "my-pst",
    "github_version": "main"
}


# -- Options for internationalisation ----------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#intl-options

locale_dirs = ['locale/']
gettext_compact = False
