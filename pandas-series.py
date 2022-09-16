# 載入 pandas 模組
import pandas as pd
# 資料索引
# data=pd.Series([5, 4, -2, 3, 7], index=["a", "b", "c", "d", "e"])
# print(data)
# 觀察資料
# print("資料型態", data.dtype)
# print("資料數量", data.size)
# print("資料索引", data.index)
# 取得資料：根據順序、根據索引
# print(data[2], data[0])
# print(data["e"], data["d"])
# data=pd.Series([5, 4, -2, 3, 7], index=["a", "b", "c", "d", "e"])
# 數字運算
# print("最大值",data.max())
# print("總和",data.sum())
# print("標準差",data.std())
# print("中位數",data.median())
# print("最大的三個數",data.nlargest(3))
data=pd.Series(["您好", "Python", "Pandas"])
# 字串運算
# print(data.str.lower())
# print(data.str.len())
# print(data.str.cat(sep="-")) # 把字串串起來，可以自訂串接符號
# print(data.str.contains("好")) # 判斷每個字串是否包含特定的字元
print(data.str.replace("您好", "Hello"))
