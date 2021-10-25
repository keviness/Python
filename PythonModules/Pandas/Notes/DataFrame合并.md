# pandas.DataFrame.append

DataFrame.**append**( *other* ,  *ignore_index**=**False* ,  *verify_integrity**=**False* ,  *sort**=**False* **)**[[source]](https://github.com/pandas-dev/pandas/blob/v1.3.4/pandas/core/frame.py#L8830-L8971)[](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html#pandas.DataFrame.append "Permalink to this definition")Append rows of other to the end of caller, returning a new object.

Columns in other that are not in the caller are added as new columns.

Parameters**other**DataFrame or Series/dict-like object, or list of theseThe data to append.

**ignore_index**bool, default FalseIf True, the resulting axis will be labeled 0, 1, …, n - 1.

**verify_integrity**bool, default FalseIf True, raise ValueError on creating index with duplicates.

**sort**bool, default FalseSort columns if the columns of self and other are not aligned.

**Changed in version 1.0.0:** Changed to not sort by default.

ReturnsDataFrameA new DataFrame consisting of the rows of caller and the rows of other.

See also

[`<span class="pre">concat</span>`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html#pandas.concat "pandas.concat")General function to concatenate DataFrame or Series objects.

Notes

If a list of dict/series is passed and the keys are all contained in the DataFrame’s index, the order of the columns in the resulting DataFrame will be unchanged.

Iteratively appending rows to a DataFrame can be more computationally intensive than a single concatenate. A better solution is to append those rows to a list and then concatenate the list with the original DataFrame all at once.

Examples

```
>>> df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'), index=['x', 'y'])
>>> df
   A  B
x  1  2
y  3  4
>>> df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'), index=['x', 'y'])
>>> df.append(df2)
   A  B
x  1  2
y  3  4
x  5  6
y  7  8
```

With ignore_index set to True:

```
>>> df.append(df2, ignore_index=True)
   A  B
0  1  2
1  3  4
2  5  6
3  7  8
```

The following, while not recommended methods for generating DataFrames, show two ways to generate a DataFrame from multiple data sources.

Less efficient:

```
>>> df = pd.DataFrame(columns=['A'])
>>> for i in range(5):
...     df = df.append({'A': i}, ignore_index=True)
>>> df
   A
0  0
1  1
2  2
3  3
4  4
```

More efficient:

```
>>> pd.concat([pd.DataFrame([i], columns=['A']) for i in range(5)],
...           ignore_index=True)
   A
0  0
1  1
2  2
3  3
4  4
```
