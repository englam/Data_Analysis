import pandas as pd
from pandas import ExcelWriter

'''
   pip install openpyxl
'''

Result = pd.read_csv('wireless_channel_result', names=['WiFi_Throughput', 'WiFi_Channel(Windows)', 'GUI_Channel', 'GUI_Mode','GUI_SSID', 'GUI_Region', 'WiFi_Mode_Manually', 'WiFi_Band', 'GUI_Security', 'WiFi_Security_Manually', 'Time'])

#print (Result.drop_duplicates().GUI_Mode.value_counts())
#print (Result.drop_duplicates().WiFi_Security_Manually.value_counts())
#print (Result.drop_duplicates().WiFi_Band.value_counts())

#Test_result = Result[(Result['WiFi_Band'] == '2.4G') & (Result['WiFi_Mode_Manually'] == 1) & (Result['WiFi_Security_Manually'] == 'No_Security')]
#print(Test_result)

def store_result_to_excel(Result,WiFi_Band,WiFi_Mode,WiFi_Security,GUI_Security):
    for i in WiFi_Mode:
        Test_result = Result[(Result['WiFi_Band'] == WiFi_Band) & (Result['WiFi_Mode_Manually'] == i) & (Result['WiFi_Security_Manually'] == WiFi_Security)& (Result['GUI_Security'] == GUI_Security)]
        sheet = str(i) + '_' + str(WiFi_Band) + '_' + str(WiFi_Security)
        Test_result.to_excel(writer, sheet)



WiFi_Mode_2g = ['1','2','3']
WiFi_Mode_5g = ['7','8','9']
WiFi_Security = ['No_Security', 'WPA2_AES','WPA_TKIP']

writer = ExcelWriter('Wireless_Report.xlsx')
store_result_to_excel(Result,'2.4G',WiFi_Mode_2g,'No_Security','no')
store_result_to_excel(Result,'2.4G',WiFi_Mode_2g,'WPA2_AES','wpa2aes')
store_result_to_excel(Result,'2.4G',WiFi_Mode_2g,'WPA2_AES','mixed')
store_result_to_excel(Result,'2.4G',WiFi_Mode_2g,'WPA_TKIP','mixed')
store_result_to_excel(Result,'5G',WiFi_Mode_5g,'No_Security','no')
store_result_to_excel(Result,'5G',WiFi_Mode_5g,'WPA2_AES','wpa2aes')
store_result_to_excel(Result,'5G',WiFi_Mode_5g,'WPA2_AES','mixed')
store_result_to_excel(Result,'5G',WiFi_Mode_5g,'WPA_TKIP','mixed')
writer.save()

