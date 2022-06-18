from Review import Review
from User import User
import Const
from haversine import haversine

# 1. 좋아요순 2. 거리순 3. 좋아요 거리랑 가중치 만드는걸로
class Place:
    def __init__(self, name, place_type, location): # str, list, tuple
        self.name = name
        self.reviews = []
        self.place_type = place_type # []
        self.avg_star = 0
        place_type += ["공통"]
        
        # 마음에 들지 않을 때 고를 태그가 없음
        # 별점 1이여도 keyword 선호도를 일단 1씩 올리기로 함 별점 5점이여도 마찬가지로 1씩
        keyword_set = set([])
        for keywords in [Const.PLACES_KEYWORDS[type] for type in place_type]:
            for kw in keywords:
                keyword_set.add(kw)
        
        self.keywords = {key : 0 for key in keyword_set}
        self.location = location # (0, 0)

    def update_avg_star(self):
        self.avg_star = sum([r.star for r in self.reviews]) / len(self.reviews)
        
    def create_review(self, _user: User, _keywords, _star):
        #### keywords, star input
        review = Review(_user, _keywords, _star)
        _user.update_key_like(review)
        for k in _keywords:
            self.keywords[k] += 1
        self.reviews.append(review)
        self.update_avg_star()
        
    # def set_keywords(self):
    #     Const.PLACES_KEYWORDS[]
    
    @staticmethod
    def get_places_by_star(user, places): # 매번 오름차순으로 하는건 프로토타입에서만!!!
        sorted_places = sorted([(place.name, Place.get_distance_meters(user.location, place.location), place.avg_star, user.cal_place_similar(place)) for place in places], key=lambda x:x[2], reverse=True)
        return sorted_places

    @staticmethod
    def get_distance_meters(user_loc, place_loc):
        distance_meters = haversine(user_loc, place_loc, unit='m')
        return distance_meters
    
    @staticmethod
    def get_places_by_distance(user, places):
        sorted_places = sorted([(place.name, Place.get_distance_meters(user.location, place.location), place.avg_star, user.cal_place_similar(place)) for place in places], key= lambda x:x[1])
        return sorted_places
    
    def __str__(self) -> str:
        return self.name
    

# from collections import defaultdict
# user_key_like = defaultdict(int)
# user_key_like['공부'] += 5
# user_key_like['24시'] += 5
# user_loc = [37.54027736489841, 127.07432285195323]
# user1 = User('konkuk', user_key_like, user_loc)
# places = []
# place1 = Place('동생대 K-CUBE', ['교내'], (37.54027736489841, 127.07432285195323))
# places.append(place1)
# place2 = Place('황소상', ['교내'], (37.543132363665535, 127.07615879242665))
# places.append(place2)
# place3 = Place('기숙사 할리스', ['카페'], (37.53923142850558, 127.0755466497599))
# places.append(place3)
# place4 = Place('일감호', ['교내'], (37.54085273416675, 127.07631488542982))
# places.append(place4)
# place5 = Place('학생회관 식당', ['교내', '식당'], (37.54198237505499, 127.07801898911505))
# places.append(place5)
# place6 = Place('가츠시', ['식당'], (37.54636274700634, 127.07568963740945))
# places.append(place6)
# place7 = Place('도서관 6층 K-CUBE', ['교내'], (37.542217015745166, 127.07392591185358))
# places.append(place7)
# place8 = Place('공학관 1층 K-CUBE', ['교내'], (37.541641714457114, 127.07882201660733))
# places.append(place8)
# place9 = Place('와우도', ['교내'], (37.54007545027526, 127.07657999593698))
# places.append(place9)
# place10 = Place('새천년관 4층 실습실', ['교내'], (37.543656334117365, 127.07748324485432))
# places.append(place10)
# place11 = Place('산학관 카페', ['교내', '카페'], (37.540034819355874, 127.07316282334232))
# places.append(place11)
# place12 = Place('개미집', ['식당'], (37.545781282915016, 127.07618694787281))
# places.append(place12)
# print(user1.get_places_similar_list(places))