# 81 별 표현식 star expression
#    10개의 값이 저장된 scores 리스트가 있을 때, start expression(*)을 사용하여
#    좌측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores
print(valid_score)

# 82 우측 8개의 값을 valid_score 변수에 바인딩하여라.
_, _, *valid_score = scores
print(valid_score)

# 83 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.
_, *valid_score, _ = scores
print(valid_score)

# 84 temp 이름의 비어있는 딕셔너리를 만들라.
temp = {}
print(type(temp))

# 85 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.
price = {'메로나': 1000, '폴라포': 1200, '빵빠레': 1800}
print(price)

# 86 085 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
price['죠스바'] = 1200
price['월드콘'] = 1500
print(price)

# 87 다음 딕셔너리를 사용하여 메로나 가격을 출력하라.
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print('메로나 가격 :', ice['메로나'])

# 88 다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
ice['메로나'] = 1300
print(ice)

# 89 다음 딕셔너리에서 메로나를 삭제하라.
del ice['메로나']
print(ice)

# 90 다음 코드에서 에러가 발생한 원인을 설명하라.
icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바']
# 딕셔너리에 없는 키를 인덱싱 했기 때문이다.

