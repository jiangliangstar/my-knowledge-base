import os
import datetime
from pathlib import Path

def update_last_modified():
    """更新所有笔记的最后修改日期"""
    notes_dir = Path('docs/notes')
    for note in notes_dir.glob('*.md'):
        content = note.read_text(encoding='utf-8')
        
        # 添加或更新最后修改日期
        if 'last_modified:' in content:
            content = content.replace(
                'last_modified: .*',
                f'last_modified: {datetime.date.today().isoformat()}'
            )
        else:
            content = content.replace(
                '---\n',
                f'---\nlast_modified: {datetime.date.today().isoformat()}\n'
            )
        
        note.write_text(content, encoding='utf-8')

def update_index():
    """更新首页内容"""
    index_path = Path('docs/index.md')
    content = f"""
# 我的知识库

> 最后更新: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}

## 最新内容

- [Python 高级技巧](notes/python.md)
- [系统设计面试指南](interviews/system-design.md)
- [Docker 部署问题解决方案](problems/deployment.md)

[![知识图谱](https://via.placeholder.com/800x400?text=自动生成的知识图谱)](diagrams/knowledge-map.png)
"""
    index_path.write_text(content, encoding='utf-8')

if __name__ == '__main__':
    update_last_modified()
    update_index()