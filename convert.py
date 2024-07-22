import pandas as pd
import json

# JSON数据
data1 = [
    {
        "uId": 6128105,
        "rId": 2004788,
        "un": "管理员",
        "pn": "13581757554",
        "rn": "工作通管理员",
        "rl": 2,
        "on": "云狐时代",
        "oc": "5736403-5773337",
        "ol": 2,
        "oId": 5773337,
        "op": "总部-云狐时代",
        "photo": "",
        "mailAddr": ""
    },
    {
        "uId": 6130511,
        "rId": 2004788,
        "un": "18518500000",
        "pn": "18518500000",
        "rn": "工作通管理员",
        "rl": 2,
        "on": "云狐时代",
        "oc": "5736403-5773337",
        "ol": 2,
        "oId": 5773337,
        "op": "总部-云狐时代",
        "photo": "",
        "mailAddr": ""
    }
]



# 读取JSON文件
with open('data2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 将JSON数据转换为DataFrame
df = pd.DataFrame(data)

# 将DataFrame保存为Excel文件
df.to_excel("output.xlsx", index=False)

print("JSON数据已成功转换为Excel文件并保存为output.xlsx")
