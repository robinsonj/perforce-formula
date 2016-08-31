================
perforce-formula
================

A salstack formula for installing and managing perforce packages.

Available States
================

.. contents::
  :local:

``p4.broker``
-------------

Installs the helix-broker package.

``p4.client``
-------------

Installs the helix-cli package.

``p4.p4dctl``
-------------

Installs the helix-p4dctl package for managing Perforce services.

``p4.server``
-------------

Installs the helix-p4d package.

Testing
=======

This formula uses test-kitchen and kitchen-salt to test the formula.

``kitchen test [name]``
----------------

Builds, runs, and tears down the full test suite.

``kitchen converge [name]``
--------------------

Builds the VM(s) and executes the salt formula.

``kitchen verify [name]``
-------------------------

Verifies VM(s) against their test suites.
