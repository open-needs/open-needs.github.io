:title: Tesat me



.. image:: ../images/open-needs-logo.png
   :align: center
   :width: 50%
   :class: index-logo

**Status**: Concepts under development

Concept and Ideas
=================

.. sidebar:: Tools & Extensions

   * `Open-Needs-IDE <https://github.com/open-needs/open-needs-ide>`_

This documentation describes the concept and current ideas of Open-Needs, which realization shall start
in 2022.

User manuals or details of implementation can be found in the documentation of the related tool/extensions

**Open-Needs** is funded from March-September 2022 by the Prototype Fund of the Federal Ministry of
Education and Research.

.. list-table::

   * - .. image:: _static/PrototypeFund-P-Logo.png
          :align: center
          :scale: 15
          :target: https://prototypefund.de/en/
     - .. image:: _static/bmbf_logo_en.svg
          :align: center
          :width: 150px
          :target: https://www.bmbf.de/bmbf/en/


Motivation
----------
Open-Needs is based on ideas and wishes coming from the Open-Source project
`Sphinx-Needs <https://sphinxcontrib-needs.readthedocs.io/en/latest/>`__, which provides the possibility to
create and maintain **need**-objects inside the docs-as-code tool `Sphinx <https://www.sphinx-doc.org/>`__.

A **need**  in a documentation looks like this:

.. tabbed:: Need

    .. req:: Show Need-Example
       :id: REQ_001
       :status: open
       :tags: example, open-needs
       :collapse: True

       I'm a **need**-object, or better a Requirement.
       You can set all kind of meta-data and link me to other **need**-objects.
       Click the small "arrow" above to see the meta-data.

       Also filtering and presentation in tables, list and multiple types of charts is supported out-of-the-box.

       **Need**-objects are great to fulfill traceability requirements, which are often requested in safety relevant
       projects, like for the automotive or aerospace industry.

.. tabbed:: Code

   .. code-block:: rst

       .. req:: Show Need-Example
          :id: REQ_001
          :status: open
          :tags: example, open-needs
          :collapse: True

          I'm a **need**-object, or better a Requirement.
          You can set all kind of meta-data and link me to other **need**-objects.
          Click the small "arrow" above to see the meta-data.

          Also filtering and presentation in tables, list and multiple types of charts is supported out-of-the-box.

          **Need**-objects are great to fulfill traceability requirements, which are often requested in safety relevant
          projects, like for the automotive or aerospace industry.

In professional documentations there are often thousands of these **need**-objects, used to handle information
for Requirement Engineers, SW architects, SW developers, Test engineers or Quality and Process experts.

The following flow chart illustrates how the current workflow looks like when using Sphinx-Needs:

.. uml::
   :scale: 99%

    @startuml
    rectangle "Open-Needs DB" as db {

        card "REST API" as rest
        database "SQL DB" as sql
    }
    card Sphinx as s {
        card "Sphinx-Needs" as sn
        database "DOM" as dom
        card "HTML builder" as builder
    }

    artifact "Requirement\nObject" as req_obj

    artifact "RST files" as rst {
        card "Requirement\nDefinition" as req_def
    }

    artifact "HTML\ndocumentation" as html

    req_def --> sn : 1) read by
    sn --> req_obj : 2) creates
    req_obj --> rest  : 3) is send to
    rest <-> sql : 4) interacts
    rest -> sn:  5) provides\n final data
    sn -> dom: 6) updates
    dom -> builder: 7) interpreted\nby
    builder --> html: 8) builds
    @enduml

Problem
~~~~~~~
The definition of **need**-objects are done by writing textual files in the **rst** format.
And a later Sphinx-Build creates objects out of this definitions, sets attributes and links and generates needed tables
and charts. The result is a PDF or HTML documentation, which represents the current status only.

So all information is technical only available during the build itself.
The capabilities to support the user during writing of **need**-objects are very limited. E.g. checks, if a used
status name is allowed, or if the used Id is really unique, are not possible.

Also historical data is not easily accessible. It is stored in the source-code repository and only accessible if a build
is executed for this specific "point in time".

Another problem is that Sphinx-Needs can only be used with Sphinx.
No AsciiDoc or MkDocs support. It would be nice, if the idea of Sphinx-Needs could be easily used
in other documentation-generators, without the need to reimplement the same ideas and concepts.

Solution
~~~~~~~~
As solution for the above problems, a Database is planned, which can store all kind of **need**-objects, separated
by project and able to provide all needed information via a REST-API.

The database project is called **Open-Needs DB**.

Additionally specific interfaces shall be created, to make the database features and data available for different
documentation-generators like AsciiDoc or MkDocs. **Sphinx-Needs** will be also updated to support
**Open-Needs DB** in advance to its own, internal storage format.

Goals
-----

There are three main goals for **Open-Needs**:

1) Technology independent data access.
2) 100% server-side feature implementation
3) Small & fast, but scalable

Technology independent access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A mostly technology independent data access is the most important goal for Open-Needs.
For sure there must be a single API interface technology used (REST), but as all modern programming
languages are able to communicate with a REST-API, Open-Needs can be accessed by tools written in
Python, Java, C, JavaScript and more.

And even the type of the "tool" is not defined. It can be a documentation generator like AsciiDoc.
Or an extension for VS Code. Or a web interface. Or an Excel reader. It simply shall not matter.

**Open-Needs** is open to every type of tooling.

.. uml::
   :scale: 99%

   @startuml
    card "Open-Needs DB" as db #aaaaaa {
        card "REST API" as rest
        database "SQL DB" as sql
    }

    card "Documentation Generators" as dg {
        card "Sphinx"
        card "AsciiDoc"
        card "MkDocs"
        card "..." as 1
    }

    card "Jupyter\nNotebooks" as jupyter

    card "IDE Extensions" as ide {
        card "VS Code"
        card "PyCharm"
        card "IntelliJ"
        card "..." as 2
    }
    ide <-d--> rest
    jupyter <-u-> rest
    dg <-l-> rest

    @enduml

100% server-side
~~~~~~~~~~~~~~~~
Maintaining a feature twice, but in different programming language, is hard, annoying and a good way to mess up
everything.

Therefore **Open-Needs** tries to provide its feature all server-side, so that the different interface like
Sphinx-Needs can be kept as dumb as possible.

Small & fast, but scalable
~~~~~~~~~~~~~~~~~~~~~~~~~~
The main scenario for Open-Needs is to be started and stopped during a single documentation build, using a
local database (like sqlite). That would already allow to use all documentation related features.

For bigger projects, with maybe hundreds of developers, a common data storage provides some benefit.
So **Open-Needs** shall also be able to be executed on a powerful server, running 24/7 and handling hundreds of
parallel access.




Use cases
---------
tbd

Single source of truth
~~~~~~~~~~~~~~~~~~~~~~

Data history
~~~~~~~~~~~~

Multi framework / source support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IDE / Dev support
~~~~~~~~~~~~~~~~~

Comparison / Proposals
~~~~~~~~~~~~~~~~~~~~~~

Technical concept
-----------------
The following pages describe the ideas and concepts for a technical realisation.
They may not be up to date for all details, but they should be a good starting point to understand the general setup.

For details about usage and configuration, please take a look into the related project documentation.

.. toctree::

    open_needs_db

