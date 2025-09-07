# Running Stress Analysis

## 📌 프로젝트 개요
- 러닝 방식(Interval, Fartlek, LSD, TimeTrial, BuildUp)에 따른 **스트레스 감소 효과** 연구
- **웨어러블 데이터 + 설문 데이터**를 통합하여 분석
- `tempo (km/h)` 포함 → 달리기 강도와 스트레스 감소 간의 관계 연구 가능

## 📂 폴더 구조
- `data/raw/` : 원시 데이터 (웨어러블, 설문)
- `data/processed/` : ETL 후 정제된 데이터
- `sql/` : MySQL 스키마
- `scripts/` : ETL, HRV 계산, 분석 스크립트
- `notebooks/` : Jupyter Notebook 분석
- `docs/` : 설문지 예시

## ⚙️ 실행 방법
1. 데이터베이스 생성
   ```bash
   mysql -u root -p < sql/running_neuro_with_run_type.sql
