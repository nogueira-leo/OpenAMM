from setuptools import setup, find_packages

setup(
    name='OpenAMM',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your project's dependencies here
        
    ],
    test_suite='tests',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python library for acoustic metamaterials',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nogueira-leo/OpenAMM',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
