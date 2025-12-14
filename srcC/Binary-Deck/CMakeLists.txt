cmake_minimum_required(VERSION 3.10)
project(binary_to_deck)

option(TESTS "Build tests" OFF)

add_library(binary_to_deck STATIC binary_to_deck.c)
target_link_libraries(binary_to_deck m)

add_executable(main main.c)
target_link_libraries(main binary_to_deck)

if(TESTS)
    add_executable(test binaryTests.c)
    target_link_libraries(test binary_to_deck)
endif()
