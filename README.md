# 🧠 NeuRunning — Running & Stress Analysis

## 📌 프로젝트 개요
**NeuRunning**은 러닝 방식(run type)과 템포(tempo)가 스트레스 지수 감소에 어떤 영향을 미치는지를  
웨어러블 데이터(심박수, HRV 등)와 설문 데이터를 통합하여 분석하는 프로젝트입니다.  

연구 목적:
- 인터벌, 파틀렉(Fartlek), LSD(Long Slow Distance), 타임 트라이얼(Time Trial), 빌드업(Build-up), 템포런(Tempo) 등  
  다양한 러닝 방식에 따른 **스트레스 감소 효과** 탐구
- HRV(Heart Rate Variability), 심박수, 설문 스트레스 지수 기반 **러닝-스트레스 상관관계 분석**
- 뇌과학적 관점에서 **러닝 후 스트레스 완화 메커니즘** 연구 기초 데이터 제공

---

## 📂 프로젝트 구조
NeuRunning/
│
├── README.md # 프로젝트 소개
├── LICENSE # 라이선스
├── data/
│ ├── raw/ # 원본 데이터 (웨어러블, 설문)
│ └── processed/ # 처리된 데이터
├── sql/
│ └── running_neuro_with_run_type.sql # DB 스키마 정의
├── scripts/
│ ├── etl.py # 데이터 적재/변환 스크립트
│ ├── hrv_calc.py # HRV 계산 모듈
│ ├── analysis_run_type.py # 러닝 방식별 분석
│ └── utils.py # 공통 유틸 함수
├── notebooks/
│ └── analysis_notebook.ipynb # Jupyter 분석 노트북
├── docs/
│ └── survey_template.pdf # 설문 템플릿 (예시)
└── .gitignore

yaml
코드 복사

---

## ⚙️ 설치 및 실행 방법

### 1. GitHub 클론
```bash
git clone https://github.com/ercb312/NeuRunning.git
cd NeuRunning
2. 가상환경 및 패키지 설치
bash
코드 복사
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
3. MySQL DB 초기화
bash
코드 복사
mysql -u root -p < sql/running_neuro_with_run_type.sql
4. 데이터 로드 & 전처리
bash
코드 복사
python scripts/etl.py
5. HRV 계산
bash
코드 복사
python scripts/hrv_calc.py
6. 분석 실행
bash
코드 복사
python scripts/analysis_run_type.py
또는 Jupyter Notebook 실행:

bash
코드 복사
jupyter notebook notebooks/analysis_notebook.ipynb
📊 분석 예시
LSD vs Interval: 장거리 러닝이 HRV 회복에 더 효과적인지 검증

Tempo Run: 일정한 템포가 스트레스 감소에 주는 안정적 효과 확인

설문 + HRV 결합 분석: 자기보고식 스트레스 지수와 생체 신호 간 상관관계 분석

🧩 향후 발전 방향
뇌파(EEG) 신호와 HRV 결합 연구

머신러닝 기반 러닝-스트레스 예측 모델

개인 맞춤형 러닝 플랜 추천 시스템

📜 라이선스
이 프로젝트는 MIT License 하에 배포됩니다.
