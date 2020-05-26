#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on Tue Apr 22 07:14:05 2014
# License is MIT, see COPYING.txt for more details.
# @author: Danilo de Jesus da Silva Bellini

from programs.fractals.Mandelbrot.fractal import Point, exec_command
try:
  from collections import OrderedDict
except ImportError: # Python 2.6
  from ordereddict import OrderedDict

# String formatting functions
Point.__str__ = lambda self: "x".join(map(str, self))
basic_str = lambda el: str(el).lstrip("(").rstrip(")") # Complex or model name
item_str = lambda k, v: (basic_str(v) if k in ["model", "c"] else
                         "{}={}".format(k, v))
filename = lambda kwargs: "_".join(item_str(*pair) for pair in kwargs.items())

# Example list
kwargs_list = [
  OrderedDict([("model", "mandelbrot"),
               ("size", Point(500, 500)),
               ("depth", 10),
               ("zoom", 0.5),
               ("center", Point(-0, 0)),
  ]),
    OrderedDict([("model", "mandelbrot"),
                 ("size", Point(300, 300)),
                 ("depth", 40),
                 ("zoom", 1.2),
                 ("center", Point(-1, 0)),
    ]),
  OrderedDict([("model", "mandelbrot"),
               ("size", Point(300, 300)),
               ("depth", 80),
               ("zoom", 1.2),
               ("center", Point(-1, 0)),
  ]),
  OrderedDict([("model", "mandelbrot"),
               ("size", Point(400, 300)),
               ("depth", 80),
               ("zoom", 2),
               ("center", Point(-1, 0)),
  ]),
  OrderedDict([("model", "mandelbrot"),
               ("size", Point(500, 500)),
               ("depth", 256),
               ("zoom", 6.5),
               ("center", Point(-1.2, .35)),
  ]),
  OrderedDict([("model", "mandelbrot"),
               ("size", Point(600, 600)),
               ("depth", 256),
               ("zoom", 90),
               ("center", Point(-1.255, .38)),
  ]),
]

# Creates all examples
if __name__ == "__main__":
  for kwargs in kwargs_list:
    kwargs["output"] = "files/mandelbrot/{}.png".format(filename(kwargs))
    #kwargs["show"] = True
    exec_command(kwargs)
