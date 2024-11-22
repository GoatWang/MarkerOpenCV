1. find the location of opencv
    ```
    pkg-config --cflags --libs opencv4
    ```


is in the "/usr/local/include/opencv4/opencv2"




-std=c++11
g++ -o check_aruco check_aruco.cpp -I/opt/homebrew/Cellar/opencv/4.10.0/include/opencv4/ -L/opt/homebrew/Cellar/opencv/4.10.0/lib -lopencv_core -lopencv_imgcodecs -lopencv_highgui -lopencv_aruco -lopencv_imgproc -lopencv_calib3d

g++ -o check_aruco check_aruco.cpp


g++ -std=c++11 -c check_aruco.cpp `pkg-config --cflags --libs opencv4`
g++ -std=c++11 -o check_aruco check_aruco.cpp `pkg-config --cflags --libs opencv4`

clang++ -std=c++11 -c check_aruco.cpp -I/usr/local/include/opencv4



g++ -std=c++17 -o aruco_test check_aruco.cpp -I/opt/homebrew/opt/opencv/include/opencv4 -L/opt/homebrew/opt/opencv/lib -lopencv_core -lopencv_imgproc -lopencv_aruco -lopencv_highgui
g++ -std=c++17 -o check_aruco check_aruco.cpp `pkg-config --cflags --libs opencv4`
g++ -o check_aruco check_aruco.cpp `pkg-config --cflags --libs opencv4`


g++ -std=c++17 -o marker_generator marker_generator.cpp `pkg-config --cflags --libs opencv4`


cv::Mat markerImage;
cv::aruco::Dictionary dictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_6X6_250);
cv::aruco::generateImageMarker(dictionary, 23, 200, markerImage, 1);
cv::imwrite("marker23.png", markerImage);

# Install OpenCV on mac
1. use brew: `brew install opencv`

2. Storage: use `pkg-config --cflags --libs opencv4` to check
   1. Header Files: `-I/opt/homebrew/opt/opencv/include/opencv4`
   2. Libraries: `-L/opt/homebrew/opt/opencv/lib`

3. Compilation: 
```
g++ -std=c++11 -o marker_generator marker_generator.cpp `pkg-config --cflags --libs opencv4`
```

# Other Tools
```
brew list
brew info opencv
brew list opencv | grep aruco 
brew uninstall opencv
pkg-config --modversion opencv4
```

# Lintint
C/C++: Edit Configureations (JSON)
```
            "includePath": [
                "${workspaceFolder}/**", 
                "/opt/homebrew/opt/opencv/include/opencv4"
            ],
````