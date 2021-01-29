import subprocess

def main():
    quality = input("Pass desired quality of the map. Options are: 'Low', 'High', 'Epic'. \n")
    if quality == "":
        quality = "Low"
    subprocess.Popen('CarlaUE4.exe' + f' -windowed -carla-server -benchmark -fps=20 -quality-level=' + quality,
                          cwd='./', shell=True)

if __name__ == '__main__':
   main()