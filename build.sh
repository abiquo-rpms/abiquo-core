CHROOT=centos-5.5-x86_64
CHROOT_DIR=/var/lib/mock/$CHROOT/root
PKGVER=1.7
PKGNAME=abiquo-core
MOCK_CMD="/usr/bin/mock -q"

rm -rf tmp
mkdir tmp

rm -rf rpms
mkdir -p rpms/SRPMS

$MOCK_CMD --init -r  $CHROOT
rm -rf $PKGNAME-$PKGVER/tomcat/webapps/legal 
cp -r $PKGNAME-$PKGVER/legal $PKGNAME-$PKGVER/tomcat/webapps/
tar czf tmp/$PKGNAME-$PKGVER.tar.gz $PKGNAME-$PKGVER
$MOCK_CMD -r $CHROOT --copyin tmp/$PKGNAME-$PKGVER.tar.gz /builddir/build/SOURCES/
$MOCK_CMD -r $CHROOT --copyin abiquo-release /builddir/build/SOURCES/
$MOCK_CMD -r $CHROOT --copyin $PKGNAME.spec /root
$MOCK_CMD -r $CHROOT --shell "rpmbuild -ba /root/$PKGNAME.spec"

cp $CHROOT_DIR/builddir/build/RPMS/*.rpm rpms
cp $CHROOT_DIR/builddir/build/SRPMS/*.rpm rpms/SRPMS/
rm -rf tmp
