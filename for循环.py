# path='attack.csv'
def new(path):
    # ips=[line.strip() for line in open(path,'r') if line.strip()]
# strip()取消换行符    for循环    for line in open(path,'r')打开文件只读模式每一行
    data=set(ips)
    data_dict={}
# 创建一个空集合
    for i in ips:
            # 用for循环定义一个变量在这个文件中
        if i in data_dict:
            # 判断他是否已经存在
            data_dict[i]+=1
            # 已存在的进行累加
        else:
            data_dict[i]=1
    print(data_dict)
    sorted_items=sorted(data_dict.items(),key=lambda x: x[0],reverse=False)

# data_dict.items()以元组的形式输出
    print(sorted_items)
path="attack.csv"
ips = [line.strip() for line in open(path, 'r') if line.strip()]
new(path)
