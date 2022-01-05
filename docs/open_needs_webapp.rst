Open-Needs WebApp concept
=========================

.. sidebar:: Logo

   .. image:: /_static/open-needs-webapp-logo.png
      :align: center
      :width: 200px

:status: :badge:`work in progress,badge-primary`
:repository: tbd
:user documentation: tbd

**Open-Needs WebApp** shall provide a simple user interface to find, read and analyse need objects.

Motivation
----------
To get an easy overview about existing needs and make fast searches, a simple WebApp is needed.

As **Open-Needs** is general focusing on making need based information available in as many system as possible,
**Open-Needs WebApp** is only one of several solutions.

It may be the starting point for a more complex WebApp in future, to be used as the base for a SaaS solution.

Technology Stack
----------------

* React

Extension
---------
**Open-Needs WebApp** shall be extensible for some specific function collections.
E.g. the representations (tabs in the mockup) can be extended.

The goal is that an **Open-Needs** extension, can provide new features for backend and/or frontend.

Functional Mockup
-----------------
The mockups only show the functional aspects. They are no proposal for a final graphical design ;)

Main page
~~~~~~~~~
This is the most important page and shall be used also as entry page.

It shall provide all needed technical features:

* Authentication
* Project selection
* Filtering
* Need objects representation

The manipulation of need objects shall be done by a side-menu, which drops out when a single need is selected.

Bulk changes shall be not supported in the first versions.

.. uml::

   @startsalt
   scale 2
    {+
        {* Open-Needs WebApp  }
        { **User**: | Mister X | [ Logout ] }
        ~~
        { **Selector**: |^organisation^ | / | ^project^ | }
        ~~
        { **Filter**: | "version=='1.0 and status=='open'"}
        ~~
        **Results**:
        {/ **Cards** | Table | List | Flowchart | Piechart}
        {
            {+ **Need #1**
                some content
            } | {+
                **Need #2**
                some content
            } | {+
                **Need #3**
                some content
            } | {+
                **Need #4**
                some content
            }

            {+
                **Need #5**
                some content
            } | {+
                **Need #6**
                some content
            }
        }

   }

   @endsalt

URLs
----
.. http:get:: /

   Shows the main page.

   :example: https://app.open-needs.org/

.. http:get:: /(str:org_id)/

   Shows the main page with the selected organisation from the url

   :example: https://app.open-needs.org/rocketLabs

.. http:get:: /(str:org_id)/(str:project)

   Shows the main page with the selected organisation and project from the url

   :example: https://app.open-needs.org/rocketLabs/neptune3000

.. http:get:: /(str:org_id)/(str:project)?filter=

   Shows the main page with the selected organisation and project from the url

   :query filter: An Open-Needs Query Language (ONQL) string

   :example: https://app.open-needs.org/rocketLabs/neptune3000?filter=status=open


.. include:: discussion.rst
