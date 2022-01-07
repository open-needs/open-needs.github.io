.. _contribute:

Contribute
==========
Everybody is welcome to discuss the content with us or even sends us Pull Requests, containing changes or additional
information.

To do this, please create a PR on https://github.com/open-needs/open-needs.github.io.

It is also possible to talk directly to us, for this please write an e-mail to
`Daniel <mailto:daniel@useblocks.com?subject=Open-Needs>`__

Model definition
----------------
To describe / update a model for :ref:`models`, please take a look into the folder ``/models``.

Each schema has its own model and it gets imported to the documentation automatically by using
``.. jsonschema::`` directive.
See `sphinx-jsonschema extension <https://sphinx-jsonschema.readthedocs.io/en/latest/index.html>`__ for details.

Sphinx setup
------------
For everybody who wants to know which Sphinx extensions this side is using, here is the
used ``doc-requirements.txt`` file:

.. literalinclude:: doc-requirements.txt

Contributors
------------
.. literalinclude:: ../AUTHORS

License
-------
.. literalinclude:: ../LICENSE



