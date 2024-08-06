METADATA =\
{
	'name': 'AUM LIVE',
	'description': 'Next generation face swapper and enhancer',
	'version': '2.6.1',
	'license': 'MIT',
	'author': 'Henry Ruhs',
	'url': 'https://aumpos.com'
}


def get(key : str) -> str:
	return METADATA[key]
