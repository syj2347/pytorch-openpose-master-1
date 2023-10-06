import cv2
import matplotlib.pyplot as plt
import copy
import numpy as np
import torch
import os
from tqdm import tqdm

from src import model
from src import util
from src.body import Body
from src.hand import Hand

body_estimation = Body('model/body_pose_model.pth')
hand_estimation = Hand('model/hand_pose_model.pth')

print(f"Torch device: {torch.cuda.get_device_name()}")

cap = cv2.VideoCapture("demo2.mp4")
cap.set(3, 640)
cap.set(4, 480)
i = 0
option = 1  # 是否将原图作为背景 0是/1否
exp_name = "final"
output_folder = os.path.join('results_img', exp_name)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

while True:
    ret, oriImg = cap.read()
    output_path = os.path.join(output_folder, '{}_{}.jpg'.format(exp_name, i))
    if os.path.exists(output_path):
        print("Image already exists, skipping frame:", i)
        i += 1
        continue
    candidate, subset = body_estimation(oriImg)
    if option == 0:
        canvas = copy.deepcopy(oriImg)
    else:
        canvas = np.zeros_like(oriImg)
    canvas = util.draw_bodypose(canvas, candidate, subset)

    # # detect hand
    # hands_list = util.handDetect(candidate, subset, oriImg)
    # all_hand_peaks = []
    # for x, y, w, is_left in hands_list:
    #     peaks = hand_estimation(oriImg[y:y + w, x:x + w, :])
    #     peaks[:, 0] = np.where(peaks[:, 0] == 0, peaks[:, 0], peaks[:, 0] + x)
    #     peaks[:, 1] = np.where(peaks[:, 1] == 0, peaks[:, 1], peaks[:, 1] + y)
    #     all_hand_peaks.append(peaks)
    # canvas = util.draw_handpose(canvas, all_hand_peaks)

    # 保存图片
    cv2.imwrite(os.path.join(output_folder, '{}_{}.jpg'.format(exp_name, i)), canvas)
    print(i)
    i += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
