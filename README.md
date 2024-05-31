# yolov5  
## 드론 영상에서 객체 인식 
I. 개발환경 만들기 
1. Pc에서 폴더 만들기
    실습환경에 따라 폴더 이름이 다를수 있어요.   
    나는 이곳에 만들고 dataSet폴더를 따로 만들었어요.

![image](https://github.com/jiwon0629/yolov5_Drone/assets/149983498/cf38f66d-64b7-4431-b11b-ac46551c1c01)


2. VSCode를 실행하고 
3. 터미널에서 conda 가상 환경  yolov5를 만들었어요.

![image](https://github.com/jiwon0629/NativeAppYoloCustom/assets/149983498/7340f99b-c129-4c39-83e8-4d5487860cf9)
 
4. VSCode와 가상환경을 연결하세요 CTRL+SHIFT+P
5. 새로운 터미널을 열어서 작업을 시작합니다. 
6. git clone로 yolo 가져오기

![image](https://github.com/jiwon0629/NativeAppYoloCustom/assets/149983498/9d7082d0-fe21-4aaa-a43e-7a4bb201928a)

7. yolo개발 패키지 설치  - pip install -r requirements.txt  

![image](https://github.com/jiwon0629/NativeAppYoloCustom/assets/149983498/18c89030-4a84-4a87-9e3b-7654b7b54c89)

II. 데이터세트 준비  
8. 데이터세트 준비   
zip으로 다운로드 받아서 yolov5 폴더 아래에 dataset 폴더를 만들고 그곳에 풀어줌   

![image](https://github.com/jiwon0629/NativeAppYoloCustom/assets/149983498/92b60a9f-eaa4-4a4d-95d7-be8a92c203b0)


9. dataset 폴더에 있는 data.yaml을 직접 수정 - 폴더의 위치에 집중  

![image](https://github.com/jiwon0629/yolov5_Drone/assets/149983498/db5da1c3-32e8-4838-a21f-d9f344584b97)


우리는 학습을 yolov5 폴더에서 할것이기 때문에 현재 폴더 밑에 ./dataSet이라고 지정을 꼭 하고 저장!  
nc : 5 인것을 기억해 놓기 바랍니다. (custom-yolov5s.yaml에서 사용할 예정)

10. ./models/폴더에 있는 yolov5s.yaml을 복사해서 custom_yolov5s.yaml로 만들기  
그리고 nc : 5로 바꾸어 줍니다.  

![image](https://github.com/jiwon0629/yolov5_Drone/assets/149983498/6695fa92-95f3-4509-94ad-2b9fc229a303)


11. dataset 폴더에 myGlob.py를 만든다(코랩의 내용을 복사)
![image](https://github.com/jiwon0629/yolov5_Drone/assets/149983498/54b031c3-76fb-4d62-97bf-fce590c3134d)  


정상 실행 되면  

![image](https://github.com/jiwon0629/yolov5_Drone/assets/149983498/df324d76-697c-4e5a-b9c5-8dc09b357475)


3개의 txt파일이 만들어 진다 

이렇게 모든 준비가 끝나면  
III. 학습  
11. data.yaml의 위치가 가장 중요하다.  
python train.py  
--img 416 --batch 16 --epochs 100 --data ./dataSet/data.yaml --cfg ./models/custom_yolov5s.yaml --weights '' --name  
_result --cache  

![image](https://github.com/jiwon0629/yolov5_Drone/assets/149983498/4d1c913c-da66-4117-ae39-623e1de21d36)  

여기 까지 하게 되면 best.pt를 구할 수 있고 다음은 inference








DataSet : https://public.roboflow.com/object-detection/aerial-maritime  

![1](https://github.com/jiwon0629/yolov5/assets/149983498/b5ffb12e-9ffe-4732-943f-1d4506e85e1b)
![2](https://github.com/jiwon0629/yolov5/assets/149983498/d82b2307-ddfb-4c5c-bf0d-d8b0f8353dba)

