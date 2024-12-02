import pandas as pd
import os



def excel_to_strings(excel_path, output_dir):
    # 读取Excel文件
    df = pd.read_excel(excel_path)

    # 获取所有语言列名
    languages = df.columns[3:]

    # 为每种语言创建一个 strings.xml 文件
    for lang in languages:
        # 创建输出目录
        dir_file_name = f"values-{lang}"
        if lang == "en":
            dir_file_name = f"values"
        lang_dir = os.path.join(output_dir, dir_file_name)
        os.makedirs(lang_dir, exist_ok=True)

        # 设置输出文件路径
        output_file = os.path.join(lang_dir, "strings.xml")

        with open(output_file, "w", encoding="utf-8") as f:
            # 写入XML头部
            f.write('<?xml version="1.0" encoding="utf-8"?>\n')
            f.write('<resources>\n')

            # 写入每个字符串
            for _, row in df.iterrows():
                key = row[2]
                value = row[lang]
                # 转义特殊字符
                value = str(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '\\"').replace("'", "\\'")
                if value == "nan":
                    f.write(f'    <string name="{key}" />\n')
                else:
                    f.write(f'    <string name="{key}">{value}</string>\n')

            # 写入XML尾部
            f.write('</resources>\n')

    print("转换完成！所有语言文件已生成。")

# 使用示例
excel_path = "/Users/xxx/Downloads/多国.xlsx"  # Excel文件路径
output_dir = "/Users/xxx/PycharmProjects/pythonProject/res"  # 输出目录路径
excel_to_strings(excel_path, output_dir)
