# FIND A GYM TO PRACTICE SELF-DEFENSE
## (자기 방어 수련을 위한 체육관 데이터를 분석한 앱)
- 데이터 출처 : 국민체육진흥공단
- 가까운 체육관 찾기
- 연령대별 추천 운동
- 지역별 스포츠 동호회 참여도
<br /><br /><br />
![title](./data/main_img.jpg)
<br /><br />

## 1. 체육관 검색
- 지역, 시/군, 읍면동, 운동종목을 선택해서 가까운 체육관을 검색할수 있습니다.
- 서울특별시, 인천광역시, 대전광역시, 광주광역시, 대구광역시, 부산광역시, 울산광역시, 세종특별자치시,
  제주특별자치도, 강원도, 경기도, 경상남도, 경상북도, 전라남도, 전라북도, 충청남도, 충청북도 17개의
  지역 선택에 따라 시/군을 선택이 달라집니다. 
- 체육관 종류를 분리하기 위해 사업장명 컬럼에서 운동종목 단어들을 추출   
- 사업장명에 종목이 아닌 체육관으로만 되어있는 예외처리 후 멀티로 구분
- 검색되는 데이터가 없는경우 '검색된 데이터가 없습니다'로 예외처리
- 목록 리스트와 지도를 확인할수 있습니다.
<br />

##### 지역, 읍면동, 운동종목 셀렉트박스 부분 Code
```js
addr_1 = ['서울특별시','인천광역시','대전광역시','광주광역시','대구광역시',\
          '부산광역시','울산광역시','세종특별자치시','제주특별자치도', '강원도',\
          '경기도', '경상남도', '경상북도', '전라남도', '전라북도','충청남도','충청북도']
column_list = ['태권도','합기도', '주짓수', '유도', '공수도', '킥복싱', '복싱',\
               '택견', '검도', '마샬아츠','트릭킹','멀티']
```
<br /><br />

![title](./data/screenshot01.jpg)
<br /><br />

##### 지역에 따라 시/군 셀렉트박스가 바뀌는 부분 Code
```js
choice_list = st.selectbox('지역을 선택하세요!', addr_1, index=3)          
if choice_list == addr_1[0] :
    addr_2 = ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구',\
              '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구',\
              '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구',\
              '중구', '중랑구']
    choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2)

if choice_list == addr_1[1] :
    addr_2 = ['강화군', '계양구', '남동구', '동구', '미추홀구', '부평구', '서구',\
              '연수구', '옹진군', '중구']
    choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2)

if choice_list == addr_1[2] :
    addr_2 = ['대덕구', '동구', '서구', '유성구', '중구']
    choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2)       

if choice_list == addr_1[3] :
    addr_2 = ['광산구', '남구', '동구', '북구', '서구']
    choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2)        

if choice_list == addr_1[4] :
    addr_2 = ['남구', '달서구', '달성군', '동구', '북구', '서구', '수성구', '중구']
    choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

if choice_list == addr_1[5] :
    addr_2 = ['강서구', '금정구', '기장군', '남구', '동구', '동래구', '부산진구', '북구', '사상구',\
              '사하구', '서구', '수영구', '연제구', '영도구', '중구', '해운대구']
    choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

if choice_list == addr_1[6] :
    addr_2 = ['남구', '동구', '북구', '울주군', '중구']
    choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

if choice_list == addr_1[7] :
    addr_2 = ['세종특별자치시']
    choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

if choice_list == addr_1[8] :
    addr_2 = ['서귀포시', '제주시']
    choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

if choice_list == addr_1[9] :
    addr_2 = ['강릉시', '고성군', '동해시', '삼척시', '속초시', '양구군', '양양군', '영월군', '원주시',\
              '인제군', '정선군', '철원군','춘천시', '태백시', '평창군', '홍천군', '화천군', '횡성군']
    choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

if choice_list == addr_1[10] :
    addr_2 = ['가평군', '고양시 덕양구', '고양시 일산동구', '고양시 일산서구', '과천시', '광명시', '광주시',\
              '구리시', '군포시', '김포시', '남양주시', '동두천시', '부천시', '성남시', '성남시 분당구',\
              '성남시 수정구', '성남시 중원구', '수원시', '수원시 권선구', '수원시 영통구', '수원시 장안구',\
              '수원시 팔달구', '시흥시', '안산시', '안산시 단원구', '안산시', '상록구', '안성시', '안양시',\
              '안양시 동안구', '안양시 만안구', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시',\
              '용인시 기흥구', '용인시 수지구', '용인시 처인구', '의왕시', '의정부시', '이천시', '파주시',\
              '평택시', '포천시', '하남시', '화성시']
    choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

if choice_list == addr_1[11] :
    addr_2 = ['거제시', '거창군', '고성군', '김해시', '남해군', '밀양시', '사천시', '산청군', '양산시',\
              '의령군', '진주시', '창녕군', '창원시',' 창원시 마산합포구', '창원시 마산회원구',\
              '창원시 성산구', '창원시 의창구', '창원시 진해구', '통영시', '하동군','함안군', '함양군',\
              '합천군']
    choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

if choice_list == addr_1[12] :
    addr_2 = ['경산시', '경주시', '고령군', '구미시', '군위군', '김천시', '문경시', '봉화군', '상주시', '성주군',\
             '안동시', '영덕군','영양군', '영주시', '영천시', '예천군', '울릉군', '울진군', '의성군', '청도군',\
             '청송군', '칠곡군', '포항시', '포항시 남구', '포항시 북구']
    choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

if choice_list == addr_1[13] :
    addr_2 = ['강진군', '고흥군', '곡성군', '광양시', '구례군', '나주시', '담양군', '목포시', '무안군', '보성군',\
              '순천시', '신안군', '여수시', '영광군', '영암군', '완도군', '장성군', '장흥군', '진도군', '함평군',\
              '해남군', '화순군']
    choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

if choice_list == addr_1[14] :
    addr_2 = ['고창군', '군산시', '김제시', '남원시', '무주군', '부안군', '순창군', '완주군', '익산시', '임실군',\
              '장수군', '전주시 덕진구', '전주시 완산구', '정읍시', '진안군']
    choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

if choice_list == addr_1[15] :
    addr_2 = ['계룡시', '공주시', '금산군', '논산시', '당진시', '보령시', '부여군', '서산시', '서천군', '아산시',\
              '연기군', '예산군', '천안시', '천안시 동남구', '천안시 서북구', '청양군', '태안군', '홍성군']
    choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2) 

if choice_list == addr_1[16] :
    addr_2 = ['괴산군', '단양군', '보은군', '영동군', '옥천군', '음성군', '제천시', '증평군', '진천군', '청원군',\
              '청주시 상당구', '청주시 서원구', '청주시 청원구', '청주시 흥덕구', '충주시']
    choice_list2 = st.selectbox('시/군을 선택하세요!', addr_2)     
addr_3 = st.text_input('읍면동을 입력하세요! ex)구월동', max_chars=20)
choice_list3 = st.selectbox('운동 종목을 선택하세요! (종목이 없는 체육관은 멀티로 분류)', column_list, index=0)
```
<br />

