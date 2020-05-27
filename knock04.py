word = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# 1文字取り出す単語
initials = [1, 5, 6, 7, 8, 9, 15, 16, 19]

# スペースで分ける
words = word.split()

# 元素記号
word = {}

for it, str in enumerate(words):
    if it + 1 in initials:
        # 先頭一文字だけ
        word[it+1] = str[0]
    else:
        # ２文字
        word[it+1] = str[:2]

print(word)
