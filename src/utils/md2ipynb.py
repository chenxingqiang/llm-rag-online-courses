import os
import re
import nbformat as nbf

def text_to_notebook(input_file, output_file):
    # 读取输入文件
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 创建一个新的notebook
    nb = nbf.v4.new_notebook()

    # 分割内容为单元格
    cells = re.split(r"\n```python\n|\n```\n", content)

    for i, cell_content in enumerate(cells):
        if i % 2 == 0:  # Markdown 单元格
            nb["cells"].append(nbf.v4.new_markdown_cell(cell_content.strip()))
        else:  # 代码单元格
            nb["cells"].append(nbf.v4.new_code_cell(cell_content.strip()))

    # 写入notebook文件
    with open(output_file, "w", encoding="utf-8") as f:
        nbf.write(nb, f)



# 主目录路径
root_path = "/Users/xingqiangchen/TASK/llm-rag-online-courses/notebooks"

# 两个阶段的目录
phase_dirs = ["phase1_fundamentals_of_llm", "phase2_rag_knowledge_and_practice"]

# 遍历每个阶段目录
for phase_dir in phase_dirs:
    phase_path = os.path.join(root_path, phase_dir)

    # 遍历目录中的所有文件
    for filename in os.listdir(phase_path):
        if filename.endswith(".ipynb"):
            input_file = os.path.join(phase_path, filename)
            output_file = input_file  # 输出文件与输入文件相同，即原地更新

            try:
                text_to_notebook(input_file, output_file)
                print(f"处理完成: {filename}")
            except Exception as e:
                print(f"处理 {filename} 时出错: {str(e)}")

print("所有文件处理完成")
