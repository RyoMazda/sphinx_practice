Tests
================


Basic rst syntax
--------------------------------

This is `Link text <https://google.com/>`_.

List

* item1
* item2
* item3

Mark *italic text* with one asterisk, **bold text** with two.
For ``monospaced text``, use two "backquotes" instead.

A normal paragraph ending with ``::`` will flow and be word-wrapped::

    If the next paragraph is indented by four or more spaces, it will be monospaced text, without flow (or even wrapping in some non-print cases.)

    You can have multiple paragraphs like this, as long as they
    are all indented by the same amount.


Roles
-------------------

https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html


* :term:`pigimaru`
* :abbr:`LIFO (last-in, first-out)`
* :command:`command`
* :dfn:`definition`


Directives
---------------------------


Basics
~~~~~~~

.. versionadded:: 2.5
   The *spam* parameter.

.. note::
   This function is not suitable for sending spam e-mails.

.. warning::
    This is warning.


Images
^^^^^^^^^^^^^^^

.. image:: _static/images/pigimaru.png
   :width: 50%
   :align: center


Horizontal List
^^^^^^^^^^^^^^^

.. hlist::
   :columns: 3

   * A list of
   * short items
   * that should be
   * displayed
   * horizontally


Glossary
^^^^^^^^^^^^^^^

.. glossary::

   pigimaru
      No one knows.

   pijimaru
      Yet another :term:`pigimaru`.


For Codes
~~~~~~~~~~

.. py:function:: enumerate(sequence[, start=0])

   Return an iterator that yields tuples of an index and an item of the
   *sequence*. (And so on.)


.. code-block:: python
    :caption: this.py
    :name: this-py

    def zen() -> None:
        print("Explicit is better than implicit.")


Auto module
-----------------------------

.. automodule:: main
   :members:



Math
------------------------------------
Using roles: :math:`a^2 + b^2 = c^2`

Using directives:

.. math::

   (a + b)^2 = a^2 + 2ab + b^2

   (a - b)^2 = a^2 - 2ab + b^2


Markdown
-------------------------------

:doc:`md_sample`
