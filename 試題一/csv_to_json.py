import pandas as pd
import json

# 讀取資料
df = pd.read_csv('/Users/joe/Desktop/試題一/CSV2JSON.zip')

# 定義函數（處理tag、detail）
def process_group(group):
    return {
        'tag_name': group.name,
        'detail': group[['detail_name', 'detail_value']].to_dict('records')
    }

# 構建JSON結構
result = df.groupby('member_id').apply(lambda x: {
    '_id': x.name,
    'member_id': x.name,
    'tags': x.groupby('tag_name').apply(process_group).tolist()
}).tolist()

#轉換為JSON格式
json_result = json.dumps(result, ensure_ascii=False, indent=4)

#儲存結果
with open('/Users/joe/Desktop/json_result', 'w', encoding='utf-8') as f:
    f.write(json_result)
