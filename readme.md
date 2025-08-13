# 🤎 똥강아지들의 우당탕탕 숙소 데이터 분석 🤎

# 🐕 팀원 소개
> **GitHub** 
<div align="center">
  <table width="100%">
    <tbody>
      <tr>
        <td align="center" width="25%">
          <a href="https://github.com/Nadaeji">
            <img src="./image/04.jpg" width="180" height="180" alt="jiyoon"><br>
            <strong>나지윤</strong>
          </a>
        </td>
        <td align="center" width="25%">
          <a href="https://github.com/SHINJINSEUL">
            <img src="./image/02.jpg" width="180" height="180" alt="jinseul"><br>
            <strong>신진슬</strong>
          </a>
        </td>
        <td align="center" width="25%">
          <a href="https://github.com/comet39">
            <img src="./image/01.jpg" width="180" height="180" alt="hyeondae"><br>
            <strong>이현대</strong>
          </a>
        </td>
        <td align="center" width="25%">
          <a href="https://github.com/yubnyx">
            <img src="./image/03.jpg" width="180" height="180" alt="yubin">
            <strong>전유빈</strong>
          </a>
        </td>
      </tr>
    </tbody>
  </table>
</div>

---
# 🐕 개발기간
> **2025.03.10 ~ 2025.03.13 (4일)**

---
# 🐕 주제
> **에어비앤비 데이터 분석을 통해 최적의 숙소 선택 인사이트**

##  주제 선정 이유
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/국민%20해외%20관광객%20추이.png" width="900" alt="국민 해외 관광객 추이"><br />
      </td>
    </tr>
  </table>
</div>
<br>
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/여행%20선택시%20고려도%20조사.jpg" width="900" alt="숙박 선택에 결정 장애를 격은 비율에 대한 설문"><br />
        <small>숙박 선택에 결정 장애를 겪은 비율에 대한 설문</small>
      </td>
    </tr>
  </table>
</div>

