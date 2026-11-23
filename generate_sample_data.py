#!/usr/bin/env python
"""
샘플 결과를 생성하여 보고서 생성 스크립트 테스트
"""

import pandas as pd
import numpy as np

# 샘플 데이터 생성
np.random.seed(42)

n_samples = 100

data = {
    'chembl_id': [f'CHEMBL{1000000 + i}' for i in range(n_samples)],
    'smiles': [
        'CCCC#Cc1cccc([C@@]2(c3ccc(OC(F)F)cc3)N=C(N)N(C)C2=O)c1',
        'CN1C(=O)[C@@](c2ccc(OC(F)F)cc2)(c2cccc(C#CCF)c2)N=C1N',
        'CCC#Cc1cccc([C@@]2(c3ccc(OC(F)F)cc3)N=C(N)N(C)C2=O)c1',
        'Cc1cc([C@]2(c3cccc(C#CCF)c3)N=C(N)N(C)C2=O)ccc1OC(F)F',
        'CN1C(=O)[C@@](c2ccc(OC(F)F)cc2)(c2cccc(C#CCCF)c2)N=C1N',
    ] * 20,
    'bace_activity_prob': np.random.uniform(0.5, 0.98, n_samples),
    'prediction': np.random.choice(['Active', 'Potential'], n_samples, p=[0.7, 0.3]),
    'MW': np.random.uniform(350, 450, n_samples),
    'LogP': np.random.uniform(2.0, 4.5, n_samples),
    'TPSA': np.random.uniform(60, 100, n_samples),
    'HBA': np.random.randint(3, 7, n_samples),
    'HBD': np.random.randint(0, 3, n_samples),
    'RotatableBonds': np.random.randint(2, 8, n_samples),
    'NumAromaticRings': np.random.randint(1, 3, n_samples),
    'NumHeterocycles': np.random.randint(0, 3, n_samples),
    'FractionCSP3': np.random.uniform(0.15, 0.4, n_samples),
    'QED': np.random.uniform(0.6, 0.95, n_samples),
    'LipinskiViolations': np.random.randint(0, 2, n_samples),
}

df = pd.DataFrame(data)
df['composite_score'] = 0.7 * df['bace_activity_prob'] + 0.3 * df['QED']

# 정렬
df = df.sort_values('composite_score', ascending=False).reset_index(drop=True)

# 저장
df.to_csv('D:/deep-learning/skills/bace-screening-report/assets/sample_results.csv', index=False)
print(f"샘플 데이터 생성 완료: {len(df)}개 화합물")
print(f"저장 위치: assets/sample_results.csv")
