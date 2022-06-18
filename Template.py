from re import L
import get_xy

def main_menu():
    MAIN = """
------------------------------------------
1. 장소 추천
2. 장소 선택, 리뷰 등록
3. 장소 검색
4. 종료
------------------------------------------
"""
    print(MAIN)
    n = 0
    try:
        n = int(input(': '))
    except:
        pass
    return n

# 유사도 #별점 #거리
def place_list_cui(recommand_list, other_list):
    if recommand_list:
        print('------------------[추천]------------------')
        for recommand in recommand_list:
            # print(recommand[1], end='')
            # blank = ' ' * (30 - len(recommand[1].encode('cp949')))
            # print(blank, end='')
            # print(f'{round(recommand[0] * 100, 3)} %')
            print('<' + recommand[0] + '>')
            print(f'{int(recommand[1])} m', end=' / ')
            print(f'{round(recommand[2], 1)} 점', end=' / ')
            print(f'{round(recommand[3] * 100, 3)} %')
            print()
        print('------------------------------------------')
    for other in other_list:
        # print(other[1], end='')
        # blank = ' ' * (30 - len(other[1].encode('cp949')))
        # print(blank, end='')
        # print(f'{int(other[0])} m')
        # print(f'{int(other[0])} 점')
        print('<' + other[0] + '>')
        print(f'{int(other[1])} m', end=' / ')
        print(f'{round(other[2], 1)} 점', end=' / ')
        print(f'{round(other[3] * 100, 3)} %')
        print()
    print('------------------------------------------')
    print('0. 나가기')
    
    n = 0
    while True:
        try:
            n = int(input(': '))
        except:
            pass
        if n == 0:
            break
    
    return True


def place_select_cui(place_list):
    place_dic = {i + 1 : place for i, place in enumerate(place_list)}
    print('------------------[장소]------------------')
    for key in place_dic:
        print(key, place_dic[key])
    print('------------------------------------------')
    # print('0. 나가기')
    
    n = 0
    while True:
        try:
            n = int(input('장소를 선택하세요: '))
        except:
            pass
        
        if n not in range(1, len(place_dic) + 1):
            continue
        
        break
        
    return place_dic[n]

def place_add_cui():
    print('----------------[장소 검색]----------------')
    search_word = input(': ')
    print('----------------[검색 결과]----------------')
    json_file = get_xy.get_coord_by_query(search_word)
    for place_info in json_file['documents']:
        print(place_info['place_name'])
        print(f"위도: {place_info['x']}")
        print(f"경도: {place_info['y']}")
        print()
    print('------------------------------------------')
    print('0. 나가기')
    n = 0
    while True:
        try:
            n = int(input(': '))
        except:
            pass
        if n == 0:
            break
    
    return True

def get_show_type_cui():
    print('------------------------------------------')
    print('1. 거리순')
    print('2. 별점순')
    n = 0
    while True:
        try:
            n = int(input(': '))
        except:
            pass
        
        if n not in [1, 2]:
            continue
        
        break
    
    return n