from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

setup(
    name="switch-file",
    version="1.0.4",
    packages=find_packages(),
    install_requires=[
        # dependencies
        "img2pdf",
        "pandas",
        "reportlab",
        "python-docx2pdf",
        "pywin32",
    ],
    entry_points={
    "console_scripts": [
        "switch-file = switch_file.converter:main"
    ]
},
    long_description= long_description,
    long_description_content_type='text/markdown',
    author="Harshita Dhurwe",
    author_email="harshitadhurwe@gmail.com",
    license="MIT",
)