#### 사업장명에서 종목별로 데이터 가져오는 Code
```js
df = df[ (df['소재지전체주소'].str.contains(choice_list)) & (df['소재지전체주소'].str.contains(choice_list2)) &\
         (df['소재지전체주소'].str.contains(addr_3)) & (df['사업장명'].str.contains(choice_list3))]
df = df.reset_index(drop=True)    
```
<br />

#### 데이터가 없는 경우 예외처리 Code
```js
if df.empty :
    st.markdown("***")                            
    st.text('검색된 데이터가 없습니다!!')
```
<br />

#### 사업장명에서 종목이 구분 안되는 부분 멀티로 예외처리 Code
```js
df_mlt = df[ (df['소재지전체주소'].str.contains(choice_list)) & (df['소재지전체주소'].str.contains(choice_list2)) & \
    (df['소재지전체주소'].str.contains(addr_3)) & (~df['사업장명'].str.contains('태권도') & \
        ~df['사업장명'].str.contains('합기도') & ~df['사업장명'].str.contains('주짓수') & \
        ~df['사업장명'].str.contains('복싱') & ~df['사업장명'].str.contains('택견') & \
        ~df['사업장명'].str.contains('검도') & ~df['사업장명'].str.contains('마샬아츠') & \
        ~df['사업장명'].str.contains('택견'))]
df_mlt = df_mlt.reset_index(drop=True)
st.table(df_mlt)
```
<br /><br />

![title](./data/screenshot02.jpg)
<br /><br />

#### 지도 맵 보여주는 Code
```js
if df.empty :                      
    st.text('검색된 데이터가 없습니다!!')
else :                         
    st.table(df)
```
<br /><br />

![title](./data/screenshot03.jpg)
<br /><br />

## 2. 지역별 체육관 현황 
- 지역, 시/군구, 운동종목을 선택후 검색하면 목록 리스트, 지도, 3개의 차트를 보여줍니다.
  17개의 지역에 따라 시/군구 선택사항이 달라집니다.<br>
<br />

##  3. 지역별 스포츠 동호회 현황(검도, 복싱, 유수, 주짓수, 태권도, 킥복싱, 카라테)
- 각 지역구별 동호회 참여 회원수와 지역별 운동종목 회원수를 리스트와 차트로 보여줍니다.
<br /><br />

![title](./data/screenshot04.jpg)
<br /><br />

#### 지역별 운동종목과 회원수 보여주는 Code
```js
gym_use_total1 = pd.DataFrame(gym_use.groupby(['시도명','운동종목'])['회원수'].sum()).loc['서울특별시']
st.subheader('서울특별시')
st.table(gym_use_total1)
# 각 지역마다 구분코드 다름
```
<br />

#### 지역별 회원수 보기 시각화 Code
```js
gym_use_1 = gym_use.loc[ gym_use['시도명'].str.contains('서울특별시'), ]
gym_use_1.groupby('군구명')['회원수'].sum()

fig1 =  px.pie(gym_use_1, names='군구명', values='회원수')
st.plotly_chart(fig1)
# 각 지역마다 구분코드 다름
```
<br />

## 4. 연령별 운동 추천
- 10대~ 20대, 30대, 40대, 50대, 60대 이상
운동에 대한 간단한 설명과 운동을 추천합니다.
- 라디오 버튼으로 구분
<br />

## programming language / graphic tool
- [ Python ] [ Pandas ] [ Streamlit ] [ AWS ec2 ] [ Visuil Studio Code ] [ Photoshop ]
<br />

## Link   
- [🚗 Visit EASYME.md's Repo](https://github.com/soej24/gym-rubber-stamp_search/blob/main/README.md)   
- [🙋‍♂️ Visit ONE:A's Github](https://github.com/soej24/gym-rubber-stamp_search)