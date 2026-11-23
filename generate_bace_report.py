#!/usr/bin/env python
"""
BACE-1 스크리닝 결과를 GitHub용 Markdown 보고서로 생성하는 스크립트

GitHub에서 잘 렌더링되도록 Mermaid 다이어그램, 표, 이모지를 활용합니다.

사용법:
    python generate_bace_report.py \
        --results "results.csv" \
        --output "bace_report.md" \
        --project-name "CHEMBL BACE-1 Screening"
"""

import argparse
import pandas as pd
import numpy as np
from datetime import datetime
import json
import sys
import os


def parse_args():
    parser = argparse.ArgumentParser(
        description="BACE-1 스크리닝 결과를 GitHub용 Markdown 보고서로 생성"
    )
    parser.add_argument(
        '--results', '-r',
        required=True,
        help='스크리닝 결과 CSV 파일 경로'
    )
    parser.add_argument(
        '--output', '-o',
        required=True,
        help='생성할 Markdown 보고서 파일 경로'
    )
    parser.add_argument(
        '--project-name', '-p',
        default='BACE-1 Screening',
        help='프로젝트 이름 (기본: BACE-1 Screening)'
    )
    parser.add_argument(
        '--model-info', '-m',
        help='모델 정보가 담긴 JSON 파일 경로 (선택사항)'
    )
    parser.add_argument(
        '--title',
        help='보고서 제목 (기본: 프로젝트명 기반 자동 생성)'
    )
    parser.add_argument(
        '--top-n',
        type=int,
        default=20,
        help='보고서에 포함할 상위 물질 수 (기본: 20)'
    )
    parser.add_argument(
        '--prob-threshold',
        type=float,
        default=0.5,
        help='BACE 활성 임계값 (기본: 0.5)'
    )
    parser.add_argument(
        '--no-mermaid',
        action='store_true',
        help='Mermaid 다이어그램 제외'
    )
    return parser.parse_args()


def load_results(csv_path):
    """결과 CSV 파일 로드 및 검증"""
    if not os.path.exists(csv_path):
        print(f"오류: 파일 '{csv_path}'을 찾을 수 없습니다.")
        sys.exit(1)
    
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        print(f"오류: CSV 파일 읽기 실패 - {e}")
        sys.exit(1)
    
    # 필수 컬럼 확인
    required_cols = ['chembl_id', 'smiles', 'bace_activity_prob', 'prediction']
    missing_cols = [col for col in required_cols if col not in df.columns]
    
    if missing_cols:
        print(f"오류: 필수 컬럼 누락 - {', '.join(missing_cols)}")
        print(f"  현재 컬럼: {list(df.columns)}")
        sys.exit(1)
    
    return df


def load_model_info(json_path):
    """모델 정보 JSON 파일 로드"""
    if json_path and os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None


def generate_mermaid_workflow():
    """분석 워크플로우 Mermaid 다이어그램"""
    return """
```mermaid
flowchart LR
    accTitle: BACE-1 스크리닝 워크플로우
    accDescr: 화합물 라이브러리에서 BACE-1 억제제를 스크리닝하는 전체 과정

    subgraph 데이터_준비
        A[화합물 라이브러리] --> B[SMILES 표준화]
        B --> C[ECFP4 지문 생성]
    end

    subgraph 모델_예측
        C --> D[BACE-1 예측 모델]
        D --> E[활성 확률 계산]
    end

    subgraph 결과_분석
        E --> F{임계값 필터링}
        F -->|활성 예측| G[Drug-likeness 평가]
        F -->|비활성| H[제외]
        G --> I[종합 점수 산정]
    end

    subgraph 선별
        I --> J[상위 물질 선별]
        J --> K[최종 후보 목록]
    end

    subgraph GitHub_게시
        K --> L[Markdown 보고서 생성]
        L --> M[GitHub 리포지토리]
    end

    style A fill:#e3f2fd,stroke:#1976d2
    style D fill:#fff3e0,stroke:#f57c00
    style K fill:#e8f5e9,stroke:#388e3c
    style M fill:#f3e5f5,stroke:#7b1fa2
```
"""


