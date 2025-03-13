# 🫡팀원 소개
| 이현대 | 신진슬 | 전유빈 | 나지윤 |
|--------|--------|--------|-------|
| ![이현대](/images/01.jpg) | ![신진슬](/images/02.jpg) | ![전유빈](/images/03.jpeg) | ![나지윤](/images/04.jpg) |

# DataSet을 통해 얻고자 하는 인사이트
1. **airbnb 숙소 선호도를 확인, 숙소 예약에 영향을 주는 요소가 무엇인지?** 

2. **숙소 유형별 평균 가격 → 각 room type과 지역을 바탕으로 평균 가격**  

3. **평점과 예약율(연중 예약 가능 일수를 바탕으로 예약율 전처리)의 상관 관계** 


# 📅개발기간
2025.03.10 ~ 2025.03.13 (3일)

# 주제 선정 이유
![](https://www.traveldaily.co.kr/news/photo/202406/52838_53810_4952.jpg)

**여행객들은 자신의 요구와 예산에 맞는 최적의 선택을 할 수 있으며, 데이터 기반 인사이트는 에어비앤비 호스트들에게도 유용한 정보를 제공할 수 있다.**

[가성비 럭셔리 여행 기사](https://www.traveldaily.co.kr/news/articleView.html?idxno=52838)
[가성비 여행 가이드 기사](https://www.sukbakmagazine.com/news/articleView.html?idxno=61073)
# 데이터셋
![NewYork Airbnb](/images/nyairbnb.jpg)
[뉴욕 에어비엔비 Open Data](https://www.kaggle.com/datasets/arianazmoudeh/airbnbopendata)


# 데이터셋 Info
| 속성 | 설명 | 데이터 타입 |
| --- | --- | --- |
| id | 숙소 고유 ID | int64 |
| NAME | 숙소 이름 | object |
| host id | 호스트 ID | int64 |
| host_identity_verified | 호스트의 신원 인증 여부 | object |
| host name | 호스트 이름 | object |
| neighbourhood group | 숙소가 위치한 대략적인 구역(도시나 큰 행정구역) | object |
| neighbourhood | 숙소가 위치한 동네 (구,동 단위) | object |
| lat | 위도 | float64 |
| long | 경도 | float64 |
| country | 숙소가 위치한 국가 | object |
| country code | 국가 코드 | object |
| instant_bookable | 즉시 예약 가능 여부 | object |
| cancellation_policy | 취소 정책 | object |
| room type | 숙소 유형 | object |
| Construction year | 건축 연도 | float64 |
| price | 1박당 숙박 요금(달러) | object |
| service fee | 서비스 이용 수수료 | object |
| minimum nights | 최소 숙박 가능 일수 | float64 |
| number of reviews | 리뷰 수 | float64 |
| last review | 마지막으로 리뷰가 작성된 날짜 | object |
| reviews per month | 월별 평균 리뷰 수 | float64 |
| review rate number | 리뷰 평점(별점) | float64 |
| calculated host listings count | 해당 호스트가 운영하는 숙소 개수 | float64 |
| availability 365 | 1년(365일) 중 숙소 예약 가능 일수 | float64 |
| house_rules | 숙소 이용 규칙 | object |
| license | 숙소의 공식 라이선스(허가) 여부 | object |


# EDA 절차

1. **데이터 로드**
```
airbnb_df = pd.read_csv('./data/Airbnb_Open_Data.csv',low_memory=False)
```

## 데이터 구조 기초 통계 확인
- 데이터 프레임 정보
![](/images/데이터프레임info.png)
- 기본 통계 정보
![](/images/이상치확인데이터.png)

## 결측치 및 이상치 탐색
1. **불필요한 column 제거**
```
    host_name
    country
    country_code
    calculated host listings count
    license
    house_rules
    last review
    instant_bookable
    long
    lat
    NAME
    host id
    host_identity_verified
    host name
```
    
2. **결측치 탐색**
    ```
    cancellation_policy : 
    minimum nights : 
    number of reviews  : 
    neighbourhood :
    neighbourhood group :
    Construction year :
    availability 365 :
    price : 결측치 =>
    service fee : 
    reviews per month :
    number of reviews  :
    review rate number :
    availability 365 :
    ```
## 데이터시각화를 통한 탐색

## 데이터 정제 및 전처리
 ```
    cancellation_policy : 결측치 제거 
    minimum nights : 결측치 1로 변경 => 0이하, 10이상 제거
    number of reviews  : 0으로 변경
    neighbourhood : 결측치 제거
    neighbourhood group : 결측치 제거
    Construction year : 결측치 제거
    availability 365 : 결측치 제거 -> 50이하 제거 ,365 이상 제거
    price : 결측치 => roomtype별 평균 가격으로 대체 => int형 변환 => 50이하 제거 1000이상 제거 => $ => 000세개 붙이기
    service fee : 0으로 변경 결측치 => roomtype별 평균 가격으로 대체 => int형 변환 $ => 000세개 붙이기
    reviews per month : 리뷰 수를 12으로 나눈 값으로 대체
    number of reviews  : 0으로 변경
    review rate number : 0
    availability 365 : 365로 나누어서 예약율 값으로 변경
    지역별 
    ```