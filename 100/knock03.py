str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics'
str = str.replace('.','') #ピリオドなくした
str = str.replace(',','') #コンマなくした
str = str.split() #split 分割

list = []

for word in str: #for 変数 in オブジェクト: 実行する処理 以上がpyhon for文の書き方です。pythonのfor文では、変数の後ろに「in」が付くことと、オブジェクトの後ろに「:」が付くことに注意しましょう。
    list.append(len(word))
print(list)
#len長さ取得 append末尾に要素を追加
