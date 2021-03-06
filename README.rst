=========================================================
 Create randomised sheet music to practice sight reading
=========================================================

.. image:: https://travis-ci.com/damian-t-p/guitar-sightreading.svg?branch=master
    :target: https://travis-ci.com/damian-t-p/guitar-sightreading

Introduction
============

This is a python command-line interface module that produces a randomised staff of sheet music with the purpose of learning the fretboard of a guitar.

Users can choose strings, frets and positions to focus on as well as specifying if they would like to include sharps and flats.
The chosen notes will be shuffled randomly and the resulting staff saved as a png.

Example: position practice
--------------------------

Generate natural notes in seventh position without string numbering:

``python -m sightreading -p7 -d -n -o seventh-position``

.. image:: docs/seventh-position.png


Example: string practice
------------------------
	   
Generate notes on the fifth and sixth strings on frets 0 - 9

``python -m sightreading -s56 -f 0:9 -o low-strings``

.. image:: docs/low-strings.png

Installation
============

From this directory, run ``$ pip install .``.
Subsequently, this module is run by invoking ``$ python -m sightreading``.

Usage
=====

By default, the module will produce a staff containing a random permutation of notes found on every string and frets 0 - 12 on the neck, as well as an indicator of which string they should be played on.
This staff is saved to ``staff.png``

Command line arguments
----------------------

* ``-b``, ``--bars NUM``: generate staff with ``NUM`` bars per line
  
* ``-d``, ``--diatonic``: only include notes in the key of C major
  
* ``-f``, ``--frets RAN``: include only frets in ``RAN``
  
* ``-n``, ``--no-string-symbols``: suppress string number symbols
  
* ``-o``, ``--output FILE``: save output to ``FILE``

* ``-p``, ``--position NUM``: only include notes in ``NUM`` th position. This is defined as the frets between ``NUM`` and ``NUM + 5`` inclusive. Open strings are treated as zeroth frets.  
  
* ``-r``, ``--repeats NUM``: repeat the randomisation ``NUM`` times in a single staff
  
* ``-s``, ``--strings RAN``: include only strings in ``RAN``

Range specification
-------------------

The allowed strings and frets are specified passing a range of numbers to the ``-s`` and ``-f`` switches.
The format of this range is either

* a concatenation of desired numbers (eg. ``-s 136`` will select the first, third and sixth string), or

* an inclusive upper and lower limit separated by a colon. The order of the limits doesn't matter (eg, ``-f 7:12`` and ``-f 12:7`` will both select frets 7, 8, 9, 10, 11 and 12).
