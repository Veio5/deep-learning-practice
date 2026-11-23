---
name: BACE-Screening-Report
description: BACE-1 활성 예측 결과를 GitHub용 Markdown 보고서로 생성하는 스킬
version: 1.0.0
category: cheminformatics
tags: [bace, screening, cheminformatics, report, markdown, github]
---

# BACE-Screening-Report Skill

## 목적
ChEMBL 등의 화합물 라이브러리에서 BACE-1 (Beta-secretase 1) 억제 활성을 예측하고, 그 결과를 GitHub에서 잘 렌더링되는 Markdown 보고서로 변환합니다.

## 사용 시기
- BACE-1 활성 예측 스크리닝 완료 후
- 결과를 GitHub 리포지토리에 게시할 때
- 동료와 분석 결과를 공유할 때
- 논문/발표 자료의 기초 자료로 활용할 때

## 사용법

### 1. 스크리닝 결과 준비
BACE 스크리닝 스크립트 실행 후 CSV 결과 파일이 있어야 합니다.

### 2. 보고서 생성 스크립트 실행
```bash
python generate_bace_report.py \
    --results results.csv \
    --output bace_report.md \
    --project-name "CHEMBL BACE Screening"
```

### 3. GitHub에 푸시
```bash
git add bace_report.md results.csv
git commit -m "Add BACE-1 screening report"
git push origin main
```

## 입력 파일 형식

### 결과 CSV (results.csv)
필수 컬럼:
- `chembl_id`: ChEMBL 화합물 ID
- `smiles`: SMILES 문자열
- `bace_activity_prob`: BACE 활성 예측 확률 (0~1)
- `prediction`: 예측 클래스 (Active/Potential/Inactive)
- `MW`: 분자량
- `LogP`: LogP 값
- `TPSA`: 극성 표면적
- `QED`: 약물 유사성 점수
- `LipinskiViolations`: Lipinski Rule of 5 위반 수

선택 컬럼:
- `HBA`, `HBD`, `RotatableBonds`, `NumAromaticRings`
- `NumHeterocycles`, `FractionCSP3`, `composite_score`

### 모델 정보 JSON (선택사항)
```json
{
  "model_type": "RandomForest",
  "training_dataset": "MoleculeNet BACE-1 Classification",
  "test_roc_auc": 0.8687,
  "test_accuracy": 0.7303,
  "test_precision": 0.9322,
  "test_recall": 0.5978,
  "features": "ECFP4 (Morgan fingerprint, 1024 bits)",
  "model_params": {
    "n_estimators": 200,
    "max_depth": 20
  }
}
```

## 출력 보고서 구조

1. **제목 및 개요** - 프로젝트 정보, 분석 개요
2. **방법론** - 모델 훈련, 스크리닝 조건
3. **결과 요약** - 전체 통계 테이블
4. **상위 물질** - 상위 20-50개 상세 테이블
5. **구조 분석** - 공통 구조 특징, Mermaid 다이어그램
6. **특성 분포** - 시각화 (matplotlib 차트)
7. **결론 및 제언** - 향후 방향

## GitHub 최적화 기능

- ✅ Mermaid 다이어그램 (GitHub에서 자동 렌더링)
- ✅ 표 형식의 구조화된 데이터
- ✅ 이모지를 활용한 시각적 구분
- ✅ collapsible 섹션 (<details> 태그)
- ✅ 모바일 친화적 레이아웃

## 문제 해결

### CSV 파일이 인식되지 않음
- 인코딩 확인 (UTF-8 권장)
- 구분자 확인 (쉼표 또는 탭)
- 필수 컬럼명 확인

### Mermaid 다이어그램이 렌더링되지 않음
- GitHub는 Mermaid를 기본 지원
- `accTitle`, `accDescr` 속성 확인
- 올바른 Mermaid 문법 사용

---

## 예시

### 예시 보고서
`examples/example_report.md` 참조

### 샘플 데이터
- `assets/sample_results.csv` - 100개 화합물 샘플
- `assets/sample_model_info.json` - 모델 정보 예시

---

## 관련 스킬

- `deepchem` - 분자 머신러닝 모델 훈련
- `rdkit` - 분자 구조 처리 및 지문 생성
- `scientific-visualization` - 출판 품질 시각화
- `markdown-mermaid-writing` - Mermaid 다이어그램 표준

---

## 라이선스

MIT License
