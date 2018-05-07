from columns import a, b, c, d, e, f, g, h

def grid(coords):
    item = [
    [a.one, a.two, a.three, a.four, a.five, a.six],
    [b.one, b.two, b.three, b.four, b.five, b.six],
    [c.one, c.two, c.three, c.four, c.five, c.six],
    [d.one, d.two, d.three, d.four, d.five, d.six],
    [e.one, e.two, e.three, e.four, e.five, e.six],
    [f.one, f.two, f.three, f.four, f.five, f.six],
    [g.one, g.two, g.three, g.four, g.five, g.six],
    [h.one, h.two, h.three, h.four, h.five, h.six]
    ]

    return item[coords[0]][coords[1]]