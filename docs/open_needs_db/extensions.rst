.. _db_extensions:

Extensions
==========

**Open-Needs DB** shall be as simple as possibile, to provide basic functionality in a secured way.
However, there are a lot of ideas how to extend **Open-Needs DB** to support more complex or user specific features.

Therefore **Open-Needs DB** will have an extension mechanism, which allows to load extensions during start-up phase
(no hot plug in during runtime).

Features
--------
An extension shall be able to provide the following elements:

* Custom tables in the database
* Custom functions registered on events
* Custom routes for the API
* Custom React components for **Open-Needs WebApp**. Examples:

  * An additional need representation (e.g. a specific diagram type)
  * A complete view, e.g. for metrics
  * Forms to edit needs or other elements

Use cases
---------
A list of ideas, which could be realized by **Open-Needs Extensions**:

* **Open-Needs Metrics**: Collect and provide metrics (e.g. amount of reads, last update)
* **Open-Needs Rules**: Checks rules before needs get created/updated (e.g. is "done" allowed for "status" field?)
* **Open-Needs Auth**: Check Authentication and Authorization on need level
  (e.g. is "user x" allowed to modify field "status" of "need y"?)

Some of these extension ideas may be integrated into **Open-Needs DB** by default (as internal extensions).

Technology stack
----------------
We are not sure if there is an "extension framework" for Python out there, which really can fulfill all our
requirements.

Our experience shows us, that "extension handling" is in most cases deeply product specific and must be implemented
mostly from scratch.

Some team members worked on the `Groundwork Framework <https://groundwork.readthedocs.io/en/latest/>`__ in the past,
which is now deprecated / not maintained.
Maybe some ideas can be taken from there.

But overall, **Open-Needs Extensions** will be a complete new implementation, with no existing "extension framework" as
basement.



