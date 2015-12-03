# Solutions Architect Tools

Some tools to aid in day-to-day SA tasks.

## sizing.py

Interprets a string of comma-separated [tshirt]-[moscow] tokens and outputs a story points calculation

#### Example

```shell
$ python sizing.py -t 'XS-M, M-S, XL-M, XL-M'
Must: 1 (2) + 40 (80) = 41 (82)
Should: 8 (13)
Total: between 49 and 95 points
```