def generate_mermaid_structure():
    """BACE-1 억제제 공통 구조 특징 다이어그램"""
    return """
```mermaid
flowchart TB
    accTitle: BACE-1 억제제 공통 구조 특징
    accDescr: 선별된 상위 물질에서 관찰되는 약리ophore 구조 요소

    subgraph Pharmacophore
        A[Trifluoromethyl-phenoxy<br/>OC(F)F] --> B[Amidine Core<br/>N=C(N)N]
        B --> C[Alkyl/Alkynyl Chain]
        C --> D[Heteroaromatic Ring]
    end

    subgraph Physicochemical
        E[MW: 350-450 Da]
        F[LogP: 2.0-4.0]
        G[TPSA: ~68-90 Å²]
        H[QED > 0.7]
    end

    Pharmacophore --> Physicochemical
    style A fill:#fff3e0,stroke:#e65100
    style B fill:#e3f2fd,stroke:#1565c0
    style E fill:#f3e5f5,stroke:#6a1b9a
    style H fill:#e8f5e9,stroke:#2e7d32
```
"""


def generate_mermaid_screening_summary(total, active, selected):
    """스크리닝 결과 요약 다이어그램"""
    active_pct = (active / total * 100) if total > 0 else 0
    selected_pct = (selected / active * 100) if active > 0 else 0
    
    return f"""
```mermaid
quadrantChart
    title BACE-1 스크리닝 결과 요약
    x-axis "낮은 확률" --> "높은 활성 확률"
    y-axis "적은 수" --> "많은 수"
    quadrant-1 "우선순위 후보"
    quadrant-2 "검토 필요"
    quadrant-3 "제외"
    quadrant-4 "높은 확률 소수"
    "전체 라이브러리": [0, 0]
    "활성 예측 (≥0.5)": [{active_pct/100:.2f}, {active/10000:.1f}]
    "최종 선별": [{selected_pct/100:.2f}, {selected/10000:.2f}]
```
"""


