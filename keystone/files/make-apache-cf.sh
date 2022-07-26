cd /usr/share/keystone
exec >/etc/httpd/conf.d/wsgi-keystone.conf
case "$1" in
1)
SSL_OVERRIDES='/<\/Directory>/a\
    SSLEngine on\
    SSLCertificateFile /etc/keystone/private/wutubus.pem\
    SSLCertificateKeyFile /etc/keystone/private/wutubus.key\
    SSLCACertificateFile /etc/openldap/certs/degu-ca.crt'
	;;
esac

sed "$SSL_OVERRIDES" wsgi-keystone.conf
echo
sed "s%5000%35357%g;s%public%admin%g
$SSL_OVERRIDES" wsgi-keystone.conf
