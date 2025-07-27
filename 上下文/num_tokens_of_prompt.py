# 计算文本中的token数量，用于经济性考量。

import os
import tiktoken


def num_tokens_from_string(string: str, model_name: str) -> int:
    """返回str中的token数。"""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def num_tokens_from_markdown(file_path: str, model_name: str) -> int:
    """返回Markdown文件中的token数。"""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return num_tokens_from_string(content, model_name)


def num_tokens(dir:str, model_name: str) -> str:
    """返回目录中（及子目录）每个Markdown文件的token数。以markdown表格形式返回。"""
    table = "| 文件名 | token数 |\n| --- | --- |\n"
    
    for root, _, files in os.walk(dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                num_tokens = num_tokens_from_markdown(file_path, model_name)
                table += f"| {file_path} | {num_tokens} |\n"
    return table


if __name__ == "__main__":
    # usage:

    # 返回str中的token数。
    print(num_tokens_from_string("Hello, world!", "gpt-4-0314"))

    # 返回Markdown文件中的token数。
    print(num_tokens_from_markdown("README.md", "gpt-4-0314"))

    # 返回目录中每个Markdown文件的token数。
    print(num_tokens("上下文", "gpt-4-0314"))