import os
import zipfile

project_name = "NeuRunning"

folders = [
    "data/raw",
    "data/processed",
    "sql",
    "scripts",
    "notebooks",
    "docs"
]

files_content = {
    "README.md": '''# NeuRunning — Running Stress Analysis

## 프로젝트 개요
- 러닝 방식(run_type) 및 tempo 기반 스트레스 감소 분석
- 웨어러블 + 설문 통합 분석

## 사용법
1. DB 설정
   ```bash
   mysql -u root -p < sql/running_neuro_with_run_type.sql
'''}