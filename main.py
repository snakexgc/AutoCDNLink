import base64

# 处理 source.txt
try:
    with open('source.txt', 'r') as file:
        print("发现源文件source.txt，开始套用优选域名！")
        source_lines = file.readlines()
        source_lines = [line.strip() for line in source_lines if line.strip()]
        num_source_lines = len(source_lines)
        print(f"源链接数: {num_source_lines}")
        if num_source_lines == 0:
            print("请将您需要套用优选域名的节点信息存放到source.txt文件中再次启动主程序！")
            input("请按任意键结束本程序！")
            exit()

    with open('source.txt', 'w') as file:
        file.writelines('\n'.join(source_lines) + "\n")
except FileNotFoundError:
    # 如果文件不存在，创建一个新文件 source.txt
    with open('source.txt', 'w') as file:
        print("尚未创建源文件source.txt，现已自动创建！")
        print("请将您需要套用优选域名的节点信息存放到source.txt文件中再次启动主程序！")
        input("请按任意键结束本程序！")
        exit()

# 判断域名是否全为空
ifnull = 0

# 处理 domaindx.txt
try:
    with open('domaindx.txt', 'r') as file:
        print("发现电信联通优选域名domaindx.txt，开始进行预处理！")
        domaindx_lines = file.readlines()
        domaindx_lines = [line.strip() for line in domaindx_lines if line.strip()]
        num_domaindx_lines = len(domaindx_lines)
        if num_domaindx_lines == 0:
            print("未获取到电信联通优选域名！请您将电信联通优选域名填入domaindx.txt中！")
            ifnull += 1
        else:
            print(f"电信联通优选域名数为: {num_domaindx_lines}")
    with open('domaindx.txt', 'w') as file:
        file.writelines('\n'.join(domaindx_lines))
except FileNotFoundError:
    # 如果文件不存在，创建一个新文件 domaindx.txt
    with open('domaindx.txt', 'w') as file:
        print("尚未找到domaindx.txt，现已自动创建！")
        print("请将您的电信联通优选域名写入domaindx.txt文件！")

# 处理 domainyd.txt
try:
    with open('domainyd.txt', 'r') as file:
        print("发现移动优选域名domainyd.txt，开始进行预处理！")
        domainyd_lines = file.readlines()
        domainyd_lines = [line.strip() for line in domainyd_lines if line.strip()]
        num_domainyd_lines = len(domainyd_lines)
        if num_domainyd_lines == 0:
            print("未获取到移动优选域名！请您将移动优选域名填入domainyd.txt中！")
            ifnull += 1

        else:
            print(f"移动优选域名数为: {num_domainyd_lines}")
    with open('domainyd.txt', 'w') as file:
        file.writelines('\n'.join(domainyd_lines))
except FileNotFoundError:
    # 如果文件不存在，创建一个新文件 domainyd.txt
    with open('domainyd.txt', 'w') as file:
        print("尚未发现domainyd.txt，现已自动创建！")
        print("请将您的移动优选域名写入domainyd.txt文件！")
if ifnull == 2:
    print("由于没有发现任何优选域名，本程序结束！")
    input("请按任意键结束本程序！")
    exit()

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
valid_source_link = 0
invalid_source_link = 0
error_source_link = 0
# 处理 dx.txt 和 yd.txt 文件
for line in source_lines:
    if line.startswith("vless://") or line.startswith("trojan://"):
        parts = line.split('@')
        if len(parts) == 2:
            before_at = parts[0]
            after_colon = parts[1].split(':')[1]
            valid_source_link += 1
            for domain_dx in domains_dx:
                modified_line = before_at + "@" + domain_dx + ":" + after_colon
                dx_lines.append(modified_line)
            for domain_yd in domains_yd:
                modified_line = before_at + "@" + domain_yd + ":" + after_colon
                yd_lines.append(modified_line)
        else:
            invalid_source_link += 1
            dx_lines.append(line)  # 未能正确分割的行原样写入
            yd_lines.append(line)

    if line.startswith("vmess://"):
        # 去掉开头的"vmess://"并使用base64解码
        temp_link = base64.b64decode(line[len("vmess://"):]).decode('utf-8')
        # 切分字符串并存入parts变量
        parts = temp_link.split('"add":', 1)

        if len(parts) == 2:
            # 使用split方法以逗号分割，然后保留第二部分
            before_at = parts[0]
            after_colon = parts[1].split('\n', 1)[1]
            valid_source_link += 1
            for domain_dx in domains_dx:
                modified_line = before_at + "\"add\": \"" + domain_dx + "\",\n" + after_colon
                modified_line_dx = base64.b64encode(modified_line.encode('utf-8')).decode('utf-8')
                dx_lines.append("vmess://" + modified_line_dx + "\n")
            for domain_yd in domains_yd:
                modified_line = before_at + "\"add\": \"" + domain_yd + "\",\n" + after_colon
                modified_line_yd = base64.b64encode(modified_line.encode('utf-8')).decode('utf-8')
                yd_lines.append("vmess://" + modified_line_yd + "\n")
        else:
            invalid_source_link += 1
            dx_lines.append(line)  # 未能正确分割的行原样写入
            yd_lines.append(line)  # 未能正确分割的行原样写入
    if (line.startswith("vmess://") or line.startswith("vless://") or line.startswith("trojan://")) == 0:
        error_source_link += 1
        dx_lines.append(line)  # 不属于目前支持的三大协议
        yd_lines.append(line)  # 不属于目前支持的三大协议
        print("暂不支持该分享链接：" + line)

# 写入 dx.txt 文件
with open('dx.txt', 'w') as dx_file:
    dx_file.writelines(dx_lines)
# 写入 yd.txt 文件
with open('yd.txt', 'w') as yd_file:
    yd_file.writelines(yd_lines)
print("--------------------------------------------------\n")
print("处理完成，已生成 dx.txt 和 yd.txt 文件。\n")
print("成功源链接数：", valid_source_link)
print("失败源链接数：", invalid_source_link)
print("暂不支持的源链接数：", error_source_link)
print("--------------------------------------------------\n")
# 程序暂停以便查看结果
input("感谢您的使用，请按任意键结束本程序！")
