cmake_minimum_required(VERSION 3.16)

project(stroka C)

add_executable(stroka
    stroka.c
)

set_property(TARGET stroka PROPERTY C_STANDARD 11)
set_property(TARGET stroka PROPERTY C_STANDARD_REQUIRED ON)
set_property(TARGET stroka PROPERTY C_EXTENSIONS OFF)


if (MSVC)
    target_compile_options(stroka PRIVATE
        /W4
        /permissive-
    )
else()
    target_compile_options(stroka PRIVATE
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
