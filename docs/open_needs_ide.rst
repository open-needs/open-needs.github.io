Open-Needs IDE concept
======================

:status: :badge:`work in progress,badge-primary`
:repository: https://github.com/open-needs/open-needs-ide
:user documentation: tbd

**Open-Needs IDE** shall provide extensions for different IDEs (VS Code, PyCharm) and is based on
the `Language Server Protocol <https://microsoft.github.io/language-server-protocol/>`__.


.. hint::

    There is already existing code available on https://github.com/open-needs/open-needs-ide, which is based
    on a code donation from the Automotive section of the `Robert Bosch GmbH <https://www.bosch.com/>`__.

    .. image:: _static/bosch_logo.png
       :align: center
       :width: 200px

    The current version of **Open Needs IDE** works with the
    `needs.json <https://sphinxcontrib-needs.readthedocs.io/en/latest/builders.html>`__ file of
    `Sphinx-Needs <https://sphinxcontrib-needs.readthedocs.io>`__ only.

Motivation
----------
**Open-Needs IDE** shall support the developer with time-saving functions to write needs inside an IDE more efficiently.
It shall support autocompletion, following need references, syntax checks and much more.

For most of this tasks a technical knowledge about existing needs and their configuration is needed, so that
**Open-Needs IDE** communicates with **Open-Needs DB**.

Architecture
------------
**Open-Needs IDE** is based on the Language server protocol, which makes it possible to use the same logic of checks
and autocompletion for IDES of different vendors.

Only the IDE specific client part (IDE extension) is IDE specific, but it should mostly contain configurations
and logic to connect to the Language Server only.

.. uml::

    @startuml
    card "IDE" as ide #aaa{
        card "Open-Needs\nIDE extension" as ext #6fa {
            card "code completion" as comp
            card "goto reference"
            card "need id generation"
            card "need preview"

        }


        artifact "code document" as doc
        hexagon "code change" as change

       doc -> change
       change --> comp
    }

    card "Open Needs\nLanguage server" #6fa {
        card "code completion" as ls_comp
        card "goto reference" as ls_ref
        card "need id generation" as ls_id
        card "need preview" as ls_preview
    }

    comp <-left-> ls_comp

    @enduml

