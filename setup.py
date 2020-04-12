from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='pyeasydcer',
    version='1.0.0',
    description='Easy way to import default content in drupal using python',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Ruthvik Vegunta',
    author_email='ruthvikv@icloud.com',
    keywords=['Drupal', 'Default Content', 'dcer', 'easydcer'],
    url='https://github.com/ncthuc/elastictools',
    download_url='https://pypi.org/project/elastictools/'
)

install_requires = [
    'elasticsearch>=6.0.0,<7.0.0',
    'jinja2'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
    
    
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name='pyeasydcer',
    version='1.0.0',
    description='Easy way to import default content in drupal using python',
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author='Ruthvik Vegunta',
    author_email='ruthvikv@icloud.com',
    keywords=['Drupal', 'Default Content', 'dcer', 'easydcer'],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    #install_requires=["feedparser", "html2text"],
    entry_points={
        "console_scripts": [
            "realpython=reader.__main__:main",
        ]
    },
)