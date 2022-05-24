from setuptools import setup, find_packages


setup(
    name='Insta Bot',
    version='0.1',
    description='A bot that automatically posts a random image and a random programming quote to the instagram.',
    author='Rasla',

    packages=find_packages(),
    install_requires=[
        # requirments.txt
    ],
    entry_points={
        'console_scripts': [
            'instabot = instabot.__main__:main'
        ]
    }
)