from matplotlib import pyplot as plt

plt.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'pgf.preamble': r'\usepackage{color}\usepackage{dashrule}',
    'text.usetex': True,
    'text.latex.preamble':  r'\usepackage{color}\usepackage{dashrule}',
})

fig, ax = plt.subplots()
ylabel = r'Y $\;$ \textcolor[rgb]{1.0, 0.0, 0.0}{\hdashrule[0.5ex]{3cm}{1pt}{1pt 0pt}}'
ax.set_ylabel(ylabel)
ax.set_xlabel(r'N $\;$ \textcolor[rgb]{0.0, 1.0, 0.0}{\rule[0.5ex]{3cm}{1pt}}')
fig.savefig('test.png', backend='pgf')
plt.show()
