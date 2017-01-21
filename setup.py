
from setuptools import setup

setup(name="imaxmovie",
	  version="1.0",
	  description="Get stream movies/ tv episodes",
	  url="http://twitter.com/maximehip",
	  author="Maximehip",
	  author_email="imax-my@live.fr",
	  license='MIT',
	  packages=["imaxmovie"],
	  scripts=["bin/imaxmovie"],
	  install_requires=[
		  'BeautifulSoup4',
		  'requests'],
	  zip_safe=False)
