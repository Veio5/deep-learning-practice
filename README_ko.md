# BACE-1 스크리닝 리포트 생성 스킬

![BACE-1 Screening](https://img.shields.io/badge/BACE--1-Screening-blue)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

BACE-1 (Beta-secretase 1) 활성 예측 결과를 GitHub에 게시하기 위한 Markdown 보고서 생성 도구입니다.

## 📌 개요

이 스킬은 다음과 같은 기능을 제공합니다:

- ✅ ChEMBL 화합물 라이브러리의 BACE-1 활성 예측 결과 보고서 생성
- ✅ GitHub에서 렌더링되는 Mermaid 다이어그램 포함
- ✅ 표 형식의 구조화된 데이터 정리
- ✅ 물리화학적 특성 분석 요약
- ✅ Drug-likeness (QED) 평가 포함

## 🚀 빠른 시작

### 1. 의존성 설치

```bash
pip install pandas numpy
```

### 2. 보고서 생성

```bash
python generate_bace_report.py \
    --results your_results.csv \
    --output bace_report.md \
    --project-name "My BACE-1 Screening"
```

### 3. GitHub에 푸시

```bash
git add bace_report.md your_results.csv
git commit -m "Add BACE-1 screening report"
git push
```

## 📊 보고서 예시

생성된 보고서는 다음과 같은 내용을 포함합니다:

```markdown
# My BACE-1 Screening - BACE-1 활성 예측 결과 보고서

## 📋 개요
- 전체 화합물: 2,897,819개
- BACE 활성 예측: 13,259개 (0.46%)

## 🔬 방법론
- 모델: Random Forest
- 특징: ECFP4 지문

## 📊 결과
- 상위 20개 물질 테이블

## 📝 결론
- BBB 투과 가능성 분석
```

## 📁 프로젝트 구조

```
bace-screening-report/
├── README.md                    # 이 파일
├── SKILL.md                     # 스킬 메타데이터
├── generate_bace_report.py      # 보고서 생성 스크립트
├── generate_sample_data.py      # 샘플 데이터 생성
├── templates/
│   └── (향후 템플릿 추가 가능)
├── assets/
│   ├── sample_results.csv       # 샘플 결과 데이터
│   └── sample_model_info.json   # 샘플 모델 정보
└── examples/
    └── example_report.md        # 생성된 예시 보고서
```

## ⚙️ 옵션

| 옵션 | 설명 | 기본값 |
|------|------|--------|
| `--results` | 결과 CSV 파일 경로 | 필수 |
| `--output` | 출력 Markdown 파일 경로 | 필수 |
| `--project-name` | 프로젝트 이름 | "BACE-1 Screening" |
| `--model-info` | 모델 정보 JSON 파일 | 없음 |
| `--top-n` | 포함할 상위 물질 수 | 20 |
| `--prob-threshold` | BACE 활성 임계값 | 0.5 |
| `--no-mermaid` | Mermaid 다이어그램 제외 | 거짓 |

## 🧪 샘플 데이터로 테스트

```bash
# 샘플 데이터 생성
python generate_sample_data.py

# 보고서 생성 테스트
python generate_bace_report.py \
    --results assets/sample_results.csv \
    --output examples/example_report.md \
    --project-name "Test BACE-1 Screening"
```

## 📄 결과 CSV 형식

결과 CSV 파일은 다음 컬럼을 포함해야 합니다:

| 컬럼 | 설명 | 필수 |
|------|------|:---:|
| chembl_id | ChEMBL ID | ✅ |
| smiles | SMILES 문자열 | ✅ |
| bace_activity_prob | BACE 활성 확률 (0~1) | ✅ |
| prediction | 예측 클래스 | ✅ |
| MW | 분자량 | ❌ |
| LogP | LogP 값 | ❌ |
| TPSA | 극성 표면적 | ❌ |
| QED | 약물 유사성 | ❌ |
| LipinskiViolations | Lipinski 위반 수 | ❌ |

## 🔧 커스터마이징

### 보고서 템플릿 수정

`generate_bace_report.py` 파일의 `generate_markdown_report()` 함수를 수정하여 보고서 형식을 변경할 수 있습니다.

### Mermaid 다이어그램 추가

스크립트 내 `generate_mermaid_*()` 함수들을 수정하여 원하는 다이어그램을 추가할 수 있습니다.

## 🌐 GitHub 활용 팁

1. **README에 보고서 링크 추가**
   ```markdown
   ## 보고서
   - [BACE-1 스크리닝 결과](bace_report.md)
   ```

2. **Mermaid 다이어그램 미리보기**
   GitHub는 Mermaid를 기본 지원하므로 별도 이미지 생성 불필요

3. **데이터 파일 관리**
   - 공개 가능한 데이터만 커밋
   - 대용량 파일은 Git LFS 사용 고려

## 📚 관련 자료

- [BACE-1 Wikipedia](https://en.wikipedia.org/wiki/Beta-secretase_1)
- [MoleculeNet](https://moleculenet.org/)
- [ChEMBL Database](https://www.ebi.ac.uk/chembl/)
- [RDKit](https://www.rdkit.org/)

## 🤝 기여하기

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 라이선스

MIT License - 자유롭게 사용, 수정, 배포 가능

---

**문의**: 이슈 탭에 질문을 남겨주세요.
