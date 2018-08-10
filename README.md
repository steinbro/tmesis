Deconstruct examples of tmesis, in which a word can be constructed by
inserting one word somewhere within another word.

```
>>> import tmesis
>>> next(tmesis.find_tmesis('sparking'))
('sing', 'park')
>>> next(tmesis.find_tmesis('frankly'))
('fly', 'rank')
```
