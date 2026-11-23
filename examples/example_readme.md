## 예시 보고서

이 파일은 `generate_bace_report.py` 스크립트로 생성된 보고서의 예시입니다.

### 생성 방법

```bash
python generate_bace_report.py \
    --results assets/sample_results.csv \
    --output examples/example_report.md \
    --project-name "CHEMBL BACE-1 Screening Example" \
    --model-info assets/sample_model_info.json \
    --top-n 20
```

### 보고서 특징

✅ GitHub에서 Mermaid 다이어그램 자동 렌더링  
✅ 표 형식의 구조화된 데이터  
✅ 이모지를 활용한 시각적 구분  
✅ collapsible 섹션 지원  

### 주의

이 예시 파일은 샘플 데이터로 생성되었기 때문에 실제 분석 결과와 다를 수 있습니다.
실제 사용 시에는 자신의 스크리닝 결과 CSV 파일로 생성하세요.
