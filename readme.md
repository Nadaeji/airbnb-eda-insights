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
데이터 시각화에 영향을 줄 결측치에 대해 제거 또는 치환 이후 이상치를 제거.
```
- 결측치 제거
    ```
    cancellation_policy
    neighbourhood 
    neighbourhood group
    Construction year
    availability 365
    ```
- 결측치 치환
    ```
    minimum nights
    number of reviews 
    service fee
    price
    reviews per month
    number of reviews
    review rate number
    availability 365
    ```
- 이상치 탐색
    ```
    minimum nights
    number of reviews
    price
    service fee
    reviews per month
    number of reviews
    review rate number
    availability 365
    ```
## 데이터시각화를 통한 탐색
- 룸타입별 가격과 리뷰 수의 관계 산점도 
![](./images/가격과%20리뷰%20수의%20관계.png)
- 숙소 선호 상관 관계 히트맵
![](./images/숙소%20선호도%20상관%20관계.png)
- 예약에 영향을 주는 상관관계
![](./images/예약에%20영향을%20주는%20상관관계.png)
- 지역 및 객실 유형별 평균 가격 히트맵
![](./images/주%20및%20객실%20유형별%20평균%20가격.png)
- 건축년도와의 데이터 상관관계
![](./images/건축%20년도에%20따른%20(평균%20가격,%20예약율,%20리뷰수).png)
- 지역별 건축년도 건물 분포 그래프
![](./images/건축년도별%20건물%20수.png)
- 방 타입별 리뷰 수
![](./images/방%20타입-%20리뷰수.png)
- 상위 10개 주의 리뷰 수
![](./images/상위10개의%20주.png)
- 숙소 유형별 갯수
![](./images/숙소%20유형별%20선호도%20파악_숙소개수.png)
- 숙소 종류별 예약율에 따른 평균 가격
![](./images/숙소%20종류별%20예약율에%20따른%20평균%20가격.png)
- 전체 지역의 리뷰 막대 그래프프
![](./images/전체%20지역-리뷰.png)

## 데이터 정제 및 전처리
### 결측치 치환
```python
def fillna(df,columns,default=0):
    for column in columns:
        df[column] = df[column].fillna(default)
    return df
```
### 결측치 제거
```python
def dropna(df,column_list):
    df = df.dropna(subset=column_list,axis=0)
    return df
```
### 데이터 타입 변환
```python
def change_type(df,columns,type):
    for column in columns:
        df[column] = df[column].astype(type)
    return df
```
### 이상치 제거
```python
def cleaned_data(df: pd.DataFrame, columns: List[str], value: Union[int, float, List[Union[int, float]]], compare_type: str) -> pd.DataFrame:
    if not columns:
        raise ValueError("컬럼 리스트가 비어있습니다.")
    
    if compare_type == "over":
        if not isinstance(value, (int, float)):
            raise TypeError("value가 숫자가 아닙니다.")
        for column in columns:
            df = df[df[column] < value]
    elif compare_type == "under":
        if not isinstance(value, (int, float)):
            raise TypeError("value가 숫자가 아닙니다.")
        for column in columns:
            df = df[df[column] > value]
    elif compare_type == "between":
        if not isinstance(value, (list, tuple)) or len(value) != 2:
            raise TypeError("value가 리스트 또는 튜플이 아니거나 길이가 2가 아닙니다.")
        lower, upper = value[0], value[1]
        for column in columns:
            df = df[(df[column] > lower) & (df[column] < upper)]
    else:
        raise ValueError(f"Invalid compare_type: {compare_type}. Use 'over', 'under', or 'between'")
    return df
```

```python
# room type 별 평균 가격 계산
room_type_avg_price = airbnb_df.groupby('room type')['price'].mean()
# 데이터 전처리
airbnb_df = fillna(airbnb_df,['price'],airbnb_df['room type'].map(room_type_avg_price))
airbnb_df = fillna(airbnb_df,['minimum nights','availability 365'],1)
airbnb_df = fillna(airbnb_df,['service fee','number of reviews','review rate number'])
airbnb_df = fillna(airbnb_df,['reviews per month'],airbnb_df['review rate number']/12)
airbnb_df = dropna(airbnb_df,['Construction year','neighbourhood group','cancellation_policy'])

airbnb_df = cleaned_data(airbnb_df,['price'],[50,1000],'between')
airbnb_df = cleaned_data(airbnb_df,['availability 365'],[100,365],'between')
airbnb_df = cleaned_data(airbnb_df,['number of reviews'],100,'over')
airbnb_df = cleaned_data(airbnb_df,['minimum nights'],0,'under')

airbnb_df = change_type(airbnb_df,['availability 365','number of reviews','Construction year','price','service fee'],int)
airbnb_df['availability 365'] = round((365 - airbnb_df['availability 365']) / 365, 2)
airbnb_df['price'] = airbnb_df['price'] * 1400
airbnb_df['service fee'] = airbnb_df['service fee'] *1400
```


```python
# Label Encoder 초기화
le_neighbourhood = LabelEncoder()
le_cancellation = LabelEncoder()
le_room_type = LabelEncoder()

# 범주형 데이터에 Label Encoding 적용
airbnb_df['neighbourhood group'] = le_neighbourhood.fit_transform(airbnb_df['neighbourhood group'])
airbnb_df['cancellation_policy'] = le_cancellation.fit_transform(airbnb_df['cancellation_policy'])
airbnb_df['room type'] = le_room_type.fit_transform(airbnb_df['room type'])
# 취소 정책의 유연성에 따라 데이터 처리
airbnb_df['cancellation_policy'] = 2 - airbnb_df['cancellation_policy']

```