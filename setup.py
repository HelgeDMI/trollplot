from distutils.core import setup

setup(
    name='trollplot',
    version='1.0',
    packages=['globeplot'],
    package_data={
        'globeplot': [
            'webgl_globe/third-party/Three/Detector.js',
            'webgl_globe/third-party/Three/RequestAnimationFrame.js',
            'webgl_globe/third-party/Three/ThreeExtras.js',
            'webgl_globe/third-party/Three/ThreeWebGL.js',
            'webgl_globe/third-party/Three/LICENSE',
            'webgl_globe/third-party/Tween.js',
            'webgl_globe/globe.js',
            'webgl_globe/index_template.html',
            'webgl_globe/index_template_small.html',
            'webgl_globe/loading.gif',
            'webgl_globe/world.jpg',],
    },
    url='http://www.pytroll.org',
    license='Apache 2.0',
    author='Helge Pfeiffer',
    author_email='rhp@dmi.dk',
    description='Test'
)



# from setuptools import setup
# import sys

# requirements = ['Jinja2', 'numpy']

# setup(name='trollplot',
#       version=1.0,
#       description='Plotting of numerical geo-located data onto a WebGL Globe.',
#       author='Helge Pfeiffer',
#       author_email='rhp@dmi.dk',
#       # package_dir={'globeplot': 'globeplot'},
#       packages=['globeplot', 'webgl_globe'],
#       install_requires=requirements,
#       package_data={
#         '': [
#             'webgl_globe/third-party/Three/Detector.js',
#             'webgl_globe/third-party/Three/RequestAnimationFrame.js',
#             'webgl_globe/third-party/Three/ThreeExtras.js',
#             'webgl_globe/third-party/Three/ThreeWebGL.js',
#             'webgl_globe/third-party/Three/LICENSE',
#             'webgl_globe/third-party/Tween.js',
#             'webgl_globe/globe.js',
#             'webgl_globe/index_template.html',
#             'webgl_globe/index_template_small.html',
#             'webgl_globe/loading.gif',
#             'webgl_globe/world.jpg',]
#       },
#       # data_files=[
#       #       'webgl_globe/third-party/Three/Detector.js',
#       #       'webgl_globe/third-party/Three/RequestAnimationFrame.js',
#       #       'webgl_globe/third-party/Three/ThreeExtras.js',
#       #       'webgl_globe/third-party/Three/ThreeWebGL.js',
#       #       'webgl_globe/third-party/Three/LICENSE',
#       #       'webgl_globe/third-party/Tween.js',
#       #       'webgl_globe/globe.js',
#       #       'webgl_globe/index_template.html',
#       #       'webgl_globe/index_template_small.html',
#       #       'webgl_globe/loading.gif',
#       #       'webgl_globe/world.jpg',],
#       # extras_require=extras_require,
#       # test_suite='pyresample.test.suite',
#       zip_safe=False,
#       classifiers=[
#           'Development Status :: 5 - Production/Stable',
#           'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
#           'Programming Language :: Python',
#           'Operating System :: OS Independent',
#           'Intended Audience :: Science/Research',
#           'Topic :: Scientific/Engineering'
#       ]
# )