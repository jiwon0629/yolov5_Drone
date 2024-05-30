from glob import glob
train_img_list = glob('D:/Jiwon/Ai_Model/DRONE/yolov5/dataSet/train/images/*.jpg')
test_img_list = glob('D:/Jiwon/Ai_Model/DRONE/yolov5/dataSet/test/images/*.jpg')
valid_img_list = glob('D:/Jiwon/Ai_Model/DRONE/yolov5/dataSet/valid/images/*.jpg')
print(len(train_img_list), len(test_img_list), len(valid_img_list))


if len(train_img_list) > 0:
    import yaml
    with open('D:/Jiwon/Ai_Model/DRONE/yolov5/dataSet/train.txt','w') as f:
         f.write('\n'.join(train_img_list) + '\n')
    with open('D:/Jiwon/Ai_Model/DRONE/yolov5/dataSet/test.txt','w') as f:
        f.write('\n'.join(test_img_list) + '\n')
    with open('D:/Jiwon/Ai_Model/DRONE/yolov5/dataSet/val.txt','w') as f:
        f.write('\n'.join(valid_img_list) + '\n')
else:
    print("not found")