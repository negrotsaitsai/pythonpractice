score=90
name="蔡易熾"
count=1
#{n}:n(0~n)表示編號順序
print("{0}你的第{1}次物理成績是{2}".format(name,count,score))
print("{2}你的第{1}次物理成績是{0}".format(score,count,name))
#用參數
print("{z}你的第{x}次物理成績是{c}".format(z='蔡易熾',x=1,c=90))
