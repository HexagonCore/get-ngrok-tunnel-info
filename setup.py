from setuptools import setup
import re
import ast


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('ngrok_info/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(name='ngrok_info',
      version=version,
      description='Easy and fast tool written in python 3 to get info about running ngrok tunnel',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      url='https://github.com/HexagonCore/get-ngrok-tunnel-info',
      author='Hexagon Core Development',
      author_email='mp3martin.developer@gmail.com',
      license='MIT',
      packages=['ngrok_info'],
      install_requires=[
          'markdown',
          'requests'
      ],
      zip_safe=False)