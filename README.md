# BACE-Screening-Report Skill

BACE-1 (Beta-secretase 1) 활성 예측 결과를 GitHub에 게시할 수 있는 형식의 Markdown 보고서로 생성하는 스킬입니다.

## 개요

이 스킬은 ChEMBL 등의 화합물 라이브러리에서 BACE-1 억제 활성을 예측하고, 그 결과를 GitHub에서 잘 렌더링되는 Markdown 보고서로 변환합니다.

## 사용 방법

### 기본 사용법

```bash
python generate_bace_report.py \
    --results results.csv \
    --output bace_screening_report.md \
    --project-name "CHEMBL BACE-1 Screening"
```

### 옵션

| 옵션 | 설명 | 필수 |
|------|------|------|
| `--results` | 스크리닝 결과 CSV 파일 경로 | ✅ |
| `--output` | 생성할 Markdown 보고서 경로 | ✅ |
| `--project-name` | 프로젝트 이름 | ❌ |
| `--model-info` | 모델 정보 (JSON) | ❌ |
| `--include-figures` | 시각화 포함 여부 | ❌ (기본: true) |

---

## 스킬 구성

```
bace-screening-report/
├── README.md                    # 스킬 문서
├── SKILL.md                     # 스킬 메타데이터 (AI 에이전트용)
├── generate_bace_report.py      # 보고서 생성 스크립트
├── templates/
│   └── report_template.md       # Markdown 보고서 템플릿
├── assets/
│   ├── sample_results.csv       # 샘플 결과 데이터
│   └── sample_model_info.json   # 샘플 모델 정보
└── examples/
    └── example_report.md        # 생성된 보고서 예시
```

---

## 보고서 템플릿 구조

생성되는 보고서는 다음 구조로 구성됩니다:

```markdown
# [프로젝트명] BACE-1 활성 예측 결과 보고서

## 개요
- 분석 대상, 예측 타겟, 분석 목적

## 방법론
- 모델 훈련 정보
- 스크리닝 조건

## 스크리닝 결과 요약
- 전체 통계

## 상위 예측 물질
- 상위 20-50개 표

## 구조 분석
- 공통 구조 특징 (Mermaid 다이어그램)

## 파일 정보
- 저장 위치

## 결론 및 제언
```

---

## 설치

```bash
# 필요한 패키지
pip install pandas matplotlib seaborn rdkit

# 스킬 사용
python generate_bace_report.py --help
```

---

## GitHub 게시 팁

1. **Markdown 보고서에 Mermaid 다이어그램 포함** - GitHub에서 자동 렌더링
2. **결과 CSV 파일 함께 커밋** - 데이터가 공개 가능한 경우에만
3. **README에 분석 요약 포함** - 리포지토리 방문자가 빠르게 이해 가능
4. **라이선스 명시** - 데이터 사용 권한 확인

---

## 예시 보고서 미리보기

생성되는 보고서는 다음과 같은 형식을 포함합니다:

- 표 형식의 상위 물질 목록
- Mermaid 다이어그램을 사용한 워크플로우 시각화
- 물리화학적 특성 분포 차트 (matplotlib/seaborn)
- 구조-활성 관계 분석 요약

---

## 기여 방법

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Submit a pull request

---

## 라이선스

MIT License - 자유롭게 사용 및 수정 가능

---

## 참고

- BACE-1: Beta-secretase 1, 알츠하이머병 치료제 주요 타겟
- ChEMBL: 유럽 생물정보학 연구소(EBI)의 생물활성 데이터베이스
- MoleculeNet: 분자 머신러닝 벤치마크 데이터셋
