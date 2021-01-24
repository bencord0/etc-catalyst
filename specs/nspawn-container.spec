subarch: amd64
target: stage3

version_stamp: 2021.01.24
snapshot: 2021.01.24
rel_type: nspawn-container

portage_confdir: /etc/catalyst/confdir
profile: bencord0:default/linux/amd64/nspawn

# From distfiles.gentoo.org
# Save to /var/tmp/catalyst/builds/distfiles/stage3-amd64-systemd.tar.xz
source_subpath: distfiles/stage3-amd64-systemd

# Needs app-arch/pixz
compression_mode: pixz_x

# eselect repository add bencord0 git https://github.com/bencord0/portage-overlay
portage_overlay: /var/db/repos/bencord0
pkgcache_path: /var/cache/binpkgs
