#!/usr/bin/python3

import threading
import time
import boto3

exitFlag = 0

client = boto3.client("sagemaker-runtime",region_name='us-west-2')
endpoint_name = "tensorflow-inference-2020-12-18-16-46-08-105"
# endpoint_name = "tensorflow-training-2020-12-16-16-03-23-077"

content_type="application/json"
accept="application/json"

# sayload='{"instances":[{"adid":["1"],"adv_id":["1"],"adx":["1"],"als_sim_sum":["1"],"campaignid":["1"],"campaignsetid":["1"],"category":["1"],"city":["1"],"click14":["1"],"click3":["1"],"click7":["1"],"connection_type":["1"],"country":["1"],"creative_clicks1":["1"],"creative_clicks3":["1"],"creative_clicks7":["1"],"creative_convs1":["1"],"creative_convs3":["1"],"creative_convs7":["1"],"creative_ctr1":["1"],"creative_ctr3":["1"],"creative_ctr7":["1"],"creative_cvr1":["1"],"creative_cvr3":["1"],"creative_cvr7":["1"],"creative_id":["1"],"creative_imps1":["1"],"creative_imps3":["1"],"creative_imps7":["1"],"creative_ivr1":["1"],"creative_ivr3":["1"],"creative_ivr7":["1"],"creative_update_days":["1"],"device_model_name":["1"],"device_type":["1"],"ds_publish_id":["1"],"hour":["1"],"impression14":["1"],"impression3":["1"],"impression7":["1"],"imptype":["1"],"install14":["1"],"install3":["1"],"install7":["1"],"install_bundle_category":["1"],"install_bundle_size":["1"],"language":["1"],"make":["1"],"os_ver_name":["1"],"pkg_adx_clicks1":["1"],"pkg_adx_clicks3":["1"],"pkg_adx_clicks7":["1"],"pkg_adx_convs1":["1"],"pkg_adx_convs3":["1"],"pkg_adx_convs7":["1"],"pkg_adx_ctr1":["1"],"pkg_adx_ctr3":["1"],"pkg_adx_ctr7":["1"],"pkg_adx_cvr1":["1"],"pkg_adx_cvr3":["1"],"pkg_adx_cvr7":["1"],"pkg_adx_imps1":["1"],"pkg_adx_imps3":["1"],"pkg_adx_imps7":["1"],"pkg_adx_ir1":["1"],"pkg_adx_ir3":["1"],"pkg_adx_ir7":["1"],"pkg_adx_ivr1":["1"],"pkg_adx_ivr3":["1"],"pkg_adx_ivr7":["1"],"pkg_all_rank":["1"],"pkg_category_rank":["1"],"pkg_dau":["1"],"pkg_download":["1"],"pkg_name":["1"],"pkg_pub_ir1":["1"],"pkg_pub_ir3":["1"],"pkg_pub_ir7":["1"],"pkg_score":["1"],"pkg_size":["1"],"pkg_sub_category_rank":["1"],"pkg_update_days":["1"],"pkg_user":["1"],"pub_bundleid":["1"],"pub_category":["1"],"pub_clicks1":["1"],"pub_clicks3":["1"],"pub_clicks7":["1"],"pub_convs1":["1"],"pub_convs3":["1"],"pub_convs7":["1"],"pub_ctr1":["1"],"pub_ctr3":["1"],"pub_ctr7":["1"],"pub_cvr1":["1"],"pub_cvr3":["1"],"pub_cvr7":["1"],"pub_imps1":["1"],"pub_imps3":["1"],"pub_imps7":["1"],"pub_ir1":["1"],"pub_ir3":["1"],"pub_ir7":["1"],"pub_ivr1":["1"],"pub_ivr3":["1"],"pub_ivr7":["1"],"request14":["1"],"request3":["1"],"request7":["1"],"tagid":["1"],"user_adx_click14":["1"],"user_adx_impression14":["1"],"user_adx_request14":["1"],"user_bundle_list":["1"],"user_same_bundle_count":["1"],"user_same_bundle_flag":["1"],"weekday":["1"]}]}'


start_str = '{"instances":['

