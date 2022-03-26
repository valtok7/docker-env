cmake_minimum_required(VERSION 3.0.0)
project(hello VERSION 0.1.0)

include(CTest)
enable_testing()

add_executable(hello src/main.cpp)
add_executable(send src/send.cpp src/simple_udp.h)
add_executable(recv src/recv.cpp src/simple_udp.h)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
