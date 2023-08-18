from setuptools import setup, find_packages

setup(name='KismetCaptureGnumac',
      version='2020.10.1',
      description='Kismet rtl_433 datasource',
      author='Mike Kershaw / Dragorn',
      author_email='dragorn@kismetwireless.net',
      url='https://www.kismetwireless.net/',
      install_requires=['protobuf', 'websockets'],
      python_requires='>=3.2',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'kismet_cap_sdr_gnumac = KismetCaptureRtl433.kismet_cap_sdr_rtl433:main',
              ],
          },
     )


