# 原始列表，包含重复项  
items = ['水墨', '白描', '重彩-金碧', '重彩', '淡彩', '淡彩-螺青', '设色、描金', '重彩-青绿', '设色', '吴妆', '浅设色', '淡彩-浅绛']  
  
# 使用集合（set）去除重复项，然后再转回列表（list）  
unique_items = list(set(items))  
  
# 构造所需的数组形式，每个项都是一个字典，包含value和label属性  
formatted_array = [{'value': item, 'label': item} for item in unique_items]  
  
# 打印结果  
print(formatted_array)
unique_values = set(item['value'] for item in formatted_array)  
if len(formatted_array) == len(unique_values):  
    print("没有重复项")  
else:  
    print("存在重复项")