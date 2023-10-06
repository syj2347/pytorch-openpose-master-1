import cv2
import os
import glob
from tqdm import tqdm

root_path = os.path.abspath("./results_img")
video_save_path = os.path.abspath("./frame2vedio")

done_set = {"demo2", "image", "test1", "test2"}


def generateVedio(name_list):
    global video_save_path
    for i in range(len(name_list)):
        if name_list[i] in done_set:
            continue
        person_name = name_list[i]
        frame_path = root_path + "/" + person_name
        image_files = glob.glob(frame_path + "/*.jpg")
        image_files.sort(key=lambda x: int(os.path.splitext(os.path.basename(x))[0].split("_")[-1]))

        first_image = cv2.imread(image_files[0])
        height, width, channels = first_image.shape
        size = (width, height)
        print(size)

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        # 30 is the FPS
        x = 0
        st = 5520
        ed = 5696
        videowrite = cv2.VideoWriter(video_save_path + "/" + person_name + "_" + str(ed) + ".mp4", fourcc, 30, size)
        img_array = []
        for filename in image_files:
            if x < st or x > ed:
                x += 1
                continue
            img = cv2.imread(filename)
            img_array.append(img)
            x += 1

        for j in tqdm(range(ed - st + 1)):
            videowrite.write(img_array[j])

        print("视频{0}_{1}.mp4生成完毕！".format(person_name, ed))


if __name__ == "__main__":
    name_list = os.listdir(root_path)
    print(name_list)
    generateVedio(name_list)
