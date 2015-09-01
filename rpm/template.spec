Name:           ros-indigo-xacro
Version:        1.9.4
Release:        1%{?dist}
Summary:        ROS xacro package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/xacro
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-roslaunch
BuildRequires:  ros-indigo-catkin >= 0.5.68
BuildRequires:  ros-indigo-roslint
BuildRequires:  ros-indigo-rostest

%description
Xacro (XML Macros) Xacro is an XML macro language. With xacro, you can construct
shorter and more readable XML files by using macros that expand to larger XML
expressions.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Sep 01 2015 Morgan Quigley <morgan@osrfoundation.org> - 1.9.4-1
- Autogenerated by Bloom

* Wed Apr 01 2015 Morgan Quigley <morgan@osrfoundation.org> - 1.9.4-0
- Autogenerated by Bloom

* Wed Jan 14 2015 Morgan Quigley <morgan@osrfoundation.org> - 1.9.3-0
- Autogenerated by Bloom

