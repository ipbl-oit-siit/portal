# Image Processing Environment for iPBL

## Objectives
- This page explains how to install both Python and VSCode to constitute our image processing environment.
- It is not affecting the PC environment (like the registry) even if this environment is installed. <br>
  
    > **Note** All you have to do is delete the folder when this environment is no longer needed.
  
  <br>

#### Details of the installed environment
- Python3.10.11.amd64 (WPy64-310111)
  - dlib 19.24.2
  - matplotlib 3.8.4
  - mediapipe 0.10.11
  - numpy 1.26.4
  - opencv-contrib-python 4.9.0.80
  - opencv-python 4.9.0.80
  - Pillow 10.3.0
  - pip 24.0
  - PyAutoGUI 0.9.54
  - PyDirectInput 1.0.4
  - PyQt5 5.15.10
  - pyqtgraph 0.13.7
  - pywin32 306
  - scikit-learn 1.4.2
  - scipy 1.13.0 <br>
  and more...
- Visual Studio Code 1.87.2 (Portable)

## prerequisite
- Windows 10 or 11
- Built-in camera or USB-camera
- Uninstalling or stopping antivirus software
  - They may remove our installer and batch files.

## Setup both Python and VSCode with our installer
### procedure
- Input PW and Download our installer file by clicking the following URL.
    - [py24ipbl_install.exe](https://oskit-my.sharepoint.com/:u:/g/personal/yoshiyuki_kamakura_oit_ac_jp/EUtCHAQ4YodPiPsj98XU7-MBpznKn3AKZ0PVCbmOelydqg?e=gvmRcA)<br>
      <image src="../image/pw.png" width="40%" height="40%">    <image src="../image/dl.png" width="40%" height="40%"><br>
      - **PW is written on XXXX.**
      - If you have installed some antivirus software, this executable file and other batch files may not work properly.
- Execute "py24ipbl_install.exe" file.
    > **Note**
    > - This installer is safe.<br>
    > - If the following warning pops up (The background color is red in some cases.), Please choose "run anyway" after clicking the "more info" link. <br>
    > <image src="../image/warning01.png" width="40%" height="40%"><br>
    > <image src="../image/warning02.png" width="40%" height="40%"><br>
    > - Please select `More info` and `Run anyway`.
- Choose "次へ(N)" means NEXT.<br>
  <image src="../image/inst01.png" width="40%" height="40%"><br>
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
- This installer sets up the image processing environment (Python3.X + VSCode) into "C:\oit\py24", creates the folder for source code in "C:\oit\home\ipbl24" and creates the following link on your Desktop.<br>
  <image src="../image/icon.png" width="10%" height="10%">

> **Note**
> Creating a link on the Desktop often fails. In that case, please run "C:\oit\py24\ipbl24_start.bat" directly. It is possible to create the link manually, but DO NOT move anything in the py24 folder!)

#### Installed folder structure
- This environment is installed to "C:\oit\py24\" and "C:\oit\home\ipbl24\" and its inside is included the following.
  - **C:\oit\home\ipbl24**: the working directory for saving the source code (Directory "py24" NEED NOT touch)
  - **C:\oit\py24\_tmp_**: NEED NOT touch
  - **C:\oit\py24\VSCode**: NEED NOT touch, Visual Studio Code 1.87.2
  - **C:\oit\py24\WPy64-31180**: NEED NOT touch, Python3.11.8.amd64 (WPy64-31180)
  - **C:\oit\py24\py24_start.bat**: NEED NOT touch 
  - **C:\oit\py24\ipbl24_start.bat**: bat file to start this environment up 

### :o:Checkpoint(Start the environment 1)
- Start the environment from "ipbl24_start" icon on the Desktop (or C:\oit\py24\ipbl24_start.bat).
- **If the following warning pops up...**
  - **CHECK** the "Trust the authors..." box out
  - CLICK the **"YES"** button <br>
    <image src="../image/trust_vsws.png" width="50%" height="50%">

### :o:Checkpoint(Start the environment 2)
- **If the location of the EXPLORER does not be the SouceCode folder(SOURCECODE), you have to open the "C:\oit\home\ipbl24\" from the [File]-[Open Folder] menu.** <br>
  <image src="../image/vsws_explorer.png" width="50%" height="50%">
- **If the terminal window has not shown, please open it from the [Terminal]-[New Terminal] menu.** <br>
  <image src="../image/vsws_tmenu.png" width="50%" height="50%">
- Please confirm Python modules by inputting the `pip list` command in the terminal window.<br>
  <image src="../image/vsws_piplist.png" width="50%" height="50%">

### :o:Checkpoint(Run python code with VSCode)
- Please confirm how to execute the sample Python code with VSCode.
  - Open the "hello_python.py" file with Double Click in [ipbl24] folder of the explorer menu.<br>
    <image src="../image/vs_sample1.png" width="100%" height="100%">
  - Open the terminal window if it has not appeared.<br>
    <br>
    > **Note** The current Working directory shown in the terminal window has to be the same as the file's location to execute. <br>
    > **Note** You have to change the directory using the 'cd' command, in case the current directory shown in the terminal window is different from the source code directory. <br>
    <br>
  - Please confirm that the Python code can execute in the terminal window.
    ```sh
    C:\oit\py23_ipbl\SourceCode\samples> python hello_python.py
    ```
    <br>
    
    > **Note** The program is executable with the run button, but **we suggest executing with the command line**. <br>
    > <image src="../image/vs_runbutton.png"><br>
    <br>

  - The following are running results successfully.<br>
    <image src="../image/vs_runsample1.png"><br>

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
- Give it a try to run the "test_mediapipe.py"
  - This program is written in the old usage of the Mediapipe, but you can experiment with the following methods defined in the Mediapipe.<br>
    - All methods simultaneously with \'a\' button
    - FACE with \'f\' button
    - FACE MESH with \'m\' button
    - HANDS with \'h\' button
    - POSE with \'p\' button <br>
  
  <br>
  
  > **Note** The latest usage of the Mediapipe is able to be learned in another section.

  <br>
