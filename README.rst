===========
simpleasset
===========
Simple asset pipeline toolset

----

What does it do?
================

``simpleasset`` is a library to manage an asset pipleline in a generic configurable way without being tightly coupled to any Framework.
It aims to do the following:

- Support many ``classes`` of content, e.g. Javascript or CSS

- Supports translating content through a MIME-type mapping

  - MIME-types can be recognised through file extentions, and can be chained.
  - Through Piping content through external applications
  - Through a Python function (extra ``context`` can be configured)

- Supports compression of content by content ``class``

- Entierly configuration driven

- Differentiates between Debug/Development modes and production modes

  - Can use rules specified to concatenate a set of input files based on Globs.

- Able to run stand-alone

  - As part of a build step
  - As a daemon that watches a set of input files, and generates output files

- Support simple integration to common frameworks

  - Bottle
  - Django
  - Tornado

Usage:
======

You can speficy a configuration file through the ``ASSETCONFIG`` Environment variable.


Feature Plan:
=============

1. Simple stand-alone tool that can translate data through an extention-determined MIME-type. This is to output the translated document to a configured location.

2. Ability to pipe data through both external programs and python functions (with configurable context)

3. Ability to concatenate input sources based on Glob rules speficied in configuration, for "Production" data.

4. Ability to "translate" production data (treat it as its own mime-type?)

5. Deaemonize tool.

6. Investigate how to do simple integration with some frameworks.
