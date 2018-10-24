import argparse







if __name__ == "__main__":
	print('Starting....')
	parser = argparse.ArgumentParser(description='Just Application')
	parser.add_argument('-c', '--config', help='config file', required=True)
	args = parser.parse_args()

	print(args.config)


