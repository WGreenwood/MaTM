post_install() {
	echo 'Make sure to enable the matm-daemon.  (systemctl enable --user matm-daemon)'
}

post_upgrade() {
	post_install
}