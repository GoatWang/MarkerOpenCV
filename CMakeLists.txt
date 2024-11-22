cmake_minimum_required(VERSION 3.10)

project(TOFPCL LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# set to C++ 17
set(CMAKE_C_COMPILER "clang")
set(CMAKE_CXX_COMPILER "clang++")

# set(CMAKE_PREFIX_PATH "/opt/homebrew/Cellar/libomp/19.1.2")

# include opencv
find_package(OpenCV REQUIRED)
include_directories("/opt/homebrew/opt/opencv/include/opencv4")

# add executable
add_executable(marker_generator src/marker_generator.cpp)

# link opencv
target_link_libraries(marker_generator ${OpenCV_LIBS})
