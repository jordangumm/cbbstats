from setuptools import setup, find_packages


install_requires = [
    'click',
    'kaggle',
    'numpy',
    'pandas',
]

setup_requires = [
    'setuptools_scm',
]


setup(
    name='cbbstats',
    description='College basketball statistics generator and interface',
    author='Jordan Gumm',
    author_email='jordan@variantanalytics.com',
    packages=find_packages(),
    use_scm_version=True,
    install_requires=install_requires,
    setup_requires=setup_requires,
)
