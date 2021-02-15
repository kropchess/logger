import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='logger',
    version='0.1',
    description='Testing installation of Package',
    url='https://github.com/kropchess/logger/',
    long_description=long_description,
    author='dimitborz',
    author_email='author@email.com',
    license='MIT',
    packages=['logger'],
    zip_safe=False
)