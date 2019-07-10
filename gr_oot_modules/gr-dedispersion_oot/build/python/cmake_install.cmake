# Install script for directory: /home/andy/FRB_Pipeline_and_Contributions/gr-transient/gr_oot_modules/gr-dedispersion_oot/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/dedispersion_oot" TYPE FILE FILES
    "/home/andy/FRB_Pipeline_and_Contributions/gr-transient/gr_oot_modules/gr-dedispersion_oot/python/__init__.py"
    "/home/andy/FRB_Pipeline_and_Contributions/gr-transient/gr_oot_modules/gr-dedispersion_oot/python/dedisperse_roll.py"
    "/home/andy/FRB_Pipeline_and_Contributions/gr-transient/gr_oot_modules/gr-dedispersion_oot/python/Pulse_Detection.py"
    "/home/andy/FRB_Pipeline_and_Contributions/gr-transient/gr_oot_modules/gr-dedispersion_oot/python/Kelvin_to_Janskey.py"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/dedispersion_oot" TYPE FILE FILES
    "/home/andy/FRB_Pipeline_and_Contributions/gr-transient/gr_oot_modules/gr-dedispersion_oot/build/python/__init__.pyc"
    "/home/andy/FRB_Pipeline_and_Contributions/gr-transient/gr_oot_modules/gr-dedispersion_oot/build/python/dedisperse_roll.pyc"
    "/home/andy/FRB_Pipeline_and_Contributions/gr-transient/gr_oot_modules/gr-dedispersion_oot/build/python/Pulse_Detection.pyc"
    "/home/andy/FRB_Pipeline_and_Contributions/gr-transient/gr_oot_modules/gr-dedispersion_oot/build/python/Kelvin_to_Janskey.pyc"
    "/home/andy/FRB_Pipeline_and_Contributions/gr-transient/gr_oot_modules/gr-dedispersion_oot/build/python/__init__.pyo"
    "/home/andy/FRB_Pipeline_and_Contributions/gr-transient/gr_oot_modules/gr-dedispersion_oot/build/python/dedisperse_roll.pyo"
    "/home/andy/FRB_Pipeline_and_Contributions/gr-transient/gr_oot_modules/gr-dedispersion_oot/build/python/Pulse_Detection.pyo"
    "/home/andy/FRB_Pipeline_and_Contributions/gr-transient/gr_oot_modules/gr-dedispersion_oot/build/python/Kelvin_to_Janskey.pyo"
    )
endif()

