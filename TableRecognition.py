import base64
import urllib
import requests
import json
import os
import sys
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

def main():
        
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/table?access_token=" + get_access_token()
    
    if len(sys.argv) > 1 and sys.argv[1]:
        image_path = sys.argv[1]
    else:
        image_path =input('请输入图片所在文件夹路径：')

    images = get_image(image_path)

    for image in images:
        if os.path.basename(image).split('.')[1] == "jpg" or os.path.basename(image).split('.')[1] == "png" or os.path.basename(image).split('.')[1] == "jpeg" or os.path.basename(image).split('.')[1] == "bmp":
            excel_path = os.path.join(image_path,os.path.basename(image).split('.')[0] + '.xlsx')
            image_content=get_file_content_as_base64(image,True)
            payload='image='+image_content+'&cell_contents=false&return_excel=true'
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json'
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            result = json.loads(response.text)
            decoded_data = base64.b64decode(result["excel_file"])
            # 将解码后的数据写入文件
            with open(excel_path, 'wb') as file:
                file.write(decoded_data)

def get_image(image_path):
    images=[]   #存储文件夹内所有文件的路径（包括子目录内的文件）
    for root, dirs, files in os.walk(image_path):
        path =[os.path.join(root, name) for name in files]
        images.extend(path)
    return images    

def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded 
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": config['DEFAULT'].get('BAIDU_API_KEY'), "client_secret": config['DEFAULT'].get('BAIDU_SECRET_KEY')}
    return str(requests.post(url, params=params).json().get("access_token"))

if __name__ == '__main__':
    main()
