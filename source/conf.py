extensions = [
  'sphinxcontrib.blockdiag',
  'sphinxcontrib.nwdiag', 'sphinx.ext.todo', 'sphinx_fontawesome',
  'zuul_sphinx'
]
source_suffix = '.rst'
master_doc = 'index'
project = u'OSISM'
copyright = u'2017-2023, OSISM GmbH'
author = u'OSISM GmbH'
version = u''
release = u''
language = 'en'
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = True
html_theme = 'sphinx_material'
html_show_sphinx = False
html_show_sourcelink = False
html_show_copyright = True
htmlhelp_basename = 'documentation'
html_theme_options = {
    "nav_title": "OSISM Documentation",
    "color_primary": "blue",
    "color_accent": "light-blue",
    "globaltoc_depth": 3,
    "globaltoc_collapse": True,
}
html_context = {
    'display_github': True,
    'github_user': 'osism',
    'github_repo': 'documentation',
    'github_version': 'main',
    'conf_py_path': '/source/'
}
html_logo = 'images/logo.png'
html_title = "OSISM Documentation"
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}
#html_static_path = [
#    '_static'
#]
latex_elements = {}
zuul_role_paths = []
