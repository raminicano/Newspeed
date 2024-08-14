# Newspeed
버블 차트를 통해 뉴스 기사의 주요내용과 키워드를 시각적으로 표현해 사용자가 빠르게 내용을 파악할 수 있습니다.
인공지능 기술을 사용해 뉴스기사의 핵심 내용을 자동으로 요약해 제공합니다.
사용자의 관심사와 선호도를 분석해 개인화된 뉴스를 제공합니다.

<br>
<br>

## 📍프로젝트 개요

### 3인 프로젝트
**포지션 및 기여도**

송윤주(팀장) : 백엔드 100%, AI 20%, 프론트엔드 10%

김은호(팀원) : AI 80%

정세민(팀원) : 프론트엔드 90%

<br>

### 담당 업무
1. **사용자 인증 및 회원가입:** JWT 토큰을 이용해 로그인 및 회원가입 기능을 구현하였으며, 콜드스타트 문제를 해결하기 위해 회원가입 시 6개의 뉴스 주제(정치, 경제, 사회, 문화, 과학, 세계)에 대한 사용자의 관심도를 입력받는 시스템을 설계했습니다.

2. **핫토픽 뉴스 기능:** 정치, 경제, 사회, 생활/문화, IT/과학, 세계 등 6개 주제로 분류된 실시간 핫토픽 뉴스를 주제별로 10개씩 제공하며, 댓글 수에 따라 시각화된 버블의 크기를 다르게 표시하는 기능을 구현했습니다.

3. **개인화 뉴스 추천:** 유저의 뉴스 버블 키워드 클릭 데이터를 기반으로 개인화된 뉴스 추천 시스템을 개발했습니다. 클릭된 키워드가 3개 미만일 경우 회원가입 시 입력된 선호도를 정규화하여 추천하고, 3개 이상일 경우 사용자 벡터를 기반으로 유사한 주제의 뉴스를 추천하는 알고리즘을 구현했습니다.

4. **상세 기사 페이지:** 사용자가 뉴스 버블 키워드를 클릭하면 해당 주제의 기사를 3줄 요약하여 제공하며, 관련 뉴스 목록과 기사 전문 조회 기능을 개발했습니다.

5. **카드뉴스 제공:** 각 뉴스 주제에서 댓글 수가 가장 많은 뉴스를 카드 뉴스 형태로 제공하는 기능을 구현했습니다.

6. **북마크 기능:** 사용자가 관심 있는 기사를 북마크할 수 있도록 하고, 북마크한 기사 목록을 별도의 페이지에서 관리할 수 있도록 구현했습니다.


<br>
<br>

## 🗂️기술 스택
<div algin=center>
  
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">
  <img src="https://img.shields.io/badge/openai-412991?style=for-the-badge&logo=openai&logoColor=white">

</div>

<br>
<br>

## 💽 ERD

<img width="800" alt="erd" src="https://github.com/user-attachments/assets/b21cbe03-93d5-4828-b589-daf5a191698a">

<br>
<br>


## 📚세부 내용

![뉴스피드-01](https://github.com/user-attachments/assets/6649ed4b-9b96-45ba-9dbc-8fc725ded9bf)
![뉴스피드-03](https://github.com/user-attachments/assets/5875a4dd-1085-49dd-a6a4-0455504e62ff)
![뉴스피드-07](https://github.com/user-attachments/assets/ba50e365-0e90-4b8b-abec-81b5b715ef82)
![뉴스피드-08](https://github.com/user-attachments/assets/b6bdcf9d-1fe4-4832-a3a4-a13f5bd687f2)
![뉴스피드-09](https://github.com/user-attachments/assets/48f57db3-474e-436e-8f09-eb0e1f057f4c)
![뉴스피드-10](https://github.com/user-attachments/assets/99704a7b-c1be-4640-a2f5-7eda0ddd03c4)
![뉴스피드-11](https://github.com/user-attachments/assets/54ae311f-e65a-4d17-8e22-78bacdce216b)
![뉴스피드-12](https://github.com/user-attachments/assets/55e6de4b-945d-454f-bfb1-fbb34c977b60)
![뉴스피드-13](https://github.com/user-attachments/assets/de047a61-003a-4a49-9491-e16335e489c6)
![뉴스피드-14](https://github.com/user-attachments/assets/e909b012-6d2f-44ae-8bff-159e4cfe14e7)
![뉴스피드-15](https://github.com/user-attachments/assets/24502d87-6a78-48c2-b69f-cea239ad1068)
![뉴스피드-16](https://github.com/user-attachments/assets/54699aa7-6933-4126-99cb-d8dd3e5ebf3d)
![뉴스피드-17](https://github.com/user-attachments/assets/44780d06-c40a-45f0-b856-8cfb6dd51e28)
![뉴스피드-18](https://github.com/user-attachments/assets/051080b1-6821-4ac4-bf42-32efa9010818)











