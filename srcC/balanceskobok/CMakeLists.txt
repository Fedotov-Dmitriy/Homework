cmake_minimum_required(VERSION 3.16)

project(balanceskobok C)

add_executable(balanceskobok
    balanceskobok.c
)

set_property(TARGET balanceskobok PROPERTY C_STANDARD 11)
set_property(TARGET balanceskobok PROPERTY C_STANDARD_REQUIRED ON)
set_property(TARGET balanceskobok PROPERTY C_EXTENSIONS OFF)



if (MSVC)
    target_compile_options(balanceskobok PRIVATE
        /W4
        /permissive-
    )
else()
    target_compile_options(balanceskobok PRIVATE
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
