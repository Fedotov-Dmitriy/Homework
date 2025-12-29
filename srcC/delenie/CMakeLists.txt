cmake_minimum_required(VERSION 3.16)

project(delenie C)

add_executable(delenie main.c)

set_property(TARGET delenie PROPERTY C_STANDARD 11)
set_property(TARGET delenie PROPERTY C_STANDARD_REQUIRED ON)
set_property(TARGET delenie PROPERTY C_EXTENSIONS OFF)

if (MSVC)
    target_compile_options(delenie PRIVATE
        /W4
        /permissive-
    )
else()
    target_compile_options(delenie PRIVATE
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
