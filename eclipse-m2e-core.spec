%{?scl:%scl_package eclipse-m2e-core}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global baserelease 1

%global release_dir          m2e-core-3aeac6a44a58749cefd18994c9ea09f5416dfb9c

Name:           %{?scl_prefix}eclipse-m2e-core
Version:        1.7.1
Release:        0.3.git3aeac6a.%{baserelease}%{?dist}
Summary:        Maven integration for Eclipse

# Most of components are under EPL, but some of them are licensed under
# ASL 2.0 license.
License:        EPL and ASL 2.0
URL:            http://eclipse.org/m2e/

Source0:        http://git.eclipse.org/c/m2e/m2e-core.git/snapshot/%{release_dir}.tar.xz
Source1:        http://www.eclipse.org/legal/epl-v10.html

# Add some necessary stuff (mainly requires & imports) to manifests
Patch0:         %{pkg_name}-fix-manifests.patch

# API changes to accomodate maven-indexer 5.1.1
Patch1:        %{pkg_name}-indexer-5.1.1.patch

# API change in aether (remove once implemented)
Patch2:        %{pkg_name}-LifecycleMappingFactory.patch

# Port tests to latest Jetty
Patch3:        %{pkg_name}-jetty.patch

# Remove "mandatory" attirbutes from OSGi manifests, which cause problems with P2.
# See https://dev.eclipse.org/mhonarc/lists/p2-dev/msg05465.html
Patch4:        %{pkg_name}-mandatory-OSGi-attributes.patch

# Port to lucene 5
Patch5:        %{pkg_name}-lucene-5.patch

BuildArch:      noarch

# Maven build-requires for the main build.  After successfull build
# they can be regenerated with the following command:
#   xmvn-builddep <path-to-build-log>
BuildRequires:  %{?scl_prefix_maven}maven-local
BuildRequires:  %{?scl_prefix}mvn(io.takari.m2e.workspace:org.eclipse.m2e.workspace.cli)
BuildRequires:  %{?scl_prefix_maven}mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  %{?scl_prefix_maven}mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.eclipse.tycho:target-platform-configuration)
BuildRequires:  %{?scl_prefix}mvn(org.eclipse.tycho:tycho-maven-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.eclipse.tycho:tycho-source-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.eclipse.tycho:tycho-surefire-plugin)
BuildRequires:  %{?scl_prefix_maven}mvn(org.sonatype.forge:forge-parent:pom:)


# Additional Maven build-requires for m2e-maven-runtime.  They cannot
# be regenerated using xmvn-builddep because m2e-maven-runtime is not
# built using %%mvn_build.
BuildRequires:  %{?scl_prefix}mvn(com.google.guava:guava)
BuildRequires:  %{?scl_prefix}mvn(io.takari.aether:aether-connector-okhttp)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.maven.archetype:archetype-common)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.indexer:indexer-core)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.maven:maven-compat)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.maven:maven-core)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.maven:maven-embedder)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.maven.wagon:wagon-file)
BuildRequires:  %{?scl_prefix_maven}mvn(org.eclipse.aether:aether-connector-basic)
BuildRequires:  %{?scl_prefix_maven}mvn(org.eclipse.aether:aether-impl)
BuildRequires:  %{?scl_prefix_maven}mvn(org.eclipse.aether:aether-transport-wagon)
BuildRequires:  %{?scl_prefix_maven}mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  %{?scl_prefix}mvn(org.eclipse.tycho:tycho-maven-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.eclipse.tycho:tycho-p2-plugin)
BuildRequires:  %{?scl_prefix_java_common}mvn(org.slf4j:slf4j-simple)
BuildRequires:  %{?scl_prefix_maven}mvn(org.sonatype.forge:forge-parent:pom:)
BuildRequires:  %{?scl_prefix_maven}mvn(org.sonatype.plexus:plexus-build-api)


