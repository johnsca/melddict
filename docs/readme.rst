MeldDict |badge|
----------------

.. |badge| image:: https://travis-ci.org/johnsca/melddict.svg?branch=master
    :target: https://travis-ci.org/johnsca/melddict

A dict subclass that supports adding and subtracting other Mappings to perform
recursive merging and removal.

By default, lists are also melded, but this can be configured. You can also
have keys whose values are empty after a subtraction dropped automatically.

The full documentation is available online at: https://melddict.readthedocs.io/


Examples
--------

You can add two mappings together to combine them:

.. code:: python

    meld_dict = MeldDict({'a': 'a',
                          'b': [1, 2],
                          'c': {'1': 1},
                          'd': 'd'})
    norm_dict = {'b': [3, 4],
                 'c': {'2': 2},
                 'd': 'D',
                 'e': 'e'}
    meld_res = meld_dict + norm_dict
    meld_res == {'a': 'a',
                 'b': [1, 2, 3, 4],
                 'c': {'1': 1, '2': 2},
                 'd': 'D',
                 'e': 'e'}
    meld_dict += norm_dict  # a.k.a. meld_dict.add(norm_dict)
    meld_dict == meld_res

You can also subtract one mapping from another:

.. code:: python

    meld_dict = MeldDict({'a': 'a',
                          'b': [1, 2],
                          'c': {'1': 1, '2': 2},
                          'd': 'd'})
    norm_dict = {'b': [2, 3],
                 'c': {'2': 2, '3': 3},
                 'd': 'D',
                 'e': 'e'}
    meld_res = meld_dict - norm_dict
    meld_res == {'a': 'a',
                 'b': [1],
                 'c': {'1': 1}}
    meld_dict -= norm_dict  # a.k.a. meld_dict.subtract(norm_dict)
    meld_dict == meld_res
