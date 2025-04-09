print("Hello There!")
print("This is a code to get to know more about you")
print("--------------------")

#name　名前
name = input(str("What is your name? "))
print("Hi",name,"nice to meet you.")
print("--------------------")

#age　年齢ですか。
age = input(str("How old are you? "))
print("You are",age,"year(s) old!")
print

#food　好きな食べ物
food = input(str("What is your favourite food? "))
print("Oh!",food,"?! That's my favourite too!")

#hobby
hobby = input(str("What is your hobby? "))
print("Oh!",hobby,"?! That's my hobby too!")

#from?どこ？
place = input(str("Where are you from? "))
print("Wow!",place,"I'm from there too!")

#日本語わかりましたか
japanese = input(str("日本語はわかりましたか。")).lower()
if japanese == "yes":
  print("うわーすごいね！")
elif japanese == "no":
  print("あ、だいじょぶです！")