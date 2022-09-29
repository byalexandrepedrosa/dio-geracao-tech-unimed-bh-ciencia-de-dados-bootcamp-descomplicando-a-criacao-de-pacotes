from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-byalexandrepedrosa",
    version="0.0.7",
    author="Alexandre Fernandes Pedrosa",
    author_email="contact@alexandrepedrosa.com",
    description="Test version - Image processing. This project belongs to Karina Tiemi Kato, Tech Lead, Machine Learning Engineer, Data Scientist Specialist at Take. This package is a demo for simulation of upload on the Test Pypi website, and it's from class of the Bootcamp Generation Tech Unimed-BH. E-mail:karinatkato@gmail.com.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/byalexandrepedrosa/dio-geracao-tech-unimed-bh-ciencia-de-dados-bootcamp-descomplicando-a-criacao-de-pacotes/",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
