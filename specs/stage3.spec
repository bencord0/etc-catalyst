subarch: amd64
target: stage3

version_stamp: 2021.04
snapshot: 2021.04
rel_type: default

portage_confdir: /etc/catalyst/confdir
profile: default/linux/amd64/17.1/systemd

# From stage2.spec
source_subpath: default/stage2-amd64-2021.04

# Needs app-arch/pixz
compression_mode: pixz_x

# eselect repository add bencord0 git https://github.com/bencord0/portage-overlay
portage_overlay: /var/db/repos/bencord0
pkgcache_path: /var/cache/binpkgs
