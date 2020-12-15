# /etc/catalyst/

This repository contains the specfiles needed to drive `dev-util/catalyst`.

## Install

    # git clone https://github.com/bencord0/etc-catalyst /etc/catalyst

## Run

    # emerge dev-util/catalyst
    # catalyst -f /etc/catalyst/specs/nspawn-container.spec

## Builds

A stage3 will then be available under

    /var/tmp/catalyst/builds/nspawn
