from moviepy.editor import TextClip, concatenate_videoclips

def generate_text_video(script_lines, output_file="output/video.mp4"):
    clips = []
    for line in script_lines:
        txt_clip = TextClip(line, fontsize=50, color='white', bg_color='black', size=(1280, 720))
        txt_clip = txt_clip.set_duration(3).set_position('center')
        clips.append(txt_clip)

    final_video = concatenate_videoclips(clips)
    final_video.write_videofile(output_file, fps=24)
