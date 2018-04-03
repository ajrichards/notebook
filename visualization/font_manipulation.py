import os
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('bmh')

fontsize = 16
fontname = 'sans'

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

N = 5
total_instructors = 7.0
denver = np.array([23, 24, 25, 26, 27])
boulder = np.array([12, 13, 14, 15, 16])
total_students = denver + boulder
ratios = total_students / total_instructors 
ratios = ["%s:1"%round(r,1) for r in ratios]

xpos = np.arange(N)
width = 0.5

p1 = plt.bar(xpos, denver, width, color='deepskyblue')
p2 = plt.bar(xpos, boulder, width,bottom=denver, color='darkorange')

ax.set_xticks(xpos)
ax.set_xticklabels(ratios,fontsize=fontsize,fontname=fontname)
ax.set_ylabel('total students',fontsize=fontsize,fontname=fontname)
ax.set_xlabel('ratios',fontsize=fontsize,fontname=fontname)
ax.set_title('student to instructor ratios',fontsize=fontsize,fontname=fontname)
leg = ax.legend((p1[0], p2[0]), ('Denver', 'Boulder'))
for l in leg.get_lines():
    l.set_linewidth(1.5)  # the legend line width
    l.set_fontsize(fontsize)
    l.set_fontname(fontname)
plt.savefig(os.path.join("staffing","staffing_ratios.png"))
plt.show()
