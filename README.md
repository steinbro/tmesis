Deconstruct examples of tmesis, in which a word can be constructed by
inserting one word somewhere within another word.

```
>>> from tmesis import find_tmesis
>>> next(find_tmesis('sparking', 'en_US'))
('sing', 'park')
>>> next(find_tmesis('frankly', 'en_US'))
('fly', 'rank')
```

Use the system word list to find some random examples:
```
$ sort -R /usr/share/dict/words | xargs python tmesis.py
flowing - ow = fling
flowing - win = flog
flashlight - lash = flight
...
```

Any language supported by [pyenchant](https://github.com/rfk/pyenchant) can be used:
```
$ python tmesis.py --language es_ES determinando
determinando - terminan = dedo
```
