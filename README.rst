`%hierarchy`, `%%dot` and `%%dotstr` magics for IPython
=======================================================

Install::

  %install_ext https://raw.github.com/tkf/ipython-hierarchymagic/master/hierarchymagic.py

Usage:

  In an ipython notebook run `%load_ext hierarchymagic` to load the extension.

First magic is ``%hierarchy``.  This magic command draws hierarchy of
given class or the class of given instance.  For example, the
following shows class hierarchy of currently running IPython shell.::

  %hierarchy get_ipython()


Second magic is ``%%dot``.  You can write graphiz dot language in a
cell using this magic.  Example::

  %%dot -- -Kfdp
  digraph G {
      a->b; b->c; c->d; d->b; d->a;
  }


Third magic is ``%%dotstr``. When you have a string written in the dot
language, use this function. E.g. when using pydot objects. Example::

  %%dotstr -f svg
  pydot_obj.to_string


Screenshot:

.. figure:: http://farm8.staticflickr.com/7083/7167551113_70f3b77b26_b.jpg
