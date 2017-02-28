PKG_NAME := jdk-apache-rat
URL := http://repo1.maven.org/maven2/org/apache/rat/apache-rat/0.12/apache-rat-0.12.jar
ARCHIVES := http://repo1.maven.org/maven2/org/apache/rat/apache-rat/0.12/apache-rat-0.12.pom . \
	http://repo1.maven.org/maven2/org/apache/rat/apache-rat-api/0.12/apache-rat-api-0.12.jar . \
    http://repo1.maven.org/maven2/org/apache/rat/apache-rat-api/0.12/apache-rat-api-0.12.pom . \
    http://repo1.maven.org/maven2/org/apache/rat/apache-rat-core/0.12/apache-rat-core-0.12.jar . \
    http://repo1.maven.org/maven2/org/apache/rat/apache-rat-core/0.12/apache-rat-core-0.12.pom . \
    http://repo1.maven.org/maven2/org/apache/rat/apache-rat-plugin/0.12/apache-rat-plugin-0.12.jar . \
    http://repo1.maven.org/maven2/org/apache/rat/apache-rat-plugin/0.12/apache-rat-plugin-0.12.pom . \
    http://repo1.maven.org/maven2/org/apache/rat/apache-rat-tasks/0.12/apache-rat-tasks-0.12.jar . \
    http://repo1.maven.org/maven2/org/apache/rat/apache-rat-tasks/0.12/apache-rat-tasks-0.12.pom . \
    http://repo1.maven.org/maven2/org/apache/rat/apache-rat-project/0.12/apache-rat-project-0.12.pom

include ../common/Makefile.common
