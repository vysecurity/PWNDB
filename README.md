# PWNDB Parser
# Usage: 
```python pwndb-convert.py <file.txt>```

# Example:

```
0
Array
(
    [id] => 11805103
    [luser] => abcdef
    [domain] => raw.com
    [password] => abcdef
)

1
Array
(
    [id] => 11808053
    [luser] => abcdef2
    [domain] => raw.com
    [password] => abcdef
)
```

# Output:

```
abcdef@raw.com:abcdef
abcdef2@raw.com:abcdef
```


