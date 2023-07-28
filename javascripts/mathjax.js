window.MathJax = {
	tex: {
		tags: 'all',
		packages: {
			'[+]': [
				'base',
				'color',
				'boldsymbol',
				'textmacros'
			]
		},
		// Configure what delimiters will display math
		inlineMath: [ ['$', '$'], ['\\(', '\\)'] ],
		displayMath: [ ['$$', '$$'], ['\\[', '\\]'] ],
		processEscapes: true,
	    processEnvironments: true
	},
	loader: {
		load: [
			'[tex]/color',
			'[tex]/boldsymbol',
			'[tex]/textmacros'
		]
	},
	options: {
		ignoreHtmlClass: ".*|",
		processHtmlClass: 'arithmatex'
	}
};

document$.subscribe(() => { 
	MathJax.typesetPromise()
})
