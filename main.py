# 处理 source.txt
with open('source.txt', 'r') as file:
    source_lines = file.readlines()
source_lines = [line.strip() for line in source_lines if line.strip()]
num_source_lines = len(source_lines)

# 写回 source.txt 文件
with open('source.txt', 'w') as file:
    file.writelines('\n'.join(source_lines) + "\n")

print(f"源链接数: {num_source_lines}")

# 处理 domaindx.txt
with open('domaindx.txt', 'r') as file:
    domaindx_lines = file.readlines()
domaindx_lines = [line.strip() for line in domaindx_lines if line.strip()]
num_domaindx_lines = len(domaindx_lines)

# 写回 domaindx.txt 文件
with open('domaindx.txt', 'w') as file:
    file.writelines('\n'.join(domaindx_lines))

print(f"电信联通优选域名数: {num_domaindx_lines}")

# 处理 domainyd.txt
with open('domainyd.txt', 'r') as file:
    domainyd_lines = file.readlines()
domainyd_lines = [line.strip() for line in domainyd_lines if line.strip()]
num_domainyd_lines = len(domainyd_lines)

# 写回 domainyd.txt 文件
with open('domainyd.txt', 'w') as file:
    file.writelines('\n'.join(domainyd_lines))

print(f"移动优选域名数: {num_domainyd_lines}")


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
        before_at = parts[0]
        after_colon = parts[1].split(':')[1]
        for domain_dx in domains_dx:
            modified_line = before_at + "@" + domain_dx + ":" + after_colon
            dx_lines.append(modified_line)
    else:
        dx_lines.append(line)  # 未能正确分割的行原样写入

# 处理 yd.txt 文件
for line in source_lines:
    parts = line.split('@')
    if len(parts) == 2:
        before_at = parts[0]
        after_colon = parts[1].split(':')[1]
        for domain_yd in domains_yd:
            modified_line = before_at + "@" + domain_yd + ":" + after_colon
            yd_lines.append(modified_line)
    else:
        yd_lines.append(line)  # 未能正确分割的行原样写入

# 写入 dx.txt 文件
with open('dx.txt', 'w') as dx_file:
    dx_file.writelines(dx_lines)

# 写入 yd.txt 文件
with open('yd.txt', 'w') as yd_file:
    yd_file.writelines(yd_lines)

print("处理完成，已生成 dx.txt 和 yd.txt 文件。")

# 程序暂停以便查看结果
input()
