from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='aziraphale',
      version='0.0.00',
      description='A personal library to make it easy to load data into programs, particularly nlp focused data, with a side goal of version control',
      author='Keith Murray',
      author_email='kmurrayis@gmail.com',
      license='MIT',
      packages=['aziraphale'],
      install_requires=[
      ],
      include_package_data=True,
      zip_safe=False)
