Deconstruct examples of tmesis, in which a word can be constructed by
inserting one word somewhere within another word.

```
>>> import tmesis
>>> next(tmesis.find_tmesis('sparking'))
('sing', 'park')
>>> next(tmesis.find_tmesis('frankly'))
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
