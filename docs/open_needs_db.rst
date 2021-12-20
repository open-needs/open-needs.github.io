Open-Needs DB concept
=====================

Open-Needs is a generic lib to create, manage, link and automate life cycle objects in Python applications.

It is designed to be used as backend in use-case specific tools like [Sphinx-Needs](https://sphinxcontrib-needs.readthedocs.io/en/latest/).

Different Interfaces can be build on top of it to access shared or independet datasets of need objects.

.. note::

    Project is currently in conceptual phase. So nothing to use, yet

Data objects
------------

Need object
~~~~~~~~~~~
A Need object is a general object, which can be a requirement, a specification, a rule, an employee or
whatever it shall represent.

But all Need objects have some common data / functions. They have:

* a project reference
* a key
* a title
* some content
* some meta data, like status, tags
* some references to other need objects, like links.


Project object
~~~~~~~~~~~~~~
A Project object mostly contains rules, which assigned need objects must follow.

It contains the following information:

* a key
* a name
* a description
* configurations for Need objects
* rules for Need objects


Data JSON example
~~~~~~~~~~~~~~~~~

.. code-block:: json

    "projects": {
      "MY_PROJECT": {
        "key": "MY_PROJECT",
        "name": "My first project with Open-Needs",
        "description": "Just used for some tests",
        "config": {},
        "rules": {},
        "needs": {
          "NEED_1": {
            "project": "MY_PROJECT",
            "key": "NEED_1",
            "title": "Example Need",
            "content": "Just some content as example",
            "status": "open",
            "tags": ["example", "awesome"],
            "links": ["NEED_2"]
          },
          "NEED_2": {
            "project": "MY_PROJECT",
            "key": "NEED_2",
            "title": "Another Example Need",
            "content": "",
            "status": "closed",
            "tags": ["example"],
            "links": []
          }
        }
      }
    }

Philosophy
----------
- Data is document based
- No strict schema for documents
- No rules checks

This philosophy is for this project only.
Extensions and interfaces may introduce functions to e.g. check project rules before a Need gets stored in the Database.

Event system
------------
Open needs is based on an event system, which is used to execute internal functions but also functions from extensions or other sources.
All functions have to be registered via the Open-Needs API.

Current events are:

* Lib handling

  * ``open_needs_init``
  * ``open_needs_init_done``
  * ``open_needs_loading_extensions``
  * ``open_needs_loading_extensions_done``
  * ``open_needs_shutdown``
  * ``open_needs_shutdown_done``

* Database handling

  * ``database_open``
  * ``database_open_done``
  * ``database_close``
  * ``database_close_done``

* Project handling

  * ``project_create``
  * ``project_create_done``
  * ``project_read``
  * ``project_read_done``
  * ``project_change``
  * ``project_change_done``
  * ``project_delete``
  * ``project_delete_done``

* Needs handling

  * ``need_create``
  * ``need_create_done``
  * ``need_read``
  * ``need_read_done``
  * ``need_change``
  * ``need_change_done``
  * ``need_delete``
  * ``need_delete_done``

**Attention**: It is not allowed to make any object manipulations on events with postfix ``_done``.
Events with ``_done`` are mostly for notification and to update additional objects, like some metrics.

If events are missing, feel free to create a PR.

Extensions
----------
Extensions need to be registered during runtime of Open-Needs, so that their features become part of the backend.
They are used to extend the internal data handling logic of Open-Needs by registering their functions in the Open-Needs event system.

Use cases may be: Collect metrics, check project rules before need creation, check authentication, trigger external systems.

Interfaces
----------
Interfaces are a way to access the data of Open-Needs.
Open-Needs provides a Python-API only.
On top of this additional interfaces can be build.

Possible interfaces may be: A REST or GraphQL API, IDE Extension, Static site generator interfaces, JSON exporter, WebViewer, ...

Currently planned is the improvement of [Sphinx-Needs](https://sphinxcontrib-needs.readthedocs.io/en/latest/) to support Open-Needs.

Database schema
---------------
Main tables:
* Projects
* Needs
* Fields

Projects
~~~~~~~~
* id: unique id
* key : unique key
* title: string
* description: string
* configs: JSON dict
* rules: JSON dict
* needs: back_reference from Needs


.. list-table::

   * - id
     - key
     - title
     - description
     - configs
     - rules
     - needs
   * - 1
     - SW_X
     - Module X Docs
     - SW Dev of module X
     - {configs.1;config.3}
     - {... }
     - [...]

Needs
~~~~~
Contains the main information of needs

* id: unique id
* key : key
* project: reference to Projects
* title: string
* content: JSON dict (value, format)
* fields: back_references from Fields


.. list-table::

   * - id
     - key
     - project
     - title
     - content
     - fields
   * - 1
     - NEED_001
     - Projects:1
     - Use Python
     - {"value": "Use Python >3.7 for **module x**", "format": "markdown"
     - FIELDS:1, FIELD:321

Fields
~~~~~~
Contains the single fields of all the needs.

* id: unique key
* project: Reference to Projects
* need: Reference to Needs
* field: JSON dict (field name, field value, field type)


.. list-table::

   * - id
     - project
     - need
     - field
   * - 1
     - Projects:1
     - Needs:1
     - {"name": "status", "value":: "open", "type": "str" }
   * - 2
     - Projects:2
     - Needs:3
     - {"name": "status", "value":: "closed", "type": "str" }
   * - 3
     - Projects:1
     - Needs:2
     - {"name": "type", "value":: "Requirement", "type": "str" }
   * - 4
     - Projects:1
     - Needs:2
     - {"name": "Price", "value":: 130.25, "type": "float" }