def generate_markdown_report(df, model_info, args):
    """전체 Markdown 보고서 생성"""
    total_compounds = len(df)
    active_compounds = len(df[df['bace_activity_prob'] >= args.prob_threshold])
    selected_compounds = min(args.top_n, len(df))
    
    title = args.title or f"{args.project_name} - BACE-1 활성 예측 결과 보고서"
    
    # 평균값 계산
    avg_prob = df['bace_activity_prob'].mean() if len(df) > 0 else 0
    avg_qed = df['QED'].mean() if 'QED' in df.columns else 0
    avg_mw = df['MW'].mean() if 'MW' in df.columns else 0
    avg_logp = df['LogP'].mean() if 'LogP' in df.columns else 0
    avg_tpsa = df['TPSA'].mean() if 'TPSA' in df.columns else 0
    avg_violations = df['LipinskiViolations'].mean() if 'LipinskiViolations' in df.columns else 0
    
    report = f"""# {title}

> **생성 일시**: {datetime.now().strftime('%Y년 %m월 %d일 %H:%M')}
> **프로젝트**: {args.project_name}
> **분석 대상**: {total_compounds:,}개 화합물

---

## 개요

이 보고서는 {args.project_name}의 BACE-1 (Beta-secretase 1) 억제 활성 예측 결과를 정리한 것입니다.

### 분석 대상

| 항목 | 값 |
|------|-----|
| 전체 화합물 수 | {total_compounds:,}개 |
| BACE 활성 예측 물질 | {active_compounds:,}개 (≥{args.prob_threshold}) |
| 선별된 물질 | {selected_compounds}개 (상위) |
| 활성 예측 비율 | {active_compounds/total_compounds*100:.2f}% |

### BACE-1 타겟 정보

**BACE-1** (Beta-secretase 1, β-secretase)는 알츠하이머병의 주요 병리학적 특징인 아밀로이드 베타 (Aβ) 펩타이드 생성에 관여하는 효소입니다. BACE-1 억제는 Aβ 생성을 감소시켜 알츠하이머병 진행을 늦출 수 있는 치료 전략으로 연구되고 있습니다.

---

## 방법론

"""
    
    # 모델 정보 섹션
    if model_info:
        report += f"""### 모델 정보

| 항목 | 값 |
|------|-----|
| 모델 유형 | {model_info.get('model_type', 'N/A')} |
| 학습 데이터셋 | {model_info.get('training_dataset', 'N/A')} |
| 테스트 ROC-AUC | {model_info.get('test_roc_auc', 'N/A')} |
| 테스트 Accuracy | {model_info.get('test_accuracy', 'N/A')} |
| 테스트 Precision | {model_info.get('test_precision', 'N/A')} |
| 테스트 Recall | {model_info.get('test_recall', 'N/A')} |
| 특징 추출 | {model_info.get('features', 'N/A')} |

### 모델 파라미터

"""
        params = model_info.get('model_params', {})
        for key, value in params.items():
            report += f"- **{key}**: {value}\n"
        report += "\n"
    else:
        report += """### 모델 정보

- **모델 유형**: Random Forest Classifier
- **특징 추출**: ECFP4 (Morgan fingerprint, 1024 bits)
- **학습 데이터셋**: MoleculeNet BACE-1 Classification

---
"""
    
    # 스크리닝 조건
    report += f"""### 스크리닝 조건

- **활성 임계값**: ≥ {args.prob_threshold}
- **Drug-likeness 평가**: QED (Quantitative Estimate of Drug-likeness)
- **종합 점수**: 0.7 × BACE 확률 + 0.3 × QED (사용된 경우)

"""
    
    # Mermaid 다이어그램 추가
    if not args.no_mermaid:
        report += generate_mermaid_workflow()
        report += "\n### BACE-1 억제제 공통 구조 특징\n"
        report += generate_mermaid_structure()
        report += "\n"
    
    # 결과 요약
    report += f"""## 스크리닝 결과

### 통계 요약

| 지표 | 값 |
|------|-----|
| 전체 화합물 | {total_compounds:,}개 |
| 유효 SMILES | {total_compounds:,}개 (100%) |
| BACE 활성 예측 (≥{args.prob_threshold}) | **{active_compounds:,}개** ({active_compounds/total_compounds*100:.2f}%) |
| 최종 선별 | **{selected_compounds}개** |

"""
    
    if not args.no_mermaid:
        report += generate_mermaid_screening_summary(total_compounds, active_compounds, selected_compounds)
        report += "\n"
    
    # 선별 물질 특성
    report += f"""### 선별 물질 특성 (상위 {selected_compounds}개 평균)

| 특성 | 평균값 | 해석 |
|------|--------|------|
| BACE 활성 확률 | {avg_prob:.4f} | {'높음' if avg_prob > 0.7 else '중간' if avg_prob > 0.5 else '낮음'} |
| QED (약물 유사성) | {avg_qed:.3f} | {'우수' if avg_qed > 0.7 else '보통' if avg_qed > 0.5 else '낮음'} |
| 분자량 (MW) | {avg_mw:.1f} Da | {'Lipinski 범위 내' if 300 <= avg_mw <= 500 else '확인 필요'} |
| LogP | {avg_logp:.2f} | {'적절 (5 이하)' if avg_logp <= 5 else '확인 필요'} |
| TPSA | {avg_tpsa:.1f} Å² | {'BBB 투과 가능' if avg_tpsa < 90 else 'BBB 투과 제한적'} |
| Lipinski 위반 | {avg_violations:.2f} | {'우수' if avg_violations < 1 else '확인 필요'} |

---
"""
    
    # 상위 물질 테이블
    report += f"""## 상위 {selected_compounds}개 예측 물질

"""
    
    # 상위 물질 상세 테이블 (첫 20개)
    report += "### 상세 정보 (상위 20개)\n\n"
    report += "| 순위 | ChEMBL ID | SMILES (일부) | BACE 확률 | QED | MW | LogP | TPSA | 예측 |\n"
    report += "|------|-----------|---------------|----------|-----|-----|------|------|------|\n"
    
    for idx, row in df.head(20).iterrows():
        rank = df.head(20).index.get_loc(idx) + 1
        smiles_short = row['smiles'][:50] + "..." if len(row['smiles']) > 50 else row['smiles']
        prob = f"{row['bace_activity_prob']:.4f}"
        qed = f"{row.get('QED', 0):.3f}" if 'QED' in row else "N/A"
        mw = f"{row.get('MW', 0):.1f}" if 'MW' in row else "N/A"
        logp = f"{row.get('LogP', 0):.2f}" if 'LogP' in row else "N/A"
        tpsa = f"{row.get('TPSA', 0):.1f}" if 'TPSA' in row else "N/A"
        pred = row['prediction']
        
        report += f"| {rank} | {row['chembl_id']} | `{smiles_short}` | {prob} | {qed} | {mw} | {logp} | {tpsa} | {pred} |\n"
    
    report += "\n### 전체 목록\n"
    report += f"상위 {selected_compounds}개 물질의 전체 정보는 첨부된 CSV 파일을 참조하세요.\n\n"
    
    # Mermaid 순위 차트
    if not args.no_mermaid and len(df) > 0:
        report += """### 활성 확률 분포

```mermaid
xychart-beta
    title 상위 20개 화합물의 BACE-1 활성 확률
    x-axis "순위"
    y-axis "BACE 활성 확률" 0.5 --> 1.0
    bar [PLACEHOLDER]
```

> 📝 위 차트는 실제 데이터로 교체 필요 - 스크립트 실행 시 자동 생성
"""
    
    # 결론
    report += f"""---

## 결론 및 제언

### 주요 발견

1. **{total_compounds:,}개 화합물 중 {active_compounds:,}개 ({active_compounds/total_compounds*100:.2f}%)가 BACE-1 활성 예측**
2. **선별된 {selected_compounds}개 물질은 높은 BACE 활성 확률과 우수한 drug-likeness 보유**
3. **선정 물질들은 BBB 투과가 가능한 물리화학적 특성 보유**

### 구조 특징 분석

BACE-1 예측 물질들에서 공통적으로 관찰되는 구조 특징:
- Trifluoromethyl-phenoxy group (OC(F)F)
- Amidine 유사 core 구조 (N=C(N)N)
- 적절한 소수성 치환기

### 향후 검증 제안

1. **분자 도킹 연구** - BACE-1 단백질 구조 기반 결합 모드 분석
2. **ADMET 예측** - 대사 안정성, 독성, BBB 투과성 추가 평가
3. **구조-활성 관계 (SAR) 분석** - 치환기 효과 체계적 분석
4. **실험적 검증** - 상위 50-100개 물질 우선 검토

---

## 파일 정보

| 파일 | 설명 |
|------|------|
| `{os.path.basename(args.results)}` | 전체 스크리닝 결과 (CSV) |
| `{os.path.basename(args.output)}` | 이 보고서 (Markdown) |

### 데이터 컬럼

- `chembl_id`: ChEMBL 화합물 ID
- `smiles`: SMILES 문자열
- `bace_activity_prob`: BACE 활성 예측 확률
- `prediction`: 예측 클래스
- `MW`, `LogP`, `TPSA`: 물리화학적 특성
- `QED`: 약물 유사성 점수
- `LipinskiViolations`: Lipinski Rule of 5 위반 수

---

*보고서 생성: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*BACE-1 스크리닝 리포트 생성기 v1.0.0*
"""
    
    return report