"""
Result_no_security_2g_1 = Result[(Result['WiFi Band'] == '2.4G') & (Result['GUI Mode'] == 'Up to 54 Mbps')]
Result_no_security_2g_2 = Result[(Result['WiFi Band'] == '2.4G') & (Result['GUI Mode'] == 'Up to 347 Mbps')]
Result_no_security_2g_3 = Result2[(Result2['WiFi Band'] == '2.4G') & (Result['GUI Mode'] == 'Up to 800 Mbps')]

Result_no_security_5g_1 = Result3[(Result3['WiFi Band'] == '5G') & (Result3['GUI Mode'] == 'Up to 347 Mbps')& (Result3['WiFi Security'] == 'No_Security')]
Result_no_security_5g_2 = Result3[(Result3['WiFi Band'] == '5G') & (Result3['GUI Mode'] == 'Up to 800 Mbps')& (Result3['WiFi Security'] == 'No_Security')]
Result_no_security_5g_3 = Result3[(Result3['WiFi Band'] == '5G') & (Result3['GUI Mode'] == 'Up to 1733 Mbps')& (Result3['WiFi Security'] == 'No_Security')]

Result_aes_2g_1 = Result4[(Result4['WiFi Band'] == '2.4G') & (Result4['GUI Mode'] == 'Up to 54 Mbps')& (Result4['WiFi Security'] == 'WPA2_AES')]
Result_aes_2g_2 = Result4[(Result4['WiFi Band'] == '2.4G') & (Result4['GUI Mode'] == 'Up to 347 Mbps')& (Result4['WiFi Security'] == 'WPA2_AES')]
Result_aes_2g_3 = Result4[(Result4['WiFi Band'] == '2.4G') & (Result4['GUI Mode'] == 'Up to 800 Mbps')& (Result4['WiFi Security'] == 'WPA2_AES')]

Result_aes_5g_1 = Result3[(Result3['WiFi Band'] == '5G') & (Result3['GUI Mode'] == 'Up to 347 Mbps')& (Result3['WiFi Security'] == 'WPA2_AES')]
Result_aes_5g_2 = Result3[(Result3['WiFi Band'] == '5G') & (Result3['GUI Mode'] == 'Up to 800 Mbps')& (Result3['WiFi Security'] == 'WPA2_AES')]
Result_aes_5g_3 = Result3[(Result3['WiFi Band'] == '5G') & (Result3['GUI Mode'] == 'Up to 1733 Mbps')& (Result3['WiFi Security'] == 'WPA2_AES')]

Result_mix_aes_2g_1 = Result4[(Result4['WiFi Band'] == '2.4G') & (Result4['GUI Mode'] == 'Up to 54 Mbps')& (Result4['WiFi Security'] == 'WPA_AES')]
Result_mix_aes_2g_2 = Result4[(Result4['WiFi Band'] == '2.4G') & (Result4['GUI Mode'] == 'Up to 347 Mbps')& (Result4['WiFi Security'] == 'WPA_AES')]
Result_mix_aes_2g_3 = Result4[(Result4['WiFi Band'] == '2.4G') & (Result4['GUI Mode'] == 'Up to 800 Mbps')& (Result4['WiFi Security'] == 'WPA_AES')]

Result_mix_aes_5g_1 = Result3[(Result3['WiFi Band'] == '5G') & (Result3['GUI Mode'] == 'Up to 347 Mbps')& (Result3['WiFi Security'] == 'WPA_AES')]
Result_mix_aes_5g_2 = Result3[(Result3['WiFi Band'] == '5G') & (Result3['GUI Mode'] == 'Up to 800 Mbps')& (Result3['WiFi Security'] == 'WPA_AES')]
Result_mix_aes_5g_3 = Result3[(Result3['WiFi Band'] == '5G') & (Result3['GUI Mode'] == 'Up to 1733 Mbps')& (Result3['WiFi Security'] == 'WPA_AES')]

Result_mix_tkip_2g_1 = Result4[(Result4['WiFi Band'] == '2.4G') & (Result4['GUI Mode'] == 'Up to 54 Mbps')& (Result4['WiFi Security'] == 'WPA_TKIP')]
Result_mix_tkip_2g_2 = Result4[(Result4['WiFi Band'] == '2.4G') & (Result4['GUI Mode'] == 'Up to 347 Mbps')& (Result4['WiFi Security'] == 'WPA_TKIP')]
Result_mix_tkip_2g_3 = Result4[(Result4['WiFi Band'] == '2.4G') & (Result4['GUI Mode'] == 'Up to 800 Mbps')& (Result4['WiFi Security'] == 'WPA_TKIP')]

Result_mix_tkip_5g_1 = Result3[(Result3['WiFi Band'] == '5G') & (Result3['GUI Mode'] == 'Up to 347 Mbps')& (Result3['WiFi Security'] == 'WPA_TKIP')]
Result_mix_tkip_5g_2 = Result3[(Result3['WiFi Band'] == '5G') & (Result3['GUI Mode'] == 'Up to 800 Mbps')& (Result3['WiFi Security'] == 'WPA_TKIP')]
Result_mix_tkip_5g_3 = Result3[(Result3['WiFi Band'] == '5G') & (Result3['GUI Mode'] == 'Up to 1733 Mbps')& (Result3['WiFi Security'] == 'WPA_TKIP')]





writer = ExcelWriter('Wireless_Report.xlsx')
Result_no_security_2g_1.to_excel(writer,'WiFi_2.4G_NoSecurity_1')
Result_no_security_2g_2.to_excel(writer,'WiFi_2.4G_NoSecurity_2')
Result_no_security_2g_3.to_excel(writer,'WiFi_2.4G_NoSecurity_3')
Result_no_security_5g_1.to_excel(writer,'WiFi_5G_NoSecurity_1')
Result_no_security_5g_2.to_excel(writer,'WiFi_5G_NoSecurity_2')
Result_no_security_5g_3.to_excel(writer,'WiFi_5G_NoSecurity_3')
Result_aes_2g_1.to_excel(writer,'WiFi_2.4G_AES_1')
Result_aes_2g_2.to_excel(writer,'WiFi_2.4G_AES_2')
Result_aes_2g_3.to_excel(writer,'WiFi_2.4G_AES_3')
Result_aes_5g_1.to_excel(writer,'WiFi_5G_AES_1')
Result_aes_5g_1.to_excel(writer,'WiFi_5G_AES_2')
Result_aes_5g_1.to_excel(writer,'WiFi_5G_AES_3')
Result_mix_aes_2g_1.to_excel(writer,'WiFi_2.4G_Mixed_AES_1')
Result_mix_aes_2g_2.to_excel(writer,'WiFi_2.4G_Mixed_AES_2')
Result_mix_aes_2g_3.to_excel(writer,'WiFi_2.4G_Mixed_AES_3')
Result_mix_aes_5g_1.to_excel(writer,'WiFi_5G_Mixed_AES_1')
Result_mix_aes_5g_2.to_excel(writer,'WiFi_5G_Mixed_AES_2')
Result_mix_aes_5g_3.to_excel(writer,'WiFi_5G_Mixed_AES_3')
Result_mix_tkip_2g_1.to_excel(writer,'WiFi_2.4G_Mixed_TKIP_1')
Result_mix_tkip_2g_2.to_excel(writer,'WiFi_2.4G_Mixed_TKIP_2')
Result_mix_tkip_2g_3.to_excel(writer,'WiFi_2.4G_Mixed_TKIP_3')
Result_mix_tkip_5g_1.to_excel(writer,'WiFi_5G_Mixed_TKIP_1')
Result_mix_tkip_5g_2.to_excel(writer,'WiFi_5G_Mixed_TKIP_2')
Result_mix_tkip_5g_3.to_excel(writer,'WiFi_5G_Mixed_TKIP_3')

writer.save()










#print (Result[(Result['WiFi Band'] == '2.4G')])
#print (Result[(Result['WiFi Band'] == '2.4G') & (Result['GUI Mode'] == 'Up to 54 Mbps')])




# save to xlsx and sheet
#writer = ExcelWriter('Wireless_Report.xlsx')
#test.to_excel(writer,'WiFi_2.4G_NoSecurity')
#writer.save()

# save to xlsx and sheet
#writer = ExcelWriter('PythonExport.xlsx')
#Result.to_excel(writer,'Sheet5')
#writer.save()

# DF TO CSV
#Result.to_csv('PythonExport.csv', sep=',')

#Result.to_csv('out.csv', sep=',')

"""
