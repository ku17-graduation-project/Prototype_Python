from User import User
from Place import Place
import sys, Template
import Const
from collections import defaultdict

def init_users():
    # 유저 생성 및 설정
    users = []

    user_key_like = defaultdict(int)
    user_key_like['공부'] += 5
    user_key_like['24시'] += 5
    user_loc = [37.54027736489841, 127.07432285195323]
    user1 = User('konkuk', user_key_like, user_loc)
    users.append(user1)
    
    return users


def init_places():
    # 장소 생성 및 설정, 장소 불러오는 api 사용하여 프로토타입 난이도 올리자!
    # 위도, 경도 https://tablog.neocities.org/keywordposition.html
    
    user_key_like = defaultdict(int)
    user_loc = [37.54027736489841, 127.07432285195323]
    user1 = User('konkuk1', user_key_like, user_loc)
    user2 = User('konkuk2', user_key_like, user_loc)
    user3 = User('konkuk3', user_key_like, user_loc)
    user4 = User('konkuk4', user_key_like, user_loc)
    user5 = User('konkuk5', user_key_like, user_loc)
    
    # PLACES_KEYWORDS = {'교내': ['지름길', '자판기'], '카페': ['맛집', '학생할인'], 
    # '식당': ['맛집', '점심', '해장', '저녁'], '공통': ['공부', '콘센트많음', '공강', '만쥬', '건덕', '24시', '팀플', '무료']}

    places = []
    place1 = Place('동생대 K-CUBE', ['교내'], (37.54027736489841, 127.07432285195323))
    place1.create_review(user1, ['공부', '팀플', '무료'], 5)
    place1.create_review(user2, ['공부', '팀플', '무료', '콘센트많음'], 4)
    place1.create_review(user3, ['공부', '팀플', '무료', '자판기'], 3)
    # place.create_review(user, keywords_str, stars)


    places.append(place1)
    place2 = Place('황소상', ['교내'], (37.543132363665535, 127.07615879242665))
    place2.create_review(user1, ['지름길'], 2)
    place2.create_review(user2, ['24시', '지름길', '무료'], 4)
    place2.create_review(user3, ['지름길', '만쥬'], 5)
    places.append(place2)
    
    place3 = Place('기숙사 할리스', ['카페'], (37.53923142850558, 127.0755466497599))
    place3.create_review(user1, ['맛집', '학생할인', '24시'], 5)
    place3.create_review(user2, ['맛집', '학생할인', '공강'], 4)
    place3.create_review(user3, ['24시', '팀플'], 5)
    places.append(place3)
    
    place4 = Place('일감호', ['교내'], (37.54085273416675, 127.07631488542982))
    place4.create_review(user1, ['지름길'], 1)
    place4.create_review(user2, ['지름길', '건덕'], 4)
    place4.create_review(user3, ['24시', '팀플'], 5)
    places.append(place4)
    
    place5 = Place('학생회관 식당', ['교내', '식당'], (37.54198237505499, 127.07801898911505))
    place5.create_review(user1, ['점심','저녁'], 2)
    place5.create_review(user2, ['공강'], 3)
    place5.create_review(user3, ['점심','공강','저녁'], 2)
    places.append(place5)
    
    place6 = Place('가츠시', ['식당'], (37.54636274700634, 127.07568963740945))
    place6.create_review(user1, ['공강','맛집','저녁'], 4)
    place6.create_review(user2, ['점심','맛집'], 3)
    place6.create_review(user3, ['점심','저녁'], 5)
    places.append(place6)
    
    place7 = Place('도서관 6층 K-CUBE', ['교내'], (37.542217015745166, 127.07392591185358))
    place7.create_review(user1, ['공부', '팀플', '무료'], 5)
    place7.create_review(user2, ['공부', '팀플', '무료', '콘센트많음'], 4)
    place7.create_review(user3, ['공부', '팀플', '무료', '자판기'], 3)
    places.append(place7)
    
    place8 = Place('공학관 1층 K-CUBE', ['교내'], (37.541641714457114, 127.07882201660733))
    place8.create_review(user1, ['공부', '팀플', '무료'], 5)
    place8.create_review(user2, ['공부', '팀플', '무료', '콘센트많음'], 4)
    place8.create_review(user3, ['공부', '팀플', '무료', '자판기'], 3)
    places.append(place8)
    
    place9 = Place('와우도', ['교내'], (37.54007545027526, 127.07657999593698))
    places.append(place9)
    
    
    place10 = Place('새천년관 4층 실습실', ['교내'], (37.543656334117365, 127.07748324485432))
    place10.create_review(user1, ['공부', '팀플', '24시'], 5)
    place10.create_review(user2, ['공부', '팀플', '공강', '무료'], 5)
    place10.create_review(user3, ['공부', '팀플', '무료','자판기'], 4)
    places.append(place10)

    place11 = Place('산학관 카페', ['교내', '카페'], (37.540034819355874, 127.07316282334232))
    place11.create_review(user1, ['맛집', '학생할인'], 5)
    place11.create_review(user2, ['맛집', '학생할인', '공강'], 4)
    place11.create_review(user3, ['콘센트많음', '학생할인'], 5)
    places.append(place11)

    place12 = Place('개미집', ['식당'], (37.545781282915016, 127.07618694787281))
    place12.create_review(user1, ['점심', '맛집'], 5)
    place12.create_review(user2, ['저녁', '해장', '점심'], 3)
    place12.create_review(user3, ['해장', '저녁'], 5)
    places.append(place12)
    
    return places


