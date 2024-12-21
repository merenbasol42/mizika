from setuptools import setup, find_packages
#sss
setup(
    name='mizika',
    version='0.1.0',
    author='Mustafa Eren BAŞOL',
    author_email='merenbasol@gmail.com',
    description='Python VLC tabanlı müzik çalar paketi',
    # long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/merenbasol42/softcommpy',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',
    install_requires=[
        'typing-extensions',  # Tip desteği için
    ],
    extras_require={
        'dev': [
            'pytest',
            'mypy',
        ],
        'test': [
            'pytest',
        ],
    },
    keywords='python music playlist player',
    project_urls={
        'Source': 'https://github.com/merenbasol42/softcommpy',
    }, 
)
