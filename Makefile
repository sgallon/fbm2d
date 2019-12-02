SHELL=/bin/bash
all:
		f2py3 -c 2Dfbm.f90 -m fortranfbm
