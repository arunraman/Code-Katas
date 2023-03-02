def intersecting_area(rect1, rect2):
    # Unpack the coordinates of the two rectangles
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2

    # Find the coordinates of the intersection rectangle
    x_intersect = max(x1, x2)
    y_intersect = max(y1, y2)
    x_intersect_end = min(x1 + w1, x2 + w2)
    y_intersect_end = min(y1 + h1, y2 + h2)

    # Check if the rectangles intersect
    if x_intersect > x_intersect_end or y_intersect > y_intersect_end:
        # If the intersection coordinates are invalid, the rectangles do not intersect
        return 0
    else:
        # The rectangles intersect, so calculate the area of the intersection
        intersect_width = x_intersect_end - x_intersect
        intersect_height = y_intersect_end - y_intersect
        return intersect_width * intersect_height


# Test the function
rect1 = (0, 0, 10, 10)  # x, y, width, height
rect2 = (5, 5, 10, 10)
print(intersecting_area(rect1, rect2))  # should print 25
