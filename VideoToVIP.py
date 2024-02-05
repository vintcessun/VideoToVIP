#灵感来自于UP主博雅小骆驼原视频为AV1150055073
#本代码作者为UP主恒星sun
#推荐使用ffmpeg对视频进行先头处理，先转换成30帧（其实是我懒得再写代码了，就用造好的能用就行）
#ffmpeg -ss 0 -to 20 -i 鸡块旋转四分钟.mp4 -r 30 output.mp4
from moviepy.editor import *
from PIL import Image
import os
import moviepy.video.io.ImageSequenceClip


def Video_30fpsToVIPVideo(filename,output):
    ##变量名：
    #v->video
    #v2->video2
    #img->images
    #fn->filename
    #fn_1->filename2
    #a->audio
    #f_l->filelist
    
    v=VideoFileClip(filename)
    f_l=[]
    img = Image.new('RGB', v.size, (255, 255, 255))
    for idx, frame in enumerate(v.iter_frames()):
        fn="imgs/frame{}.png".format(2*(int(idx))+1)
        fn_1="imgs/frame{}.png".format(2*(int(idx)))
        f_l=f_l+[fn_1,fn]
        Image.fromarray(frame).save(fn)
        img.save(fn_1)
    
    v2=moviepy.video.io.ImageSequenceClip.ImageSequenceClip(f_l, fps=60)
    v2.set_audio(v.audio)
    v2.write_videofile(output,fps=60)

if __name__=='__main__':
    Video_30fpsToVIPVideo("output.mp4","result.mp4")