def scenario_recommand(user : User, places):
    # 유저 선택(거리, 좋아요)에 따른 추천 장소 리스트 구성    
    show_type = {1: '거리순', 2: '별점순'}
    type_flag = Template.get_show_type_cui()
    
    show_list, other_list = user.get_places_similar_list(places), []
    if show_type[type_flag] == '별점순':
        other_list = Place.get_places_by_star(user, places)
    else:
        other_list = Place.get_places_by_distance(user, places)

    other_show = []
    for other in other_list:
        if other[1] not in [show[1] for show in show_list]:
            other_show.append(other)

    return [show_list, other_show]


def scenario_review(user: User, place: Place):
    # 장소 선택된 상태
    # 키워드 최소 1개 선택 받기
    # 인풋에 대한 예외처리 엄청 많이 해야됨!!!! 잘 입력하도록ㅁ
    code_dict = {i + 1 : v for i, v in enumerate(place.keywords.keys())}
    print(f'[장소 리뷰] {place.name}')
    print('[키워드]')
    for key in code_dict:
        print(key, code_dict[key])
    keywords_code = list(map(int, input(': ').split())) # 숫자로 메뉴 입력받기, ex) [0, 1]
    stars = int(input('[별점] : '))
    keywords_str = [code_dict[k] for k in keywords_code]
    place.create_review(user, keywords_str, stars)


if __name__ == '__main__':
    
    # 초기화
    users = init_users()
    places = init_places()

    # 로그인
    curr_user = users[0]
    
    # 메인 메뉴 선택 화면
    while True:
        flag = Template.main_menu()
        print()
        if flag == 1: # 1. 장소 추천 리스트
            Template.place_list_cui(*scenario_recommand(curr_user, places))
        elif flag == 2: # 장소 선택 & 리뷰 등록
            selected_place = Template.place_select_cui(places)
            scenario_review(curr_user, selected_place)
        elif flag == 3: # 장소 검색
            Template.place_add_cui()
        else: # 나가기
            break
        
        print()
        
        
