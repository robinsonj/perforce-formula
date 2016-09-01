================
perforce-formula
================

----------
Unreleased
----------

Changed
#######

* Handle the Amazon-built CentOs AWS AMI's. For some reason, though labeled as
  'CentOS' images and still belonging to the 'RedHat' family, the machine lists
  its 'os' grain as 'Amazon.'

Fixed
#####

* Don't specify a path to `p4dctl` until an OS-map is implemented to handle
  cases where it is installed to different locations.

-------------------
v0.0.0 (2016-08-31)
-------------------

Initial release. Basic functionality includes:
  - Installing basic packages.
  - Managing broker and p4dctl config files.
  - Starting services managed by p4dctl.
  - Implementation of a basic p4dctl salt execution module.
