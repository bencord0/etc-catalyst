subarch: amd64
target: livecd-stage1

version_stamp: 2021.04
snapshot: 2021.04
rel_type: default

portage_confdir: /etc/catalyst/confdir
profile: default/linux/amd64/17.1/systemd

# From stage3
source_subpath: default/stage3-amd64-2021.04

# Needs app-arch/pixz
compression_mode: pixz_x

# eselect repository add bencord0 git https://github.com/bencord0/portage-overlay
portage_overlay: /var/db/repos/bencord0
pkgcache_path: /var/cache/binpkgs

livecd/use:
	livecd

livecd/packages:
	app-editors/vim
	app-misc/tmux
	app-portage/eix
	app-portage/gentoolkit
	app-portage/mirrorselect
	app-portage/portage-utils
	net-misc/curl
	net-misc/rsync
	net-wireless/wpa_supplicant
	sys-kernel/linux-firmware
	sys-process/htop
	www-client/links