# OSGi build-requires.  They can be regenerated with the following command:
#   sed -n 's/^Require-Bundle: //;T;:l;s/[;=,].*//;/^org.eclipse.m2e/bn;s/..*/BuildRequires:  osgi(&)/;T;p;:n;n;s/^ //;T;bl' `find -name *.MF` | sort -u
BuildRequires:  %{?scl_prefix}osgi(com.google.guava)
BuildRequires:  %{?scl_prefix}osgi(com.ibm.icu)
BuildRequires:  %{?scl_prefix}osgi(org.apache.ant)
BuildRequires:  %{?scl_prefix_java_common}osgi(org.apache.lucene.queryparser)
BuildRequires:  %{?scl_prefix_maven}osgi(org.apache.maven.archetype.catalog)
BuildRequires:  %{?scl_prefix_maven}osgi(org.apache.maven.archetype.descriptor)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.compare)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.core.expressions)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.core.filebuffers)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.core.filesystem)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.core.jobs)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.core.resources)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.core.runtime)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.core.variables)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.debug.core)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.debug.ui)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.emf.common)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.emf.ecore)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.emf.ecore.edit)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.emf.ecore.xmi)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.emf.edit)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.equinox.common)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.equinox.p2.core)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.equinox.p2.discovery)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.equinox.p2.discovery.compatibility)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.equinox.p2.metadata)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.equinox.p2.operations)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.equinox.p2.repository)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.equinox.p2.ui)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.equinox.p2.ui.discovery)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.equinox.registry)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.jdt.core)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.jdt.debug)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.jdt.debug.ui)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.jdt.launching)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.jdt.ui)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.jem.util)
BuildRequires:  %{?scl_prefix_java_common}osgi(org.eclipse.jetty.http)
BuildRequires:  %{?scl_prefix_java_common}osgi(org.eclipse.jetty.io)
BuildRequires:  %{?scl_prefix_java_common}osgi(org.eclipse.jetty.security)
BuildRequires:  %{?scl_prefix_java_common}osgi(org.eclipse.jetty.server)
BuildRequires:  %{?scl_prefix_java_common}osgi(org.eclipse.jetty.util)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.jface)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.jface.text)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.license)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.ltk.core.refactoring)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.ltk.ui.refactoring)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.osgi)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.search)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.swt)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.ui)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.ui.console)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.ui.editors)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.ui.externaltools)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.ui.forms)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.ui.ide)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.ui.workbench)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.ui.workbench.texteditor)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.wst.common.emf)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.wst.common.uriresolver)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.wst.sse.core)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.wst.sse.ui)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.wst.xml.core)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.wst.xml.ui)
BuildRequires:  %{?scl_prefix}osgi(org.eclipse.wst.xsd.core)
BuildRequires:  %{?scl_prefix_java_common}osgi(org.junit)

# Maven POM doesn't require maven-parent
BuildRequires: %{?scl_prefix_maven}maven-parent

# Bundle requires are auto-generated, but explicit requires are needed
# for symlinks to JARs installed by other packages.  After installing
# m2e these requires can be regenerated with the following command:
#   rpm -qf --qf 'Requires:       %{pkg_name}\n' $(readlink -f $(find /usr/share/eclipse/droplets/m2e-core -type l)) | sort -u
Requires:       %{?scl_prefix_maven}aether-api
Requires:       %{?scl_prefix_maven}aether-connector-basic
Requires:       %{?scl_prefix}aether-connector-okhttp
Requires:       %{?scl_prefix_maven}aether-impl
Requires:       %{?scl_prefix_maven}aether-spi
Requires:       %{?scl_prefix_maven}aether-transport-wagon
Requires:       %{?scl_prefix_maven}aether-util
Requires:       %{?scl_prefix_java_common}aopalliance
Requires:       %{?scl_prefix_java_common}apache-commons-cli
Requires:       %{?scl_prefix_java_common}apache-commons-collections
Requires:       %{?scl_prefix_java_common}apache-commons-io
Requires:       %{?scl_prefix_java_common}apache-commons-lang
Requires:       %{?scl_prefix_java_common}apache-commons-lang3
Requires:       %{?scl_prefix_java_common}atinject
Requires:       %{?scl_prefix_java_common}dom4j
Requires:       %{?scl_prefix}eclipse-m2e-workspace >= 0.4.0
Requires:       %{?scl_prefix_maven}google-guice
Requires:       %{?scl_prefix}guava
Requires:       %{?scl_prefix_maven}jchardet
Requires:       %{?scl_prefix_java_common}jdom
Requires:       %{?scl_prefix_java_common}jetty-util
Requires:       %{?scl_prefix_java_common}lucene-grouping
Requires:       %{?scl_prefix_java_common}lucene5-highlighter
Requires:       %{?scl_prefix_java_common}lucene5-join
Requires:       %{?scl_prefix_java_common}lucene5-memory
Requires:       %{?scl_prefix_maven}maven-archetype-catalog
Requires:       %{?scl_prefix_maven}maven-archetype-common
Requires:       %{?scl_prefix_maven}maven-archetype-descriptor
Requires:       %{?scl_prefix_maven}maven-archetype-registry
Requires:       %{?scl_prefix_maven}maven-artifact-manager
Requires:       %{?scl_prefix}maven-indexer >= 5.1.2
Requires:       %{?scl_prefix_maven}maven-invoker
Requires:       %{?scl_prefix_maven}maven
Requires:       %{?scl_prefix_maven}maven-model
Requires:       %{?scl_prefix_maven}maven-plugin-registry
Requires:       %{?scl_prefix_maven}maven-profile
Requires:       %{?scl_prefix_maven}maven-project
Requires:       %{?scl_prefix_maven}maven-wagon-file
Requires:       %{?scl_prefix_maven}maven-wagon-provider-api
Requires:       %{?scl_prefix_java_common}objectweb-asm5
Requires:       %{?scl_prefix}okhttp
Requires:       %{?scl_prefix}okio
Requires:       %{?scl_prefix_maven}plexus-build-api
Requires:       %{?scl_prefix_maven}plexus-cipher
Requires:       %{?scl_prefix_maven}plexus-classworlds
Requires:       %{?scl_prefix_maven}plexus-containers-component-annotations
Requires:       %{?scl_prefix_maven}plexus-containers-container-default
Requires:       %{?scl_prefix_maven}plexus-interpolation
Requires:       %{?scl_prefix_maven}plexus-sec-dispatcher
Requires:       %{?scl_prefix_maven}plexus-utils
Requires:       %{?scl_prefix_maven}plexus-velocity
Requires:       %{?scl_prefix_maven}sisu-inject
Requires:       %{?scl_prefix_maven}sisu-plexus
Requires:       %{?scl_prefix_java_common}slf4j
Requires:       %{?scl_prefix_maven}velocity
Requires:       %{?scl_prefix_java_common}xbean
Requires:       %{?scl_prefix_java_common}xml-commons-apis

