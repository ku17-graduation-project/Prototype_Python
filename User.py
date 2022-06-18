from Review import Review
import numpy as np
from numpy import dot
from numpy.linalg import norm
from collections import defaultdict
import warnings

warnings.filterwarnings(action='ignore')

def cos_sim(A, B):
  return dot(A, B)/(norm(A)*norm(B))


class User:
    def __init__(self, name, key_like, location):
        self.user_name = name   # 
        self.key_like = key_like
        self.place_like = {}
        self.location = location # [0, 0]
        
        
    def update_key_like(self, review: Review):
        for k in review.keywords:
            if self.key_like[k] + (review.star - 3) < 0:
                self.key_like[k] = 0
            else:
                self.key_like[k] += (review.star - 3)

    # def cal_place_score(self, place):
    #     score = 0
    #     valid_place_keys = [k for k, v in place.keywords.items() if v>=1]
    #     temp = self.key_like.keys()
    #     for k in set(self.key_like.keys()) & set(valid_place_keys):
    #         score += self.key_like[k]
    #     return score
    
    # def get_recommanded_places(self, places):
    #     # 최소 점수 5, 최대 갯수 3
    #     recommend_place = [p for p in places if self.cal_place_score(p) >= 5]
    #     return recommend_place

    def cal_place_similar(self, place):
        valid_place_key = defaultdict(int, {k:v for k, v in place.keywords.items() if v>=2})
        # a b c d
        # 1 1 0 0  유저
        # 0 1 1 1  장소

        users_like = []
        place_key = []
        
        for key in (set(self.key_like.keys()) | set(valid_place_key.keys())):
            users_like.append(self.key_like[key])
            place_key.append(valid_place_key[key])
            
        ret = cos_sim(users_like, place_key)
        if np.isnan(ret):
            ret = 0

        return ret

    def get_places_similar_list(self, places):
        # 최소 점수 5, 최대 갯수 3
        recommend_place = sorted([(p.name, p.get_distance_meters(self.location, p.location), p.avg_star, self.cal_place_similar(p)) for p in places if self.cal_place_similar(p)>=0.4], key=lambda x:x[3], reverse=True)
        return recommend_place
    
    