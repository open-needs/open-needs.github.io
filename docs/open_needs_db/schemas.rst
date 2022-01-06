.. _db_json_schemas:

JSON schemas
============
All kind of data provided by or stored inside **Open-Needs DB** shall have a schema defined by
`json-schema <https://json-schema.org/>`__.

This shall affect all **Open-Needs** related files, which are created/used by client tools.
E.g. a project configuration, stored as ``open_needs_project_conf.json``, which is used by a client tool like
`Sphinx-Needs <https://sphinxcontrib-needs.readthedocs.io/en/latest/>`__ to setup the project configuration on an
**Open-Needs DB** server.

json-schema will no be used to validate REST API requests or the content of the database.
It is mostly used to validate files, which are used inside a docs-as-code approach to keep information in files and
therefore also on git repositories.

This kind of files can be:

* Project configuration files, which define config and rules of a project
* Need data files, which contain need-information for im/export. Like the
  `needs.json file of Sphinx-Needs <https://sphinxcontrib-needs.readthedocs.io/en/latest/builders.html#format>`__

Project configuration schema
----------------------------
tbd

Needs data schema
-----------------
tbd


