#
# A little script to help with calculating story points from t-shirt sizes
#

import argparse

# Valid T-shirt sizes, with lower/upper story point estimates
sizes = {
	'XS': [1, 2],
	'S': [3, 5],
	'M': [8, 13],
	'L': [13, 20],
	'XL': [20, 40],
	'XXL': [40, 80]
}

orderedSizes = ['XS', 'S', 'M', 'L', 'XL', 'XXL']

# Valid MoSCoW codes mapper to human-readable strings
moscows = {
	'M': "Must",
	'S': "Should",
	'C': "Could",
	'W': "Won't"
}

orderedMoscows = ['M', 'S', 'C', 'W']

parser = argparse.ArgumentParser(description='Calculate story points from T-shirt sizes')

parser.add_argument('-t', '--tshirts', metavar='tshirts', required=True,
					dest='tshirts', action='store',
 					help='<tshirt-MoSCoW>, [...], e.g. "XS-M, L-S"')

args = parser.parse_args()

tshirts = args.tshirts.split(',')

# Set up our running totals
totals = {}
for m in moscows:
	totals[m] = {}

for tshirt in tshirts:
	tshirt = tshirt.strip()
	size, moscow = tshirt.split('-')

	if size not in sizes:
		raise ValueError("%s not a valid size!" % size)

	if moscow not in moscows:
		raise ValueError("%s not a valid MoSCoW!" % moscow)

	if size in totals[moscow]:
		totals[moscow][size] += 1;
	else:
		totals[moscow][size] = 1;

totalLower = totalUpper = 0

# Iterate MoSCoW in order
for m in orderedMoscows:

	if not totals[m]:
		continue

	lower = upper = 0
	text = "%s: " % moscows[m]
	sizeText = []

	for s in orderedSizes:

		# print m, s
		if s not in totals[m]:
			continue;

		count = totals[m][s]

		sLower = count * sizes[s][0]
		sUpper = count * sizes[s][1]

		lower += sLower
		upper += sUpper

		sizeText.append("%d (%d)" % (sLower, sUpper))

	totalLower += lower
	totalUpper += upper

	text += ' + '.join(sizeText)

	if len(totals[m]) > 1:
		text += ' = %d (%d)' % (lower, upper)

	print text

print 'Total: between %d and %d points' % (totalLower, totalUpper)