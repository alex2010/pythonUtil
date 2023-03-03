import pandas as pd
import matplotlib.pyplot as plt


def generate_bar_chart_from_excel(filepath):
    try:
        # 从Excel文件中读取数据
        df = pd.read_excel(filepath, sheet_name='Data')

        # 按国家分组并计算总销售额
        sales_by_country = df.groupby('Country')['Sales'].sum()

        # 创建柱形图
        fig, ax = plt.subplots()
        ax.bar(sales_by_country.index, sales_by_country.values)

        # 设置图表标题和标签
        ax.set_title('Financial Data By Country')
        ax.set_xlabel('Country')
        ax.set_ylabel('Sales')

        # 显示图表
        plt.show()

        # 将图表保存为文件
        fig.savefig('Financial Data By Country.png')

    except Exception as e:
        print('Error: {}'.format(e))


def prompt():
    # 提示用户输入Excel文件路径
    excel_path = input("请输入Excel文件路径: ")
    # 调用send_email()函数发送电子邮件
    generate_bar_chart_from_excel(excel_path)


prompt()
