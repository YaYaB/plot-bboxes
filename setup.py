from setuptools import setup
from setuptools import find_packages


setup(name='plot-bboxes',
      version='0.0.1',
      description='Display bounding boxes on images',
      author='YaYaB',
      author_email='bezzayassine@gmail.com',
      url='https://github.com/YaYaB/plot-bboxes',
      download_url='https://github.com/YaYaB/plot-bboxes',
      license='MIT',
      classifiers=['License :: MIT License',
                   'Programming Language :: Python',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX',
                   'Operating System :: Unix',
                   'Operating System :: MacOS',
                   'Programming Language :: Python :: 3.5',
                   ],
      install_requires=[],
      extras_require={},
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'plot-bboxes=plot_bboxes.plot_bboxes:main'
          ]},

)