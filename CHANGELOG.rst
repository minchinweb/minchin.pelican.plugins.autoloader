AutoLoader Changelog
====================

1.2.3 -- 2025-11-03
-------------------

- **bug**: don't break on valid PEP440 versions (e.g. ``4.11.0.post0``). See
  `Issue #4`_.
- **support**: add (limited) test suite, using ``pytest``. Available as an
  *invoke* command: ``invoke run-tests``

1.2.2 -- 2025-10-24
-------------------

- **bug**: don't include extra top level directories in build artifact. See
  `Issue #1`_.
- **support**: swap from ``setup.py`` to ``pyproject.toml``

1.2.1 -- 2023-08-03
-------------------

- **bug**: don't break if no plugins exist in the namespace you are trying to
  load from.

1.2.0 -- 2023-07-11
-------------------

- **feature**: include autoloading from additional "private" namespace of
  ``minchin.pelican.readers``.
- **note**: this release has a bug that will crash if you're not using a plugin
  in the ``minchin.pelican.readers`` namespace.

1.1.0 -- 2022-04-09
-------------------

- **feature**: allow autoloading of specificed plugins to be skipped via
  ``AUTOLOADER_PLUGIN_BLACKLIST`` variable (on Pelican 4.5+ only).
- **bug**: don't try and initialize ``pelican.plugins._utils`` or
  ``pelican.plugins.signals``

1.0.3 - 2022-03-20
------------------

- **support**: update to ``minchin.releaser`` 0.8.2, and thus officially support
  Python 3.10.

1.0.2 - 2021-10-24
------------------

- **feature**: original implementation
- **support**: first release to PyPI under `minchin.pelican.plugins.autoloader`_

.. _minchin.pelican.plugins.autoloader: https://pypi.org/project/minchin.pelican.plugins.autoloader/
.. _Issue #1: https://github.com/minchinweb/minchin.pelican.plugins.autoloader/issues/1
.. _Issue #4: https://github.com/minchinweb/minchin.pelican.plugins.autoloader/issues/4