"""
   공부  24시  지름길  팀플  콘센트많음  맛집  점심  해장  저녁  학생할인  공강  만쥬  건덕
0   5    5    0   0      0   0   0   0   0     0   0   0   0
0   0    0    0   0      0   0   0   0   0     0   0   0   0
0   0    0    0   0      0   0   0   0   0     0   0   0   0
0   0    0    0   0      0   0   0   0   0     0   0   0   0
0   0    0    0   0      0   0   0   0   0     0   0   0   0
0   0    0    0   0      0   0   0   0   0     0   0   0   0
0   0    0    0   0      0   0   0   0   0     0   0   0   0
0   0    0    0   0      0   0   0   0   0     0   0   0   0
0   0    0    0   0      0   0   0   0   0     0   0   0   0
0   0    0    0   0      0   0   0   0   0     0   0   0   0
0   0    0    0   0      0   0   0   0   0     0   0   0   0
0   0    0    0   0      0   0   0   0   0     0   0   0   0
0   0    0    0   0      0   0   0   0   0     0   0   0   0

"""

# 1. 중복
# 2. 리뷰 점수 반영 확인
# 3. 거리순, 추천순 
"""
---------[추천]---------
동생대 K-CUBE
황소상
기숙사 할리스
일감호
학생회관 식당
가츠시
도서관 6층 K-CUBE
공학관 1층 K-CUBE
와우도
새천년관 4층 실습실
산학관 카페
개미집
------------------------
(13182654.947267085, '가츠시')
(13182706.50456284, '도서관 6층 K-CUBE')
(13182721.815436529, '개미집')
(13182746.865879929, '산학관 카페')
(13182828.493342495, '동생대 K-CUBE')
(13182842.757178169, '황소상')
(13182924.45492924, '새천년관 4층 실습실')
(13182961.274784895, '일감호')
(13182975.145160044, '기숙사 할리스')
(13183018.6545456, '와우도')
(13183045.213462025, '학생회관 식당')
(13183125.367553785, '공학관 1층 K-CUBE')
------------------------
"""


'''

사용자가 어떤 장소에 리뷰를 남겼을 때 사용자가 남긴 리뷰를 모아 분석
사용자 장소 비슷 추천 테이블
사용자 가본 장소들에 대해 가중치 -> 

맛집 -> 공부 : 
맛집 리뷰 등록 -> 유사한 것들 추천 리스트에 추가
공부하는 곳을 리뷰 등록 -> 비슷한 것들 추천 리스트에 추가

맛집 X

맛집, 공부 -> 0.6

장소에 대한 키워드 점수 
=>
추천 리스트에 맛집?

추천 리스트에 넣고
sorted 등록 


맛집, 공부가 모두 동등하게 추천 리스트에 올라간다

1. 장소의 키워드들로 아이템들간 유사도 테이블 구하기 -> 추출, 
장소 1에 장소 2, 3, 4, 5.. 

(장소 1과 장소n의 겹치는 키워드)/(장소1 키워드 개수)

평점 유사도

키워드를 가진 장소 유사도 모두 구해서 각각
별점 유사도, 공부 유사도 테이블, 맛집 유사도 테이블

사용자 공부, 콘센트


문서 dog 1
문서 dog 100


10 0 0 0
10000 10000 10000 10000
500 20 39 10


사용자 공부 10 ...
장소1  공부 10000
장소2  공부 500
장소3  공부 7000

place1 = np.array([5000,4000,3000,3000])
place2 = np.array([5000,0,0,0])
place3 = np.array([5,4,3,3])


장소1 공부 100 콘센트 50 ㅁ ㅁ ㅁ ㅁ
장소2 공부 70 콘센트 30 ㅁ ㅁ ㅁ ㅁ

키워드를 순서대로
공부, 콘센트, 1123414124
장소 1   100 60 70 
13       56 64  46
123      45  34  34
장소1 공부 100 -> 5
장소2 공부 40 -> 2
장소3 공부 10 -> 0.5


나머지 1 ,1,2,3,4,1,,,1....

2. 사용자가 한 장소에 별점을 좋게 줌 (4~5)
3. 그 장소와 유사한 아이템들을 추천 목록에 넣음
4. 추천 리스트에서 사용자가 이미 별점을 준 장소들을 제거함

'''

"""

사용자에 대한 선호도와 장소들에 대한 선호도 한 행렬로 만들기
만든 행렬을 오름차순으로 만들어 내가 

"""