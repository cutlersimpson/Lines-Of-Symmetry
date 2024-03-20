import numpy as np


def find_lines_of_symmetry(points):
    """
    Find lines of symmetry given set of input points by:
    1. Find centroid of input points
    2. Find the midpoints of all inputs and the adjacent points
    3. Determine line through set of input points and midpoints through centroid
    4. Determine if all input points have a mirrored point reflected across
       current line through centroid. If all input points have a mirror,
       this is a valid line of symmetry
    5. Normalize the coefficients defining the line to ensure no duplicates
    """
    if not points:
        return []

    centroid = calculate_centroid(points)
    midpoints = find_midpoints(points)
    all_points = list(set(midpoints + points))

    lines_of_symmetry = []

    for point in all_points:
        seen_points = []
        is_line_of_symmetry = True

        # Skip centroid because a line needs to go through 2 points
        if point == centroid:
            continue

        # Find line going through point and centroid
        line_coefficients = get_line_coefficients(centroid, point)

        for input_point in points:
            if input_point in seen_points or input_point == point:
                continue

            # If point is on centroid line there is no reflection
            if is_point_on_line(input_point, line_coefficients):
                continue

            mirror_point = find_mirror_point(input_point, line_coefficients)

            # If mirror is not valid this line can't be a line of symemtry
            if mirror_point not in points:
                is_line_of_symmetry = False
                break

            # Mark mirror as seen to avoid duplicate calculations
            if mirror_point not in seen_points:
                seen_points.append(mirror_point)

        # Ensure no duplicate lines and append the coefficients to the lines_of_symmetry list
        if is_line_of_symmetry:
            normalized_coefficients = normalize_line_coefficients(line_coefficients)

            if normalized_coefficients not in lines_of_symmetry:
                lines_of_symmetry.append(normalized_coefficients)

    return lines_of_symmetry


def calculate_centroid(points):
    """
    Calculate the centroid (mean) of a set of points.
    """
    x_coords, y_coords = zip(*points)
    centroid_x = np.mean(x_coords)
    centroid_y = np.mean(y_coords)
    return centroid_x, centroid_y


def find_midpoints(points):
    """
    Find the midpoints between each point and its adjacent points.
    """
    midpoints = []
    for i, (x1, y1) in enumerate(points):
        for _, (x2, y2) in enumerate(points[i + 1 :], start=i + 1):
            midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
            if midpoint not in midpoints and midpoint not in points:
                midpoints.append(midpoint)
    return midpoints


def is_point_on_line(point, line_coefficients):
    """
    Use equation of a line (ax + by + c = 0) to check if the point is on a line
    """
    a, b, c = line_coefficients
    x, y = point
    return a * x + b * y + c == 0


def find_mirror_point(point, line_coefficients):
    """
    Find point reflected across line
    Explaation: https://stackoverflow.com/q/8954326
    """
    a, b, c = line_coefficients
    x, y = point

    denominator = a ** 2 + b ** 2
    temp = -2 * ((a * x + b * y + c) / denominator)
    mirror_x = temp * a + x
    mirror_y = temp * b + y
    return mirror_x, mirror_y


def get_line_coefficients(point1, point2):
    """
    Calculate the coefficients (a, b, c) of the line passing through two points.
    ax + by + c = 0
    """
    x1, y1 = point1
    x2, y2 = point2
    a = y2 - y1
    b = x1 - x2
    c = x2 * y1 - x1 * y2
    return a, b, c


def normalize_line_coefficients(coefficients):
    """
    Normalize values to identify lines with equal slopes and intercepts to
    avoid duplicates
    """
    a, b, c = coefficients

    # Divide by nonzero b
    if a == 0 and c == 0:
        return (0, 1, 0)

    # Divide by nonzero a
    if b == 0 and c == 0:
        return (1, 0, 0)

    # Divide by nonzero c
    if a == 0 and b != 0 and c != 0:
        b = b / c
        c = 1
        return (a, b, c)

    # Divide by nonzero c
    if b == 0 and a != 0 and c != 0:
        a = a / c
        c = 1
        return (a, b, c)

    # Divide by nonzero b
    if c == 0 and a != 0 and b != 0:
        a = a / b
        b = 1
        return (a, b, c)

    a = a / c
    b = b / c
    c = 1
    return (a, b, c)


def coefficients_to_equation(a, b, c):
    """
    Convert line coefficients to y = mx + b equation
    """
    if b == 0:
        return "x = " + str(-c / a)
    slope = -a / b
    intercept = -c / b
    return f"y = {slope}x + {intercept}"


def print_results(points, eqns):
    print(f"Initial points: {points}")
    print(f"Total number of lines found: {len(eqns)}")
    print(eqns)


def test_square():
    square = [(0, 0), (0, 1), (1, 0), (1, 1)]

    coeffs = find_lines_of_symmetry(square)
    equations = [coefficients_to_equation(a, b, c) for a, b, c in coeffs]
    print_results(square, equations)


if __name__ == "__main__":
    test_square()
