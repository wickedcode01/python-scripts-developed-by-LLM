import os
import hashlib

def get_file_hash(file_path):
    """计算文件的SHA-1哈希值"""
    hasher = hashlib.sha1()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def find_duplicate_photos(folder_path):
    """查找指定文件夹中的重复照片"""
    file_hashes = {}
    duplicates = []

    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                # 跳过文件大小大于100MB的文件
                if os.path.getsize(file_path) > 100 * 1024 * 1024:
                    print(f"跳过大文件: {file_path} (大小: {os.path.getsize(file_path) / (1024 * 1024):.2f} MB)")
                    continue

                # 获取文件的哈希值
                file_hash = get_file_hash(file_path)

                if file_hash in file_hashes:
                    # 如果文件重复，记录该文件
                    duplicates.append(file_path)
                else:
                    # 保存唯一文件的哈希值
                    file_hashes[file_hash] = file_path

            except Exception as e:
                print(f"处理文件 {file_path} 时出错: {e}")

    return duplicates

def main():
    folder_path = input("请输入文件夹路径: ")
    duplicates = find_duplicate_photos(folder_path)

    if duplicates:
        print(f"找到 {len(duplicates)} 个重复文件。")
        print("前 10 个重复文件:")
        for file in duplicates[:10]:
            print(file)

        confirm = input("是否确认删除这些重复文件？(y/n): ").lower()
        if confirm == 'y':
            for file_path in duplicates:
                try:
                    os.remove(file_path)
                    print(f"删除文件: {file_path}")
                except Exception as e:
                    print(f"删除文件 {file_path} 时出错: {e}")
            print("删除操作完成。")
        else:
            print("未删除任何文件。")
    else:
        print("未找到重复文件。")

if __name__ == "__main__":
    main()
