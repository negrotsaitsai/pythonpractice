<迴圈搭配的指令：break 和 continue>
# 一定要寫在迴圈內
<強制結束迴圈 - break>
while 布林值:
  break
for 變數名稱 in 列表或字串:
  break

<程式範例 - break>
n = 1
while n < 5:
  if n == 3:
    break  # 程咬金
  n+=1
print(n) # 印出3

<強制繼續下一圈 - continue>
while 布林值:
  continue
for 變數名稱 in 列表或字串:
  continue

<程式範例 - continue>
n = 0
for x in [0,1,2,3]:
  if x % 2 == 0:
    continue
  n+=1
print(n)  # 印出2

<基本語法 - while, else>
while 布林值:
  若布林值為True，執行命令
  回到上方，做下一次的迴圈判斷
else:
  回圈結束前，執行此區的命令

<程式範例 - while, else> 
n = 1;
while n < 5:
  print("變數n的資料是:", n)
  n+=1
else:
  print(n) # 結束迴圈前，印出5
>>> 變數n的資料是: 1
>>> 變數n的資料是: 2
>>> 變數n的資料是: 3
>>> 變數n的資料是: 4
>>> 5

<基本語法 - for, else>
for 變數名稱 in 列表或字串:
  將列表中的項目或字串中的字元
  逐一取出、逐一處理
else:
  回圈結束前，執行此區的命令

<程式範例 - for, else>
for c in "Hello":
  print("逐一取得字串中的字元", c)
else:
  print(c) # 結束迴圈前，印出c
>>> 逐一取得字串中的字元 H
>>> 逐一取得字串中的字元 e
>>> 逐一取得字串中的字元 l
>>> 逐一取得字串中的字元 l
>>> 逐一取得字串中的字元 o
>>> o

# break
n = 0 
while n < 5:
  if n == 3:
    break
  print(n) # 印出迴圈中的n
  n+=1
print("最後的n: ", n) # 印出迴圈結束後的n
>>> 0
>>> 1
>>> 2
>>> 最後的n: 3

# continue
n = 0
for x in [0,1,2,3]:
  if x % 2 == 0:     # x是偶數
    continue
  print(x)
  n+=1
print("最後的n: ", n)
>>> 1
>>> 3
>>> 最後的n: 2
# 遇到0,2會被跳過不印，continue執行下一個

# else
sum = 0
for n in range(11):
  sum += n
else: 
  print(sum)  # 印出1+2+3+...+10的結果
>>> 55

# 綜合範例: 找出整數平方根
# 輸入9,得到3
# 輸入11,得到【沒有】整數的平方根
n = input("輸入一個正整數： ")
n = int(n)           # 轉換輸入值為數字
for i in range(n):   # i 從 0 ~ n-1
  if i * i == n:
    print("整數平方根", i))
    break     # 用break強制結束回圈時，不會執行else區塊
  else:
    print("沒有整數平方根")
>>> 輸入一個正整數： 25
>>> 整數平方根 5
>>> 輸入一個正整數：11
>>> 沒有整數平方根