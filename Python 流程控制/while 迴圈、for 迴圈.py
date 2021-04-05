<while基本語法>
while 布林值：
  若布林值為True, 執行命令
  回到上方,做下一次的回圈判斷
  # 直到布林值為false才會離開迴圈
<程式範例>
n = 1
while n < 5:
  print("變數n的資料是：", n)
  n+=1  
<for基本語法>
for 變數名稱 in 列表或字串：
  將列表中的項目或字串中的字元
  逐一取出、逐一處理
<程式範例-列表>
for x in [4,1,2]:
  print("逐一取得列表中的資料", x)
<程式範例-字串>
for c in "Hello":
  print("逐一取得字串中的字元", c)  
<使用range()-1> 
# 製造出連續數字的列表
for 變數名稱 in range(3):
相當於
for 變數名稱 in [0,1,2]:
<使用range()-2>
# 包含開頭不包含結束
for 變數名稱 in range(3,6): 
相當於
for 變數名稱 in [3,4,5]: 

# while迴圈
<01>
# 這個不要執行，是無限迴圈，電腦會當機=..=
n = 1
while True: 
  print(n)
  n+=1      
<02>
n = 1
while n<=3:
  print(n)
  n+=1
>>> 1
>>> 2
>>> 3
<03> # 1+2+3+...+10
n = 1
sum = 0
while n <= 10:
  sum = sum + n
  n+=1
print(sum)

# for迴圈
<01>
for x in [3,5,1]:
  print(x)
>>> 3
>>> 5
>>> 1
<02>
for x in "Hello":
  print(x)
>>> H
>>> e
>>> l
>>> l
>>> o
<03>
for x in range(5):
  print(x)
>>> 0
>>> 1
>>> 2
>>> 3
>>> 4
<04>
for x in range(5,10):
  print(x)
>>> 5
>>> 6
>>> 7
>>> 8
>>> 9  
<05> # 1+2+3...+10
for x in range(1,11):
  sum = sum + x 
print(sum)