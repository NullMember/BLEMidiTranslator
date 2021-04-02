"""
Usage instructions:
- If you are installing: `python setup.py install`
- If you are developing: `python setup.py sdist --format=zip bdist_wheel --universal bdist_wininst && twine check dist/*`
"""
import BLEMidiTranslator

from setuptools import setup
setup(
    name='BLEMidiTranslator',
    version=BLEMidiTranslator.version,
    author='Malik Enes Safak',
    author_email='e.maliksafak@gmail.com',
    packages=['BLEMidiTranslator'],
    url='https://github.com/NullMember/BLEMidiTranslator',
    license='MIT',
    install_requires=[],
    description='MIDI<=>BLE MIDI Translator',
    keywords = 'midi ble encoder decoder translator'
)