%description
The goal of the m2ec project is to provide a first-class Apache Maven support
in the Eclipse IDE, making it easier to edit Maven's pom.xml, run a build from
the IDE and much more. For Java developers, the very tight integration with JDT
greatly simplifies the consumption of Java artifacts either being hosted on open
source repositories such as Maven Central, or in your in-house Maven repository.

m2e is also a platform that let others provide better integration with
additional Maven plugins (e.g. Android, web development, etc.), and facilitates
the distribution of those extensions through the m2e marketplace.

%package tests
Summary:        Eclipse M2E testing helpers

%description tests
This package contains common code used by tests for Eclipse M2E.

%package javadoc
Group:          Documentation
Summary:        API documentation for %{pkg_name}

%description javadoc
This package contains %{summary}.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%setup -q -n %{release_dir}

find -name '*.class' -delete
find -name '*.jar' -delete

# Copy license files so they can be installed more easily.
cp -p %{SOURCE1} .
cp -p org.eclipse.m2e.core/about_files/LICENSE-2.0.txt .

# These don't currently build, but don't seem to be absolutely necessary
for mod in org.eclipse.m2e.logback.appender \
           org.eclipse.m2e.logback.configuration \
           org.eclipse.m2e.logback.feature \
           org.eclipse.m2e.sdk.feature \
           org.eclipse.m2e.site
do
  %pom_disable_module $mod
  rm -rf $mod
done

# Test bundle goes to its own subpackage.
%mvn_package ":*.tests*::{}:" tests
%mvn_package ":::{}:"

# Embed all Maven dependencies.  They may be some superflous deps
# added this way, but in Fedora we don't have enough manpower to test
# dependency correctness.  And we don't even run m2e tests...
# Except for lucene, avoid embedding that because of problems
for d in `find m2e-maven-runtime/* -maxdepth 0 -type d`; do
    %pom_xpath_inject pom:instructions "<Embed-Directory>jars</Embed-Directory>" $d
    %pom_xpath_set pom:Embed-Dependency "*;scope=compile|runtime;groupId=!org.apache.lucene" $d
done

%autopatch -p0

# Avoid embedding lucene, use as ordinary OSGi bundle instead
%pom_xpath_set pom:Import-Package "org.apache.lucene*,!*" m2e-maven-runtime/org.eclipse.m2e.maven.indexer
sed -i -e '/org.slf4j/s|^\(.*\)|\1,org.apache.lucene.analysis,org.apache.lucene.analysis.standard,org.apache.lucene.analysis.util,org.apache.lucene.document,org.apache.lucene.index,org.apache.lucene.queryparser.classic,org.apache.lucene.search,org.apache.lucene.search.highlight,org.apache.lucene.store,org.apache.lucene.util|' \
  org.eclipse.m2e.core/META-INF/MANIFEST.MF org.eclipse.m2e.core.ui/META-INF/MANIFEST.MF
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
# Building m2e is a two step process.  See upstream documentation:
# http://wiki.eclipse.org/M2E_Development_Environment#Building_m2e_on_command_line
repo=localrepo
xmvn -B -o install -f m2e-maven-runtime/pom.xml -Dmaven.repo.local=${repo}
%mvn_build -f -- -Dmaven.repo.local=${repo} -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x

