cmake_minimum_required(VERSION 3.0)
project(edgex)

include_directories(/home/qinyong/device-sdk-c/build/release/_CPack_Packages/Linux/TGZ/csdk-1.2.1/include)
link_directories(/home/qinyong/device-sdk-c/build/release/_CPack_Packages/Linux/TGZ/csdk-1.2.1/lib)

add_executable(main ../random.c)
target_link_libraries(main libcsdk.so)
