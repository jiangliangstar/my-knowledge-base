---
title: Python 高级技巧
date: 2025-06-23
tags:
  - python
  - programming
---

## 装饰器高级用法

```python
def debug_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数 {func.__name__}，参数: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"返回结果: {result}")
        return result
    return wrapper

@debug_decorator
def complex_calculation(a, b):
    return a * b + 100