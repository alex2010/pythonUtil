import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os


def send_email(filepath):
    # 读取 Excel 文件
    df = pd.read_excel(filepath, sheet_name="email", header=0)

    # 设置邮件信息
    print(df.iloc[0])
    print(df.iloc[0]['Name'])
    subject = "主题图片"
    body = "{0}您好，您要的图片在附件里".format(df.iloc[0]['Name'])
    from_addr = "69692418@qq.com"
    password = "rock200*"
    smtp_server = "smtp.qq.com"
    smtp_port = 587
    to_addr = df.iloc[0]['Email']
    bless = df.iloc[0]['End']
    image_path = df.iloc[0]['Pic']

    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    # 添加邮件正文
    msg.attach(MIMEText(body, 'plain'))

    # 添加图片附件
    if os.path.isfile(image_path):
        with open(image_path, 'rb') as f:
            img_data = f.read()
        image = MIMEImage(img_data, name=os.path.basename(image_path))
        msg.attach(image)

    # 添加祝福语
    msg.attach(MIMEText(bless, 'plain'))

    # 发送邮件
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
        print("邮件发送成功！")
    except Exception as e:
        print("邮件发送失败：", e)


send_email("/Users/alexwang/Projects/pythonUtil/office/formula.xlsx")

# send_email("/Users/alexwang/Projects/pythonUtil/office/formula.xlsx", "smtp.qq.com", 465, "69692418@qq.com", "rock200*")