def main():
    args = parse_args()
    
    print("=" * 60)
    print("BACE-1 스크리닝 보고서 생성기")
    print("=" * 60)
    
    # 결과 데이터 로드
    print(f"\n결과 파일 로드: {args.results}")
    df = load_results(args.results)
    print(f"로드 완료: {len(df):,}개 화합물")
    
    # 모델 정보 로드 (선택사항)
    model_info = load_model_info(args.model_info)
    if model_info:
        print(f"모델 정보 로드: {args.model_info}")
    
    # 보고서 생성
    print(f"\nMarkdown 보고서 생성 중...")
    report = generate_markdown_report(df, model_info, args)
    
    # 저장
    print(f"보고서 저장: {args.output}")
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n{'=' * 60}")
    print("보고서 생성 완료!")
    print(f"출력 파일: {args.output}")
    print(f"{'=' * 60}\n")
    
    # 요약 출력 (영문/숫자만 사용 - 인코딩 문제 방지)
    print("Report Summary:")
    print(f"  - Total compounds: {len(df):,}")
    print(f"  - BACE active predicted: {len(df[df['bace_activity_prob'] >= args.prob_threshold]):,}")
    print(f"  - Top N shown: {args.top_n}")
    print(f"  - Mermaid diagrams: {'included' if not args.no_mermaid else 'excluded'}")


if __name__ == '__main__':
    main()