%mvn_artifact m2e-maven-runtime/$mod/pom.xml
for mod in org.eclipse.m2e.archetype.common \
           org.eclipse.m2e.maven.indexer \
           org.eclipse.m2e.maven.runtime \
           org.eclipse.m2e.maven.runtime.slf4j.simple
do
    %mvn_artifact -Dtype=eclipse-plugin m2e-maven-runtime/$mod/pom.xml m2e-maven-runtime/$mod/target/$mod-%{version}-SNAPSHOT.jar
done

%mvn_install

# Replace bundled JARs with symlinks to system JARs using XMvn Subst.  This way
# there is no need to manually synchronize JAR lists between Maven and M2E when
# some Maven dependency changes.  All that needs to be done is rebuilding M2E.
xmvn-subst -s $(find %{buildroot}%{_datadir}/eclipse/droplets/m2e-core -name jars)
%{?scl:EOF}


%files -f .mfiles
%doc epl-v10.html LICENSE-2.0.txt

%files tests -f .mfiles-tests

%files javadoc -f .mfiles-javadoc
%doc epl-v10.html LICENSE-2.0.txt

%changelog
* Fri Feb 10 2017 Mat Booth <mat.booth@redhat.com> - 1.7.1-0.3.git3aeac6a.1
- Auto SCL-ise package for rh-eclipse46 collection

* Fri Feb 10 2017 Mat Booth <mat.booth@redhat.com> - 1.7.1-0.3.git3aeac6a
- Rebuild against new maven-indexer
- Port tests to latest jetty to drop dep on obsolete jetty8
- Port to latest lucene and use from OSGi instead of embedding
- Organise patches

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-0.2.git3aeac6a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Mat Booth <mat.booth@redhat.com> - 1.7.1-0.1.git3aeac6a
- Update to 1.7.1 snapshot to get slf4j fixes

* Fri Dec 02 2016 Mat Booth <mat.booth@redhat.com> - 1.7.0-1
- Update to latest release
- Re-generate runtime requires

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.2-6
- Add missing build-requires

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Gerard Ryan <galileo@fedoraproject.org> - 1.6.2-4
- Force minimum maven-indexer Requires

* Sat Dec 12 2015 Gerard Ryan <galileo@fedoraproject.org> - 1.6.2-3
- Update for new maven-indexer build (lucene3)

* Wed Oct 14 2015 Mat Booth <mat.booth@redhat.com> - 1.6.2-2
- Rebuild for new eclipse-m2e-workspace

* Sun Sep 13 2015 Gerard Ryan <galileo@fedoraproject.org> - 1.6.2-1
- Update to upstream 1.6.2 release.

* Fri Sep 04 2015 Roland Grunberg <rgrunber@redhat.com> - 1.6.1-2
- Minor changes to build as a droplet.

* Wed Jul 8 2015 Alexander Kurtakov <akurtako@redhat.com> 1.6.1-1
- Update to upstram 1.6.1 release.
- Port to Lucene 5 API.

* Mon Jun 22 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.0-1
- Update to upstream release 1.6.0 (Mars)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.0-0.3
- Update to upstream milestone 1.6.0.20150506-1605

* Mon Mar 16 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.0-0.2
- Remove "mandatory" attirbutes from OSGi manifests

* Thu Feb 19 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6.0-0.1
- Update to upstream milestone 1.6.0.20150203-1921

* Mon Feb  9 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0-18
- Enable test bundle

* Sat Feb  7 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0-17
- Install runtime bundles in dropins directory

* Fri Dec 12 2014 Roland Grunberg <rgrunber@redhat.com> - 1.5.0-16
- Fix FTBFS by removing unnecessary type attribute.

* Thu Sep 18 2014 Michal Srb <msrb@redhat.com> - 1.5.0-15
- Rebuild to fix metadata

* Wed Sep 10 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0-14
- Install with XMvn

* Sun Aug 31 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0-14
- Rebuild for Maven 3.2.3

* Sat Jul 05 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.5.0-13
- Symlink guava so bundles can get resolved

* Fri Jun 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0-12
- Update to final 1.5.0 (Luna)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.5.0-10
- Replace old BR on tesla-concurrent-localrepo

* Thu May 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0-9
- Regenerate requires and build-requires, again

* Thu May 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0-8
- Regenerate requires and build-requires

* Sun May 25 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.5.0-7
- Update to latest upstream 1.5.0 milestone

