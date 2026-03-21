import imageio
import numpy as np
import argparse

def crop_center_square(frame):
    """
    接收一个 numpy 数组 (H, W, C)，返回中心裁剪后的正方形数组
    """
    h, w, _ = frame.shape
    min_dim = min(h, w)
    
    # 计算裁剪的起始点
    start_x = (w - min_dim) // 2
    start_y = (h - min_dim) // 2
    
    # NumPy 切片: [y开始:y结束, x开始:x结束, 所有通道]
    return frame[start_y : start_y + min_dim, start_x : start_x + min_dim, :]

def process_video(input_path, output_path, max_frames=None, target_fps=24):
    try:
        # 1. 获取读取器
        reader = imageio.get_reader(input_path)
        meta = reader.get_meta_data()
        original_fps = meta.get('fps', 24)
        
        print(f"原始视频信息: {meta['size']}, FPS: {original_fps}")

        # 2. 获取写入器
        # macro_block_size=1 是为了防止裁剪后的尺寸不能被16整除导致报错
        writer = imageio.get_writer(output_path, fps=target_fps, macro_block_size=1)

        count = 0
        
        # 3. 逐帧处理
        for i, frame in enumerate(reader):
            # 如果设置了最大帧数，且超过了，就停止
            if max_frames and i >= max_frames:
                break

            # 执行中心裁剪
            cropped_frame = crop_center_square(frame)
            
            # 写入新视频
            writer.append_data(cropped_frame)
            count += 1

            # 简单的进度打印
            if count % 24 == 0:
                print(f"已处理 {count} 帧...", end='\r')

        writer.close()
        reader.close()
        print(f"\n完成！已保存到 {output_path} (共 {count} 帧)")

    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="使用 imageio 进行视频中心最大正方形裁剪")
    parser.add_argument("--input", "-i", type=str, required=True, help="输入视频路径")
    parser.add_argument("--output", "-o", type=str, required=True, help="输出视频路径")
    parser.add_argument("--frames", "-t", type=int, default=None, help="保留前T帧 (可选，不填则处理所有)")
    parser.add_argument("--fps", type=int, default=24, help="输出FPS (默认24)")
    
    args = parser.parse_args()
    
    process_video(args.input, args.output, args.frames, args.fps)

'''
cd /apdcephfs/private_jarrentwu_qy4/siggraph26/Project\ Page
python /apdcephfs/private_jarrentwu_qy4/siggraph26/Project\ Page/crop_mp4.py \
    -i 1.mp4 \
    -o 1_crop.mp4 \
    -t 64 \
    --fps 30

python /apdcephfs/private_jarrentwu_qy4/siggraph26/Project\ Page/crop_mp4.py \
    -i mt_render.mp4 \
    -o mt_render_ref.mp4 \
    -t 64 \
    --fps 30

python /apdcephfs/private_jarrentwu_qy4/siggraph26/Project\ Page/crop_mp4.py \
    -i walk1.mp4 \
    -o mt_real_ref.mp4 \
    -t 64 \
    --fps 30
'''