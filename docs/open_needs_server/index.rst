Open-Needs Server
=================

.. sidebar:: Logo

   .. image:: /_static/open-needs-server-logo.png
      :align: center
      :width: 200px

:status: :badge:`work in progress,badge-primary`
:repository: https://github.com/open-needs/open-needs-server
:user documentation: tbd

**Open-Needs Server** is a REST based Database to create, manage, link and automate life cycle objects.

It is designed to be used as backend in use-case specific tools like
`Sphinx-Needs <https://sphinxcontrib-needs.readthedocs.io/en/latest/>`__.

Different Interfaces can be build to access the data in different tools.

.. toctree::
   :hidden:

   extensions


Philosophy
----------
- No strict schema for need data
- No rules checks

This philosophy is for this project only.
Extensions and interfaces may introduce functions to e.g. check project rules before a Need gets stored in the Database.

Event system
------------
**Open-Needs Server** is based on an event system, which is used to execute internal functions but also functions from
extensions or other sources. All functions have to be registered via the Open-Needs API.

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
They are used to extend the internal data handling logic of Open-Needs by registering their functions in the
Open-Needs event system.

Use cases may be: Collect metrics, check project rules before need creation, check authentication,
trigger external systems.

The goal is that an **Open-Needs** extension, can provide new features for backend and/or frontend.

For more details, please take a look into :ref:`db_extensions`.

Interfaces
----------
Interfaces are a way to access the data of Open-Needs.
Open-Needs provides a REST API only.

Currently planned is the improvement of `Sphinx-Needs <https://sphinxcontrib-needs.readthedocs.io/en/latest/>`__
to support Open-Needs.

Security
--------
The data inside **Open-Needs Server** must be secured and access and edit rights must be controllable.

Example: Not all users shall be allowed to update needs for release version (e.g. Product_1.0), but for "sub-versions"
(e.g. 1.0_dev_feature_x).

Therefore a user management including roles and permissions must be implemented.

For the implementation of authentication mechanisms(e.g. OAuth2), FastAPI internal solutions shall be used.

Schemas
-------
All tools of **Open-Needs** shall use json-schemas to define the structure of information.

This kind of schema is mostly used for:

* project configuration structure
* project rules structure
* needs data structure

The goal is to allow any programming language to understand, analyse and validate Open-Needs data.

For more details, please take a look into :ref:`models`.

Database schema
---------------
Main tables:

* Organisations
* Projects
* Needs

.. uml:: ../pumls/db_models.puml

Organisations
~~~~~~~~~~~~~
A unity to represent a company or a project team.

.. uml:: ../pumls/db_organisations_model.puml

Projects
~~~~~~~~
Specifies a specific project inside an organisations.

This should be normally related to a Sphinx project or any other technical project, which contains the source code
for needs.

.. uml:: ../pumls/db_projects_model.puml

Needs
~~~~~
Stores the final needs.

Each row is a need, linked to a specific project of an organisation.

Only title and content get stored as columns. The rest of the data is stored in a single ``data`` column of type
``JSON``.

This allows to store needs of different data schemas (e.g. extra fields), without touch ing the structure of
database tables.

The content of ``data`` is filterable by all common SQL-compliant databases.

.. uml:: ../pumls/db_needs_model.puml


REST API
--------
All REST API endpoint has the following, common config:

.. http:get:: /any/open-needs/url

   :statuscode 200: No error
   :statuscode 401: Authentication needed

   :reqheader Accept: the response content type depends on :mailheader:`Accept` header
   :reqheader Authorization: optional OAuth token to authenticate

   :resheader Content-Type: this depends on :mailheader:`Accept header of request`

A complete list of all defined routes can be found here: :ref:`routingtable`.


Organisations
~~~~~~~~~~~~~
.. http:get:: /

   Lists all available organisations

   :example: https://api.open-needs.org/

.. http:post:: /

   Creates a new organisation

.. http:get:: /(str:org_id)

   Returns information of specific organisation, including all projects.

   :example: https://api.open-needs.org/rocketLabs

.. http:put:: /(str:org_id)

   Updates an existing organisation

   :example: https://api.open-needs.org/rocketLabs

Projects
~~~~~~~~

.. http:post:: /(str:org_id)

   Creates a new project inside the given organisation.

.. http:get:: /(str:org_id)/(str:project_id)

   Returns information of a specific project inside an organisation.
   Includes:

   * configs
   * rules
   * versions

   :example: https://api.open-needs.org/rocketLabs/neptune3000

.. http:put:: /(str:org_id)/(str:project_id)

   Updates a project. Allows to set configs and rules.

Versions
~~~~~~~~
**Versions** are an attribute of a ``Need`` object only.

There is no extra table for versions and they get create by simply setting the related ``version`` attribute
of a need.

Open-Needs automatically collects this information and knows, which versions are available.

.. http:get:: /(str:org_id)/(str:project_id)/(str:version)

   Returns all needs of a given version inside a specific project of an organisation.

   :example: https://api.open-needs.org/rocketLabs/neptune3000/2.1.1

Needs
~~~~~

.. http:post:: /(str:org_id)/(str:project_id)/(str:version)

   Allows to create a new need.


.. http:get:: /(str:org_id)/(str:project_id)/(str:version)/(str:need_id)

   Returns a specific need.

   :example: https://api.open-needs.org/rocketLabs/neptune3000/2.1.1/REQ_FUEL_TYPE


.. http:put:: /(str:org_id)/(str:project_id)/(str:version)/(str:need_id)

   Updates a specific need.

Filtering
~~~~~~~~~

.. http:post:: /filter

   Filters needs with a given filter string.

   .. warning::

      Sphinx-Needs currently support Python based filter string only, which allows to execute any Python code.
      This is too dangerous for a web application, so that another solution must be found or at least
      "Python based filter string feature" must be activated by user.

   :example: https://api.open-needs.org/filter


Technology Stack
----------------
**Open-Needs Server** will be based on `FastAPI <https://fastapi.tiangolo.com/>`__, which provides all needed functionality
for the API.

FastAPI
~~~~~~~

Useful FastAPI extensions may be:

* `FastAPI Permissions <https://github.com/holgi/fastapi-permissions>`__
* `FastAPI Users <https://github.com/fastapi-users/fastapi-users>`__

A great list of FastAPI links can be found at https://github.com/mjhea0/awesome-fastapi.

Database
~~~~~~~~
**Open-Needs Server** shall be based on **SQL** and support most **SQL**-based databases, like SQLite and PostgreSQL.

Therefore it uses as ORM `SQLAlchemy <https://www.sqlalchemy.org/>`__, which works pretty good with FastAPI.

.. hint::

    Projects like `SQLModel <https://sqlmodel.tiangolo.com/>`__ which allows to reuse the same model-definition for
    FastAPI routes and database models, shall not be used. Mostly because of the lack of customization, missing features
    (JSON fields) and because the models/schemas of  **Open-Needs Server** may differ between FastAPI and SQLAlchemy
    (as a lot of values may get calculated).


.. include:: ../discussion.rst
