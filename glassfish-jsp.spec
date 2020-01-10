%global artifactId javax.servlet.jsp
%global jspspec 2.2


Name:       glassfish-jsp
Version:    2.2.6
Release:    11%{?dist}
Summary:    Glassfish J2EE JSP API implementation

Group:      Development/Libraries
License:    (CDDL or GPLv2 with exceptions) and ASL 2.0
URL:        http://glassfish.org
Source0:    %{artifactId}-%{version}.tar.xz
# no source releases, but this will generate tarball for you from an
# SVN tag
Source1:    generate_tarball.sh
Source2:    http://www.apache.org/licenses/LICENSE-2.0.txt
Source3:    https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/src/main/resources/META-INF/LICENSE.txt

Patch0:     %{name}-build-eclipse-compilers.patch

BuildArch:  noarch

BuildRequires:  maven-local
BuildRequires:  mvn(javax.el:javax.el-api)
BuildRequires:  mvn(javax.servlet.jsp:javax.servlet.jsp-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(net.java:jvnet-parent)
BuildRequires:  mvn(org.eclipse.jdt:core)

Provides:   jsp = %{jspspec}
Provides:   jsp%{jspspec}

%description
This project provides a container independent implementation of JSP
2.2. The main goals are:
  * Improves current implementation: bug fixes and performance
    improvements
  * Provides API for use by other tools, such as Netbeans
  * Provides a sandbox for new JSP features; provides a reference
    implementation of next JSP spec.


%package javadoc
Summary:    API documentation for %{name}
Group:      Documentation

%description javadoc
%{summary}.

%prep
%setup -q -n %{artifactId}-%{version}
%patch0
cp -p %{SOURCE2} LICENSE
cp -p %{SOURCE3} cddllicense.txt

%mvn_alias : "javax.servlet:jsp-api" "org.eclipse.jetty.orbit:org.apache.jasper.glassfish"

# compat symlink
%mvn_file : %{name}/javax.servlet.jsp %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE cddllicense.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE cddllicense.txt


%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.2.6-11
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.6-10
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Jun 17 2013 Michal Srb <msrb@redhat.com> - 2.2.6-9
- Add compat symlink

* Fri Jun 07 2013 Michal Srb <msrb@redhat.com> - 2.2.6-8
- Build with XMvn
- Fix URL for CDDL license

* Mon Mar  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.6-7
- Add depmap for org.eclipse.jetty.orbit
- Resolves: rhbz#917623

* Tue Feb 26 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.6-6
- Change scope of Eclipse JDT dependency from compile to provided
- Fix eclipse patch

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.2.6-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Sep  4 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.6-3
- Fix license tag
- Install license files

* Thu Aug 30 2012 Krzysztof Daniel <kdaniel@redhat.com> 2.2.6-2
- Build Eclipse compiler adapters.

* Wed Aug 29 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.6-1
- Update to upstream version 2.2.6

* Mon Jul 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.5-1
- Update to upstream version 2.2.5

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 11 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.3-2
- Add explicit BR/R on java and jpackage-utils
- Fix whitespace

* Wed Mar 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.1-1
- Initial version of the package
