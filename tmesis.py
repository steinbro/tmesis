#!/usr/bin/env python3

import argparse
import unittest

import enchant


def find_tmesis(word, language):
    d = enchant.Dict(language)
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
    parser.add_argument('word', nargs='+')
    parser.add_argument(
        '--language', choices=enchant.list_languages(), default='en_US')
    args = parser.parse_args()

    for word in args.word:
        for outside, inside in find_tmesis(word, args.language):
            print('%s - %s = %s' % (word, inside, outside))
