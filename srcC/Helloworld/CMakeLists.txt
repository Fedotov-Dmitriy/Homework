cmake_minimum_required(VERSION 3.16)

project(hello C)

add_executable(hello hello.c)

set_property(TARGET hello PROPERTY C_STANDARD 11)
set_property(TARGET hello PROPERTY C_STANDARD_REQUIRED ON)
set_property(TARGET hello PROPERTY C_EXTENSIONS OFF)


if (MSVC)
    target_compile_options(hello PRIVATE /W4 /permissive-)
else()
    target_compile_options(hello PRIVATE
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
