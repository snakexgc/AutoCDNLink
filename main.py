# 打开文件
with open('source.txt', 'r') as file:
    lines = file.readlines()
# 删除空白行并统计有效文本行数
non_empty_lines = [line.strip() for line in lines if line.strip()]
num_non_empty_lines = len(non_empty_lines)
# 输出结果
print(f"源分享链接数: {num_non_empty_lines}")
with open('source.txt', 'w') as file:
    file.writelines('\n'.join(non_empty_lines)+"\n")
# 处理 "domaindx.txt"
with open('domaindx.txt', 'r') as file_dx:
    lines_dx = file_dx.readlines()
non_empty_lines_dx = {line.strip() for line in lines_dx if line.strip()}  # 使用 set 去重
num_non_empty_lines_dx = len(non_empty_lines_dx)
# 写回文件
with open('domaindx.txt', 'w') as file_dx:
    file_dx.writelines('\n'.join(non_empty_lines_dx))
print(f"domaindx.txt中的CND域名数: {num_non_empty_lines_dx}")

# 处理 "domainyd.txt"
with open('domainyd.txt', 'r') as file_yd:
    lines_yd = file_yd.readlines()
non_empty_lines_yd = {line.strip() for line in lines_yd if line.strip()}  # 使用 set 去重
num_non_empty_lines_yd = len(non_empty_lines_yd)
# 写回文件
with open('domainyd.txt', 'w') as file_yd:
    file_yd.writelines('\n'.join(non_empty_lines_yd))
print(f"domainyd.txt中的CND域名数: {num_non_empty_lines_yd}")

# 读取 domaindx.txt 和 domainyd.txt 文件
with open('domaindx.txt', 'r') as file_dx:
    domains_dx = [line.strip() for line in file_dx.readlines()]
with open('domainyd.txt', 'r') as file_yd:
    domains_yd = [line.strip() for line in file_yd.readlines()]
# 读取 source.txt 文件
with open('source.txt', 'r') as source_file:
    source_lines = source_file.readlines()
# 初始化 dx.txt 和 yd.txt 文件内容
dx_lines = []
yd_lines = []
# 处理 dx.txt 文件
for line in source_lines:
    parts = line.split('@')
    if len(parts) == 2:
        domain_part = parts[1].split(':')[0]
        for domain_dx in domains_dx:
            modified_line = line.replace(domain_part, domain_dx)
            dx_lines.append(modified_line)
# 处理 yd.txt 文件
for line in source_lines:
    parts = line.split('@')
    if len(parts) == 2:
        domain_part = parts[1].split(':')[0]
        for domain_yd in domains_yd:
            modified_line = line.replace(domain_part, domain_yd)
            yd_lines.append(modified_line)
# 写入 dx.txt 文件
with open('dx.txt', 'w') as dx_file:
    dx_file.writelines(dx_lines)
# 写入 yd.txt 文件
with open('yd.txt', 'w') as yd_file:
    yd_file.writelines(yd_lines)
print("处理完成，已生成 dx.txt 和 yd.txt 文件。")
input()
