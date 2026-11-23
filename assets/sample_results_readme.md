# BACE-1 활성 예측 결과 샘플 데이터

이 파일은 보고서 생성 스크립트 테스트를 위한 샘플 데이터입니다.

## 컬럼 설명

| 컬럼 | 설명 |
|------|------|
| chembl_id | ChEMBL 화합물 고유 ID |
| smiles | SMILES 문자열 (분자 구조 표현) |
| bace_activity_prob | BACE-1 활성 예측 확률 (0~1) |
| prediction | 예측 결과 (Active/Potential/Inactive) |
| MW | 분자량 (Dalton) |
| LogP | Octanol-water 분배 계수 |
| TPSA | Topological Polar Surface Area (Å²) |
| HBA | 수소 결합 수용체 수 |
| HBD | 수소 결합 공여체 수 |
| RotatableBonds | 회전 가능 결합 수 |
| NumAromaticRings | 방향족 고리 수 |
| NumHeterocycles | 헤테로고리 수 |
| FractionCSP3 | sp3 혼성 탄소 비율 |
| QED | 정량적 약물 유사성 추정치 (0~1) |
| LipinskiViolations | Lipinski Rule of 5 위반 수 |
| composite_score | 종합 평가 점수 (BACE 확률 + QED 조합) |
