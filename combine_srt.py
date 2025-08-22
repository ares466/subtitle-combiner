import os
import re

def combine_srt_files(directory, output_file):
    """
    Combines SRT files in a directory into a single text file.

    Args:
        directory: The directory containing the SRT files.
        output_file: The path to the output file.
    """
    srt_files = sorted([f for f in os.listdir(directory) if f.endswith(".srt")])
    
    with open(output_file, "w", encoding="utf-8") as outfile:
        for filename in srt_files:
            filepath = os.path.join(directory, filename)
            outfile.write(f"--- {filename} ---\n\n")
            with open(filepath, "r", encoding="utf-8") as infile:
                for line in infile:
                    # ignore the sequence number and timestamp
                    if not line.strip().isdigit() and "-->" not in line:
                        outfile.write(line)
            outfile.write("\n\n")


if __name__ == "__main__":
    srt_directory = "srt_files"
    output_filename = "output/combined_subtitles.txt"
    combine_srt_files(srt_directory, output_filename)
    print(f"Combined subtitles saved to {output_filename}")
