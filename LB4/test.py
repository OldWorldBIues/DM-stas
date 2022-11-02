import sqlite3
import numpy as np

conn = sqlite3.connect("D:\DM-stas\LB4\districts.db")

cur = conn.cursor()

disctricts_list = cur.execute("SELECT DISTINCT district FROM street_result").fetchall()
for i in range(len(disctricts_list)):
    values = disctricts_list[i]
    district = values[0]   
    
    jornal_test_list = cur.execute("SELECT * from street_result WHERE district = ?", (district,)).fetchall()    
    jornal_test_arr = np.array(jornal_test_list)
    
    if(len(jornal_test_arr) == 0):
        continue
        
    x_result = np.delete(jornal_test_arr, [0,9,10], axis=1)
    
    length = x_result.shape
    columns_count = length[1]
    
    for j in range(0, length[1]):
        test_result = x_result[:,j].astype(float)

    try:
        result_dict = {
    "кількість спостережень"   : len(test_result),
    "кількість пустих значень" : len(test_result) - np.count_nonzero(test_result),
    "середній бал"             : round(np.mean(test_result),1),
    "максимальний бал"         : np.max(test_result),
    "мінімальний бал"          : np.min(test_result[np.nonzero(test_result)]) ,
    "стандартне відхилення"    : round(np.std(test_result),1),
    "розмах вариації"          : np.max(test_result) - np.min(test_result[np.nonzero(test_result)]) 
    }
    except ValueError: "Empty"
    pass
    

    
    
    columns_names = cur.execute("PRAGMA table_info('street_flat_propery')").fetchall()
    print("Назва району: " + district)
    print("Назва поля: " + columns_names[j][1])
    
    print(
"""
=======================================
№  : ПОКАЗЧИК               : ЗНАЧЕННЯ     
=======================================
"""      
      )

    i = 1
    for key, value in result_dict.items():
        print (f'{i:<3} {key:<25}  {value}')
        i += 1
    print('\n')
    

    
    


    
