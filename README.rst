Cumulus
=======

Create modular AWS CloudFormation templates and then connect them together with cumulus.

This is the second generation of the cumulus tool, original version: Cumulus_.

Build status
------------

Coming soon...

The problem
-----------

Amazon CloudFormation (CF) allows you to instantiate multiple AWS
resources in a repeatable, ordered and structured method. As our
infrastructure grew, so did our CF templates and soon they were
monolothic and complex to maintain. We looked at spliting these
templates into smaller chunks, which worked as a short term solution but
created a new problem. With multiple templates dependant on other
declared resources, we were forced to manually pass parameters for
inter-stack operability. This greatly affected the repeatability of our
stacks as we did not have an easy method to keep track of what
parameters were used, especially those relating to physical resource
IDs.

The solution
------------

Cumulus attempts to solve the problem by introducing a layer above CF
templates, a stack configuration YAML file. This allows multiple CF
stacks to be created in order and maintained respecting their
dependencies. The YAML file stores values for parameters to be passed
into each of the stacks. Parameters can be assigned with static values
or will source the value of a parameter, output or resource of another
stack described in the YAML file. Cumulus actively translates reference
values to physical resource values on creation of the stack.

Current state / known issues
----------------------------

In developement.


.. _Cumulus: https://github.com/cotdsa/cumulus