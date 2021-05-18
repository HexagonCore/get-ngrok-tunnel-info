from setuptools import setup

setup(name='ngrok_info',
      version='1.0.10',
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