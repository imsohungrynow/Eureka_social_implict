# Eureka (동국대학교 산업 IAI 연구실)  
## 최종 목표
산업 현장 영상으로부터 실시간으로 위험 요소 및 상황을 탐지하고, 경로 예측을 통해 객체 요소 간 충돌을 예측하여 통합 위험도 산출  

<H1 align="center">
Eureka_social_implict</H1>


## 본 Repository
#### 탐지 된 객체에 대한 경로 예측  
- Forked by
https://github.com/abduallahmohamed/Social-Implicit.git

#### 탐지 객체
- person, forklift

## Steps to run Code  

### 환경 만들기
- Create anaconda environment
```
conda create -n {env name} python=3.9
```

### 초기 세팅 방법!

- Clone the repository
```
git clone https://github.com/imsohungrynow/Eureka_social_implict.git
```
- Goto the cloned folder.
```
cd Eureka_social_implict
```
- Install the requirements
```
pip install -r requirements.txt
```

## Code 구성
- train.py for training the code
- test_amd_amv_kde.py to test the models and report the AMD/AMV/KDE metrics
- test_ade_fde.py to test the models and report the ADE/FDE metrics 
- CFG.py contains model configratuin parameters 
- metrics.py contains ADE/FDE implementation 
- amd_amv_kde.py contains the AMD/AMV/KDE implementation 
- trajectory_augmenter.py contains the augmentations techniques for trajectories 
- utils.py general utils used by the code 
- pkls folder: stores the data pickles 
- datasets folder: contains the ETH/UCY raw data and SDD data from [DAG net](https://github.com/alexmonti19/dagnet/blob/master/datasets/README.md)
- checkpoint folder: contains the trained models

## code run

### To report the AMD/AMV/KDE 
```
python3 test_amd_amv_kde.py
```
Note that the code will take a while to run becuase the GMM fit version we use is not vecotrized version. 
### To report the ADE/FDE
```
python3 test_ade_fde.py
```

## Visualization 
The visualization script compares our model with prior models.  
- Social-implict 와 다른 모델들 비교
The visualization data is precomputed and can be downloaded using
- 사전 계산되어 다운로드하여 사용
```
Visualization/downloadVisualData.sh
```
Then you will need to run the notebook
```
Align.ipynb
```
In order to generate a suitable visualization pkls aligning the raw outputs of the models. Aftewards, 
you can visualize everything using either the zoomed or the aspect ratio constarined visualization notebooks. 
- 모델의 원시 출력들을 정렬하는 적절한 시각화 pkls를 생성 & 시각화
```
Visualize.ipynb
VisualizeZoomed.ipynb
```
