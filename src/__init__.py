# declare the package name
PACKAGENAME = 'src'
# declare the package version
VERSION = '0.0.1'
# specify the Python versions you support here. In particular, ensure
# that you indicate whether you support Python 2, Python 3 or both.
REQUIRES_PYTHON = '>=3.6'
# write a short description of your package here
DESCRIPTION = 'A package to generate commit messages from git diffs'
# write a long description of your package here
LONG_DESCRIPTION = 'A package to generate commit messages from git diffs'
# write the license type here. It can be any of the standard open source
# license types
LICENSE = 'MIT'
# specify if your package is zip safe or not
ZIP_SAFE = False
# specify the main python file
MAIN = 'main.py'
# specify the keywords
KEYWORDS = ['git', 'commit', 'message', 'diff', 'llm', 'ollama']
# specify the author's name
AUTHOR = 'Raul Cajias'
# specify the packages to be installed
PACKAGES = ['src']
# specify the entry points
ENTRY_POINTS = {
    'console_scripts': [
        'src=src.main:main',
    ],
}
# specify the package data
PACKAGE_DATA = {
    'src': [
        'data/*',
    ],
}
# specify the project urls
PROJECT_URLS = {
    'Bug Reports': 'https://github.com/cajias/llama-commit-msg/issues',
    'Source': 'https://github.com/cajias/llama-commit-msg'
}
