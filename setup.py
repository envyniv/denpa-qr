from setuptools import setup
setup(
    name='denpa-qr-edit',
    version='0.0.1',
    author='envyniv'
    icon='./icon.svg'
    entry_points={
        'console_scripts': [
            'main=main:run'
        ]
    }
)
