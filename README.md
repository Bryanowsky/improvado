# Improvado test for Junior test

## Assessment Criteria

- Working code is not the main criteria. Maintanability, readability, code extensibility is also very(!) important;
- further program usage may require ability to work with output file types such as `.yaml`;
- input files could store gigabytes of data;
- having unit tests is good practice.

## Requierments
- Use only builtin of python (Pandas, NumPy etc... is unavailable)
- The script must be run from the console

## Task

### Input
There is four files: two `.csv`, one `.json` and one `,xml` files.

First `.csv` has folowing structure:

| D1  | D2  | ... | Dn  | M1  | M2  | ... | Mn  |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|  s  |  s  | ... |  s  |  i  |  i  | ... |  i  |
| ... | ... | ... | ... | ... | ... | ... | ... |

Second `.csv` has folowing structure:

| D1  | D2  | ... | Dn  | M1  | M2  | ... | Mn  | ... | Mz  |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|  s  |  s  | ... |  s  |  i  |  i  | ... |  i  | ... |  i  |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |


`.json` has folowing structure:

```python
{
  "fields": [
    {
      "D1": "s",
      "D2": "s",
      ...
      "Dn": "s",
      "M1": i,
      ...
      "Mp": i,
    },
    ...
  ]
}
```

`.xml` has folowing structure:

```xml
<objects>
  <object name="D1">
    <value>s</value>
  </object>
  <object name="D2">
    <value>s</value>
  </object>
  ...
  <object name="Dn">
    <value>s</value>
  </object>
  <object name="M1">
    <value>i</value>
  </object>
  <object name="M2">
    <value>i</value>
  </object>
  ...
  <object name="Mn">
    <value>i</value>
  </object>
</objects>
```

Where
_z_ > _n_ and _p_ >= _n_,
_s_ is string,
_i_ is an integer.


### Task

Get the data from all the files. Union it into single table (files could contain different count of dimensions and metrics). Then write in into single `.tsv` file with headers.

if one of input file doesn't have some column, you should put empty string into output file insttad of this column data. So output could be like:

| D1  | D2  | D3  | Dn  | M1  | M2  |
| :-: | :-: | :-: | :-: | :-: | :-: | 
|  a  |  b  |     |  c  |  1  |  3  | 
| a2  |     | d   |     |     |  4  | 


Data should be sorted by **D1** column. 

### Output
`.tsv` file with unioned data from all input files
