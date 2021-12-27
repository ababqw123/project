# station = "사당", "신도림", "인천공항"

# for(a=0,2,1)
# print(station[a] + " 행 열차가 들어오고 있습니다.")

# from math import *
# print(floor(4.99))
# print(ceil(3.1))

# from random import *

# print(int(random()*10))

# from random import *

# date = randint(4,28)

# print("오프라인 스터디 모임 날자는 매월 " + str(date) + "일로 선정되었습니다.")

# glga = "Python is Amazing"

# # print(glga)
# # print(glga.upper())
# # print(glga.lower())
# # print(len(glga))
# # print(glga.islower())
# # print(glga.replace("Python", "Java"))

# index = glga.index("n")
# print(index)

# print("나는 %d살입니다." % 10)
# print("나는 {}살입니다." .format(10))
# print("나는 {1}색과 {0}색을 좋아해요." .format("빨강","초록"))

# age = 20
# color = "빨강색"
# print(f"나는 {age}살이고, {color}색을 좋아합니다.")

# site = "http://naver.com"
# a = site.replace("http://","")
# b = a[:a.index(".")]
# c = b[:3]
# print(c + str(len(b)) + str(b.count("e")) + "!")

# subway = [10, 20, 30]

# print(subway[0])

# subway1 = ["재영", "성창", "성만"]

# subway1.append("주현")
# print(subway1)
# subway1.insert(1,"수현")
# print(subway1)
# subway1.pop()
# print(subway1)

# list = [3,2,6,1,7,4]
# list.sort()
# print(list)
# list.reverse()
# print(list)
# list.clear()
# print(list)

# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])
# print(cabinet.get(3))
# print(3 in cabinet)

# bag = {"a-100":"안재영", "b-20":"노성창"}
# bag["c-30"] = "김주현"

# print(bag.keys())
# print(bag.values())
# print(bag.items())

# my_set={1,2,3,3,3,}
# print(my_set)

# java = {"성창","주현","성만"}
# python = set(["재영","수현","성창"])

# print(java & python) #intersection
# print(java | python) #union
# print(java - python) # difference

# menu = {"커피", "우유", "쥬스"}

# print(menu,type(menu))
# menu = tuple(menu)
# print(menu,type(menu))
# menu = list(menu)
# print(menu,type(menu))
# menu = set(menu)
# print(menu,type(menu))

# from random import *

# lst = range(1,21)
# print(type(lst))
# lst = list(lst)
# print(type(lst))

# shuffle(lst)
# print(lst)
# win = sample(lst,4)
# print(win)

# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {}" .format(win[0]))
# print("커피 당첨자 : {}" .format(win[1:]))
# print("-- 축하합니다 --")

# weather = input("오늘 날씨는 어때요?")
# if weather == "비" :
#    print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크 챙기세요")
# else :
#     print("준비물 필요 없어요")

# for wait_no in range(1,5) :
#     print("대기번호 : {} " .format(wait_no))

# cos = ["재영", "성창", "성만", "주현"]
# for star in cos :
#     print("{}, 커피가 준비되었습니다." .format(star))

# cos = "재영"
# index = 5
# while index >= 1:
#     print("{}님, 커피가 준비되었습니다. {}번 남았습니다." .format(cos,index))
#     index -= 1
#     if index == 0 :
#         print("커피는 폐기처분 되었습니다.")
    