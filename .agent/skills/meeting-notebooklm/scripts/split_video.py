import os
import math
import sys
import argparse
from moviepy.editor import VideoFileClip

def split_video_by_size(
    input_file,
    output_dir,
    target_size_mb=190,        # Default slightly under 200MB for safety
    safety_margin=0.95,        # 95% of the target to be safe
    audio_bitrate_kbps=96,     # reasonable mono/stereo speech quality
    overhead_kbps=32,          # container & misc overhead allowance
    min_video_kbps=200,        # don't go below this (keeps output playable)
    preset="medium"            # ffmpeg x264 preset
):
    """
    Splits a video into parts with sizes < target_size_mb by controlling output bitrates per part.
    Modified from user sample code to work locally.
    """
    try:
        # --- 1) Validate paths ---
        if not os.path.exists(input_file):
            print(f"Error: Input file not found at {input_file}")
            return []
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        # --- 2) Inspect input ---
        video = VideoFileClip(input_file)
        duration_seconds = float(video.duration)
        file_size_mb = os.path.getsize(input_file) / (1024 * 1024)
        
        if file_size_mb < target_size_mb:
            print(f"File size {file_size_mb:.2f} MB is already below {target_size_mb} MB. No split needed.")
            video.close()
            return [input_file]

        print("\n--- Source Video ---")
        print(f"File Size: {file_size_mb:.2f} MB")
        print(f"Duration: {duration_seconds:.2f} s")

        # --- 3) Plan split by time using input avg bitrate (for count only) ---
        target_bytes = target_size_mb * 1024 * 1024
        input_bps = os.path.getsize(input_file) / duration_seconds  # bytes per second
        split_duration = target_bytes / input_bps                   # seconds/part (rough)
        num_splits = max(1, math.ceil(duration_seconds / split_duration))
        print("\n--- Planning ---")
        print(f"Target part size: < {target_size_mb} MB")
        print(f"Initial (rough) split duration: {split_duration:.2f} s")
        print(f"Number of parts (planned): {num_splits}")

        file_base = os.path.splitext(os.path.basename(input_file))[0]
        print("\n--- Encoding Parts ---")

        output_files = []
        for i in range(num_splits):
            start = i * split_duration
            end   = min((i + 1) * split_duration, duration_seconds)
            part_duration = max(0.1, end - start)  # guard tiny edge cases

            # Compute total kbps that would keep us < target with margin
            total_kbps_allowed = (target_bytes * safety_margin * 8) / part_duration / 1000.0

            # Allocate kbps between video and audio (+overhead)
            video_kbps = max(min_video_kbps, total_kbps_allowed - audio_bitrate_kbps - overhead_kbps)

            # Expected size check (MB)
            expected_bits = (video_kbps + audio_bitrate_kbps + overhead_kbps) * 1000 * part_duration
            expected_mb   = expected_bits / 8 / (1024 * 1024)

            out_name = f"{file_base}_part_{i+1}.mp4"
            out_path = os.path.join(output_dir, out_name)

            print(f"\nPart {i+1}/{num_splits}")
            print(f"Start: {start:.2f}s  End: {end:.2f}s  Duration: {part_duration:.2f}s")
            print(f"Bitrate plan → video: {int(video_kbps)}k, audio: {audio_bitrate_kbps}k, overhead: {overhead_kbps}k")
            print(f"Expected size: ~{expected_mb:.2f} MB (< {target_size_mb} MB)")

            sub = video.subclip(start, end)
            # Important: set constant target bitrates so size is predictable
            sub.write_videofile(
                out_path,
                codec="libx264",
                audio_codec="aac",
                bitrate=f"{int(video_kbps)}k",
                audio_bitrate=f"{audio_bitrate_kbps}k",
                preset=preset,
                threads=None,
                logger=None # Suppress progress bar noise in logs
            )

            # Post-check actual size
            actual_mb = os.path.getsize(out_path) / (1024 * 1024)
            if actual_mb >= target_size_mb:
                print(f"WARNING: {out_name} is {actual_mb:.2f} MB (>= {target_size_mb} MB).")
            else:
                print(f"Saved: {out_path}  ({actual_mb:.2f} MB)")
            
            output_files.append(out_path)

        video.close()
        print("\n--- Done ---")
        return output_files

    except Exception as e:
        print(f"\nError: {e}")
        return []

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split video into parts of target size.")
    parser.add_argument("input", help="Input video file path")
    parser.add_argument("output_dir", help="Output directory")
    parser.add_argument("--size", type=int, default=190, help="Target size in MB (default: 190)")
    
    args = parser.parse_args()
    
    split_video_by_size(args.input, args.output_dir, args.size)
