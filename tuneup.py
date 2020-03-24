#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Mauricio "

import cProfile
import pstats
import timeit
import functools


def profile(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        prof = cProfile.Profile()
        prof.enable()
        result = func(*args, **kwargs)
        prof.disable()
        ps = pstats.Stats(prof).strip_dirs().sort_stats('cumulative')
        ps.print_stats(8)
        return result
    return decorator

    """A function that can be used as a decorator to measure performance"""


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


# def is_duplicate(title, movies):
#     """returns True if title is within movies list"""
#     for movie in movies:
#         if movie.lower() == title.lower():
#             return True
#     return False
@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    return [i for i in set(movies) if movies.count(i) > 1]


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(functools.partial(find_duplicate_movies, 'movies.txt'))
    time_result = min(t.repeat(repeat=7, number=3)) / 3
    print("Best time across 7 repeats of 3 runs per repeat:",
          time_result)


def main():
    """Computes a list of duplicate movie entries"""

    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))
    timeit_helper()


if __name__ == '__main__':
    main()