* Fri May 23 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.5.0-6
- Rebuild for plexus-velocity update

* Sat Mar 22 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5.0-5
- Add explicit requires, resolves: rhbz#1079458
- Regenerate build-requires
- Rename dropin installation dir to m2e-core
- Simplify patch application with %%autopatch macro
- Use %%mvn_build and %%mvn_install macros
- Use feclipse-maven-plugin to simplify bundle installation
- Embed all dependencies in m2e-maven-runtime bundles

* Sat Mar 15 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.5.0-4
- Use xmvn instead of mvn-rpmbuild

* Fri Mar 14 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.5.0-3
- Patch for lucene API changes

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.5.0-2
- Use Requires: java-headless rebuild (#1067528)

* Mon Jan 27 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0-SNAPSHOT

* Mon Jan 27 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.4.0-13
- Fix for RHBZ#1015324: Failing to retrieve archetypes

* Thu Jan 23 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-12
- Switch to netty3 compat package

* Sat Jan  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-11
- Fully remove CGlib from Maven runtime bundle
- Exclude AOP version of Guice from Sisu dependencies
- Fix Sisu dependency scope

* Thu Jan 02 2014 Gerard Ryan <galileo@fedoraproject.org> - 1.4.0-10
- Revert removal of workaround for missing cglib and aopalliance

* Tue Dec 31 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.0-9
- Remove workaround for rhbz#911365 (missing cglib and aopalliance)
- Add NOP SLF4J implementation JAR to classpath
- Use xmvn-subst to symlink JARs, resolves: rhbz#1020299

* Wed Dec 04 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.4.0-8
- Rebuild in Rawhide

* Wed Oct 02 2013 Roland Grunberg <rgrunber@redhat.com> - 1.4.0-7
- Fix bug with plexus-utils > 3.0.5.

* Tue Oct 01 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.4.0-6
- Add BR/R on aether-connector-basic in f20+

* Sun Sep 29 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.4.0-5
- Fixes for maven 3.1.0

* Sat Aug 24 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.4.0-4
- Bump release to rebuild in rawhide/f20

* Mon Aug 19 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.4.0-3
- Use Eclipse Sisu and Eclipse Aether
- Add patch for new maven-indexer

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 25 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.4.0-1
- Update to latest upstream version 1.4.0

* Tue May 14 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.3.1-2
- Fix broken symbolic links on f19+
- Update Requires/BuildRequires

* Sun Apr 07 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.3.1-1
- Update to upstream version 1.3.1

* Wed Feb 20 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.2.0-7
- Bump release to test again in koji (previously broken deps)

* Mon Feb 18 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-6
- Drop dependency on plexus-container-default
- Resolves: rhbz#912311

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2.0-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 30 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.2.0-4
- Update min versions of eclipse and eclipse-emf

* Thu Jan 24 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.2.0-3
- Fix incorrect changelog entry dates.

* Tue Jan 22 2013 Gerard Ryan <galileo@fedoraproject.org> - 1.2.0-2
- Remove javadoc.sh file from javadoc subpackage.
- Fix URL for source0.

* Tue Dec 11 2012 Gerard Ryan <galileo@fedoraproject.org> - 1.2.0-1
- Bump to a more sane release number

* Tue Dec 11 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-0.3
- Add javadoc subpackage
- Fix licensing

* Tue Dec 11 2012 Gerard Ryan <galileo@fedoraproject.org> - 1.2.0-0.2
- Require org.apache.maven.archetype.descriptor in OSGi for m2e.core.

* Mon Dec 10 2012 Gerard Ryan <galileo@fedoraproject.org> - 1.2.0-0.1
- Attempt update to upstream 1.2.0

* Mon Dec 10 2012 Gerard Ryan <galileo@fedoraproject.org> - 1.1.0-4
- Force usage of sisu over plexus-containers for DefaultPlexusContainer.

* Thu Dec 06 2012 Gerard Ryan <galileo@fedoraproject.org> - 1.1.0-3
- Add cglib and aopalliance as embedded dependencies.
- Use newer pom macro to add netty dependency.
- Add cglib and aopalliance as dependencies in org.eclipse.m2e.maven.runtime.
- Symlink catalog and descriptor jars from maven-archetype.
- Remove symlink to plexus-container-default.jar, fix sisu-guice.jar link.

* Fri Aug 10 2012 Gerard Ryan <galileo@fedoraproject.org> - 1.1.0-2
- Fix sources.

* Sun Aug 05 2012 Gerard Ryan <galileo@fedoraproject.org> - 1.1.0-1
- Initial packaging.