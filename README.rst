=========================================================
 Create randomised sheet music to practice sight reading
=========================================================

Introduction
============

This is a python command-line interface module that produces a randomised staff of sheet music with the purpose of learning the fretboard of a guitar.
Users can choose strings, frets and positions to focus on as well as specifying if they would like to include sharps and flats.

Installation
============

From this directory, run ``$ pip install .``.
Subsequently, this module is run by invoking ``$ python -m sightreading``.

Usage
=====

By default, the module will produce a staff containing a random permutation of notes found on every string and frets 0 - 12 on the neck, as well as an indicator of which string they should be played on.
This staff is saved to ``staff.png``

Command line arguments:
-----------------------

* ``-b``, ``--bars NUM``: generate staff with ``NUM`` bars per line
  
* ``-d``, ``--diatonic``: only include notes in the key of C major
  
* ``-f``, ``--frets RAN``: include only frets in ``RAN``
  
* ``-n``, ``--no-string-symbols``: suppress string number symbols
  
* ``-p``, ``--position NUM``: only include notes in ``NUM`` th position. This is defined as the frets between ``NUM`` and ``NUM + 5`` inclusive. Open strings are treated as zeroth frets.
  
* ``-o``, ``--output FILE``: save output to ``FILE``
  
* ``-r``, ``--repeats NUM``: repeat the randomisation ``NUM`` times in a single staff
  
* ``-s``, ``--strings RAN``: include only strings in ``RAN``

Range specification
-------------------

The allowed strings and frets are specified passing a range of numbers to the ``-s`` and ``-f`` switches.
The format of this range is either

* a concatenated of desired numbers (eg. ``-s 136`` will select the first, third and sixth string), or

* an inclusive upper and lower limit separated by a colon. The order of the limits doesn't matter (eg, ``-f 7:12`` will select frets 7,8,9,10,11 and 12).
