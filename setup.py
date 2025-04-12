from setuptools import setup, find_packages

setup(
    name='Generative AI Project',  # Project name
    version='0.0.0',               # Initial version
    author='Bappy Ahmed',          # Your name
    author_email='entbappy73@gmail.com',  # Your email
    packages=find_packages(),      # Automatically discover packages in your project
    install_requires=[             # List of dependencies your project needs
        # Example dependencies (add any required libraries here):
        # 'numpy', 'pandas', 'tensorflow'
    ],
    description='A project focused on Generative AI techniques',  # Short description of the project
    long_description=open('README.md').read(),  # Detailed description (from README.md)
    long_description_content_type='text/markdown',  # Specify markdown for README
    classifiers=[  # Optional: classifiers for PyPI categorization
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
