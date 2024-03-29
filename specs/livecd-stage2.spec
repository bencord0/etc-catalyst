subarch: amd64
target: livecd-stage2

version_stamp: 2021.04
snapshot: 2021.04
rel_type: default

portage_confdir: /etc/catalyst/confdir
profile: default/linux/amd64/17.1/systemd

# From livecd-stage1
source_subpath: default/livecd-stage1-amd64-2021.04

# eselect repository add bencord0 git https://github.com/bencord0/portage-overlay
portage_overlay: /var/db/repos/bencord0
pkgcache_path: /var/cache/binpkgs

livecd/bootargs: dokeymap docache
livecd/fstype: squashfs
livecd/fsscript: /etc/catalyst/scripts/livecd-stage2.sh
livecd/iso: livecd-amd64-systemd.iso
livecd/type: generic-livecd
livecd/volid: Gentoo AMD64 Systemd 2021.04

boot/kernel: gentoo
boot/kernel/gentoo/sources: gentoo-sources
boot/kernel/gentoo/config: /etc/catalyst/kconfig/livecd-stage2.config
boot/kernel/gentoo/packages:
	sys-fs/zfs
