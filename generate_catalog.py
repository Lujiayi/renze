import os
from pypinyin import lazy_pinyin
from jinja2 import Environment, FileSystemLoader

# 姓名列表
names = [
    "罗淑琪", "杨曦涵", "吴治纬", "李师静羽", "韩宜橙", "陈慧怡", "王俊桥",
    "何昊阳", "艾怡杭", "马楚涵", "李希璇", "朱子涵", "段小淼", "李子曦",
    "张少凡", "李彦霆", "段旭阳", "杜宗鸿", "严浩睿", "戴炜昊", "孙璐瑶",
    "范恒溢", "王姣皓", "戴益宏", "贾梦欣", "和钰涵", "尹李桧", "胡宇佳",
    "卢梵希", "袁文俊辉", "何其洵", "左家玮", "曾铭伟", "杨清然","许瑾裕","李晨"
]

# 将姓名转换为拼音并创建字典
pinyin_dict = {name: ''.join(lazy_pinyin(name)) for name in names}

# 创建目录结构
for name, pinyin in pinyin_dict.items():
    folder = pinyin
    os.makedirs(folder, exist_ok=True)
    index_path = os.path.join(folder, 'index.html')
    if not os.path.exists(index_path):
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(f"<!-- {name} 的页面 -->\n")

# 设置模板环境
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# 渲染模板
rendered_html = template.render(names=names, pinyin_dict=pinyin_dict)

# 保存生成的目录网页
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(rendered_html)

print("目录网页已生成：index.html")