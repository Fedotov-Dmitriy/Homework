cmake_minimum_required(VERSION 3.16)

project(nullarray C)

add_executable(nullarray
    nullarray.c
)

set_property(TARGET nullarray PROPERTY C_STANDARD 11)
set_property(TARGET nullarray PROPERTY C_STANDARD_REQUIRED ON)
set_property(TARGET nullarray PROPERTY C_EXTENSIONS OFF)

target_include_directories(nullarray PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})

if (MSVC)
    target_compile_options(nullarray PRIVATE
        /W4
        /permissive-
    )
else()
    target_compile_options(nullarray PRIVATE
        -Wall
        -Wextra
        -Wpedantic
        -Wshadow
        -Wconversion
        -Wsign-conversion
        -Wformat=2
        -Wundef
    )
endif()
