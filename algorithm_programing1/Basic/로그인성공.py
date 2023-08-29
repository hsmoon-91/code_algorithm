def solution(id_pw, db):
    answer = ''
    if id_pw[0] in db[0] and id_pw[0] in db[0]:
        answer = 'login'
    elif id_pw[0] in db[0] and id_pw[0] not in db[0]:
        answer = 'wrong pw'
    else : 
        answer = 'fail'
    return answer

# 딕셔너리사용 
def solution(id_pw, db):
    db_dict = {i[0]: i[1] for i in db}
    # id 가 있을 때
    if id_pw[0] in db_dict:
        if id_pw[1] == db_dict[id_pw[0]]:
            return "login"
        else:
            return "wrong pw"
    # id가 없을 때
    else:
        return "fail"