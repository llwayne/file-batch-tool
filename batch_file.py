
#### 2. batch_file.py
```python
import os
import shutil

# ========== 可自定义配置区 ==========
TARGET_FOLDER = "./files"  # 需要处理的目标文件夹
RENAME_PREFIX = "document_"  # 批量重命名前缀
NEED_BATCH_RENAME = True  # 是否开启批量重命名
NEED_TEXT_REPLACE = True  # 是否开启文本关键词替换
OLD_WORD = "旧关键词"
NEW_WORD = "替换后的新关键词"
TEXT_SUFFIX = [".txt", ".md"]  # 需要处理的文本后缀
# ======================================

def init_folder():
    """初始化目标文件夹，不存在则创建"""
    if not os.path.exists(TARGET_FOLDER):
        os.mkdir(TARGET_FOLDER)
        print(f"已创建文件夹：{TARGET_FOLDER}")

def batch_rename():
    """批量文件重命名，有序数字后缀"""
    if not NEED_BATCH_RENAME:
        return
    file_list = os.listdir(TARGET_FOLDER)
    count = 1
    for filename in file_list:
        old_path = os.path.join(TARGET_FOLDER, filename)
        if os.path.isfile(old_path):
            suffix = os.path.splitext(filename)[1]
            new_name = f"{RENAME_PREFIX}{count}{suffix}"
            new_path = os.path.join(TARGET_FOLDER, new_name)
            os.rename(old_path, new_path)
            count += 1
    print(f"批量重命名完成，共处理 {count-1} 个文件")

def batch_text_replace():
    """批量替换文本文件内关键词"""
    if not NEED_TEXT_REPLACE:
        return
    file_list = os.listdir(TARGET_FOLDER)
    handle_count = 0
    for filename in file_list:
        suffix = os.path.splitext(filename)[1]
        if suffix not in TEXT_SUFFIX:
            continue
        file_path = os.path.join(TARGET_FOLDER, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace(OLD_WORD, NEW_WORD)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        handle_count += 1
    print(f"文本批量替换完成，共处理 {handle_count} 个文本文件")

if __name__ == "__main__":
    init_folder()
    batch_rename()
    batch_text_replace()
    print("所有文件处理任务执行完毕！")
