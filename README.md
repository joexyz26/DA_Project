# 試題一
<br>

### 說明

本專案以Python為程式語言。<br><br>
目的為讀取 CSV2JSON.csv 檔案，包含會員ID、標籤名稱、詳細名稱和詳細數值，並將其轉換為指定JSON結構。
<br><br>

### 環境要求

在運行腳本之前，請確保已安裝以下套件：
- Python 3.x
- pandas
<br>

請運行以下命令來安裝所需的套件：
```shell
pip install -r requirements.txt
```
<br>

### 程式說明


**1. 導入必要套件：**
   <br>
   ```python
   import pandas as pd
   import json
   ```
   <br>

**2. 讀取csv文件：**
   ```python
   df = pd.read_csv('/Users/joe/Desktop/試題一/CSV2JSON.zip')
   ```
<br>

**3. 定義函數：**

process_group 函數處理每個標籤組別，將其轉換為包含標籤名稱和詳細內容的字典。
   ```python
   def process_group(group):
    return {
        'tag_name': group.name,
        'detail': group[['detail_name', 'detail_value']].to_dict('records')
    }
   ```
 

<br>

**4. 構建所需的 JSON 結構：**

使用 groupby 依據 **member_id** 進行 **第一層分組**，並對各組別應用lambda函數，產生包含 _id、member_id 和 tags 的字典結構。\
在 tags 中再次使用 groupby 依據 **tag_name** 進行 **第二層分組**，並應用 process_group 函數。
   ```python
   result = df.groupby('member_id').apply(lambda x： {
    '_id': x.name,
    'member_id': x.name,
    'tags':x.groupby('tag_name').apply(process_group).tolist()
    }).tolist()
   ```
 
<br>


**5. 將結果轉換為 JSON 字串：**

 使用 json.dumps 函數將結果轉換為JSON字符串，並設置 ensure_ascii=False 和 indent=4 以確保非ASCII字符正確顯示並使JSON結構易於閱讀。
   ```python
   json_result = json.dumps(result, ensure_ascii=False, indent=4)
   ```
<br>


**6. 將 JSON 字串寫入檔案 json_result：**
   ```python
   with open('/Users/joe/Desktop/json_result', 'w', encoding='utf-8') as f:
    f.write(json_result)
   ```

<br><br>
### 注意事項
請根據您的實際 CSV2JSON.csv 檔案存放位置及輸出檔案預計存放位置修改路徑。

輸入路徑：
```python 
df = pd.read_csv('/Users/joe/Desktop/試題一/CSV2JSON.zip')
```
輸出路徑：
``` python
with open('/Users/joe/Desktop/json_result', 'w', encoding='utf-8') as f:
    f.write(json_result)
```
