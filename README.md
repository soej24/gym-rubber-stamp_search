# FIND A GYM TO PRACTICE SELF-DEFENSE
## (자기 방어 수련을 위한 체육관 데이터를 분석한 앱)

![title](https://postfiles.pstatic.net/MjAyMjA2MDdfMTc4/MDAxNjU0NTc5NzMwMjAx.WmpKDRgjQEOR60STcVdyffOCaU4mFthQyOS4BTl9cg0g.BGy0yQP1mTGJ1wZSMpW6f0x_rtXnqnXbIkzpMLKoiFkg.JPEG.soej24/main_img_readme.jpg?type=w966)   

## ❓ EASYME.md가 뭐예요?   
- **EASYME.md**는 **<u>개발자가 README.md를 좀 더 쉽게 작성할 수 있도록</u>** 하기 위해 만들었어요.   
- 블로그에서 글을 쓰는 것처럼 쉽게 글을 작성하고 스타일을 적용하면 오른쪽(👉)에 미리보기로 확인하실 수 있어요.   
- 스타일을 적용하면 마크다운 문법 및 md 파일에서 인식할 수 있는 소스코드가 자동으로 적용돼요.   
- 커서 위치, 드래그한 영역 등에 따라 스타일을 적용할 수 있으니 자유롭게 사용해보세요!
- 복사하기를 통해 본문 내용을 복사하고 여러분의 README에 적용해보세요.   

## 🙋‍♀️ 좀 더 구체적으로 가르쳐주세요!   
1. 왼쪽 공간에서 블로그에 글을 쓰는 것처럼 README를 작성해주세요!   
2. 👆 위에 툴바창에 보이는 다양한 스타일을 적용해보세요!   
3. 다 작성하셨나요? 예쁘게 잘 나왔는지 오른쪽 미리보기 화면에서 확인해보세요.   
4. 오른쪽에 작성한 글 전체를 복사하세요!   
(저장을 원할 경우 `Ctrl + S` / `Command + S` 또는 툴바창 제일 오른쪽에 `공유하기 아이콘`을 클릭해주세요.)   
5. 이제 여러분의 **README.md** 에 붙여넣으세요!   
(저장 또는 공유를 할 경우 링크를 다른 사람에게 전달할 수 있어요! 😀)  

## 🛠 기능 엿보기   

1. [❓ EASYME.md가 뭐예요?  ](#-easymemd가-뭐예요)
2. [🙋‍♀️ 좀 더 구체적으로 가르쳐주세요!](#-좀-더-구체적으로-가르쳐주세요)
3. [🛠 기능 엿보기](#-기능-엿보기)
    - [Header](#header)   
    - [Text Style1](#text-style1)   
    - [Text Stlye2](#text-style2)   
    - [List](#list)      
    - [Link](#link)   
    - [Code Block](#code-block)   
    - [Table](#table)   
   
## Header
- # H1 Header   
- ## H2 Header   
- ### H3 Header   
- #### H4 Header   
- ##### H5 Header   
- ###### H6 Header   

<br>   

## Text Style1
- **진하게** (`Ctrl(Command) + B`)   
- *기울이기* (`Ctrl(Command) + I`)   
- <s>취소선</s> (`Ctrl(Command) + D`)   
- <u>밑줄</u> (`Ctrl(Command) + U`)   

<br>   
   
## Text Style2

>인용문   
   
<details><summary>접고 펴는 기능
</summary>

*Write here!*
</details>

- EASYME.md를 드래그하고 상단에 `Aa` 아이콘을 누르면? 👉 Easyme.md   
- EASYME.md를 드래그하고 상단에 `A` 아이콘을 누르면? 👉 EASYME.MD   
- EASYME.md를 드래그하고 상단에 `a` 아이콘을 누르면? 👉 easyme.md   
   
<br>   
   
## List   
### Table of contents
1. [title1](#write-title-here!)   
2. [title2](#only-lowercase)   
3. [title3](#use"-"instead-of-spacing-words)   
4. [title4](#example)   
    - [❓ EASYME.md가 뭐예요?](#-easymemd가-뭐예요)   
    - [🛠 기능 엿보기](#-기능-엿보기)
   
### Unordered list   
- unordered list1   
- unordered list2   
- unordered list3   
- unordered list4   
   
### Ordered list   
1. ordered list1   
2. ordered list2   
3. ordered list3   
4. ordered list4   
   
<br>   
   
## Link   
### General link
- [🚗 Visit EASYME.md's Repo](https://github.com/EASYME-md/client)   
- [🙋‍♂️ Visit ONE:A's Github](https://github.com/onealog)

### Image link
![onealog](/assets/readme/easyme.png)   
   
<br>   
   
## Code Block   
### Code inline
- `console.log('Hello EASYME.md!');`   
   
### Code block
```js
function makeDeveloper(name, language) {
  if (name === 'ONE:A' && language === 'JavaScript') {
    return 'perfect!';
  }

  return false;
}

makeDeveloper('ONE:A', 'JavaScript');
```

<br>   
   
## Table   


| title1 | title2 | title3 |
| --- | --- | --- |
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |


<br>   






Find a Gym to Practice Self-defense
(자기 방어 수련을 위한 체육관 데이터를 분석한 앱)

1. 체육관 검색
지역, 시/군, 읍면동, 운동종목을 선택해서
가까운 체육관을 검색할수 있습니다.

2. 체육관 종류를 분리하기 위해 사업장명 컬럼에서
운동종목 단어들을 추출하였고, 사업장명에 종목이 아닌
체육관으로만 되어있는 예외처리 후 멀티로 구분

df_mlt = df[ (df['소재지전체주소'].str.contains(choice_list)) & (df['소재지전체주소'].str.contains(choice_list2)) & \
(df['소재지전체주소'].str.contains(addr_3)) & (~df['사업장명'].str.contains('태권도') & \
~df['사업장명'].str.contains('합기도') & ~df['사업장명'].str.contains('주짓수') & ~df['사업장명'].str.contains('복싱') & \
~df['사업장명'].str.contains('택견') & ~df['사업장명'].str.contains('검도') & ~df['사업장명'].str.contains('마샬아츠') & \
~df['사업장명'].str.contains('택견'))]

3. 검색 결과가 없는 경우 예외처리!
목록 리스트와 지도를 확인할수 있습니다.

if df.empty :                      
    st.text('검색된 데이터가 없습니다!!')
else :                         
    st.table(df)

new_df_map = df_map[ (df_map['시도'] == choice_list) & (df_map['시군구'] == choice_list2) & (df_map['읍면동'] == addr_3) ]
st.map(new_df_map)

4. 서울특별시, 인천광역시, 대전광역시, 광주광역시, 대구광역시,
부산광역시, 울산광역시, 세종특별자치시, 제주특별자치도, 강원도,
경기도, 경상남도, 경상북도, 전라남도, 전라북도, 충청남도, 충청북도
17개의 지역 선택에 따라 시/군을 선택이 달라집니다.

서울특별시
강남구, 강동구, 강북구, 강서구, 관악구, 광진구, 구로구, 금천구, 노원구, 도봉구, 동대문구, 동작구,
마포구, 서대문구, 서초구, 성동구, 성북구, 송파구, 양천구, 영등포구, 용산구, 은평구, 종로구, 중구,
중랑구

인천광역시
강화군, 계양구, 남동구, 동구, 미추홀구, 부평구, 서구, 연수구, 옹진군, 중구

대전광역시
대덕구, 동구, 서구, 유성구, 중구

광주광역시
광산구, 남구, 동구, 북구, 서구

대구광역시
남구, 달서구, 달성군, 동구, 북구, 서구, 수성구, 중구

부산광역시
강서구, 금정구, 기장군, 남구, 동구, 동래구, 부산진구, 북구, 사상구, 사하구, 서구, 수영구, 연제구, 영도구,
중구, 해운대구

울산광역시
남구, 동구, 북구, 울주군, 중구

세종특별자치시
세종특별자치시

제주특별자치도
서귀포시, 제주시

강원도
강릉시, 고성군, 동해시, 삼척시, 속초시, 양구군, 양양군, 영월군, 원주시, 인제군, 정선군, 철원군,
춘천시, 태백시, 평창군, 홍천군, 화천군, 횡성군

경기도
가평군, 고양시 덕양구, 고양시 일산동구, 고양시 일산서구, 과천시, 광명시, 광주시, 구리시, 군포시,
김포시, 남양주시, 동두천시, 부천시, 성남시, 성남시 분당구, 성남시 수정구, 성남시 중원구, 수원시,
수원시 권선구, 수원시 영통구, 수원시 장안구, 수원시 팔달구, 시흥시, 안산시, 안산시 단원구, 
안산시 상록구, 안성시, 안양시, 안양시 동안구, 안양시 만안구, 양주시, 양평군, 여주시, 연천군, 
오산시, 용인시, 용인시 기흥구, 용인시 수지구, 용인시 처인구, 의왕시, 의정부시, 이천시, 파주시,
평택시, 포천시, 하남시, 화성시

경상남도
거제시, 거창군, 고성군, 김해시, 남해군, 밀양시, 사천시, 산청군, 양산시, 의령군, 진주시, 창녕군,
창원시, 창원시 마산합포구, 창원시 마산회원구, 창원시 성산구, 창원시 의창구, 창원시 진해구,
통영시, 하동군, 함안군, 함양군, 합천군

경상북도
경산시, 경주시, 고령군, 구미시, 군위군, 김천시, 문경시, 봉화군, 상주시, 성주군, 안동시, 영덕군,
영양군, 영주시, 영천시, 예천군, 울릉군, 울진군, 의성군, 청도군, 청송군, 칠곡군, 포항시, 포항시 남구,
포항시 북구

전라남도
강진군, 고흥군, 곡성군, 광양시, 구례군, 나주시, 담양군, 목포시, 무안군, 보성군, 순천시, 신안군,
여수시, 영광군, 영암군, 완도군, 장성군, 장흥군, 진도군, 함평군, 해남군, 화순군

전라북도
고창군, 군산시, 김제시, 남원시, 무주군, 부안군, 순창군, 완주군, 익산시, 임실군, 장수군, 전주시 덕진구,
전주시 완산구, 정읍시, 진안군

충청남도
계룡시, 공주시, 금산군, 논산시, 당진시, 보령시, 부여군, 서산시, 서천군, 아산시, 연기군, 예산군, 천안시,
천안시 동남구, 천안시 서북구, 청양군, 태안군, 홍성군

충청북도
괴산군, 단양군, 보은군, 영동군, 옥천군, 음성군, 제천시, 증평군, 진천군, 청원군, 청주시 상당구, 청주시 서원구,
청주시 청원구, 청주시 흥덕구, 충주시

5. 지역별 체육관 현황
지역, 시/군구, 운동종목을 선택후 검색하면
목록 리스트, 지도, 3개의 차트를 보여줍니다.
17개의 지역에 따라 시/군구 선택사항이 달라집니다.

검색 결과가 없는 경우 예외처리!

6. 지역별 스포츠 동호회 현황(검도, 복싱, 유수, 주짓수, 태권도, 킥복싱, 카라테)
각 지역구별 동호회 참여 회원수와 지역별 운동종목 회원수를 리스트와 차트로 보여줍니다.

7. 연령별 운동 추천
10대~ 20대, 30대, 40대, 50대, 60대 이상
운동에 대한 간단한 설명과 운동을 추천합니다.