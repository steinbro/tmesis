#!/usr/bin/env python3

import argparse
import unittest

import enchant


def find_tmesis(word):
    d = enchant.Dict("en_US")
    for i in range(1, len(word) - 1):
        for j in range(i + 2, len(word)):
            outside = word[:i] + word[j:]
            inside = word[i:j]
            if d.check(outside) and d.check(inside):
                yield (outside, inside)


class TestFindTmesis(unittest.TestCase):
    def test_find_tmesis(self):
        self.assertEqual(next(find_tmesis('sparking')), ('sing', 'park'))
        self.assertEqual(next(find_tmesis('frankly')), ('fly', 'rank'))
        self.assertEqual(len(list(find_tmesis('whatever'))), 0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('word')
    args = parser.parse_args()

    if len(args.word) > 3:
        for outside, inside in find_tmesis(args.word):
            print('%s + %s = %s' % (outside, inside, args.word))
