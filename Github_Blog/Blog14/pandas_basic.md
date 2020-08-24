
## Import Package and Load Data


```python
import pandas as pd

df = pd.read_csv('pandas_data.csv', encoding = 'euc-kr')
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>이름</th>
      <th>전화번호</th>
      <th>주소</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>010-111-1111</td>
      <td>서울시 강남구</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>010-222-2222</td>
      <td>인천시 연수구</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>010-333-3333</td>
      <td>경기도 용인시 수지구</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>010-444-4444</td>
      <td>서울시 관악구</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>010-555-5555</td>
      <td>서울시 종로구</td>
    </tr>
    <tr>
      <th>5</th>
      <td>F</td>
      <td>010-666-6666</td>
      <td>경기도 시흥시</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>010-777-7777</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## Row and Column Counts


```python
df.shape
```




    (7, 3)



## Loop each columns to modify the data


```python
row_counts, col_counts = df.shape

for i in range(row_counts):
    print(df["전화번호"][i][4:])
    df["전화번호"][i] = df["전화번호"][i][4:]
```

    111-1111
    222-2222
    333-3333
    444-4444
    555-5555
    666-6666
    777-7777
    

## Check if the data is properly modified


```python
df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>이름</th>
      <th>전화번호</th>
      <th>주소</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>111-1111</td>
      <td>서울시 강남구</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>222-2222</td>
      <td>인천시 연수구</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>333-3333</td>
      <td>경기도 용인시 수지구</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>444-4444</td>
      <td>서울시 관악구</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>555-5555</td>
      <td>서울시 종로구</td>
    </tr>
    <tr>
      <th>5</th>
      <td>F</td>
      <td>666-6666</td>
      <td>경기도 시흥시</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>777-7777</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## Save File


```python
df.to_csv("output_csv_EUC_KR.csv", encoding='euc-kr', index=False)
df.to_csv("output_csv_CP949.csv", encoding='cp949', index=False)
df.to_csv("output_csv_UTF8.csv", encoding='utf-8', index=False)
df.to_excel("output_excel.xlsx", encoding='euc-kr', index=False)
```
