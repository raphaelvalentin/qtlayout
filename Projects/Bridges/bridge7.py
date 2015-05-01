
inf = 1000



def Bridge4x4c(width1 = 10.0, width2=10.0, width3=10.0, width4=10.0, spacing = 3.01/1.1, vector=None, **kwargs):
    angle = 45.0
    if vector==None:
        vector = Point(0,0)
    #
    y1l = 0.5*spacing+width4+spacing+width3+spacing+width2+spacing+width1
    y2l = y1l - width1
    y3l = y2l - spacing
    y4l = y3l - width2
    y5l = y4l - spacing
    y6l = y5l - width3
    y7l = y6l - spacing
    y8l = y7l - width4
    #
    y1m = 0.5*(width4+spacing+width3+spacing+width2+spacing+width1)
    y2m = y1m - width1
    y3m = y2m - spacing
    y4m = y3m - width2
    y5m = y4m - spacing
    y6m = y5m - width3
    y7m = y6m - spacing
    y8m = y7m - width4
     #
    y1r = -0.5*spacing
    y2r = y1r - width1
    y3r = y2r - spacing
    y4r = y3r - width2
    y5r = y4r - spacing
    y6r = y5r - width3
    y7r = y6r - spacing
    y8r = y7r - width4
    
    #
    #spacing2 = kwargs.pop('spacing2', 12+2*3.01/1.1)
    spacing2 = kwargs.pop('spacing2', 0)
    line1l = Line(Point(-inf, y1l+spacing2), Point(inf, y1l+spacing2))
    line2l = Line(Point(-inf, y2l+spacing2), Point(inf, y2l+spacing2))
    line3l = Line(Point(-inf, y3l), Point(inf, y3l))
    line4l = Line(Point(-inf, y4l), Point(inf, y4l))
    line5l = Line(Point(-inf, y5l), Point(inf, y5l))
    line6l = Line(Point(-inf, y6l), Point(inf, y6l))
    line7l = Line(Point(-inf, y7l), Point(inf, y7l))
    line8l = Line(Point(-inf, y8l), Point(inf, y8l))
    #
    line1m = Line(Point(-inf, y1m), Point(inf, y1m)).Rotate(angle=-angle)
    line2m = Line(Point(-inf, y2m), Point(inf, y2m)).Rotate(angle=-angle)
    line3m = Line(Point(-inf, y3m), Point(inf, y3m)).Rotate(angle=-angle)
    line4m = Line(Point(-inf, y4m), Point(inf, y4m)).Rotate(angle=-angle)
    line5m = Line(Point(-inf, y5m), Point(inf, y5m)).Rotate(angle=-angle)
    line6m = Line(Point(-inf, y6m), Point(inf, y6m)).Rotate(angle=-angle)
    line7m = Line(Point(-inf, y7m), Point(inf, y7m)).Rotate(angle=-angle)
    line8m = Line(Point(-inf, y8m), Point(inf, y8m)).Rotate(angle=-angle)
    #
    line1r = Line(Point(-inf, y1r), Point(inf, y1r))
    line2r = Line(Point(-inf, y2r), Point(inf, y2r))
    line3r = Line(Point(-inf, y3r), Point(inf, y3r))
    line4r = Line(Point(-inf, y4r), Point(inf, y4r))
    line5r = Line(Point(-inf, y5r), Point(inf, y5r))
    line6r = Line(Point(-inf, y6r), Point(inf, y6r))
    line7r = Line(Point(-inf, y7r), Point(inf, y7r))
    line8r = Line(Point(-inf, y8r), Point(inf, y8r))

    point1l = line1l.Intersect(line1m)
    point2l = line2l.Intersect(line2m)
    point3l = line3l.Intersect(line3m)
    point4l = line4l.Intersect(line4m)
    point5l = line5l.Intersect(line5m)
    point6l = line6l.Intersect(line6m)
    point7l = line7l.Intersect(line7m)
    point8l = line8l.Intersect(line8m)

    point1r = line1r.Intersect(line1m)
    point2r = line2r.Intersect(line2m)
    point3r = line3r.Intersect(line3m)
    point4r = line4r.Intersect(line4m)
    point5r = line5r.Intersect(line5m)
    point6r = line6r.Intersect(line6m)
    point7r = line7r.Intersect(line7m)
    point8r = line8r.Intersect(line8m)

    layer1 = Primitives()
    layer2 = Primitives()

    bridge = Primitive( )
    bridge.append( point2l )
    bridge.append( Point(point2l.x-3, point2l.y) )
    bridge.append( Point(point2l.x-3, point1l.y) )
    bridge.append( point1l )
    bridge.append( point1r )
    bridge.append( Point(point1r.x+3, point1r.y)  )
    bridge.append( Point(point1r.x+3, point2r.y)  )
    bridge.append( point2r )

    layer1.append(bridge.Translate(vector=vector))
    layer2.append(bridge.Translate(vector=vector).Mirror(planenormal=(1,0)))

    bridge = Primitive( )
    bridge.append( point4l )
    bridge.append( Point(point4l.x-3, point4l.y) )
    bridge.append( Point(point4l.x-3, point3l.y) )
    bridge.append( point3l )
    bridge.append( point3r )
    bridge.append( Point(point3r.x+3, point3r.y)  )
    bridge.append( Point(point3r.x+3, point4r.y)  )
    bridge.append( point4r )

    layer1.append(bridge.Translate(vector=vector))
    layer2.append(bridge.Translate(vector=vector).Mirror(planenormal=(1,0)))

    bridge = Primitive( )
    bridge.append( point6l )
    bridge.append( Point(point6l.x-3, point6l.y) )
    bridge.append( Point(point6l.x-3, point5l.y) )
    bridge.append( point5l )
    bridge.append( point5r )
    bridge.append( Point(point5r.x+3, point5r.y)  )
    bridge.append( Point(point5r.x+3, point6r.y)  )
    bridge.append( point6r )

    layer1.append(bridge.Translate(vector=vector))
    layer2.append(bridge.Translate(vector=vector).Mirror(planenormal=(1,0)))

    bridge = Primitive( )
    bridge.append( point8l )
    bridge.append( Point(point8l.x-3, point8l.y) )
    bridge.append( Point(point8l.x-3, point7l.y) )
    bridge.append( point7l )
    
    spacing = 2*spacing
    bridge.append( Line(Point(-0.5*spacing,-inf), Point(-0.5*spacing,inf)).Intersect(line7m) )
    bridge.append( Line(Point(-0.5*spacing,-inf), Point(-0.5*spacing,inf)).Intersect(line7m) - Point(0, 3) )
    bridge.append( Point(-0.5*spacing,layer1.ymin) )
    bridge.append( Point(-0.5*spacing-width4,layer1.ymin) )
    bridge.append( Line(Point(-0.5*spacing-width4,-inf), Point(-0.5*spacing-width4,inf)).Intersect(line8m) )


    layer1.append(bridge.Translate(vector=vector))
    layer2.append(bridge.Translate(vector=vector).Mirror(planenormal=(1,0)))

    #
    return layer1, layer2


#layer1 = Primitives()
#layer2 = Primitives()
##_layer1, _layer2 = Bridge4x4b()
#layer1.extend(_layer1)
#layer2.extend(_layer2)



