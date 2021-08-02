all_credit = int(input("이수학점을 말해봐:")) #163
score = float(input("졸업평점을 말해봐:")) #3.34

#print("이수학점:",all_credit,"\n졸업평점:",score)

add_credit = int(input("몇 학점 들을겨:"))
possible_score = float(input("예상 학기 평점은:"))
new_credit = all_credit+add_credit
new_score = (((all_credit*score)+add_credit*possible_score)/(all_credit+add_credit))

print("이수학점:",new_credit,"\n졸업평점:",round(new_score,3))

while 1:
    retaking = input("재수강 해볼텨? 0.아니 1.응")
    if retaking == '0':
        new_score = updated_score
        print("응 니 졸업평점",round(updated_score,3))
        break
    elif retaking == '1':
        re_credit = int(input("그 과목 몇 학점짜리임:"))
        last_score = float(input("기존점수 말해봐(ex-2.0):"))
        re_score = float(input("예상점수 말해봐(ex-4.0):"))
        updated_score = ((new_credit*new_score+re_score-last_score)/new_credit)
        print("응 니 졸업평점",round(updated_score,3))
        new_score = updated_score
    else:
        print('잘못눌렀어 임마')
        continue




# 이수학점을 말해봐:163
# 졸업평점을 말해봐:3.34
# 몇 학점 들을겨:15
# 예상 학기 평점은:4.5
# 이수학점: 178
# 졸업평점: 3.438
# 재수강 해볼텨? 0.아니 1.응1
# 그 과목 몇 학점짜리임:3
# 기존점수 말해봐(ex-2.0):2
# 예상점수 말해봐(ex-4.0):4
# 응 니 졸업평점 3.449
# 재수강 해볼텨? 0.아니 1.응1
# 그 과목 몇 학점짜리임:2
# 기존점수 말해봐(ex-2.0):0
# 예상점수 말해봐(ex-4.0):4
# 응 니 졸업평점 3.471
# 재수강 해볼텨? 0.아니 1.응0
# 응 니 졸업평점 3.471
