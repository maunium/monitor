import setuptools

setuptools.setup(
    name="maumon",
    version="0.1.0",
    url="https://github.com/maunium/monitor",

    author="Tulir Asokan",
    author_email="tulir@maunium.net",

    description="maunium.net monitoring system",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",

    packages=setuptools.find_packages(),

    install_requires=[
        "aiohttp>=3.0.1,<4",
        "mautrix>=0.4.0.dev1,<0.5.0",
        "dumbot>=1.2,<2",
    ],

    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Framework :: AsyncIO",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    entry_points="""
        [console_scripts]
        maumon=maumon.__main__:main
    """,
)
