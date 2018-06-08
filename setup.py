from setuptools import setup

setup(name='xp_xscreensaver',
      version='0.1',
      description='XP logon screensaver for xscreensaver',
      url='https://github.com/theblazehen/xp_xscreensaver',
      author='Jeandre Le Roux',
      author_email='theblazehen@theblazehen.com',
      license='MIT',
      install_requires=[
          'pygame',
      ],
      packages=['xp_xscreensaver'],
      package_data={'xp_xscreensaver': 'xp_xscreensaver/logon.png'},
      entry_points={
          'console_scripts': [
              'xp_xscreensaver = xp_xscreensaver:run_screensaver'
          ]
      },
      include_package_data=True,
      zip_safe=False)
