from setuptools import setup, find_packages

setup(
    name="zenerety",
    version="0.7",
    packages=find_packages(),  # 패키지 자동 탐색
    description="2D Game Framework for Python.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="614project",
    author_email="614project614@gmail.com",
    url="https://github.com/614project/zenerety",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)