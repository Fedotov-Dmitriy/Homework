cmake_minimum_required(VERSION 3.16)

project(sort C)

add_executable(sort
    sort.c
    sort_x86.s
)

set_property(TARGET sort PROPERTY C_STANDARD 11)
set_property(TARGET sort PROPERTY C_STANDARD_REQUIRED ON)
set_property(TARGET sort PROPERTY C_EXTENSIONS OFF)


if (MSVC)
    target_compile_options(sort PRIVATE
        /W4
        /permissive-
    )
else()
    target_compile_options(sort PRIVATE
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
