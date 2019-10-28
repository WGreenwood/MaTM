THIS_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

APP_NAME=MaTM
ZIPARGS=--exclude __pycache__ --files-from file-list.txt

VERSION=$(shell cat VERSION)
APP_FILENAME=${APP_NAME}-${VERSION}

TEMP_DIR=${THIS_DIR}/temp

TEMP_PY_OUT=${TEMP_DIR}/${APP_FILENAME}.tar.gz
TEMP_CHECKSUM_OUT=${TEMP_DIR}/${APP_FILENAME}.sha256

ARCHPKG_DIR=/home/wesley/dev/builds/python/${APP_NAME}
ARCHPKG_WORKDIR=${THIS_DIR}/build
CHROOT_DIR=/home/wesley/dev/chroot

default: build

zipped: clean
# Create the zip file containing the required assets for PKGBUILD
	@echo "Preparing zip file"
	@mkdir -p ${TEMP_DIR}
	@tar -zcf ${TEMP_PY_OUT} ${ZIPARGS}
	@sha256sum ${TEMP_PY_OUT} | cut -d" " -f1 > "${TEMP_CHECKSUM_OUT}"

# They're in separate rules because we need the shell statement to execute _AFTER_ the sum is calculated
build: zipped
	@echo "Preparing arch linux package"
	@mkdir -p ${ARCHPKG_WORKDIR}

# Replace properties in the template PKGBUILD
	@echo "Preparing PKGBUILD"
	@sed -e 's;%VERSION%;${VERSION};g'\
		-e 's;%CHECKSUM%;$(shell cat ${TEMP_CHECKSUM_OUT});g'\
		-e 's;%SRCFILE%;file://${TEMP_PY_OUT};g'\
		PKGBUILD.proto > ${ARCHPKG_WORKDIR}/PKGBUILD

# Copy the install script
	@echo "Copying install script"
	@cp ${APP_NAME}.sh ${ARCHPKG_WORKDIR}/

	@echo "Building package in chroot"
# Build the arch linux package
	@cd ${ARCHPKG_WORKDIR}; PKGDEST="${ARCHPKG_DIR}" makechrootpkg -c -r ${CHROOT_DIR} -- -c -C

clean:
	@echo "Cleaning output directories"
	@rm -r ${ARCHPKG_WORKDIR} ${TEMP_DIR} >/dev/null 2>&1 | printf ''


.PHONY: build clean
