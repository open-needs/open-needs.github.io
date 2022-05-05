.. _models:

Open-Needs Models
=================
**Open-Needs** is written to support docs-as-code philosophy and existing tools.
And as most information is stored in files on code versioning systems, also the main source of information for
**Open-Needs** shall be files.

Beside extracting need objects from documentation files (e.g. md or rst), it shall be also possible to import them
from json-files, which may contain exported data from an issue tracking systems.

Also the complete configuration of a project in **Open-Needs** shall be defined in json format and files.

.. tabbed:: Models

    .. uml:: pumls/models_overview.puml
       :align: center

.. tabbed:: Models with Schemas

    .. uml:: pumls/models_overview_with_schemas.puml
       :align: center

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

Organization configurations
---------------------------
An organization is an unique entity, which contains mostly projects only.

It may be used in future for common configuration of projects, which belong to one organization.

Schema
~~~~~~
:name: Organization schema
:uri: https://open-needs.org/organization.schema.json
:location: ``/models/organization.schema.json``
:status: :badge:`work in progress,badge-primary`

.. tabbed:: raw

    .. literalinclude:: /models/organization.schema.json
        :class: on_schema

.. tabbed:: table

    .. jsonschema:: models/organization.schema.json
       :lift_title: false

.. tabbed:: list

    .. data-viewer::
       :file: models/organization.schema.json
       :expand:

.. tabbed:: image

   .. uml::

        @startjson
        !include models/organization.schema.json
        @endjson

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
:uri: https://open-needs.org/project.schema.json
:location: ``/models/project.schema.json``
:status: :badge:`work in progress,badge-primary`

.. tabbed:: raw

    .. literalinclude:: /models/project.schema.json
        :class: on_schema

.. tabbed:: table

    .. jsonschema:: models/project.schema.json
       :lift_title: false

.. tabbed:: list

    .. data-viewer::
       :file: models/project.schema.json
       :expand:

.. tabbed:: image

   .. uml::

        @startjson
        !include models/project.schema.json
        @endjson

Domain configurations
---------------------
**Open-Needs Domains** are a collection of need types, fields, checks and automatism, which are used to configure a
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
:uri: https://open-needs.org/domain.schema.json
:location: ``/models/domain.schema.json``
:status: :badge:`work in progress,badge-primary`

.. tabbed:: raw

    .. literalinclude:: /models/domain.schema.json
       :class: on_schema

.. tabbed:: table

    .. jsonschema:: models/domain.schema.json
       :lift_title: false

.. tabbed:: list

    .. data-viewer::
       :file: models/domain.schema.json
       :expand:

.. tabbed:: image

   .. uml::

        @startjson
        !include models/domain.schema.json
        @endjson

Need item
---------
A single need item contains mostly its own data.

All dynamic elements (links, dynamic function) shall be resolved in the context of a specific documentation build/version.

It does not contain any information about project/domain configuration.
For this a :ref:`needs_container` must be used.

So it acts mostly as a key-value store.

Schema
~~~~~~
:name: Need schema
:uri: https://open-needs.org/need.schema.json
:location: ``/models/need.schema.json``
:status: :badge:`work in progress,badge-primary`

.. tabbed:: raw

    .. literalinclude:: /models/need.schema.json
        :class: on_schema

.. tabbed:: table

    .. jsonschema:: models/need.schema.json
       :lift_title: false

.. tabbed:: list

    .. data-viewer::
       :file: models/need.schema.json
       :expand:

.. tabbed:: image

   .. uml::

        @startjson
        !include models/need.schema.json
        @endjson

.. _needs_container:

Needs container
---------------
Needs can be created/imported via the documentation files or by a ``needs_container.json`` file.

A **needs container** can be used to store data from external systems (like Jira or Codebeamer) and make it available
in the docs-as-code environment.

Also the **Open-Needs** tools are using this format to export their data, so that it can be used by scripts and other
tools.

A **needs container** only contains needs related information, this may be:

* Needs: All exported needs in a list with their data
* Needs Domain: needs related project configuration as **Open-Needs Domain** config (needed types, options)

The exported **Domain** does contain information about the need configuration only.
E.g. what types and options must be configured. It shall not contain none-need specific information like
warnings, global values or automatism.

A **needs container** contains the "executed" information of needs in a specific documentation context/run.
All possible dynamic functions and references must be resolved.

Schema
~~~~~~
:name: Needs container schema
:uri: https://open-needs.org/needs_container.schema.json
:location: ``/models/needs_container.schema.json``
:status: :badge:`work in progress,badge-primary`

.. tabbed:: raw

    .. literalinclude:: /models/needs_container.schema.json
        :class: on_schema

.. tabbed:: table

    .. jsonschema:: models/needs_container.schema.json
       :lift_title: false

.. tabbed:: list

    .. data-viewer::
       :file: models/needs_container.schema.json
       :expand:

.. tabbed:: image

   .. uml::

        @startjson
        !include models/needs_container.schema.json
        @endjson

Sphinx-Needs schema
-------------------
Here is the current json schema of Sphinx-Needs, which is not so complex but maybe can provide some ideas.

Source: `needsfile.json <https://raw.githubusercontent.com/useblocks/sphinxcontrib-needs/master/sphinxcontrib/needs/needsfile.json>`__

.. jsonschema:: https://raw.githubusercontent.com/useblocks/sphinxcontrib-needs/master/sphinxcontrib/needs/needsfile.json
   :lift_title: false


.. include:: discussion.rst
