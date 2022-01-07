.. _models:

Open-Needs Models
=================
**Open-Needs** is written to support docs-as-code philosophy and existing tools.
And as most information is stored in files on code versioning systems, also the main source of information for
**Open-Needs** shall be files.

Beside extracting need objects from documentation files (e.g. md or rst), it shall be also possible to import them
from json-files, which may contain exported data from an issue tracking systems.

Also the complete configuration of a project in **Open-Needs** shall be defined in json format and files.

json-schema
-----------

All kind of data provided by or stored inside **Open-Needs** shall have a schema defined by
`json-schema <https://json-schema.org/>`__.

This shall affect all **Open-Needs** related files, which are created/used by client tools.
E.g. a project configuration, stored as ``open_needs_project_conf.json``, which is used by a client tool like
`Sphinx-Needs <https://sphinxcontrib-needs.readthedocs.io/en/latest/>`__ to setup the project configuration on
**Open-Needs Server**.

json-schema will not be used to validate REST API requests or the content of the database.
It is mostly used to validate files, which are used inside a docs-as-code approach to keep information in files and
therefore also on git repositories.

Project configurations
----------------------
In **Open-Needs** a project configuration contains the configuration for the following elements:

* need types
* need options
* need link types
* project warnings
* global option values
* and much more

Take a look into the
`configuration documentation of Sphinx-Needs <https://sphinxcontrib-needs.readthedocs.io/en/latest/configuration.html>`__
to get a feeling about what may be part of a project configuration in future.

Most configuration is clustered inside **Open-Needs Domains**, so that a project configuration contains
its project specific config under the domain ``project`` and imports the other domains under their domain specific
name.

Schema
~~~~~~
:name: Project schema
:location: ``/models/project_schema.json``
:status: :badge:`work in progress,badge-primary`

.. tabbed:: raw

    .. literalinclude:: /models/project_schema.json
        :class: on_schema

.. tabbed:: table

    .. jsonschema:: models/project_schema.json
       :lift_title: false

.. tabbed:: list

    .. data-viewer::
       :file: models/project_schema.json
       :expand:

Domain configurations
---------------------
**Open-Needs Domains** are a collection for need types, fields, checks and automatism, which are used to configure a
project for one or multiple specific domains.

With using domains a project gains the possibility to create and mange need objects for these domains.

Domains are used to provide a common setup for a specific domain, so that no projects needs define all the needed
need types and rules completely from scratch.

Examples for domains are:

* Software development (E.g. requirements and specification types)
* Software architecture (E.g. class and component types)
* Autosar (E.g. SWC and runnable types)
* Employees (E.g. employee, group and role types)
* Software processes (E.g. process, step, workflow and artifact types)

Schema
~~~~~~
:name: Domain schema
:location: ``/models/domain_schema.json``
:status: :badge:`work in progress,badge-primary`

.. tabbed:: raw

    .. literalinclude:: /models/domain_schema.json
       :class: on_schema

.. tabbed:: table

    .. jsonschema:: models/domain_schema.json
       :lift_title: false

.. tabbed:: list

    .. data-viewer::
       :file: models/domain_schema.json
       :expand:

Needs container
---------------
Schema
~~~~~~
:name: Needs container schema
:location: ``/models/needs_container_schema.json``
:status: :badge:`work in progress,badge-primary`

.. tabbed:: raw

    .. literalinclude:: /models/needs_container_schema.json
        :class: on_schema

.. tabbed:: table

    .. jsonschema:: models/needs_container_schema.json
       :lift_title: false

.. tabbed:: list

    .. data-viewer::
       :file: models/needs_container_schema.json
       :expand:

Sphinx-Needs schema
-------------------
Here is the current json schema of Sphinx-Needs, which is not so complex but maybe can provide some ideas.

Source: `needsfile.json <https://raw.githubusercontent.com/useblocks/sphinxcontrib-needs/master/sphinxcontrib/needs/needsfile.json>`__

.. jsonschema:: https://raw.githubusercontent.com/useblocks/sphinxcontrib-needs/master/sphinxcontrib/needs/needsfile.json
   :lift_title: false


.. include:: discussion.rst