### 🔗 관련 기사:
- [가성비 럭셔리 여행 기사](https://www.traveldaily.co.kr/news/articleView.html?idxno=52838)
- [가성비 여행 가이드 기사](https://www.sukbakmagazine.com/news/articleView.html?idxno=61073)
  
> 첨부된 기사에 따르면 많은 여행객들은 **가성비 좋은 숙소를 찾기 위해 리뷰와 가격을 꼼꼼히 비교**합니다.  
> 그러나 방대한 숙소 정보 속에서 **어떤 숙소를 선택해야 할지 판단하는 것은 쉽지 않은 일**입니다.
> 따라서 우리가 얻을 수 있는 데이터중 뉴욕주의 숙박 데이터를 통해 인사이트를 연역적 접근 (Deductive Approach)을 통해 도출해 보고자 합니다.

> **데이터를 활용하면 객관적인 기준으로 최적의 숙소를 선택할 수 있습니다.**  
> 이를 통해 **소비자는 자신의 요구와 예산에 맞는 숙소를 쉽게 찾을 수 있으며, 호스트들도 경쟁력을 높이기 위한 전략을 수립할 수 있습니다.**  

---
# 🐕 분석에 사용한 데이터셋
<div align="center">
  <table border="1" cellspacing="0" cellpadding="8">
    <tr>
      <td align="center">
        <img src="./image/nyairbnb.jpg" alt="NewYork Airbnb" width="900">
      </td>
    </tr>
    <tr>
      <td align="left">
        <strong>데이터 출처:</strong>
        <a href="https://www.kaggle.com/datasets/arianazmoudeh/airbnbopendata">뉴욕 에어비앤비 Open Data</a><br>
        <strong>데이터 내용:</strong>
        뉴욕의 에어비앤비 숙소 정보, 가격, 리뷰 수, 예약 가능 일수 등
      </td>
    </tr>
  </table>
</div>

---
# 🐕 기술 스택
<table width="100%">
  <tr>
    <td align="center" valign="middle" width="33%">
      <img src="https://img.shields.io/badge/pandas-FF7900?style=for-the-badge&%20api&logoColor=orange" height="400"/><br />
    </td>
    <td align="center" valign="middle" width="33%">
      <img src="https://img.shields.io/badge/matplotlib-7A1FA2?style=for-the-badge&logoColor=purple" height="400"/><br />
    </td>
    <td align="center" valign="middle" width="33%">
      <img src="https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%A0%95%EC%A0%9C&logoColor=white" height="400"/>
    </td>
  </tr>
</table>

---
# 🐕 DataSet을 통해 얻고자 하는 인사이트

## 1️. **소비자의 입장에서 숙소 예약에 참고할 수 있는 인사이트 도출**  
- 리뷰 수와 숙소 유형 간의 관계를 분석하여, 신뢰할 수 있는 숙소를 찾는 방법 탐색  
- 최소 숙박일 제한이 있는 숙소 유형 분석  

## 2️. **숙소 유형(room type)과 지역을 바탕으로 평균 가격 비교**  
- 도시별 숙소 가격 히트맵을 생성하여, **어떤 지역이 가성비 숙소를 제공하는지 분석**  

## 3️. **평점과 예약율(연중 예약 가능 일수를 바탕으로 예약율 전처리) 간의 상관 관계 분석**  
- 예약 가능 일수가 숙소의 선호도를 반영하는지 검토  

## 4️. **에어비앤비 숙소 선호도 및 예약에 영향을 주는 요소 분석**  
- 사람들이 어떤 요소를 기준으로 숙소를 예약하는지 탐색  
- 예약 가능일과 숙소 평점 간의 관계 분석  

---
# 🐕데이터셋 데이터 구조
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

---
# 🐕 EDA 절차

##  **데이터 로드** 
```python
airbnb_df = pd.read_csv('./data/Airbnb_Open_Data.csv',low_memory=False)
```

## 데이터 구조 기초 통계 확인
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/데이터프레임info.png" width="900" alt="데이터 프레임 정보"><br />
        <small>데이터 프레임 정보</small>
      </td>
    </tr>
  </table>
</div>
<br>
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/이상치확인데이터.png" width="900" alt="이상치 확인 데이터"><br />
        <small>이상치 확인 데이터</small>
      </td>
    </tr>
  </table>
</div>

---
# 🐕 결측치 및 이상치 탐색
   
## 1. **결측치 탐색**
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/결측치%20탐색.png" width="900" alt="결측치 탐색"><br />
      </td>
    </tr>
  </table>
</div>

## 2. **불필요한 column 제거**
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


# 🐕 데이터 정제 및 전처리
## • 결측치 치환
```python
def fillna(df,columns,default=0):
    for column in columns:
        df[column] = df[column].fillna(default)
    return df
```
## • 결측치 제거
```python
def dropna(df,column_list):
    df = df.dropna(subset=column_list,axis=0)
    return df
```
## • 데이터 타입 변환
```python
def change_type(df,columns,type):
    for column in columns:
        df[column] = df[column].astype(type)
    return df
```
## • 이상치 제거
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
## • 함수 활용
```python
# room type 별 평균 가격 계산
room_type_avg_price = airbnb_df.groupby('room type')['price'].mean()

# 데이터 전처리
airbnb_df = fillna(airbnb_df,['price'],airbnb_df['room type'].map(room_type_avg_price))
airbnb_df = fillna(airbnb_df,['minimum nights','availability 365'],1)
airbnb_df = fillna(airbnb_df,['service fee','number of reviews','review rate number'])
airbnb_df = fillna(airbnb_df,['reviews per month'],airbnb_df['review rate number']/12)
airbnb_df = dropna(airbnb_df,['Construction year','neighbourhood group','cancellation_policy'])

# 이상치 제거
airbnb_df = cleaned_data(airbnb_df,['price'],[50,1000],'between')
airbnb_df = cleaned_data(airbnb_df,['availability 365'],[100,365],'between')
airbnb_df = cleaned_data(airbnb_df,['number of reviews'],100,'over')
airbnb_df = cleaned_data(airbnb_df,['minimum nights'],0,'under')

# 타입 변화
airbnb_df = change_type(airbnb_df,['availability 365','number of reviews','Construction year','price','service fee'],int)
airbnb_df['availability 365'] = round((365 - airbnb_df['availability 365']) / 365, 2)
airbnb_df['price'] = airbnb_df['price'] * 1400
airbnb_df['service fee'] = airbnb_df['service fee'] *1400
```

## • 라벨 인코딩
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

## • 결측치 제거 확인
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/결측치%20제거%20및%20치환.png" width="900" alt="결측치 제거 확인"><br />
      </td>
    </tr>
  </table>
</div>

---
# 🐕 데이터 시각화를 통한 탐색

## 숙소 선호 상관 관계 히트맵
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/숙소%20선호도%20상관%20관계.png" width="900" alt="숙소 선호 상관관계"><br />
      </td>
    </tr>
  </table>
</div>

## 예약에 영향을 주는 상관관계 히트맵
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/예약에%20영향을%20주는%20상관관계.png" width="900" alt="예약에 영향을 주는 상관관계"><br />
      </td>
    </tr>
  </table>
</div>

## 가격과 리뷰수의 관계 히트맵
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/가격과%20리뷰%20수의%20관계.png" width="900" alt="가격과 리뷰수의 관계"><br />
      </td>
    </tr>
  </table>
</div>

---
# 🐕 에어비앤비 데이터 분석 결론
- 우리가 도출하고자 하는 인사이트에 대하여 다음과 같은 결과를 얻을 수 있습니다. 

## 1. 소비자의 입장에서 숙소 예약에 참고할 수 있는 인사이트

- **단기 숙박**의 경우, 일반적으로 **Hotel**을 선택하는 것이 유리합니다.  
  - 일부 숙소는 **최소 숙박일 수 제한 정책**을 운영하여, 일정 박수(n박 이상) 이하로는 예약이 불가능할 수 있습니다.
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/숙소%20타입별%20최소%20숙박%20일수.png" width="900" alt="숙소 타입별 최소 숙박일수"><br />
      </td>
    </tr>
  </table>
</div>

---
- **도시별 평균 리뷰 수를 확인한 결과**, 숙박 후기를 보고 숙소를 선택하는 경우 **Shared room(게스트하우스)를** 제외한 나머지 숙소 유형을 선택하는 것이 좋습니다.
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/도시별%20평균%20리뷰%20수.png" width="900" alt="도시별 평균 리뷰수"><br />
      </td>
    </tr>
  </table>
</div>
<br>
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/카운티%20별%20평균%20리뷰%20수.png" width="900" alt="카운티별 평균 리뷰수"><br />
      </td>
    </tr>
  </table>
</div>
<br>
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/도시별%20리뷰%20수.png" width="900" alt="도시별 리뷰 수"><br />
      </td>
    </tr>
  </table>
</div>
<br>
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/숙소%20유형별%20선호도%20파악_숙소개수.png" width="900" alt="숙소 유형별 선호도 파악_숙소개수"><br />
      </td>
    </tr>
  </table>
</div>

---
- **건축 연도와 예약률 및 평균 가격 간의 상관관계는 확인되지 않았습니다.**  
  - 이는 **주기적인 리모델링**을 통해 숙박업소가 지속적으로 관리되기 때문으로 추정됩니다.
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/건축%20년도에%20따른%20(평균%20가격,%20예약율,%20리뷰수).png" width="900" alt="건축년도에 따른 평균 가격, 예약율, 리뷰수"><br />
      </td>
    </tr>
  </table>
</div>
<br>
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/건축년도별%20건물%20수.png" width="900" alt="건축년도별 건물수"><br />
      </td>
    </tr>
  </table>
</div>

---
## 2. 지역 및 숙소 유형별 평균 가격 분석

- **도시별 숙소 타입별 평균 가격 히트맵**을 통해, **어떤 지역에서 더 저렴하게 숙박할 수 있는지 비교 가능**합니다.
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/평점별%20예약율에%20따른%20평균%20가격.png" width="900" alt="지역 및 객실 유형별 평균 가격 히트맵"><br />
      </td>
    </tr>
  </table>
</div>
<br>
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/지역구와%20숙소%20타입에%20따른%20평균%20가격%20히트맵.png" width="900" alt="지역구와 숙소 타입에 따른 평균 가격 히트맵"><br />
      </td>
    </tr>
  </table>
</div>
<br>
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/지역구와%20숙소%20타입에%20따른%20평균%20가격%20히트맵%20지역%20이상치%20제거.png" width="900" alt="Staten Island 제거 후 지역구 & 숙소 타입별 평균 가격 히트맵"><br />
      </td>
    </tr>
  </table>
</div>

---
## 3. 평점과 예약률 간의 상관관계 분석
- 시각화 데이터를 통해서는 **평점과 예약률 간의 뚜렷한 상관관계를 확인할 수 없었습니다.**
<div align="center">
  <table>
    <tr>
      <td align="center" valign="middle">
        <img src="./image/숙소%20종류별%20예약율에%20따른%20평균%20가격.png" width="900" alt="숙소 종류별 예약율에 따른 평균 가격"><br />
      </td>
    </tr>
  </table>
</div>

---
## 4. 숙소 선호도 분석 및 예약에 영향을 주는 요소

- **숙소 예약에 영향을 주는 요소를 분석한 결과**, **예약률과 평점 간의 명확한 상관관계를 확인하기 어려웠습니다.**  
- 일반적으로 **인기 있는 숙소일수록 예약 가능일이 적을 가능성이 높습니다.**  
  - 하지만, **예약 가능일(availability_365) 데이터가 신뢰성이 낮아**, 이를 기반으로 한 선호도 분석이 어렵습니다.  
  - 리뷰 평점보다는 **예약 가능일이 적은 숙소를 더 선호하는 경향이 있을 가능성이 큼**

---
##  3번과 4번의 인사이트 도출이 어려웠던 이유

###  `availability_365` 데이터의 신뢰성 문제
> `availability_365`는 데이터 수집 시점을 기준으로 **향후 365일 동안 예약 가능한 일수를 나타냅니다.**
> 하지만, **이 값이 실제 예약된 일수만을 반영하는 것이 아니라**, **호스트가 특정 기간 예약을 차단한 경우에도 영향을 받습니다.**  
> - 즉, 숙소 측에서 **미래 예약을 막아둔 경우**, 해당 숙소의 예약 가용율이 실제보다 낮게 기록될 수 있습니다.
> 따라서, **예약 가용율 데이터에 노이즈가 포함되어 있어, 신뢰할 수 없는 데이터 컬럼이 됩니다.**  
>  - 이로 인해 **평점과 예약 가능일의 관계(3번) 및 숙소 선호도 분석(4번)을** 정확히 수행하기 어렵습니다.

> 🔗 **[에어비앤비 Open Data 컬럼 설명](https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit?gid=1322284596#gid=1322284596)**  
> 해당 문서에서 `availability_365` 컬럼의 정의를 확인할 수 있습니다.

# 🐕 데이터 한계 및 예외 처리: 에러 페어(가격 오류)
---
# 🐕 데이터 한계 및 예외 처리: 에러 페어(가격 오류)

> **에러 페어(Error Fare)** 란 항공/호텔 요금 시스템의 **일시적인 가격 오류**로 정상가 대비 비정상적으로 낮은 금액이 노출·예약되는 현상을 말합니다.  
> 에어비앤비에서의 ‘가격 오류’ 역시 입력 실수, 일시 할인/프로모션 설정 오류 등으로 **극단적으로 낮거나 높은 가격**이 기록될 수 있습니다.

## 왜 이 분석에서 중요할까?
- 본 프로젝트는 **가격·리뷰·예약가용성**으로 ‘가성비’ 인사이트를 도출합니다.  
  가격 오류가 그대로 섞여 있으면 **평균/분포가 왜곡**되어 지역·숙소유형별 비교가 틀어질 수 있습니다.

## 본 분석에서의 처리 방식
- **이상치 컷오프**: `price`는 **\$50 ~ \$1000** 구간으로 제한하여 극단치(가격 오류 가능치)를 제거했습니다.  
  *(코드: `cleaned_data(airbnb_df, ['price'], [50, 1000], 'between')`)*
- **지역/유형별 비교를 유지**하기 위해 전체 컷오프 외에도 시각화 단계에서 **Staten Island 등 지역 단일 이상치 영향**을 제거한 버전도 병행 제시했습니다.
- **availability_365 노이즈 주의**: 호스트의 캘린더 차단/운영상 선택이 반영되므로 예약선호의 대리지표로 사용할 때 **오해 여지**가 있습니다(본문 참조).

## 추가로 할 수 있는 정교화(후속 작업 아이디어)
- **유형·지역별 분위기 대비 이탈치 플래그**: (room type, neighbourhood group)별 로그가격 평균±3σ 밖 데이터는 플래그 처리  
- **하위 퍼센타일 감시**: 유형·지역별 `price` 1~2 퍼센타일 구간 점검(“실수/오타/테스트 가격” 가능성)  
- **프로모션 기간 라벨링**: 공개 가능한 경우, 특정 일자/이벤트 프로모션은 별도 라벨로 모델/시각화에서 분리

## 참고 영상
- 호텔/항공 **에러 페어 개념 소개**: 100만원대 호텔을 8만원에 예약한 사례 소개 영상(개념 및 유의점 설명)
<div align="center">
  <table cellspacing="0" cellpadding="0">
    <tr>
      <td align="center">
        <a href="https://www.youtube.com/watch?v=bWoW2wectB0">
          <img src="https://img.youtube.com/vi/bWoW2wectB0/0.jpg" alt="YouTube 영상 썸네일" width="900">
        </a>
      </td>
    </tr>
  </table>
</div>

---
# 🐕 마무리

## 요약 인사이트
- **단기 숙박**은 대체로 **Hotel** 선택이 유리합니다(최소 숙박일 정책 영향).  
- **후기 기반 선택**을 선호한다면, **Shared room 제외 숙소 유형**이 평균적으로 **리뷰 수가 더 풍부**합니다.  
- **건축 연도 ↔ 예약률/가격** 간 뚜렷한 상관은 관찰되지 않았습니다(리모델링/관리 효과 추정).  
- **지역×숙소유형 히트맵**을 통해 **가성비 지역대/유형 조합**을 식별할 수 있습니다.  
- `availability_365`는 **운영상 차단·미개방** 등의 요소가 섞인 **노이즈 컬럼**으로, 선호도 해석에는 주의가 필요합니다.

## 활용 체크리스트
- **소비자**  
> (1) 숙박일수/최소숙박일 정책 확인 → (2) 지역×유형 히트맵으로 예산 범위 좁히기 →  
> (3) 리뷰 수·최근성 점검 → (4) 취소정책·수수료 확인  
- **호스트**  
> (1) 최소숙박일·취소정책의 시장 적합성 점검 → (2) 리뷰 확보 동선(체크아웃 메시지 등) 설계 →  
> (3) 지역대비 가격 밴드 재정렬 → (4) 캘린더 개방 전략(availability 관리) 최적화

## 한계와 보완
- **가격 오류(에러 페어) 및 극단치**의 잠재적 영향이 있어 컷오프로 1차 보정했으나,  
  유형·지역별 분포 기반의 **정교한 이상치 플래그**는 추후 과제로 남습니다.  
- `availability_365`는 **운영정책 노이즈**가 크므로, 실제 예약데이터(체크인 기록)나 **최근 리뷰 시계열**과의 결합이 필요합니다.
