from setuptools import setup

setup(
    name="prep",
    entry_points={
       "spacy_displacy_colors": ["colors = prep:displacy_colors"]
    }
)