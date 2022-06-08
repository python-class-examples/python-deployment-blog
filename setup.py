from setuptools import setup, find_packages

setup(
    version="0.2",
    name="mathias-blog",
    author="Mathias Santos de Brito",
    author_email="mathias@mathias.com",
    description="This is the blog system created by Mathias",
    url="https://github.com/blog-mathias",
    license="MIT",
    keywords="blog bms",
    requires=[],
    packages=find_packages(),
    entry_points={
        "console_scripts": ['blog=blog.main:main']
    }
)
