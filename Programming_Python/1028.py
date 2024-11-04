# 讀取使用者輸入
gender = input("請輸入性別（男/女）: ")
body_fat = float(input("請輸入體脂率（%）: ")) # 轉換為浮點數

if gender == '男':
    if body_fat < 2:
        body_type = "無法分類" # 0%-1% 未定義
    elif body_fat <= 5:
        body_type = "基礎脂肪"
    elif body_fat <= 13:
        body_type = "運動員"
    elif body_fat <= 17:
        body_type = "健康"
    elif body_fat <= 24:
        body_type = "正常"
    elif body_fat <= 100:
        body_type = "肥胖"
    else:
        body_type = "無法分類" # 超過100%
elif gender == '女':
    if body_fat < 10:
        body_type = "無法分類" # 0%-9% 未定義
    elif body_fat <= 13:
        body_type = "基礎脂肪"
    elif 14 <= body_fat <= 20:
        body_type = "運動員"
    elif 21 <= body_fat <= 24:
        body_type = "健康"
    elif 25 <= body_fat <= 31:
        body_type = "正常"
    elif body_fat <= 100:
        body_type = "肥胖"
    else:
        body_type = "無法分類" # 超過100%


# 判斷體型
print(f"您的體型分類為: {body_type}")

# 建立個人健康檔案
with open("個人健康檔案.txt", "a", encoding='utf-8') as file:
    file.write(f"性別: {gender}, 體脂率: {body_fat}%, 體型分類: {body_type}\n")
    
# 顯示存檔訊息
print("您的健康檔案已保存至 \'個人健康檔案.txt\'")

