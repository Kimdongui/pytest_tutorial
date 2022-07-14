from setuptools import find_packages, setup


if __name__ == "__main__":
    setup(
        name='pytest_project',
        version='0.0.1',
        packages=find_packages('src'),
        package_dir={'':'src'},
    )