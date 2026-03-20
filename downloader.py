import subprocess
import sys
import re

def run_with_progress(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    
    for line in process.stdout:
        line = line.strip()
        if "[download]" in line:
            print(f"\r{line}", end="", flush=True)
        elif "[ffmpeg]" in line or "[ExtractAudio]" in line:
            print(f"\n{line}")
        elif "ERROR" in line:
            print(f"\nERROR: {line}")
    
    process.wait()
    print()


def download(url, mode, output_folder):
    if mode == "video":
        cmd = [sys.executable, "-m", "yt_dlp", "-f", "best", "-o", f"{output_folder}/%(title)s.%(ext)s", url]
    elif mode == "audio":
        cmd = [sys.executable, "-m", "yt_dlp", "-x", "--audio-format", "mp3", "-o", f"{output_folder}/%(title)s.%(ext)s", url]
    elif mode == "image":
        cmd = [sys.executable, "-m", "yt_dlp", "--write-thumbnail", "--skip-download", "-o", f"{output_folder}/%(title)s.%(ext)s", url]
    
    run_with_progress(cmd)

def download_playlist(url, mode, output_folder):
    print("Mendeteksi playlist...")
    if mode == "video":
        cmd = [sys.executable, "-m", "yt_dlp", "-f", "best", "-o", f"{output_folder}/%(playlist_title)s/%(title)s.%(ext)s", url]
    elif mode == "audio":
        cmd = [sys.executable, "-m", "yt_dlp", "-x", "--audio-format", "mp3", "-o", f"{output_folder}/%(playlist_title)s/%(title)s.%(ext)s", url]
    
    run_with_progress(cmd)


def main():
    def main():
    print("=== Downloader ===")
    print("Platform: YouTube, Instagram, TikTok\n")

    url = input("Masukkan URL: ").strip()

    print("\nJenis download:")
    print("1. Video / lagu tunggal")
    print("2. Playlist (YouTube)")

    jenis = input("\nPilihan (1/2): ").strip()

    if jenis == "2":
        print("\nPilih format playlist:")
        print("1. Video (mp4)")
        print("2. Audio (mp3)")
        pilihan_pl = input("\nPilihan (1/2): ").strip()
        mode_map_pl = {"1": "video", "2": "audio"}
        if pilihan_pl not in mode_map_pl:
            print("Pilihan tidak valid!")
            return
        output_folder = input("\nMasukkan folder output (enter = folder ini): ").strip()
        if output_folder == "":
            output_folder = "."
        print("\nMulai download playlist...\n")
        download_playlist(url, mode_map_pl[pilihan_pl], output_folder)
        print("\nSelesai!")
        return

    print("\nPilih format:")
    print("1. Video (mp4)")
    print("2. Audio (mp3)")
    print("3. Gambar / Thumbnail")

    pilihan = input("\nPilihan (1/2/3): ").strip()

    mode_map = {"1": "video", "2": "audio", "3": "image"}

    if pilihan not in mode_map:
        print("Pilihan tidak valid!")
        return

    output_folder = input("\nMasukkan folder output (enter = folder ini): ").strip()
    if output_folder == "":
        output_folder = "."

    print("\nMulai download...\n")
    download(url, mode_map[pilihan], output_folder)
    print("\nSelesai!")

if __name__ == "__main__":
    main()