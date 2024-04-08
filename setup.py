from setuptools import setup, find_packages

setup(
    name='flightdeck',
    version='0.0.1',
    description='FlightDeck is an SDK for building, running, and supporting your AI copilot.',
    author='Bill DeRusha',
    url='https://github.com/bderusha/flightdeck',
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)