# Subtitle Combiner

This project provides a Python script to combine multiple SRT (SubRip Text) files into a single text file. This is useful for creating a transcript from a series of video lectures or for any other purpose where you need to consolidate subtitle information.

## Usage

1.  **Place your SRT files in the `srt_files` directory.**
2.  **Run the `combine_srt.py` script from the root of the project:**

    ```bash
    python combine_srt.py
    ```

3.  **The script will generate a file named `combined_subtitles.txt` in the root of the project.** This file will contain the combined text from all the SRT files, with each file's content separated by a header indicating the original filename.

4. **Use the following prompt to develop a learning plan.**  

Please analyze the provided subtitles from a lecture or series of lectures. Your goal is to create a clear and comprehensive learning plan that helps me understand the key concepts and major topics discussed. The descriptions should be keyword-dense. Please walk me through the learning plan step-by-step only moving onto the next concept when I've understood the current concept.