payload='{"adid":["1"],"adv_id":["1"],"adx":["1"],"als_sim_sum":["1"],"campaignid":["1"],"campaignsetid":["1"],"category":["1"],"city":["1"],"click14":["1"],"click3":["1"],"click7":["1"],"connection_type":["1"],"country":["1"],"creative_clicks1":["1"],"creative_clicks3":["1"],"creative_clicks7":["1"],"creative_convs1":["1"],"creative_convs3":["1"],"creative_convs7":["1"],"creative_ctr1":["1"],"creative_ctr3":["1"],"creative_ctr7":["1"],"creative_cvr1":["1"],"creative_cvr3":["1"],"creative_cvr7":["1"],"creative_id":["1"],"creative_imps1":["1"],"creative_imps3":["1"],"creative_imps7":["1"],"creative_ivr1":["1"],"creative_ivr3":["1"],"creative_ivr7":["1"],"creative_update_days":["1"],"device_model_name":["1"],"device_type":["1"],"ds_publish_id":["1"],"hour":["1"],"impression14":["1"],"impression3":["1"],"impression7":["1"],"imptype":["1"],"install14":["1"],"install3":["1"],"install7":["1"],"install_bundle_category":["1"],"install_bundle_size":["1"],"language":["1"],"make":["1"],"os_ver_name":["1"],"pkg_adx_clicks1":["1"],"pkg_adx_clicks3":["1"],"pkg_adx_clicks7":["1"],"pkg_adx_convs1":["1"],"pkg_adx_convs3":["1"],"pkg_adx_convs7":["1"],"pkg_adx_ctr1":["1"],"pkg_adx_ctr3":["1"],"pkg_adx_ctr7":["1"],"pkg_adx_cvr1":["1"],"pkg_adx_cvr3":["1"],"pkg_adx_cvr7":["1"],"pkg_adx_imps1":["1"],"pkg_adx_imps3":["1"],"pkg_adx_imps7":["1"],"pkg_adx_ir1":["1"],"pkg_adx_ir3":["1"],"pkg_adx_ir7":["1"],"pkg_adx_ivr1":["1"],"pkg_adx_ivr3":["1"],"pkg_adx_ivr7":["1"],"pkg_all_rank":["1"],"pkg_category_rank":["1"],"pkg_dau":["1"],"pkg_download":["1"],"pkg_name":["1"],"pkg_pub_ir1":["1"],"pkg_pub_ir3":["1"],"pkg_pub_ir7":["1"],"pkg_score":["1"],"pkg_size":["1"],"pkg_sub_category_rank":["1"],"pkg_update_days":["1"],"pkg_user":["1"],"pub_bundleid":["1"],"pub_category":["1"],"pub_clicks1":["1"],"pub_clicks3":["1"],"pub_clicks7":["1"],"pub_convs1":["1"],"pub_convs3":["1"],"pub_convs7":["1"],"pub_ctr1":["1"],"pub_ctr3":["1"],"pub_ctr7":["1"],"pub_cvr1":["1"],"pub_cvr3":["1"],"pub_cvr7":["1"],"pub_imps1":["1"],"pub_imps3":["1"],"pub_imps7":["1"],"pub_ir1":["1"],"pub_ir3":["1"],"pub_ir7":["1"],"pub_ivr1":["1"],"pub_ivr3":["1"],"pub_ivr7":["1"],"request14":["1"],"request3":["1"],"request7":["1"],"tagid":["1"],"user_adx_click14":["1"],"user_adx_impression14":["1"],"user_adx_request14":["1"],"user_bundle_list":["1"],"user_same_bundle_count":["1"],"user_same_bundle_flag":["1"],"weekday":["1"]}'

end_str = ']}'


class myThread (threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        predict()
        print ("退出线程：" + self.name)

def predict():
        payloads =''
        size = 999
        for index in range(0,size):
            if index == 0:
                  payloads += payload;#最后一个不加逗号
            else:
                payloads += ','+payload;
        payloads = start_str+payloads+end_str
        # print(payloads)
        for index in range(0,500):
            start = time.time()
            response = client.invoke_endpoint(
                EndpointName=endpoint_name, 
                ContentType=content_type,
                Accept=accept,
                Body=payloads
                )
            # time.sleep(1)
            print(time.time()-start)
            # print(response['Body'].read().decode('utf-8') )

           
        
# 创建新线程

# for index in range(0,2):
#     s=bytes(index)
#     thread_name = 'thread'+s
#     thread_name= myThread(1, thread_name, 1)
#     thread_name.start()
#     thread_name.join()

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(3, "Thread-3", 3)
thread4 = myThread(4, "Thread-4", 4)
thread5 = myThread(5, "Thread-5", 5)
thread6 = myThread(6, "Thread-6", 6)
thread7 = myThread(7, "Thread-7", 7)
thread8 = myThread(8, "Thread-8", 8)
thread9 = myThread(9, "Thread-9", 9)
thread0 = myThread(0, "Thread-0", 0)

# 开启新线程
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread0.start()


thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.join()
thread8.join()
thread9.join()
thread0.join()

print ("退出主线程")