# Image Processing Environment for iPBL

## Objectives
- This page explains how to install both Python and VSCode to constitute our image processing environment.
- It is not affecting the PC environment (like the registry) even if this environment is installed. <br>
  
    > **Note** All you have to do is delete the folder when this environment is no longer needed.
  
  <br>

#### Details of the installed environment
- Python3.12.10
  - [requirements.txt](./requirements.txt)
  - If you do not use the provided portable Python environment, please set up the environment using the above requirements.txt in a virtual environment.
- Visual Studio Code 1.102.3 (Portable)

## prerequisite
- Windows 10 or 11
- Built-in camera or USB-camera
- Uninstalling or stopping antivirus software
  - They may remove our installer and batch files.

## Setup both Python and VSCode with our installer
### Installation of py25en Instructions
- Download our installer file by clicking the following URL.
    - [py25en.exe](https://oskit-my.sharepoint.com/:u:/g/personal/yoshiyuki_kamakura_oit_ac_jp/EX6OAXWBpUtIsGnJsNBTvu0BJBw1vkrZ7GdApoSqDaBigw)<br>
      <image src="../image/pw.png" width="40%" height="40%"> <image src="../image/dl.png" width="40%" height="40%"><br>
    - If you have installed some antivirus software, this executable file and other batch files may not work properly.
- Execute "py25en.exe" file.
    > **Note**
    > - This installer is safe.<br>
    > - If the following warning pops up (The background color is red in some cases.), Please choose "run anyway" after clicking the "more info" link. <br>
    > <image src="../image/warning01.png" width="40%" height="40%"><br>
    > <image src="../image/warning02.png" width="40%" height="40%"><br>
    > - Please select `More info` and `Run anyway`.
- Choose "次へ(N)" means NEXT.<br>
  <image src="../image/inst01.png" width="40%" height="40%"><br>
  > Process of installation...<br>
  > <image src="../image/inst02.png" width="40%" height="40%"><br>
  > Process of installation...<br>
  > <image src="../image/inst03.png" width="40%" height="40%"><br>
  <!--
    > **Note** 
    > The following process skips if you've already installed "py24"<br>
    >  - The following image shows the process for downloading py24.<br>
    >    <image src="../image/inst02.png" width="40%" height="40%"><br>
    >  - Choose "次へ(N)" means NEXT.<br>
    >    <image src="../image/inst03.png" width="40%" height="40%"><br>
    >  - The following image shows the process for installing py24.<br>
    >    <image src="../image/inst04.png" width="40%" height="40%"><br>
    >  - The following image shows the process for installing libraries for Python.<br>
    >    <image src="../image/inst05.png" width="40%" height="40%"><br>
  -->
- This installer sets up the image processing environment (Python3.X + VSCode) into "C:\oit\py25en", creates the folder for source code in "C:\oit\py25en\source" and creates the following link on your Desktop.<br>
  <image src="../image/icon.png" width="10%" height="10%">

> **Note**
> Creating a link on the Desktop often fails. In that case, please run "C:\oit\py25en\py25en_start.bat" directly. It is possible to create the link manually, but DO NOT move anything in the `py25en` folder!)

#### Installed folder structure
- This environment is installed to "C:\oit\py25en\" and its inside is included the following.
  - **C:\oit\py25en\source**: the working directory for saving the source code (Directory "py25en" NEED NOT touch)
  - **C:\oit\py25en\\_tmp_**: NEED NOT touch
  - **C:\oit\py25en\VSCode**: NEED NOT touch, Visual Studio Code
  - **C:\oit\py24\WPy64-312101**: NEED NOT touch, Python3.12.10amd64 (WPy64-312101)
  - **C:\oit\py24\py25en_start.bat**: bat file to start this environment up 

### :o:Checkpoint(Start the environment 1)
- Start the environment from "py25en_start" icon on the Desktop (or C:\oit\py25en\py25en_start.bat).
- **If the following warning pops up...**
  - **CHECK** the "Trust the authors..." box out
  - CLICK the **"YES"** button <br>
    <image src="../image/trust_vsws.png" width="50%" height="50%">

### :o:Checkpoint(Start the environment 2)
- **If the location of the EXPLORER does not be the `souce` folder(SOURCE), you have to open the `C:\oit\py25en\sorce\` from the [File]-[Open Folder] menu.** <br>
  <image src="../image/vsws_explorer.png" width="50%" height="50%">
- **If the terminal window has not shown, please open it from the [Terminal]-[New Terminal] menu.** <br>
  <image src="../image/vsws_tmenu.png" width="50%" height="50%">
- Please confirm Python modules by inputting the `pip list` command in the terminal window.<br>
  <image src="../image/vsws_piplist.png" width="50%" height="50%">

### :o:Checkpoint(Start the environment 3)
- **When you select the `.py` file in the Explorer window, if the status bar shows `Select Python Interpreter` ...** <br>
  <image src="../image/vs_setting01.png" width="50%" height="50%">
- **you need to set the path to `python.exe` (`C:\oit\py25en\WPy64-312101\python\python.exe`) as shown below.** <br>
  <image src="../image/vs_setting02.png" width="50%" height="50%"><br>
  <image src="../image/vs_setting03.png" width="50%" height="50%">
- **To check whether the interpreter is set correctly, use the status bar or the command palette (Select Interpreter).**
  <image src="../image/vs_setting04.png" width="50%" height="50%"><br>
  <image src="../image/vs_setting05.png" width="50%" height="50%">

### :o:Checkpoint(Run python code with VSCode)
- Please confirm how to execute the sample Python code with VSCode.
  - Open the "sample1.py" file with Double Click in [source] folder of the explorer menu.<br>
    <image src="../image/vs_sample1.png" width="100%" height="100%">
  - Open the terminal window if it has not appeared.<br>
    <br>
    > **Note** The current Working directory shown in the terminal window has to be the same as the file's location to execute. <br>
    > **Note** You have to change the directory using the 'cd' command, in case the current directory shown in the terminal window is different from the source code directory. <br>
    <br>
  - Please confirm that the Python code can execute in the terminal window.
    ```sh
    C:\oit\py25en\source> python sample1.py
    ```
    <br>
    
    > **Note** The program is executable with the run button, but **we suggest executing with the command line**. <br>
    > <image src="../image/vs_sample2.png"><br>
    <br>

  - The following are running results successfully.<br>
    <image src="../image/vs_sample3.png"><br>

### :o: Practice
- Give it a try to run the ”hello_opencv.py”.
  - It is the sample of reading and showing an image file with the cv2 library.
  - The window is closed if any button is pressed.
- Give it a try to run the "show_video.py"
  - Create a new file" named "show_video.py"<br>
    <image src="../image/create_newfile.png" width="50%" height="50%"><br>
  - The following code is the sample of capturing from the camera and showing frames with the cv2 library.
    - Please copy & paste this code to "show_video.py".
    - The window is closed if \'q\' button is pressed.
    ```
    import cv2
    
    dev = 0
    
    def main():
        cap = cv2.VideoCapture(dev)
        ht = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        wt = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        print(ht," x ", wt)
    
        while cap.isOpened():
            ret, frame = cap.read()
    
            if ret==False or cv2.waitKey(1) == ord('q'):
                break
    
            cv2.imshow("video", frame)
        
        cap.release()
        cv2.destroyAllWindows()
    
    if __name__=='__main__':
        main()
    ```
  
  > **Note** The latest usage of the Mediapipe is able to be learned in another section.

  <br>
