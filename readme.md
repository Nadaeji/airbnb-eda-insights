# 팀명 : 똥강아지들의 미세먼지 분석기

# 🫡팀원 소개
<div align="center">

| 이현대 | 신진슬 | 전유빈 | 나지윤 |
|--------|--------|--------|-------|
| <img src="./img/01.jpg" width="180" height="180"> | <img src="./img/02.jpg" width="180" height="180"> | <img src="./img/03.jpeg" width="180" height="180"> | <img src="./img/04.jpg" width="180" height="180"> |

</div>



# 📅 개발기간
2025.03.17 ~ 2025.03.20 (4일)

# 주제 : 중국발 미세먼지가 주변국에 미치는 영향 분석

##  주제 선정 이유

<figure  style="text-align: center;">
<img src="./img/미세먼지사진.jpg">
<figcaption>데이터 프레임 정보</figcaption>
</figure>

🔗 관련 기사:
- [중국발 미세먼지 및 몽골발 황사 영향](https://www.chosun.com/national/transport-environment/2025/03/12/NISU7VVNRRGXZFIE27QK4C6MK4/)
- [ㄴ](https://www.sukbakmagazine.com/news/articleView.html?idxno=61073)


| 등급       | PM10 (μg/m³) | PM2.5 (μg/m³) |
|------------|--------------|---------------|
| 좋음       | 0~30         | 0~15          |
| 보통       | 31~80        | 16~35         |
| 나쁨       | 81~150       | 36~75         |
| 매우 나쁨  | 151 이상     | 76 이상       |

---

## 📂 분석에 사용한 데이터셋

Google Earth Engine

**데이터 내용:** 
도시별 미세먼지 및 초 미세먼지 농도
## 기술 스택
### 데이터 시각화

<img src="https://img.shields.io/badge/pandas-FF7900?style=for-the-badge&%20api&logoColor=orange"> |<img src="https://img.shields.io/badge/matplotlib-7A1FA2?style=for-the-badge&logoColor=purple">|<img src="https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%A0%95%EC%A0%9C&logoColor=white">| <img src="https://img.shields.io/badge/StreamLit-red?style=for-the-badge&logoColor=white">|






## 🔍 DataSet을 통해 얻고자 하는 인사이트

1️. **소비자의 입장에서 숙소 예약에 참고할 수 있는 인사이트 도출**  
   - 리뷰 수와 숙소 유형 간의 관계를 분석하여, 신뢰할 수 있는 숙소를 찾는 방법 탐색  
   - 최소 숙박일 제한이 있는 숙소 유형 분석  

2️. **숙소 유형(room type)과 지역을 바탕으로 평균 가격 비교**  
   - 도시별 숙소 가격 히트맵을 생성하여, **어떤 지역이 가성비 숙소를 제공하는지 분석**  

3️. **평점과 예약율(연중 예약 가능 일수를 바탕으로 예약율 전처리) 간의 상관 관계 분석**  
   - 예약 가능 일수가 숙소의 선호도를 반영하는지 검토  

4️. **에어비앤비 숙소 선호도 및 예약에 영향을 주는 요소 분석**  
   - 사람들이 어떤 요소를 기준으로 숙소를 예약하는지 탐색  
   - 예약 가능일과 숙소 평점 간의 관계 분석  

---



# 데이터셋 데이터 구조
| 열 번호 | 열 이름          | 데이터 개수   | 데이터 타입 |
|---------|------------------|---------------|-------------|
| 0       | Date            | 18,575        | object      |
| 1       | City            | 18,575        | object      |
| 2       | Longitude       | 18,575        | float64     |
| 3       | Latitude        | 18,575        | float64     |
| 4       | PM2.5 (µg/m³)   | 18,575        | float64     |
| 5       | PM10 (µg/m³)    | 18,575        | float64     |


# EDA 절차

##  **데이터 로드** 
```
airbnb_df = pd.read_csv('./data/Airbnb_Open_Data.csv',low_memory=False)
```

## 데이터 구조 기초 통계 확인
- 데이터 프레임 정보
<figure  style="text-align: center;">
<img src="./img/데이터프레임info.png">
<figcaption>데이터 프레임 정보</figcaption>
</figure>

- 기본 통계 정보
<figure  style="text-align: center;">
<img src="./img/이상치확인데이터.png">
<figcaption>이상치 확인 데이터</figcaption>
</figure>


## 결측치 및 이상치 탐색

    
1. **결측치 탐색**

<figure  style="text-align: center;">
<img src="./img/결측치%20탐색.png">
<figcaption>결측치 탐색</figcaption>
</figure>


# 📌 에어비앤비 데이터 분석 결론

우리가 도출하고자 하는 인사이트에 대하여 다음과 같은 결과를 얻을 수 있습니다. 



## 소비자의 입장에서 숙소 예약에 참고할 수 있는 인사이트


- **단기 숙박**의 경우, 일반적으로 **Hotel**을 선택하는 것이 유리합니다.  
  - 일부 숙소는 **최소 숙박일 수 제한 정책**을 운영하여, 일정 박수(n박 이상) 이하로는 예약이 불가능할 수 있습니다.

<figure  style="text-align: center;">
<img src="./img/숙소%20타입별%20최소%20숙박%20일수.png">
<figcaption>숙박 타입별 최소 숙박 일수</figcaption>
</figure>

- **도시별 평균 리뷰 수를 확인한 결과**, 숙박 후기를 보고 숙소를 선택하는 경우 **Shared room(게스트하우스)를** 제외한 나머지 숙소 유형을 선택하는 것이 좋습니다.

<figure style="display: flex; justify-content: center; gap: 20px; text-align: center; flex-wrap: wrap;">
  <div style="flex: 1; max-width: 50%;">
    <img src="./img/도시별%20평균%20리뷰%20수.png" style="width: 100%; height: auto;">
    <figcaption>도시별 평균 리뷰</figcaption>
  </div>

  <div style="flex: 1; max-width: 50%;">
    <img src="./img/카운티%20별%20평균%20리뷰%20수.png" style="width: 100%; height: auto;">
    <figcaption>카운티별 평균 리뷰 수</figcaption>
  </div>
</figure>


<figure  style="text-align: center;">
<img src="./img/도시별%20리뷰%20수.png" alt="샘플 이미지">
 <figcaption>도시별 리뷰 수</figcaption>
</figure>



<figure  style="text-align: center;">
<img src="./img/숙소%20유형별%20선호도%20파악_숙소개수.png" alt="샘플 이미지">
 <figcaption>숙소 유형별 개수</figcaption>
</figure>

- **건축 연도와 예약률 및 평균 가격 간의 상관관계는 확인되지 않았습니다.**  
  - 이는 **주기적인 리모델링**을 통해 숙박업소가 지속적으로 관리되기 때문으로 추정됩니다.
<figure  style="text-align: center;">
<img src="./img/건축%20년도에%20따른%20(평균%20가격,%20예약율,%20리뷰수).png" alt="샘플 이미지">
 <figcaption>건축년도에 따른 평균 가격, 예약율, 리뷰수</figcaption>
</figure>


<figure  style="text-align: center;">
<img src="./img/건축년도별%20건물%20수.png" alt="샘플 이미지">
 <figcaption>건축년도별 건물 수</figcaption>
</figure>

## 지역 및 숙소 유형별 평균 가격 분석

- **도시별 숙소 타입별 평균 가격 히트맵**을 통해, **어떤 지역에서 더 저렴하게 숙박할 수 있는지 비교 가능**합니다.

<figure  style="text-align: center;">
<img src="./img/평점별%20예약율에%20따른%20평균%20가격.png" alt="샘플 이미지">
 <figcaption>지역 및 객실 유형별 평균 가격 히트맵</figcaption>
</figure>



<figure  style="text-align: center;">
<img src="./img/지역구와%20숙소%20타입에%20따른%20평균%20가격%20히트맵.png" alt="샘플 이미지">
 <figcaption>지역구와 숙소 타입에 따른 평균 가격 히트맵</figcaption>
</figure>

<figure  style="text-align: center;">
<img src="./img/지역구와%20숙소%20타입에%20따른%20평균%20가격%20히트맵%20지역%20이상치%20제거.png" alt="샘플 이미지">
 <figcaption>Staten Island 제거 후 지역구 & 숙소 타입별 평균 가격 히트맵</figcaption>
</figure>



##  평점과 예약률 간의 상관관계 분석


- 시각화 데이터를 통해서는 **평점과 예약률 간의 뚜렷한 상관관계를 확인할 수 없었습니다.**


<figure  style="text-align: center;">
<img src="./img/숙소%20종류별%20예약율에%20따른%20평균%20가격.png" alt="샘플 이미지">
 <figcaption>숙소 종류별 예약율에 따른 평균 가격</figcaption>
</figure>


## 숙소 선호도 분석 및 예약에 영향을 주는 요소

- **숙소 예약에 영향을 주는 요소를 분석한 결과**, **예약률과 평점 간의 명확한 상관관계를 확인하기 어려웠습니다.**  
- 일반적으로 **인기 있는 숙소일수록 예약 가능일이 적을 가능성이 높습니다.**  
  - 하지만, **예약 가능일(availability_365) 데이터가 신뢰성이 낮아**, 이를 기반으로 한 선호도 분석이 어렵습니다.  
  - 리뷰 평점보다는 **예약 가능일이 적은 숙소를 더 선호하는 경향이 있을 가능성이 큼**.


## ⚠️ 3번과 4번의 인사이트 도출이 어려웠던 이유

###  `availability_365` 데이터의 신뢰성 문제
- `availability_365`는 데이터 수집 시점을 기준으로 **향후 365일 동안 예약 가능한 일수를 나타냅니다.**
- 하지만, **이 값이 실제 예약된 일수만을 반영하는 것이 아니라**, **호스트가 특정 기간 예약을 차단한 경우에도 영향을 받습니다.**  
  - 즉, 숙소 측에서 **미래 예약을 막아둔 경우**, 해당 숙소의 예약 가용율이 실제보다 낮게 기록될 수 있습니다.
- 따라서, **예약 가용율 데이터에 노이즈가 포함되어 있어, 신뢰할 수 없는 데이터 컬럼이 됩니다.**  
  - 이로 인해 **평점과 예약 가능일의 관계(3번) 및 숙소 선호도 분석(4번)을** 정확히 수행하기 어렵습니다.

> 🔗 **[에어비앤비 Open Data 컬럼 설명](https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit?gid=1322284596#gid=1322284596)**  
> 해당 문서에서 `availability_365` 컬럼의 정의를 확인할 수 있습니다.

에러 페어

[![YouTube 영상](https://img.youtube.com/vi/bWoW2wectB0/0.jpg)](https://www.youtube.com/watch?v=bWoW2wectB0)
