import pandas as pd
import json
import os
import requests
import time

# 创建asset文件夹，如果不存在
if not os.path.exists('asset'):
    os.makedirs('asset')

# 读取JSON文件
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 下载图片
base_url = "http://xhimage.gcgcloud.com/10358/upload/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

for item in data:
    if 'headImg' in item and item['headImg']:
        img_url = item['headImg']
        img_name = img_url.replace(base_url, "")
        img_path = os.path.join('asset', img_name)
        
        # 创建文件的所有父目录
        os.makedirs(os.path.dirname(img_path), exist_ok=True)
        
        # 下载图片并保存
        try:
            response = requests.get(img_url, headers=headers)
            if response.status_code == 404:
                print(f"图片未找到: {img_url}")
                continue
            response.raise_for_status()  # 检查请求是否成功
            with open(img_path, 'wb') as img_file:
                img_file.write(response.content)
            print(f"图片已下载并保存为: {img_path}")
        except requests.HTTPError as e:
            print(f"无法下载图片: {img_url}, 错误: {e}")
        
        # 增加请求间隔，避免频繁请求
        time.sleep(1)

# 将JSON数据转换为DataFrame
df = pd.DataFrame(data)

# 将DataFrame保存为Excel文件
df.to_excel("output.xlsx", index=False)

print("JSON数据已成功转换为Excel文件并保存为output.xlsx")
