# 載入 pandas 模組
import pandas as pd
# 資料索引：pd.DataFrame(字典, index=索引列表)
data=pd.DataFrame({
    "name":["Amy", "John", "Bob"],
    "salary":[30000, 50000, 40000],
}, index=["a", "b", "c"])
print(data)
print("=========")
# 觀察資料
# print("資料數量", data.size)
# print("資料形狀", data.shape)
# print("資料索引", data.index)
# 取得列 (Row/橫向) 的 Series 資料：根據順序、根據索引
# print("取得第二列", data.iloc[1], sep="\n")
# print("==================================")
# print("取得第 c 列", data.loc["c"], sep="\n")
# 取得欄 (Column/直向) 的 Series 資料：根據欄位的名稱
# print("取得 name 欄位", data["name"], sep="\n")
# names=data["name"] # 取得單維度的 Series 資料
# print("把name 全部轉大寫", names.str.upper(), sep="\n")
# # 計算薪水的平均值
# salaries=data["salary"]
# print("薪水的平均值", salaries.mean())
# 建立新的欄位
data["revenue"]=[50000, 40000, 30000] # data[新欄位的名稱]=列表
data["rank"]=pd.Series([3, 6, 1], index=["a", "b", "c"]) # data[新欄位的名稱]=Series 的資料
data["cp"]=data["revenue"]/data["salary"]
print(data)