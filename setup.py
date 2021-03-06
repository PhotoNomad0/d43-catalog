from setuptools import setup

setup(
    name='d43-catalog',
    package_dir={'acceptance-test': 'functions/acceptance-test',
                 'catalog': 'functions/catalog',
                 'signing': 'functions/signing',
                 'webhook': 'functions/webhook'},
    packages=['acceptance-test', 'catalog', 'signing', 'webhook'],
    version='0.0.1',
    author='unfoldingWord',
    author_email='unfoldingword.org',
    description='Publishing door43-catalog organization.',
    license='MIT',
    keywords='',
    url='https://github.org/unfoldingWord-dev/d43-catalog',
    long_description='Publishing door43-catalog organization.',
    classifiers=[],
    install_requires=[
        'tx-shared-tools',
        'requests'
    ]
)
