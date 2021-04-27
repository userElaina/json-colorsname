import setuptools

setuptools.setup(
    name='colorsname',
    version='1.0.1',
    description='colors\' names.',
    py_modules=['colorsname'],
	packages=setuptools.find_packages(),

    long_description='',
    author='userElaina',
    author_email='userElaina@google.com',
    url='https://github.com/userElaina',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    keywords='color name elaina',
    package_data={
        'colorsname': ['color.json'],
    },
    python_requires='>=3.6',
)