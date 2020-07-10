# encoding: utf-8
from moviepy.editor import *
from moviepy.editor import VideoFileClip, clips_array, vfx
import math
import random

def movie_upside(vedio_path):
    """
    倒序播放
    :return:
    """
    clip1 = VideoFileClip(vedio_path, audio=False).fx(vfx.crop).subclip(0, 4)
    clip_upside = clip1.fx(vfx.time_mirror) #倒序播放
    return clip_upside
    # clip_upside.write_videofile(r'D:\upside.mp4')

def movie_reverse(vedio_path):
    """
    旋转角度播放
    :return:
    """
    clip = VideoFileClip(vedio_path, audio=False)
    clip_reverse = clip.rotate(180) #旋转180度播放
    return clip_reverse


def part1(vedio_path,output_path):
    print("part1 拼接中---------")
    clip1 = movie_upside(vedio_path)
    clip2 = movie_reverse(vedio_path)  # x轴镜像
    final_clip = clips_array([
        [clip1, clip2],

    ])
    final_clip.write_videofile(output_path)
    return output_path

def part2(vedio_path,output_path):
    """
    堆叠
    :param vedio_path:
    :return:
    """
    print("part2 拼接中---------")
    clip = VideoFileClip(vedio_path, audio=False)
    clip2 = VideoFileClip(vedio_path, audio=False).add_mask().resize(0.5)

    final_clip = clip2.rotate(lambda t:20*t)
    final_clip = CompositeVideoClip([clip, final_clip.set_pos("center").set_start(1)],bg_color=(255,255,255))

    final_clip.write_videofile(output_path,fps=10)
    final_clip.close()
    return output_path



def part3(vedio_path,output_path):
    """
    时间轴特效
    :return:
    """
    print("part3 拼接中---------")

    try:
        clip = VideoFileClip(vedio_path, audio=False)
        modifiedClip1 = clip.fl_time(lambda t: 1.5 * t,)  #倍速
        modifiedClip2 = clip.fl_time(lambda t: 2 * t)
        modifiedClip3 = clip.fl_time(lambda t: 2.5 * t)
        final_clip = clips_array([
            [clip,modifiedClip1],
            [modifiedClip2,modifiedClip3],

        ])
        final_clip.duration =clip.duration

        final_clip.write_videofile(output_path)
        final_clip.close()
    except Exception:
        pass
    return output_path




def part4(vedio_path,output_path):
    """
    图片轴特效
    :return:
    """
    print("part4 拼接中---------")
    clip = VideoFileClip(vedio_path, audio=False)

    #会把一个clip每一帧的绿色和蓝色通道转换
    def invert_green_blue(image):
        return image[:, :, [0, 2, 1]]

    def invert_red_bule(image):
        return image[:, :, [2, 1, 0]]
    modifiedClip1 = clip.fl_image(invert_green_blue)
    modifiedClip2 = clip.fl_image(invert_red_bule)
    final_clip = clips_array([
        [modifiedClip1,modifiedClip2],
    ])
    final_clip.write_videofile(output_path)
    return output_path
def main():
    vedio_path = "1.mp4"
    part1_path ="part1_new.mp4"
    part2_path = "part2_new.mp4"
    part3_path = "part3_new.mp4"
    part4_path = "part4_new.mp4"
    res = "res.mp4"
    part1(vedio_path,part1_path)
    part2(vedio_path,part2_path)
    part3(vedio_path,part3_path)
    part4(vedio_path,part4_path)

    clip1 = VideoFileClip(part1_path, audio=False)
    clip2 = VideoFileClip(part2_path, audio=False)
    clip3 = VideoFileClip(part3_path, audio=False)
    clip4 = VideoFileClip(part4_path, audio=False)
    #
    x = (int(clip1.size[0] / 3), int(clip1.size[1] / 3)-80)
    final_clip = CompositeVideoClip(
        [
            clip1,
            clip2.set_pos(x).set_start(5).crossfadein(1),
         clip3.set_start(11).crossfadein(1),
         clip4.set_start(16),
    ],bg_color=(255,255,0))
    final_clip.duration = clip1.duration+clip2.duration+clip3.duration+clip4.duration+2

    # final_clip = VideoFileClip(res, audio=False)
    # 设置背景音乐
    audioclip = AudioFileClip("bg.mp3")
    audioclip.duration = final_clip.duration
    final_clip = final_clip.set_audio(audioclip)

    final_clip.write_videofile(res)
    final_clip.close()

if __name__=='__main__':
    main()
