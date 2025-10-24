```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:

    requirements = [line.strip() for line in fh if (line.strip() and not line.strip().startswith("#"))]

setup(
    name="deepseek-cli",
    version="0.1.0",
    author="Florent Dumusois",
    author_email="ton@email.com",  # Remplace par ton email
    description="CLI intelligent pour l'API DeepSeek",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FDumusois/DeepSeekCLI",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "deepseek=deepseek_cli:main",
        ],
    },
    keywords="ai cli deepseek development coding",
    license="Apache 2.0",
)