#!/usr/bin/env python3

import setuptools

requrements = [
	"flask",
	"sqlalchemy"
]

setuptools.setup(
	name="div-life",
	version="1.0.0",
	author="Moshe Reubinoff",
	author_email="reubinoff@gmail.com",
	license="MIT",

	packages=[

	],
	install_requires=requrements,
	entry_points={
		"console_scripts": [
		]
	},
	include_package_data=True
)

