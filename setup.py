from setuptools import setup
import json


with open("metadata.json", encoding="utf-8") as fp:
    metadata = json.load(fp)


setup(
    name='lexibank_chechuroborrowing',
    version="1.0",
    description=metadata['title'],
    license=metadata.get('license', ''),
    url=metadata.get('url', ''),
    py_modules=['lexibank_chechuroborrowing'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'lexibank.dataset': [
            'chechuroborrowing=lexibank_chechuroborrowing:Dataset',
        ],
        'cldfbench.commands': [
            'chechuroborrowing=commands',
        ]
    },
    install_requires=[
        'pylexibank>=1.1.1',
        'beautifulsoup4>=4.7.1',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)