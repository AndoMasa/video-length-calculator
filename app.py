import cv2
from glob import glob
import sys

def main():
    args = sys.argv
    dir_name = args [1]

    videos_path = glob(f'{dir_name}*.mov')

    total_time = 0
    for video_path in videos_path:
        cap = cv2.VideoCapture(video_path)
        video_frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT) # フレーム数を取得する
        video_fps = cap.get(cv2.CAP_PROP_FPS)                 # フレームレートを取得する
        time = video_frame_count / video_fps                  # 長さ（秒）を計算する
        total_time += time

    total_time = round(total_time/60/60, 2)
    print(f'合計時間:{total_time}')

if __name__=="__main__":
        main() 