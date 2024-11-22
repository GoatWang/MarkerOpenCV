#include <string>
#include <iomanip>
#include <iostream>
#include <filesystem>
#include <opencv2/aruco.hpp>
#include <opencv2/opencv.hpp>

using namespace std;

int main() {

    // string dir = "images";
    std::filesystem::path dir = "images";
    if (!filesystem::exists(dir)) {
        filesystem::create_directory(dir);
    }

    cv::Mat markerImage;
    cv::aruco::Dictionary dictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_6X6_250);

    for (int i = 0; i < 3; i++) {
        cout << setfill('0') << setw(2) << i << endl;
        cv::aruco::generateImageMarker(dictionary, i, 200, markerImage, 1);
        std::filesystem::path filename = dir / ("marker" + std::to_string(i) + ".png");
        cv::imwrite(filename, markerImage);
        cout << "file has been saved to " << filename << endl;
    }
    return 0;
}