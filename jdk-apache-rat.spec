Name     : jdk-apache-rat
Version  : 0.12
Release  : 6
URL      : http://www.apache.org/dist/creadur/apache-rat-0.12/apache-rat-0.12-src.tar.bz2
Source0  : http://repo1.maven.org/maven2/org/apache/rat/apache-rat/0.12/apache-rat-0.12.jar
Source1  : http://repo1.maven.org/maven2/org/apache/rat/apache-rat/0.12/apache-rat-0.12.pom
Source2  : http://repo1.maven.org/maven2/org/apache/rat/apache-rat-api/0.12/apache-rat-api-0.12.jar
Source3  : http://repo1.maven.org/maven2/org/apache/rat/apache-rat-api/0.12/apache-rat-api-0.12.pom
Source4  : http://repo1.maven.org/maven2/org/apache/rat/apache-rat-core/0.12/apache-rat-core-0.12.jar
Source5  : http://repo1.maven.org/maven2/org/apache/rat/apache-rat-core/0.12/apache-rat-core-0.12.pom
Source6  : http://repo1.maven.org/maven2/org/apache/rat/apache-rat-plugin/0.12/apache-rat-plugin-0.12.jar
Source7  : http://repo1.maven.org/maven2/org/apache/rat/apache-rat-plugin/0.12/apache-rat-plugin-0.12.pom
#Source8  : http://repo1.maven.org/maven2/org/apache/rat/apache-rat-tasks/0.12/apache-rat-tasks-0.12.jar
Source9  : http://repo1.maven.org/maven2/org/apache/rat/apache-rat-tasks/0.12/apache-rat-tasks-0.12.pom
Source10  : http://repo1.maven.org/maven2/org/apache/rat/apache-rat-project/0.12/apache-rat-project-0.12.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0

BuildRequires : openjdk-dev
BuildRequires : javapackages-tools
BuildRequires : python3
BuildRequires : six
BuildRequires : lxml

%description
Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements.  See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
(the "License; you may not use this file except in compliance with
the License.  You may obtain a copy of the License at

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms/apache-rat
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java/apache-rat

mv %{SOURCE0} %{buildroot}/usr/share/java/apache-rat/apache-rat.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/apache-rat/apache-rat.pom

mv %{SOURCE2} %{buildroot}/usr/share/java/apache-rat/apache-rat-api.jar
mv %{SOURCE3} %{buildroot}/usr/share/maven-poms/apache-rat/apache-rat-api.pom

mv %{SOURCE4} %{buildroot}/usr/share/java/apache-rat/apache-rat-core.jar
mv %{SOURCE5} %{buildroot}/usr/share/maven-poms/apache-rat/apache-rat-core.pom

mv %{SOURCE6} %{buildroot}/usr/share/java/apache-rat/apache-rat-plugin.jar
mv %{SOURCE7} %{buildroot}/usr/share/maven-poms/apache-rat/apache-rat-plugin.pom

#mv %{SOURCE8} %{buildroot}/usr/share/java/apache-rat/apache-rat-tasks.jar
mv %{SOURCE9} %{buildroot}/usr/share/maven-poms/apache-rat/apache-rat-tasks.pom

mv %{SOURCE10} %{buildroot}/usr/share/maven-poms/apache-rat/apache-rat-project.pom

python3 /usr/share/java-utils/pom_editor.py pom_disable_module apache-rat %{buildroot}/usr/share/maven-poms/apache-rat/apache-rat-project.pom
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin :animal-sniffer-maven-plugin %{buildroot}/usr/share/maven-poms/apache-rat/apache-rat-project.pom
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin :maven-enforcer-plugin %{buildroot}/usr/share/maven-poms/apache-rat/apache-rat-project.pom
python3 /usr/share/java-utils/pom_editor.py pom_xpath_remove   pom:extensions %{buildroot}/usr/share/maven-poms/apache-rat/apache-rat-project.pom

# Creates metadata
for a in apache-rat apache-rat-api apache-rat-core apache-rat-plugin \
apache-rat-project
do

# Remove plugins

    python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin :maven-antrun-plugin %{buildroot}/usr/share/maven-poms/apache-rat/$a.pom :||
    python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin :maven-invoker-plugin $%{buildroot}/usr/share/maven-poms/apache-rat/a.pom :|| 

    python3 /usr/share/java-utils/maven_depmap.py \
    -n "" \
    --pom-base %{buildroot}/usr/share/maven-poms \
    --jar-base %{buildroot}/usr/share/java \
    %{buildroot}/usr/share/maven-metadata/apache-rat-$a.xml \
    %{buildroot}/usr/share/maven-poms/apache-rat/$a.pom \
    %{buildroot}/usr/share/java/apache-rat/$a.jar
done

rm  %{buildroot}/usr/share/maven-poms/apache-rat/*.tmp
rm  %{buildroot}/usr/share/maven-poms/apache-rat/*.orig

%files
%defattr(-,root,root,-)
/usr/share/java/apache-rat/apache-rat-api.jar
/usr/share/java/apache-rat/apache-rat-core.jar
/usr/share/java/apache-rat/apache-rat-plugin.jar
#/usr/share/java/apache-rat/apache-rat-tasks.jar
/usr/share/java/apache-rat/apache-rat.jar
/usr/share/maven-metadata/apache-rat-apache-rat-api.xml
/usr/share/maven-metadata/apache-rat-apache-rat-core.xml
/usr/share/maven-metadata/apache-rat-apache-rat-plugin.xml
/usr/share/maven-metadata/apache-rat-apache-rat-project.xml
#/usr/share/maven-metadata/apache-rat-apache-rat-tasks.xml
/usr/share/maven-metadata/apache-rat-apache-rat.xml
/usr/share/maven-poms/apache-rat/apache-rat-api.pom
/usr/share/maven-poms/apache-rat/apache-rat-core.pom
/usr/share/maven-poms/apache-rat/apache-rat-plugin.pom
/usr/share/maven-poms/apache-rat/apache-rat-project.pom
/usr/share/maven-poms/apache-rat/apache-rat.pom
