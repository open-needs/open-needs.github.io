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

Problem
~~~~~~~
The definition of **need**-objects are done by writing textual files in the **rst** format.
And a later Sphinx-Build creates objects out of this definitions, sets attributes and links and generates needed tables
and charts. The result is a PDF or HTML documentation, which represents the current status only.

So all information is technical only available during the build itself.
The capabilities to support the user during writing of **need**-objects are very limited. E.g. checks, if a used
status name is allowed, of if the used Id is really unique, are not possible.

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

Additionally specific interfaces shall be created, to make the database features and data available in different
documentation-generators like AsciiDoc or MkDocs. **Sphinx-Needs** will be also updated to support
**Open-Needs DB** in advance to its own, internal storage format.


Goals
-----
tbd

Use cases
---------
tbd

* Data history
* Multi framework / source support
* IDE / Dev support
* Comparison / Proposals

