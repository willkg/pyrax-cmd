=========
pyrax-cmd
=========

Rackspace `Pyrax <https://github.com/rackspace/pyrax>`_  cloud files
command line client.

Features:

* ls - list object names in a container
* status - show the container status
* rename - rename an object in a container
* upload - upload files/folders to your cloudfiles container

It's pretty basic, but it made my life easier.

:Code:         https://github.com/willkg/pyrax-cmd/
:Issues:       https://github.com/willkg/pyrax-cmd/issues
:License:      BSD 3-clause; See LICENSE
:Contributors: See AUTHORS.rst


Note
====

This is **not** an official Rackspace pyrax cli.

If you're a Rackspace person and you want me to rename this, I
can. Just let me know.


Install
=======

From PyPI
---------

**Note:** This isn't on PyPI, yet. so this doesn't work.

Run::

    $ pip install pyrax-cmd


From git
--------

Run::

    $ pip install https://github.com/willkg/pyrax-cmd/zipball/master#egg=pyrax-cmd


For hacking
-----------

Run::

    $ git clone https://github.com/willkg/pyrax-cmd
    # Create a virtualenvironment
    $ pip install -e .


Use
===

Run::

    $ pyrax-cmd --help

This will show you help for pyrax-cmd.
