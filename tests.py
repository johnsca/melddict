import pytest
from copy import deepcopy

from melddict import MeldDict


def test_add():
    d1 = MeldDict({'a': 'a',
                   'b': 'b',
                   'c': {'a': 'c.a', 'b': 'c.b'},
                   'd': ['d.0'],
                   'e': 'e',
                   'f': 'f'})
    d2 = {'b': 'B',
          'c': {'b': 'c.B', 'c': 'c.c'},
          'd': ['d.1'],
          'e': ['e.0'],
          'f': {'f': 'f.f'},
          'g': 'g'}
    with pytest.raises(TypeError):
        d1.add('foo')
    res = d1.add(d2)
    assert d1 == {'a': 'a',
                  'b': 'B',
                  'c': {'a': 'c.a', 'b': 'c.B', 'c': 'c.c'},
                  'd': ['d.0', 'd.1'],
                  'e': ['e.0'],
                  'f': {'f': 'f.f'},
                  'g': 'g'}
    assert res is d1

    d3 = MeldDict({'a': ['a.0']})
    d3.meld_iters = False
    d3.add({'a': ['a.1']})
    assert d3 == {'a': ['a.1']}


def test_subtract():
    d1 = MeldDict({'a': 'a',
                   'b': 'b',
                   'c': {'a': 'c.a', 'b': 'c.b'},
                   'd': ['d.0', 'd.1']})
    d2 = {'b': 'B',
          'c': {'b': 'c.B', 'c': 'c.c'},
          'd': ['d.1', 'd.2'],
          'f': 'f'}
    with pytest.raises(TypeError):
        d1.subtract('foo')
    res = d1.subtract(d2)
    assert d1 == {'a': 'a',
                  'c': {'a': 'c.a'},
                  'd': ['d.0']}
    assert res is d1

    d3 = MeldDict({'a': ['a.0', 'a.1'], 'b': 'b'})
    d3.meld_iters = False
    d3.subtract({'a': ['a.1']})
    assert d3 == {'b': 'b'}

    d4 = MeldDict({'a': ['a.0'],
                   'b': {'a': 'b.a'}})
    d4.remove_emptied = True
    d4.subtract(d4)
    assert d4 == {}


def test_add_operators():
    d1 = MeldDict({'a': 'a',
                   'b': 'b',
                   'c': {'a': 'c.a', 'b': 'c.b'},
                   'd': ['d.0'],
                   'e': 'e',
                   'f': 'f'})
    d2 = {'b': 'B',
          'c': {'b': 'c.B', 'c': 'c.c'},
          'd': ['d.1'],
          'e': ['e.0'],
          'f': {'f': 'f.f'},
          'g': 'g'}
    dr = {'a': 'a',
          'b': 'B',
          'c': {'a': 'c.a', 'b': 'c.B', 'c': 'c.c'},
          'd': ['d.0', 'd.1'],
          'e': ['e.0'],
          'f': {'f': 'f.f'},
          'g': 'g'}
    drr = {'a': 'a',
           'b': 'b',
           'c': {'a': 'c.a', 'b': 'c.b', 'c': 'c.c'},
           'd': ['d.1', 'd.0'],
           'e': 'e',
           'f': 'f',
           'g': 'g'}
    assert d1 + d2 == dr
    assert d2 + d1 == drr
    d3 = MeldDict(deepcopy(d1))
    d3 += d2
    assert d3 == dr
    d4 = deepcopy(d2)
    d4 += d1
    assert d4 == drr


def test_subtract_operators():
    d1 = MeldDict({'a': 'a',
                   'b': 'b',
                   'c': {'a': 'c.a', 'b': 'c.b'},
                   'd': ['d.0', 'd.1']})
    d2 = {'b': 'B',
          'c': {'b': 'c.B', 'c': 'c.c'},
          'd': ['d.1', 'd.2'],
          'f': 'f'}
    dr = {'a': 'a',
          'c': {'a': 'c.a'},
          'd': ['d.0']}
    drr = {'c': {'c': 'c.c'},
           'd': ['d.2'],
           'f': 'f'}
    assert d1 - d2 == dr
    assert d2 - d1 == drr
    d3 = MeldDict(deepcopy(d1))
    d3 -= d2
    assert d3 == dr
    d4 = deepcopy(d2)
    d4 -= d1
    assert d4 == drr
