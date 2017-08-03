import pandas as pd
from pandas import ExcelWriter

'''
   pip install openpyxl,
'''

Result = pd.read_csv('wireless_channel_result1', names=['WiFi Throughput', 'WiFi Channel', 'GUI Channel', 'GUI Mode', 'WiFi Band', 'GUI_Security', 'WiFi Security', 'Time'])
Result2 = pd.read_csv('wireless_channel_result2', names=['WiFi Throughput', 'WiFi Channel', 'GUI Channel', 'GUI Mode','WiFi Band', 'GUI_Security', 'WiFi Security', 'Time'])
Result3 = pd.read_csv('wireless_channel_result3', names=['WiFi Throughput', 'WiFi Channel', 'GUI Channel', 'GUI Mode','Configured Mode','WiFi Band', 'GUI_Security', 'WiFi Security', 'Time'])
Result4 = pd.read_csv('wireless_channel_result4', names=['WiFi Throughput', 'WiFi Channel', 'GUI Channel', 'GUI Mode','WiFi Band', 'GUI_Security', 'WiFi Security', 'Time'])



Result_no_security_2g_1 = Result[(Result['WiFi Band'] == '2.4G') & (Result['GUI Mode'] == 'Up to 54 Mbps')]
Result_no_security_2g_2 = Result2[(Result2['WiFi Band'] == '2.4G') & (Result2['GUI Mode'] == 'Up to 347 Mbps')]
Result_no_security_2g_3 = Result2[(Result2['WiFi Band'] == '2.4G') & (Result2['GUI Mode'] == 'Up to 800 Mbps')]

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


