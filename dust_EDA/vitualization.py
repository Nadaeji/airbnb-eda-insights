import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import plotly.express as px

# 데이터 로드 및 전처리
@st.cache_data
def load_data():
    data = pd.read_csv("./data/pm25_pm10_merged.csv")  # 파일 경로 수정 필요
    data['Date'] = pd.to_datetime(data['Date'])
    return data

# 모델 학습
def train_model(data):
    pivot_data = data.pivot(index='Date', columns='City', values='PM2.5 (µg/m³)').reset_index().fillna(0)
    X = pivot_data[['Beijing']]
    y = pivot_data[['Seoul', 'Tokyo', 'Delhi', 'Bangkok']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model, pivot_data

# 예측 함수
def predict_pm25(model, beijing_pm25):
    input_value = [[beijing_pm25]]
    predicted_pm25 = model.predict(input_value)
    cities = ['Seoul', 'Tokyo', 'Delhi', 'Bangkok']
    return dict(zip(cities, predicted_pm25[0]))

# 도시 좌표 딕셔너리
city_coords = {
    'Seoul': (37.5665, 126.978),
    'Tokyo': (35.6895, 139.6917),
    'Beijing': (39.9042, 116.4074),
    'Delhi': (28.7041, 77.1025),
    'Bangkok': (13.7563, 100.5018)
}

# Streamlit 앱
st.title("Beijing PM2.5 기반 도시별 미세먼지 예측 및 시간별 지도")

# 데이터 로드
data = load_data()
model, pivot_data = train_model(data)

# 탭 구성
tab1, tab2 = st.tabs(["예측 지도", "시간별 데이터 지도"])

# 탭 1: 예측 지도
with tab1:
    st.subheader("베이징 PM2.5 값을 입력해 예측")
    beijing_pm25 = st.number_input("Beijing PM2.5 (µg/m³)", min_value=0.0, max_value=500.0, value=100.0, step=1.0)

    if st.button("예측하기"):
        predictions = predict_pm25(model, beijing_pm25)
        predictions['Beijing'] = beijing_pm25  # 입력값 포함

        # 예측 데이터프레임 생성
        pred_df = pd.DataFrame({
            'City': list(predictions.keys()),
            'PM2.5 (µg/m³)': list(predictions.values()),
            'Latitude': [city_coords[city][0] for city in predictions.keys()],
            'Longitude': [city_coords[city][1] for city in predictions.keys()]
        })

        # 지도 시각화
        fig = px.scatter_mapbox(pred_df, 
                                lat="Latitude", 
                                lon="Longitude", 
                                size="PM2.5 (µg/m³)", 
                                color="PM2.5 (µg/m³)", 
                                hover_name="City", 
                                hover_data={"PM2.5 (µg/m³)": True, "Latitude": False, "Longitude": False},
                                size_max=30,
                                zoom=2,
                                mapbox_style="open-street-map",
                                title=f"Beijing PM2.5 = {beijing_pm25} µg/m³일 때 예측")
        st.plotly_chart(fig)

# 탭 2: 시간별 데이터 지도 (슬라이더로 날짜 변경)
with tab2:
    st.subheader("시간별 미세먼지 농도 지도")
    
    # 날짜 슬라이더
    unique_dates = data['Date'].dt.date.unique()
    min_date_idx = 0
    max_date_idx = len(unique_dates) - 1
    
    selected_idx = st.slider("날짜 선택 (막대바를 이동하세요)", 
                             min_value=min_date_idx, 
                             max_value=max_date_idx, 
                             value=0, 
                             format="")  # 숫자 대신 날짜로 표시하기 위해 format 비움
    selected_date = unique_dates[selected_idx]
    st.write(f"선택된 날짜: {selected_date}")

    # 선택된 날짜 데이터 필터링
    date_data = data[data['Date'].dt.date == selected_date].copy()
    date_data['Latitude'] = date_data['City'].map(lambda x: city_coords[x][0])
    date_data['Longitude'] = date_data['City'].map(lambda x: city_coords[x][1])

    # 지도 시각화
    fig = px.scatter_mapbox(date_data, 
                            lat="Latitude", 
                            lon="Longitude", 
                            size="PM2.5 (µg/m³)", 
                            color="PM2.5 (µg/m³)", 
                            hover_name="City", 
                            hover_data={"PM2.5 (µg/m³)": True, "Latitude": False, "Longitude": False},
                            size_max=30,
                            zoom=2,
                            mapbox_style="open-street-map",
                            title=f"PM2.5 on {selected_date}")
    st.plotly_chart(fig)

    # 선택된 날짜의 데이터 테이블
    st.write(f"{selected_date}의 데이터:")
    st.table(date_data[['City', 'PM2.5 (µg/m³)', 'PM10 (µg/m³)']])

# 데이터 정보
with st.expander("원본 데이터 미리보기"):
    st.dataframe(data.head())
    st.write(f"총 데이터 행 수: {len(data)}")