#!/usr/bin/env python3

import setuptools


setuptools.setup(
	name="div-life",
	version="1.0.0",
	author="Moshe Reubinoff",
	author_email="reubinoff@gmail.com",
	license="MIT",

	packages=[
		"divorce_life",
		"divorce_life.data_models",
		"divorce_life.handlers",
		"divorce_life.routes"
	],
	entry_points={
		"console_scripts": [
		]
	},
	include_package_data=True
)

