from setuptools import setup, find_packages

setup(
    name="multimodal_bot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "spacy",
        "openai",
        "discord.py",
        "python-dotenv",
    ],
    python_requires=">=3.8",
) 